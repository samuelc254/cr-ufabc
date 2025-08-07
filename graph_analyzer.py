import pandas as pd
import networkx as nx
import numpy as np
import time
import os
import sys
import random
from collections import Counter
from networkx.algorithms import community

# ============================================================================
# ARQUIVO UNIFICADO DE ANÁLISE DE GRAFOS
# Contém todas as funções de análise utilizadas no projeto
# ============================================================================


def approximate_diameter_optimized(graph, sample_size=1000):
    """
    Calcula aproximação do diâmetro otimizada - vai direto para amostragem.
    """
    if graph.is_directed():
        components = list(nx.strongly_connected_components(graph))
    else:
        components = list(nx.connected_components(graph))

    if not components:
        return None

    largest_component = max(components, key=len)
    subgraph = graph.subgraph(largest_component)

    # Vai direto para aproximação por amostragem (otimizado para grafos grandes)
    sample_nodes = random.sample(list(largest_component), min(sample_size, len(largest_component)))

    max_distance = 0
    for i, source in enumerate(sample_nodes[:100]):  # Limita a 100 nós fonte
        try:
            lengths = nx.single_source_shortest_path_length(subgraph, source)
            if lengths:
                max_dist_from_source = max(lengths.values())
                max_distance = max(max_distance, max_dist_from_source)
        except:
            continue

    return max_distance, len(largest_component), "aproximado", largest_component


def analyze_graph_complete(graph, df, name):
    """
    Análise completa unificada incluindo métricas básicas + diâmetro + centralidade.
    """
    print(f"[{os.getpid()}] Iniciando análise completa para: {name}...")
    start_time = time.time()

    # Métricas básicas
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()

    if num_nodes == 0:
        return {"name": name, "nodes": 0, "edges": 0, "elapsed_time": time.time() - start_time, "error": "Grafo vazio"}

    metrics = {"name": name, "nodes": num_nodes, "edges": num_edges, "density": nx.density(graph), "is_directed": graph.is_directed()}

    # Análise de conectividade
    if graph.is_directed():
        scc = list(nx.strongly_connected_components(graph))
        wcc = list(nx.weakly_connected_components(graph))
        largest_wcc = max(wcc, key=len) if wcc else set()
        largest_scc = max(scc, key=len) if scc else set()

        metrics.update(
            {
                "scc_count": len(scc),
                "wcc_count": len(wcc),
                "largest_scc_size": len(largest_scc),
                "largest_wcc_size": len(largest_wcc),
                "lcc_nodes": len(largest_wcc),  # Para compatibilidade
                "lcc_percent": (len(largest_wcc) / num_nodes) * 100,
                "lcc_edges": graph.subgraph(largest_wcc).number_of_edges(),
                "lcc_edges_percent": (graph.subgraph(largest_wcc).number_of_edges() / num_edges) * 100 if num_edges > 0 else 0,
            }
        )
    else:
        cc = list(nx.connected_components(graph))
        largest_cc = max(cc, key=len) if cc else set()
        metrics.update(
            {
                "cc_count": len(cc),
                "largest_cc_size": len(largest_cc),
                "lcc_nodes": len(largest_cc),  # Para compatibilidade
                "lcc_percent": (len(largest_cc) / num_nodes) * 100,
                "lcc_edges": graph.subgraph(largest_cc).number_of_edges(),
                "lcc_edges_percent": (graph.subgraph(largest_cc).number_of_edges() / num_edges) * 100 if num_edges > 0 else 0,
            }
        )

    # Análise de graus
    degrees = dict(graph.degree())
    in_degrees = dict(graph.in_degree()) if graph.is_directed() else degrees
    out_degrees = dict(graph.out_degree()) if graph.is_directed() else degrees

    metrics.update(
        {
            "avg_degree": np.mean(list(degrees.values())),
            "max_degree": max(degrees.values()) if degrees else 0,
            "degree_mean": np.mean(list(degrees.values())),  # Para compatibilidade
            "degree_median": np.median(list(degrees.values())),
            "degree_max": max(degrees.values()) if degrees else 0,
            "avg_in_degree": np.mean(list(in_degrees.values())),
            "max_in_degree": max(in_degrees.values()) if in_degrees else 0,
            "in_degree_mean": np.mean(list(in_degrees.values())),  # Para compatibilidade
            "in_degree_median": np.median(list(in_degrees.values())),
            "in_degree_max": max(in_degrees.values()) if in_degrees else 0,
            "avg_out_degree": np.mean(list(out_degrees.values())),
            "max_out_degree": max(out_degrees.values()) if out_degrees else 0,
            "out_degree_mean": np.mean(list(out_degrees.values())),  # Para compatibilidade
            "out_degree_median": np.median(list(out_degrees.values())),
            "out_degree_max": max(out_degrees.values()) if out_degrees else 0,
            "top_in_degree": sorted(in_degrees.items(), key=lambda x: x[1], reverse=True)[:10],
            "top_out_degree": sorted(out_degrees.items(), key=lambda x: x[1], reverse=True)[:10],
        }
    )

    # Determina qual componente usar para análises mais pesadas
    if graph.is_directed():
        target_component = max(nx.weakly_connected_components(graph), key=len)
    else:
        target_component = max(nx.connected_components(graph), key=len)

    lcc = graph.subgraph(target_component)

    # Cálculo de centralidade (otimizado)
    is_large_scale = name == "Geral"
    target_graph_for_centrality = lcc

    if is_large_scale:
        # Para grafos muito grandes, usa amostragem
        sample_size = min(len(target_component), 200000)
        sample_nodes = np.random.choice(list(target_component), sample_size, replace=False)
        target_graph_for_centrality = lcc.subgraph(sample_nodes)
        metrics["centrality_info"] = f"uma amostra de {sample_size:,} nós do maior componente"
    else:
        metrics["centrality_info"] = "maior componente"

    print(f"  [{name}] Calculando PageRank...")
    pagerank = nx.pagerank(target_graph_for_centrality, alpha=0.85)
    metrics["pagerank"] = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:10]

    # Betweenness sempre aproximado para eficiência
    if is_large_scale:
        k_betweenness = min(1000, target_graph_for_centrality.number_of_nodes())
        print(f"  [{name}] Calculando Betweenness (aproximado com k={k_betweenness})...")
        betweenness = nx.betweenness_centrality(target_graph_for_centrality, k=k_betweenness, normalized=True)
        metrics["centrality_info"] += f" (Betweenness aproximado com k={k_betweenness})"
    else:
        k_betweenness = min(500, target_graph_for_centrality.number_of_nodes())
        print(f"  [{name}] Calculando Betweenness (aproximado com k={k_betweenness})...")
        betweenness = nx.betweenness_centrality(target_graph_for_centrality, k=k_betweenness, normalized=True)
        metrics["centrality_info"] += f" (Betweenness aproximado com k={k_betweenness})"

    metrics["betweenness"] = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:10]

    # Análise estrutural (apenas para grafos menores)
    if not is_large_scale:
        print(f"  [{name}] Calculando clustering e comunidades...")
        metrics["avg_clustering"] = nx.average_clustering(graph)

        # Detecção de comunidades
        communities_sets = community.louvain_communities(graph.to_undirected(), seed=42)
        modularity = community.modularity(graph.to_undirected(), communities_sets)
        metrics.update({"communities": len(communities_sets), "modularity": modularity})

    # Cálculo do diâmetro (sempre aproximado para eficiência)
    print(f"  [{name}] Calculando diâmetro aproximado...")
    diameter_result = approximate_diameter_optimized(graph)

    if diameter_result:
        diameter, component_size, method, _ = diameter_result
        metrics.update({"diameter": diameter, "diameter_method": method, "diameter_component_size": component_size, "diameter_component_percent": (component_size / num_nodes) * 100})
    else:
        metrics.update({"diameter": None, "diameter_method": "erro", "diameter_component_size": 0, "diameter_component_percent": 0})

    metrics["elapsed_time"] = time.time() - start_time
    print(f"[{os.getpid()}] Análise completa de '{name}' concluída em {metrics['elapsed_time']:.2f}s")

    return metrics


def format_complete_report(metrics):
    """
    Formata relatório completo incluindo todas as métricas.
    """
    name = metrics["name"]
    report = [f"# Análise Completa do Grafo: {name}\n"]

    if metrics.get("error"):
        report.append(f"**Erro:** {metrics['error']}")
        return "\n".join(report)

    # Métricas Básicas
    report.append("## 1. Métricas Básicas")
    report.append("| Métrica | Valor |")
    report.append("|---------|-------|")
    report.append(f"| **Nós** | {metrics['nodes']:,} |")
    report.append(f"| **Arestas** | {metrics['edges']:,} |")
    report.append(f"| **Densidade** | {metrics['density']:.8f} |")
    report.append(f"| **Direcionado** | {'Sim' if metrics['is_directed'] else 'Não'} |")
    report.append("")

    # Conectividade
    report.append("## 2. Análise de Conectividade")
    report.append("| Métrica | Valor |")
    report.append("|---------|-------|")

    if metrics["is_directed"]:
        report.append(f"| **Componentes Fortemente Conectados (SCC)** | {metrics.get('scc_count', 0):,} |")
        report.append(f"| **Componentes Fracamente Conectados (WCC)** | {metrics.get('wcc_count', 0):,} |")
        report.append(f"| **Maior SCC** | {metrics.get('largest_scc_size', 0):,} nós |")
        report.append(f"| **Maior WCC** | {metrics.get('largest_wcc_size', 0):,} nós |")
    else:
        report.append(f"| **Componentes Conectados** | {metrics.get('cc_count', 0):,} |")
        report.append(f"| **Maior Componente** | {metrics.get('largest_cc_size', 0):,} nós |")

    report.append(f"| **Nós no Maior Componente** | {metrics.get('lcc_nodes', 0):,} ({metrics.get('lcc_percent', 0):.2f}%) |")
    report.append(f"| **Arestas no Maior Componente** | {metrics.get('lcc_edges', 0):,} ({metrics.get('lcc_edges_percent', 0):.2f}%) |")
    report.append("")

    # Análise de Graus
    report.append("## 3. Análise de Graus")
    report.append("### 3.1. Estatísticas Gerais")
    report.append("| Métrica | Valor |")
    report.append("|---------|-------|")
    report.append(f"| **Grau Médio** | {metrics.get('avg_degree', 0):.2f} |")
    report.append(f"| **Grau Máximo** | {metrics.get('max_degree', 0):,} |")
    report.append(f"| **Grau Mediano** | {metrics.get('degree_median', 0):.2f} |")

    if metrics["is_directed"]:
        report.append(f"| **In-Degree Médio** | {metrics.get('avg_in_degree', 0):.2f} |")
        report.append(f"| **In-Degree Máximo** | {metrics.get('max_in_degree', 0):,} |")
        report.append(f"| **In-Degree Mediano** | {metrics.get('in_degree_median', 0):.2f} |")
        report.append(f"| **Out-Degree Médio** | {metrics.get('avg_out_degree', 0):.2f} |")
        report.append(f"| **Out-Degree Máximo** | {metrics.get('max_out_degree', 0):,} |")
        report.append(f"| **Out-Degree Mediano** | {metrics.get('out_degree_median', 0):.2f} |")

    # Top nós
    if metrics.get("top_in_degree"):
        report.append("\n### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)")
        report.append("| Rank | Dependência | In-Degree |")
        report.append("|------|-------------|-----------|")
        for i, (node, degree) in enumerate(metrics["top_in_degree"], 1):
            report.append(f"| {i} | `{node}` | {degree:,} |")

    if metrics.get("top_out_degree"):
        report.append("\n### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)")
        report.append("| Rank | Projeto | Out-Degree |")
        report.append("|------|---------|------------|")
        for i, (node, degree) in enumerate(metrics["top_out_degree"], 1):
            report.append(f"| {i} | `{node}` | {degree:,} |")

    report.append("")

    # Centralidade
    if metrics.get("pagerank"):
        report.append("## 4. Análise de Centralidade")
        report.append(f"_(Análise realizada em {metrics.get('centrality_info', 'todo o grafo')})_")

        report.append("\n### 4.1. Top 10 Nós por Influência (PageRank)")
        report.append("| Rank | Nó | PageRank Score |")
        report.append("|------|-----|----------------|")
        for i, (node, score) in enumerate(metrics["pagerank"], 1):
            report.append(f"| {i} | `{node}` | {score:.6f} |")

        if metrics.get("betweenness"):
            report.append("\n### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)")
            report.append("| Rank | Nó | Betweenness Score |")
            report.append("|------|-----|-------------------|")
            for i, (node, score) in enumerate(metrics["betweenness"], 1):
                report.append(f"| {i} | `{node}` | {score:.6f} |")

        report.append("")

    # Análise Estrutural
    if "avg_clustering" in metrics:
        report.append("## 5. Análise Estrutural e de Comunidades")
        report.append("| Métrica | Valor |")
        report.append("|---------|-------|")
        report.append(f"| **Coeficiente de Clusterização Médio** | {metrics['avg_clustering']:.6f} |")
        if "communities" in metrics:
            report.append(f"| **Comunidades Detectadas (Louvain)** | {metrics['communities']:,} |")
            report.append(f"| **Modularidade** | {metrics['modularity']:.4f} |")
        report.append("")

    # Análise de Diâmetro
    report.append("## 6. Análise de Diâmetro")
    report.append("| Métrica | Valor |")
    report.append("|---------|-------|")

    if metrics.get("diameter") is not None:
        report.append(f"| **Diâmetro** | {metrics['diameter']} |")
        report.append(f"| **Método** | {metrics['diameter_method'].title()} |")
        report.append(f"| **Componente Analisado** | {metrics['diameter_component_size']:,} nós ({metrics['diameter_component_percent']:.1f}%) |")

        # Interpretação do diâmetro
        diameter = metrics["diameter"]
        if diameter <= 6:
            interpretation = "Rede Altamente Conectada"
        elif diameter <= 10:
            interpretation = "Rede Moderadamente Conectada"
        else:
            interpretation = "Rede Dispersa"
        report.append(f"| **Interpretação** | {interpretation} |")
    else:
        report.append("| **Diâmetro** | Não foi possível calcular |")

    report.append("")

    # Resumo Final
    report.append("## 7. Resumo Executivo")
    report.append(f"Este grafo possui **{metrics['nodes']:,} nós** e **{metrics['edges']:,} arestas**.")

    if metrics.get("diameter") is not None:
        report.append(f"O diâmetro aproximado é **{metrics['diameter']}**, indicando que ")
        if metrics["diameter"] <= 6:
            report.append("a rede apresenta alta conectividade, típica de ecossistemas maduros.")
        elif metrics["diameter"] <= 10:
            report.append("a rede apresenta conectividade moderada.")
        else:
            report.append("a rede apresenta conectividade mais dispersa.")

    report.append(f"\nO maior componente conectado contém {metrics.get('lcc_percent', 0):.1f}% dos nós, ")
    report.append(f"com densidade de {metrics['density']:.6f}.")

    report.append(f"\n---\n*Análise concluída em {metrics['elapsed_time']:.2f} segundos.*")

    return "\n".join(report)


def analyze_graph_basic(graph, name, is_large_scale=False):
    """
    Análise básica (compatibilidade com analyzer.py antigo).
    """
    return analyze_graph_complete(graph, None, name)


def format_basic_report(graph_name, metrics):
    """
    Formata relatório básico (compatibilidade).
    """
    return format_complete_report(metrics)


def main():
    """Função principal para execução como script independente."""
    if len(sys.argv) != 4:
        print("Uso: python graph_analyzer.py <caminho_do_parquet> <nome_da_plataforma> <diretorio_de_saida>")
        sys.exit(1)

    parquet_path = sys.argv[1]
    platform_name = sys.argv[2]
    output_dir = sys.argv[3]

    try:
        # 1. Carrega os dados e constrói o grafo
        df = pd.read_parquet(parquet_path)
        graph = nx.from_pandas_edgelist(df, source="Project Name", target="Dependency Name", create_using=nx.DiGraph())

        # 2. Analisa (unificado)
        metrics = analyze_graph_complete(graph, df, platform_name)

        # 3. Formata e salva o relatório
        report_md = format_complete_report(metrics)
        output_filename = os.path.join(output_dir, f"analise_{platform_name}.md")

        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(report_md)

        print(f"[{os.getpid()}] Relatório completo para '{platform_name}' salvo com sucesso.")

        # Também salva métricas como JSON para análises futuras
        import json

        json_output_dir = os.path.join(output_dir, "json")
        os.makedirs(json_output_dir, exist_ok=True)
        json_filename = os.path.join(json_output_dir, f"metricas_{platform_name}.json")
        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=2, default=str)

    except Exception as e:
        print(f"[{os.getpid()}] Falha ao processar {platform_name}: {e}")
        # Salva log de erro
        error_filename = os.path.join(output_dir, f"analise_{platform_name}_ERRO.log")
        with open(error_filename, "w", encoding="utf-8") as f:
            import traceback

            f.write(traceback.format_exc())


if __name__ == "__main__":
    main()

import pandas as pd
import networkx as nx
import numpy as np
import time
import os
import sys
from networkx.algorithms import community

# (As funções format_report e analyze_graph são coladas aqui)

def format_report(graph_name, metrics):
    """Formata as métricas coletadas em uma string Markdown."""
    report = [f"# Análise do Grafo: {graph_name}\n"]
    if not metrics or metrics.get('nodes', 0) == 0:
        report.append("Grafo vazio ou análise falhou.")
        return "\n".join(report)
    report.append("## 1. Métricas Gerais")
    report.append("| Métrica | Valor |"); report.append("|---|---|")
    report.append(f"| **Nós (Projetos/Dependências)** | {metrics.get('nodes', 0):,} |")
    report.append(f"| **Arestas (Dependências)** | {metrics.get('edges', 0):,} |")
    report.append(f"| **Densidade do Grafo** | {metrics.get('density', 0):.8f} |")
    report.append(f"| **Grafo Direcionado** | {'Sim' if metrics.get('is_directed') else 'Não'} |")
    if 'wcc_count' in metrics:
        report.append("\n## 2. Análise de Conectividade"); report.append("| Métrica | Valor |"); report.append("|---|---|")
        report.append(f"| **Componentes Fracamente Conectados** | {metrics.get('wcc_count', 0):,} |")
        report.append(f"| **Nós no Maior Componente (LCC)** | {metrics.get('lcc_nodes', 0):,} ({metrics.get('lcc_percent', 0):.2f}%) |")
        report.append(f"| **Arestas no Maior Componente (LCC)** | {metrics.get('lcc_edges', 0):,} ({metrics.get('lcc_edges_percent', 0):.2f}%) |")
    if 'in_degree_mean' in metrics:
        report.append("\n## 3. Análise de Graus (Popularidade e Complexidade)"); report.append("### 3.1. Estatísticas Gerais de Grau")
        report.append("| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |"); report.append("|---|---|---|---|")
        report.append(f"| **Média** | {metrics.get('in_degree_mean', 0):.2f} | {metrics.get('out_degree_mean', 0):.2f} | {metrics.get('degree_mean', 0):.2f} |")
        report.append(f"| **Mediana** | {metrics.get('in_degree_median', 0):.2f} | {metrics.get('out_degree_median', 0):.2f} | {metrics.get('degree_median', 0):.2f} |")
        report.append(f"| **Máximo** | {metrics.get('in_degree_max', 0):,} | {metrics.get('out_degree_max', 0):,} | {metrics.get('degree_max', 0):,} |")
        report.append("\n### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)"); report.append("| Rank | Dependência | In-Degree |"); report.append("|---|---|---|")
        for i, (node, degree) in enumerate(metrics.get('top_in_degree', []), 1): report.append(f"| {i} | `{node}` | {degree:,} |")
        report.append("\n### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)"); report.append("| Rank | Projeto | Out-Degree |"); report.append("|---|---|---|")
        for i, (node, degree) in enumerate(metrics.get('top_out_degree', []), 1): report.append(f"| {i} | `{node}` | {degree:,} |")
    if 'pagerank' in metrics:
        report.append("\n## 4. Análise de Centralidade"); report.append(f"_(Análise realizada em {metrics.get('centrality_info', 'todo o grafo')})_")
        report.append("\n### 4.1. Top 10 Nós por Influência (PageRank)"); report.append("| Rank | Nó | PageRank Score |"); report.append("|---|---|---|")
        for i, (node, score) in enumerate(metrics.get('pagerank', []), 1): report.append(f"| {i} | `{node}` | {score:.6f} |")
        if 'betweenness' in metrics:
            report.append("\n### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)"); report.append("| Rank | Nó | Betweenness Score |"); report.append("|---|---|---|")
            for i, (node, score) in enumerate(metrics.get('betweenness', []), 1): report.append(f"| {i} | `{node}` | {score:.6f} |")
    if 'avg_clustering' in metrics:
        report.append("\n## 5. Análise Estrutural e de Comunidades"); report.append(f"| Métrica | Valor |"); report.append(f"|---|---|")
        report.append(f"| **Coeficiente de Clusterização Médio** | {metrics.get('avg_clustering', 0):.6f} |")
        if 'communities' in metrics:
            report.append(f"| **Comunidades Detectadas (Louvain)** | {metrics.get('communities', 0):,} |")
            report.append(f"| **Modularidade** | {metrics.get('modularity', 0):.4f} |")
    report.append(f"\n---\n*Análise concluída em {metrics.get('elapsed_time', 0):.2f} segundos.*\n\n")
    return "\n".join(report)

def analyze_graph(graph, name, is_large_scale=False):
    print(f"[{os.getpid()}] Iniciando análise para o grafo: {name}...")
    start_time = time.time()
    metrics = {}
    num_nodes = graph.number_of_nodes()
    if num_nodes == 0: return name, {'nodes': 0, 'edges': 0, 'elapsed_time': time.time() - start_time}
    metrics.update({'nodes': num_nodes, 'edges': graph.number_of_edges(), 'density': nx.density(graph), 'is_directed': graph.is_directed()})
    wcc = list(nx.weakly_connected_components(graph)); largest_wcc_nodes = max(wcc, key=len); lcc = graph.subgraph(largest_wcc_nodes)
    metrics.update({'wcc_count': len(wcc), 'lcc_nodes': lcc.number_of_nodes(), 'lcc_percent': (lcc.number_of_nodes()/num_nodes)*100, 'lcc_edges': lcc.number_of_edges(), 'lcc_edges_percent': (lcc.number_of_edges()/metrics['edges'])*100 if metrics['edges']>0 else 0})
    in_degrees=dict(graph.in_degree()); out_degrees=dict(graph.out_degree())
    metrics.update({'in_degree_mean': np.mean(list(in_degrees.values())), 'in_degree_median': np.median(list(in_degrees.values())), 'in_degree_max': max(in_degrees.values() or [0]), 'out_degree_mean': np.mean(list(out_degrees.values())), 'out_degree_median': np.median(list(out_degrees.values())), 'out_degree_max': max(out_degrees.values() or [0]), 'degree_mean': np.mean(list(dict(graph.degree()).values())), 'degree_median': np.median(list(dict(graph.degree()).values())), 'degree_max': max(dict(graph.degree()).values() or [0]), 'top_in_degree': sorted(in_degrees.items(), key=lambda item: item[1], reverse=True)[:10], 'top_out_degree': sorted(out_degrees.items(), key=lambda item: item[1], reverse=True)[:10]})
    target_graph_for_centrality = lcc
    if is_large_scale:
        sample_size = min(num_nodes, 200000); sample_nodes = np.random.choice(list(lcc.nodes()), sample_size, replace=False); target_graph_for_centrality = lcc.subgraph(sample_nodes)
        metrics['centrality_info'] = f"uma amostra de {sample_size:,} nós do maior componente"
    pagerank = nx.pagerank(target_graph_for_centrality, alpha=0.85); metrics['pagerank'] = sorted(pagerank.items(), key=lambda item: item[1], reverse=True)[:10]
    if is_large_scale:
        k_betweenness = min(1000, target_graph_for_centrality.number_of_nodes()); betweenness = nx.betweenness_centrality(target_graph_for_centrality, k=k_betweenness, normalized=True)
        metrics['centrality_info'] += f" (Betweenness aproximado com k={k_betweenness})"
    else:
        k_betweenness = min(500, target_graph_for_centrality.number_of_nodes()); betweenness = nx.betweenness_centrality(target_graph_for_centrality, k=k_betweenness, normalized=True)
        metrics['centrality_info'] = f"maior componente (Betweenness aproximado com k={k_betweenness})"
    metrics['betweenness'] = sorted(betweenness.items(), key=lambda item: item[1], reverse=True)[:10]
    if not is_large_scale:
        metrics['avg_clustering'] = nx.average_clustering(graph); communities_sets = community.louvain_communities(graph.to_undirected(), seed=42); modularity = community.modularity(graph.to_undirected(), communities_sets)
        metrics.update({'communities': len(communities_sets), 'modularity': modularity})
    metrics['elapsed_time'] = time.time() - start_time
    print(f"[{os.getpid()}] Análise de '{name}' concluída em {metrics['elapsed_time']:.2f} segundos.")
    return name, metrics

def main():
    if len(sys.argv) != 4:
        print("Uso: python analyzer.py <caminho_do_parquet> <nome_da_plataforma> <diretorio_de_saida>")
        sys.exit(1)

    parquet_path = sys.argv[1]
    platform_name = sys.argv[2]
    output_dir = sys.argv[3]

    is_large = (platform_name == "Geral")

    try:
        # 1. Carrega os dados e constrói o grafo
        df = pd.read_parquet(parquet_path)
        graph = nx.from_pandas_edgelist(df, source="Project Name", target="Dependency Name", create_using=nx.DiGraph())
        del df

        # 2. Analisa
        _name, metrics = analyze_graph(graph, platform_name, is_large_scale=is_large)

        # 3. Salva o relatório
        report_md = format_report(platform_name, metrics)
        output_filename = os.path.join(output_dir, f"analise_{platform_name}.md")
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(report_md)
        
        print(f"[{os.getpid()}] Relatório para '{platform_name}' salvo com sucesso.")

    except Exception as e:
        print(f"[{os.getpid()}] Falha ao processar {platform_name}: {e}")
        # Opcional: salvar um log de erro
        error_filename = os.path.join(output_dir, f"analise_{platform_name}_ERRO.log")
        with open(error_filename, "w", encoding="utf-8") as f:
            import traceback
            f.write(traceback.format_exc())

if __name__ == "__main__":
    main()
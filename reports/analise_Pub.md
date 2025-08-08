# Análise Completa do Grafo: Pub

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 8,667 |
| **Arestas** | 28,851 |
| **Densidade** | 0.00038413 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 8,557 |
| **Componentes Fracamente Conectados (WCC)** | 16 |
| **Maior SCC** | 62 nós |
| **Maior WCC** | 8,626 nós |
| **Nós no Maior Componente** | 8,626 (99.53%) |
| **Arestas no Maior Componente** | 28,821 (99.90%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 6.66 |
| **Grau Máximo** | 4,663 |
| **Grau Mediano** | 3.00 |
| **In-Degree Médio** | 3.33 |
| **In-Degree Máximo** | 4,655 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 3.33 |
| **Out-Degree Máximo** | 64 |
| **Out-Degree Mediano** | 2.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `flutter` | 4,655 |
| 2 | `flutter_test` | 3,723 |
| 3 | `test` | 2,299 |
| 4 | `meta` | 828 |
| 5 | `pedantic` | 782 |
| 6 | `http` | 684 |
| 7 | `path` | 639 |
| 8 | `build_runner` | 566 |
| 9 | `unittest` | 409 |
| 10 | `logging` | 404 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `magpiecli` | 64 |
| 2 | `mpcli` | 64 |
| 3 | `mgpcli` | 64 |
| 4 | `build_runner` | 41 |
| 5 | `devtools_app` | 35 |
| 6 | `over_react` | 34 |
| 7 | `pana` | 32 |
| 8 | `dartdoc` | 30 |
| 9 | `repub` | 30 |
| 10 | `webdev` | 30 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `flutter` | 0.088888 |
| 2 | `test` | 0.061618 |
| 3 | `flutter_test` | 0.058742 |
| 4 | `path` | 0.018673 |
| 5 | `pedantic` | 0.018501 |
| 6 | `meta` | 0.012119 |
| 7 | `intl` | 0.011713 |
| 8 | `http` | 0.010788 |
| 9 | `vector_math` | 0.010330 |
| 10 | `sky_tools` | 0.009566 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `flutter` | 0.006877 |
| 2 | `sky_tools` | 0.004814 |
| 3 | `test` | 0.004182 |
| 4 | `build_runner` | 0.002644 |
| 5 | `mockito` | 0.001896 |
| 6 | `vector_math` | 0.001405 |
| 7 | `test_core` | 0.001321 |
| 8 | `shelf_route` | 0.001020 |
| 9 | `build_web_compilers` | 0.000911 |
| 10 | `vm_service` | 0.000902 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.110313 |
| **Comunidades Detectadas (Louvain)** | 31 |
| **Modularidade** | 0.4839 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 8 |
| **Método** | Aproximado |
| **Componente Analisado** | 62 nós (0.7%) |
| **Interpretação** | Rede Moderadamente Conectada |

## 7. Resumo Executivo
Este grafo possui **8,667 nós** e **28,851 arestas**.
O diâmetro aproximado é **8**, indicando que 
a rede apresenta conectividade moderada.

O maior componente conectado contém 99.5% dos nós, 
com densidade de 0.000384.

---
*Análise concluída em 15.20 segundos.*
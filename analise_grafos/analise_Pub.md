# Análise do Grafo: Pub

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 8,667 |
| **Arestas (Dependências)** | 28,851 |
| **Densidade do Grafo** | 0.00038413 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 16 |
| **Nós no Maior Componente (LCC)** | 8,626 (99.53%) |
| **Arestas no Maior Componente (LCC)** | 28,821 (99.90%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 3.33 | 3.33 | 6.66 |
| **Mediana** | 0.00 | 2.00 | 3.00 |
| **Máximo** | 4,655 | 64 | 4,663 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
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
|---|---|---|
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
|---|---|---|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `flutter` | 0.006916 |
| 2 | `sky_tools` | 0.004838 |
| 3 | `test` | 0.004219 |
| 4 | `build_runner` | 0.002647 |
| 5 | `mockito` | 0.001959 |
| 6 | `vector_math` | 0.001446 |
| 7 | `test_core` | 0.001343 |
| 8 | `shelf_route` | 0.001017 |
| 9 | `vm_service` | 0.000920 |
| 10 | `build_web_compilers` | 0.000920 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.110313 |
| **Comunidades Detectadas (Louvain)** | 31 |
| **Modularidade** | 0.4839 |

---
*Análise concluída em 17.00 segundos.*


# Análise do Grafo: Conda

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 1,270 |
| **Arestas (Dependências)** | 2,866 |
| **Densidade do Grafo** | 0.00177832 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 63 |
| **Nós no Maior Componente (LCC)** | 959 (75.51%) |
| **Arestas no Maior Componente (LCC)** | 2,565 (89.50%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 2.26 | 2.26 | 4.51 |
| **Mediana** | 1.00 | 1.00 | 2.00 |
| **Máximo** | 536 | 275 | 546 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
| 1 | `python` | 536 |
| 2 | `libgcc-ng` | 327 |
| 3 | `libstdcxx-ng` | 144 |
| 4 | `numpy` | 77 |
| 5 | `zlib` | 64 |
| 6 | `six` | 36 |
| 7 | `openssl` | 28 |
| 8 | `requests` | 22 |
| 9 | `tornado` | 20 |
| 10 | `pandas` | 18 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|---|---|---|
| 1 | `anaconda` | 275 |
| 2 | `libgdal` | 31 |
| 3 | `graphviz` | 21 |
| 4 | `orange3` | 19 |
| 5 | `vtk` | 16 |
| 6 | `tensorflow-base` | 16 |
| 7 | `scikit-image` | 15 |
| 8 | `wxpython` | 15 |
| 9 | `docker-py` | 14 |
| 10 | `scikit-bio` | 14 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|---|---|---|
| 1 | `python` | 0.132325 |
| 2 | `libgcc-ng` | 0.122561 |
| 3 | `_libgcc_mutex` | 0.104456 |
| 4 | `libstdcxx-ng` | 0.037928 |
| 5 | `zlib` | 0.022327 |
| 6 | `ncurses` | 0.019351 |
| 7 | `openssl` | 0.014254 |
| 8 | `xz` | 0.012868 |
| 9 | `tk` | 0.012196 |
| 10 | `readline` | 0.011881 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `python` | 0.007094 |
| 2 | `libgcc-ng` | 0.000877 |
| 3 | `sqlite` | 0.000656 |
| 4 | `numpy` | 0.000527 |
| 5 | `dask` | 0.000214 |
| 6 | `tensorflow` | 0.000180 |
| 7 | `notebook` | 0.000165 |
| 8 | `tensorflow-base` | 0.000148 |
| 9 | `libopencv` | 0.000132 |
| 10 | `libgdal` | 0.000118 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.156843 |
| **Comunidades Detectadas (Louvain)** | 74 |
| **Modularidade** | 0.5542 |

---
*Análise concluída em 1.28 segundos.*


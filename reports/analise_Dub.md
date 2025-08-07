# Análise do Grafo: Dub

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 1,161 |
| **Arestas (Dependências)** | 1,383 |
| **Densidade do Grafo** | 0.00102691 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 93 |
| **Nós no Maior Componente (LCC)** | 780 (67.18%) |
| **Arestas no Maior Componente (LCC)** | 1,076 (77.80%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 1.19 | 1.19 | 2.38 |
| **Mediana** | 1.00 | 1.00 | 1.00 |
| **Máximo** | 70 | 21 | 76 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
| 1 | `derelict-util` | 70 |
| 2 | `vibe-d` | 63 |
| 3 | `derelict-sdl2` | 25 |
| 4 | `vibe-d:data` | 25 |
| 5 | `derelict-gl3` | 24 |
| 6 | `vibe-d:http` | 18 |
| 7 | `pegged` | 17 |
| 8 | `vibe-d:core` | 16 |
| 9 | `openssl` | 15 |
| 10 | `hunt` | 15 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|---|---|---|
| 1 | `arsd-official` | 21 |
| 2 | `soupply` | 18 |
| 3 | `selery` | 17 |
| 4 | `dplug` | 16 |
| 5 | `vibe-d` | 13 |
| 6 | `armos` | 13 |
| 7 | `tsv-utils-dlang` | 12 |
| 8 | `aurorafw` | 12 |
| 9 | `tsv-utils` | 12 |
| 10 | `evael` | 12 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|---|---|---|
| 1 | `derelict-util` | 0.060536 |
| 2 | `vibe-d` | 0.029374 |
| 3 | `mir-core` | 0.022981 |
| 4 | `stdx-allocator` | 0.018380 |
| 5 | `vibe-d:data` | 0.013662 |
| 6 | `taggedalgebraic` | 0.010843 |
| 7 | `pegged` | 0.009873 |
| 8 | `derelict-sdl2` | 0.008482 |
| 9 | `tinyendian` | 0.008188 |
| 10 | `openssl` | 0.007783 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `vibe-d` | 0.001625 |
| 2 | `unit-threaded` | 0.000144 |
| 3 | `stdx-allocator` | 0.000108 |
| 4 | `fluent-asserts` | 0.000108 |
| 5 | `vibe-core` | 0.000103 |
| 6 | `libdparse` | 0.000074 |
| 7 | `uim-html` | 0.000071 |
| 8 | `dlangui` | 0.000059 |
| 9 | `mysql-native` | 0.000052 |
| 10 | `soupply` | 0.000046 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.032632 |
| **Comunidades Detectadas (Louvain)** | 112 |
| **Modularidade** | 0.8532 |

---
*Análise concluída em 1.38 segundos.*


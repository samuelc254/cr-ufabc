# Análise do Grafo: Hex

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 5,706 |
| **Arestas (Dependências)** | 11,201 |
| **Densidade do Grafo** | 0.00034409 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 119 |
| **Nós no Maior Componente (LCC)** | 5,403 (94.69%) |
| **Arestas no Maior Componente (LCC)** | 11,000 (98.21%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 1.96 | 1.96 | 3.93 |
| **Mediana** | 0.00 | 2.00 | 2.00 |
| **Máximo** | 1,048 | 24 | 1,048 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
| 1 | `poison` | 1,048 |
| 2 | `httpoison` | 893 |
| 3 | `jason` | 485 |
| 4 | `plug` | 445 |
| 5 | `ecto` | 351 |
| 6 | `timex` | 192 |
| 7 | `hackney` | 191 |
| 8 | `google_gax` | 168 |
| 9 | `cowboy` | 165 |
| 10 | `phoenix` | 137 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|---|---|---|
| 1 | `ejabberd` | 24 |
| 2 | `fulib` | 24 |
| 3 | `islands_engine` | 21 |
| 4 | `rig` | 16 |
| 5 | `materia` | 16 |
| 6 | `riak_core_ng` | 15 |
| 7 | `riak_core_ng_up` | 15 |
| 8 | `sentinel` | 14 |
| 9 | `ex_admin_runtime` | 14 |
| 10 | `ami_models` | 14 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|---|---|---|
| 1 | `poison` | 0.038199 |
| 2 | `hackney` | 0.031532 |
| 3 | `decimal` | 0.030116 |
| 4 | `httpoison` | 0.027000 |
| 5 | `plug` | 0.023849 |
| 6 | `jason` | 0.023641 |
| 7 | `ecto` | 0.013673 |
| 8 | `google_gax` | 0.011859 |
| 9 | `telemetry` | 0.010527 |
| 10 | `elixir_make` | 0.008372 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `hackney` | 0.000339 |
| 2 | `httpoison` | 0.000241 |
| 3 | `tesla` | 0.000186 |
| 4 | `google_gax` | 0.000140 |
| 5 | `plug` | 0.000084 |
| 6 | `phoenix` | 0.000067 |
| 7 | `idna` | 0.000057 |
| 8 | `jason` | 0.000034 |
| 9 | `timex` | 0.000032 |
| 10 | `cowboy` | 0.000030 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.040453 |
| **Comunidades Detectadas (Louvain)** | 151 |
| **Modularidade** | 0.6516 |

---
*Análise concluída em 6.71 segundos.*


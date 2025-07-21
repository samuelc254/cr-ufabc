# Análise do Grafo: Cargo

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 24,305 |
| **Arestas (Dependências)** | 115,856 |
| **Densidade do Grafo** | 0.00019613 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 152 |
| **Nós no Maior Componente (LCC)** | 23,951 (98.54%) |
| **Arestas no Maior Componente (LCC)** | 115,628 (99.80%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 4.77 | 4.77 | 9.53 |
| **Mediana** | 0.00 | 3.00 | 4.00 |
| **Máximo** | 5,175 | 77 | 5,176 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
| 1 | `serde` | 5,175 |
| 2 | `serde_json` | 3,580 |
| 3 | `log` | 3,193 |
| 4 | `serde_derive` | 3,108 |
| 5 | `rand` | 2,538 |
| 6 | `libc` | 2,410 |
| 7 | `clap` | 2,251 |
| 8 | `lazy_static` | 2,213 |
| 9 | `futures` | 1,699 |
| 10 | `failure` | 1,697 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|---|---|---|
| 1 | `sccache` | 77 |
| 2 | `sn0int` | 74 |
| 3 | `solana` | 63 |
| 4 | `solana-core` | 63 |
| 5 | `rustpython-vm` | 59 |
| 6 | `snowchains` | 57 |
| 7 | `cargo` | 55 |
| 8 | `exonum` | 53 |
| 9 | `ciruela` | 52 |
| 10 | `cargo-semverver` | 52 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|---|---|---|
| 1 | `serde_derive` | 0.036235 |
| 2 | `serde` | 0.030830 |
| 3 | `quote` | 0.030196 |
| 4 | `proc-macro2` | 0.025523 |
| 5 | `libc` | 0.018776 |
| 6 | `rand` | 0.018686 |
| 7 | `syn` | 0.018169 |
| 8 | `unicode-xid` | 0.012141 |
| 9 | `winapi` | 0.011835 |
| 10 | `serde_json` | 0.010846 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `syn` | 0.004509 |
| 2 | `flate2` | 0.003202 |
| 3 | `serde_derive` | 0.001940 |
| 4 | `tokio` | 0.001667 |
| 5 | `tokio-tcp` | 0.001574 |
| 6 | `parking_lot` | 0.001524 |
| 7 | `rand_core` | 0.001520 |
| 8 | `clap` | 0.001397 |
| 9 | `parking_lot_core` | 0.001369 |
| 10 | `backtrace` | 0.001350 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.114293 |
| **Comunidades Detectadas (Louvain)** | 183 |
| **Modularidade** | 0.4845 |

---
*Análise concluída em 54.33 segundos.*


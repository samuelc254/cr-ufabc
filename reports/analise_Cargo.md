# Análise Completa do Grafo: Cargo

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 24,305 |
| **Arestas** | 115,856 |
| **Densidade** | 0.00019613 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 24,016 |
| **Componentes Fracamente Conectados (WCC)** | 152 |
| **Maior SCC** | 164 nós |
| **Maior WCC** | 23,951 nós |
| **Nós no Maior Componente** | 23,951 (98.54%) |
| **Arestas no Maior Componente** | 115,628 (99.80%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 9.53 |
| **Grau Máximo** | 5,176 |
| **Grau Mediano** | 4.00 |
| **In-Degree Médio** | 4.77 |
| **In-Degree Máximo** | 5,175 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 4.77 |
| **Out-Degree Máximo** | 77 |
| **Out-Degree Mediano** | 3.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
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
|------|---------|------------|
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
|------|-----|----------------|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `syn` | 0.004625 |
| 2 | `flate2` | 0.003214 |
| 3 | `serde_derive` | 0.002237 |
| 4 | `tokio` | 0.001792 |
| 5 | `parking_lot` | 0.001605 |
| 6 | `tokio-tcp` | 0.001576 |
| 7 | `parking_lot_core` | 0.001425 |
| 8 | `rand_core` | 0.001408 |
| 9 | `backtrace` | 0.001347 |
| 10 | `tokio-reactor` | 0.001285 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.114293 |
| **Comunidades Detectadas (Louvain)** | 183 |
| **Modularidade** | 0.4845 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 18 |
| **Método** | Aproximado |
| **Componente Analisado** | 164 nós (0.7%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **24,305 nós** e **115,856 arestas**.
O diâmetro aproximado é **18**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 98.5% dos nós, 
com densidade de 0.000196.

---
*Análise concluída em 51.61 segundos.*
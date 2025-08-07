# Análise do Grafo: CRAN

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 15,413 |
| **Arestas (Dependências)** | 102,241 |
| **Densidade do Grafo** | 0.00043041 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 3 |
| **Nós no Maior Componente (LCC)** | 15,409 (99.97%) |
| **Arestas no Maior Componente (LCC)** | 102,239 (100.00%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 6.63 | 6.63 | 13.27 |
| **Mediana** | 0.00 | 5.00 | 6.00 |
| **Máximo** | 9,587 | 107 | 9,587 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
| 1 | `R` | 9,587 |
| 2 | `knitr` | 4,239 |
| 3 | `testthat` | 4,080 |
| 4 | `stats` | 3,777 |
| 5 | `rmarkdown` | 3,257 |
| 6 | `methods` | 2,728 |
| 7 | `ggplot2` | 2,442 |
| 8 | `utils` | 2,302 |
| 9 | `graphics` | 1,889 |
| 10 | `Rcpp` | 1,792 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|---|---|---|
| 1 | `mlr` | 107 |
| 2 | `broom` | 81 |
| 3 | `fitteR` | 76 |
| 4 | `rattle` | 67 |
| 5 | `Seurat` | 60 |
| 6 | `fscaret` | 59 |
| 7 | `nlmixr` | 52 |
| 8 | `BiodiversityR` | 49 |
| 9 | `RxODE` | 49 |
| 10 | `CNVScope` | 49 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|---|---|---|
| 1 | `R` | 0.093825 |
| 2 | `testthat` | 0.026385 |
| 3 | `methods` | 0.025335 |
| 4 | `stats` | 0.025040 |
| 5 | `knitr` | 0.021490 |
| 6 | `utils` | 0.017440 |
| 7 | `rmarkdown` | 0.015607 |
| 8 | `graphics` | 0.013062 |
| 9 | `MASS` | 0.011680 |
| 10 | `Rcpp` | 0.011633 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `broom` | 0.019051 |
| 2 | `dplyr` | 0.016171 |
| 3 | `Hmisc` | 0.015483 |
| 4 | `ggplot2` | 0.015317 |
| 5 | `knitr` | 0.015122 |
| 6 | `mice` | 0.010724 |
| 7 | `caret` | 0.009188 |
| 8 | `styler` | 0.007171 |
| 9 | `earth` | 0.006567 |
| 10 | `nlme` | 0.006489 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.176208 |
| **Comunidades Detectadas (Louvain)** | 16 |
| **Modularidade** | 0.3258 |

---
*Análise concluída em 54.49 segundos.*


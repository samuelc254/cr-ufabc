# Análise Completa do Grafo: CRAN

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 15,413 |
| **Arestas** | 102,241 |
| **Densidade** | 0.00043041 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 14,386 |
| **Componentes Fracamente Conectados (WCC)** | 3 |
| **Maior SCC** | 882 nós |
| **Maior WCC** | 15,409 nós |
| **Nós no Maior Componente** | 15,409 (99.97%) |
| **Arestas no Maior Componente** | 102,239 (100.00%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 13.27 |
| **Grau Máximo** | 9,587 |
| **Grau Mediano** | 6.00 |
| **In-Degree Médio** | 6.63 |
| **In-Degree Máximo** | 9,587 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 6.63 |
| **Out-Degree Máximo** | 107 |
| **Out-Degree Mediano** | 5.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
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
|------|---------|------------|
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
|------|-----|----------------|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `broom` | 0.019273 |
| 2 | `dplyr` | 0.017341 |
| 3 | `knitr` | 0.015418 |
| 4 | `Hmisc` | 0.015339 |
| 5 | `ggplot2` | 0.014547 |
| 6 | `mice` | 0.010068 |
| 7 | `caret` | 0.008864 |
| 8 | `testthat` | 0.007677 |
| 9 | `styler` | 0.007480 |
| 10 | `nlme` | 0.007129 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.176208 |
| **Comunidades Detectadas (Louvain)** | 16 |
| **Modularidade** | 0.3258 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 17 |
| **Método** | Aproximado |
| **Componente Analisado** | 882 nós (5.7%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **15,413 nós** e **102,241 arestas**.
O diâmetro aproximado é **17**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 100.0% dos nós, 
com densidade de 0.000430.

---
*Análise concluída em 47.77 segundos.*
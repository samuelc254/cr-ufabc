# Análise Completa do Grafo: Conda

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 1,270 |
| **Arestas** | 2,866 |
| **Densidade** | 0.00177832 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 1,270 |
| **Componentes Fracamente Conectados (WCC)** | 63 |
| **Maior SCC** | 1 nós |
| **Maior WCC** | 959 nós |
| **Nós no Maior Componente** | 959 (75.51%) |
| **Arestas no Maior Componente** | 2,565 (89.50%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 4.51 |
| **Grau Máximo** | 546 |
| **Grau Mediano** | 2.00 |
| **In-Degree Médio** | 2.26 |
| **In-Degree Máximo** | 536 |
| **In-Degree Mediano** | 1.00 |
| **Out-Degree Médio** | 2.26 |
| **Out-Degree Máximo** | 275 |
| **Out-Degree Mediano** | 1.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
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
|------|---------|------------|
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
|------|-----|----------------|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `python` | 0.007259 |
| 2 | `libgcc-ng` | 0.000867 |
| 3 | `sqlite` | 0.000667 |
| 4 | `numpy` | 0.000585 |
| 5 | `libmxnet` | 0.000239 |
| 6 | `libopencv` | 0.000213 |
| 7 | `mxnet` | 0.000193 |
| 8 | `bokeh` | 0.000186 |
| 9 | `notebook` | 0.000160 |
| 10 | `dask` | 0.000155 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.156843 |
| **Comunidades Detectadas (Louvain)** | 74 |
| **Modularidade** | 0.5542 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 0 |
| **Método** | Aproximado |
| **Componente Analisado** | 1 nós (0.1%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **1,270 nós** e **2,866 arestas**.
O diâmetro aproximado é **0**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 75.5% dos nós, 
com densidade de 0.001778.

---
*Análise concluída em 1.48 segundos.*
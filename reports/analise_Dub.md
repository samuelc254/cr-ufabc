# Análise Completa do Grafo: Dub

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 1,161 |
| **Arestas** | 1,383 |
| **Densidade** | 0.00102691 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 1,161 |
| **Componentes Fracamente Conectados (WCC)** | 93 |
| **Maior SCC** | 1 nós |
| **Maior WCC** | 780 nós |
| **Nós no Maior Componente** | 780 (67.18%) |
| **Arestas no Maior Componente** | 1,076 (77.80%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 2.38 |
| **Grau Máximo** | 76 |
| **Grau Mediano** | 1.00 |
| **In-Degree Médio** | 1.19 |
| **In-Degree Máximo** | 70 |
| **In-Degree Mediano** | 1.00 |
| **Out-Degree Médio** | 1.19 |
| **Out-Degree Máximo** | 21 |
| **Out-Degree Mediano** | 1.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
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
|------|---------|------------|
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
|------|-----|----------------|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `vibe-d` | 0.001628 |
| 2 | `unit-threaded` | 0.000126 |
| 3 | `vibe-core` | 0.000113 |
| 4 | `fluent-asserts` | 0.000108 |
| 5 | `stdx-allocator` | 0.000095 |
| 6 | `dlangui` | 0.000090 |
| 7 | `libdparse` | 0.000048 |
| 8 | `mir-lapack` | 0.000046 |
| 9 | `soupply` | 0.000046 |
| 10 | `mysql-native` | 0.000039 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.032632 |
| **Comunidades Detectadas (Louvain)** | 112 |
| **Modularidade** | 0.8532 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 0 |
| **Método** | Aproximado |
| **Componente Analisado** | 1 nós (0.1%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **1,161 nós** e **1,383 arestas**.
O diâmetro aproximado é **0**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 67.2% dos nós, 
com densidade de 0.001027.

---
*Análise concluída em 1.38 segundos.*
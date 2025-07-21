# Análise do Grafo: Elm

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 1,474 |
| **Arestas (Dependências)** | 3,781 |
| **Densidade do Grafo** | 0.00174143 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 1 |
| **Nós no Maior Componente (LCC)** | 1,474 (100.00%) |
| **Arestas no Maior Componente (LCC)** | 3,781 (100.00%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 2.57 | 2.57 | 5.13 |
| **Mediana** | 0.00 | 2.00 | 3.00 |
| **Máximo** | 1,467 | 16 | 1,467 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
| 1 | `elm-lang/core` | 1,467 |
| 2 | `elm-lang/html` | 628 |
| 3 | `elm-lang/http` | 123 |
| 4 | `elm-lang/svg` | 102 |
| 5 | `elm-community/list-extra` | 82 |
| 6 | `NoRedInk/elm-decode-pipeline` | 48 |
| 7 | `rtfeldman/elm-css` | 43 |
| 8 | `elm-community/elm-test` | 39 |
| 9 | `elm-lang/mouse` | 37 |
| 10 | `elm-lang/navigation` | 31 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|---|---|---|
| 1 | `cmditch/mel-bew3` | 16 |
| 2 | `Gizra/elm-essentials` | 13 |
| 3 | `williamwhitacre/scaffold` | 12 |
| 4 | `elm-bodybuilder/elegant` | 12 |
| 5 | `lucamug/elm-style-framework` | 12 |
| 6 | `williamwhitacre/gigan` | 10 |
| 7 | `xarvh/elm-slides` | 10 |
| 8 | `micktwomey/elmo-8` | 10 |
| 9 | `NoRedInk/elm-doodad` | 10 |
| 10 | `folkertdev/one-true-path-experiment` | 9 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|---|---|---|
| 1 | `elm-lang/core` | 0.339190 |
| 2 | `elm-lang/html` | 0.063411 |
| 3 | `elm-lang/virtual-dom` | 0.031589 |
| 4 | `elm-lang/http` | 0.010381 |
| 5 | `elm-lang/svg` | 0.007007 |
| 6 | `elm-community/list-extra` | 0.005940 |
| 7 | `elm-lang/dom` | 0.004808 |
| 8 | `elm-lang/lazy` | 0.003664 |
| 9 | `elm-community/elm-test` | 0.003423 |
| 10 | `rtfeldman/elm-css` | 0.003258 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `elm-lang/html` | 0.000275 |
| 2 | `elm-community/elm-test` | 0.000104 |
| 3 | `rtfeldman/elm-css` | 0.000084 |
| 4 | `elm-lang/svg` | 0.000028 |
| 5 | `elm-lang/navigation` | 0.000020 |
| 6 | `Bogdanp/elm-combine` | 0.000018 |
| 7 | `elm-lang/mouse` | 0.000016 |
| 8 | `gampleman/elm-visualization` | 0.000012 |
| 9 | `folkertdev/one-true-path-experiment` | 0.000012 |
| 10 | `rundis/elm-bootstrap` | 0.000012 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.300517 |
| **Comunidades Detectadas (Louvain)** | 12 |
| **Modularidade** | 0.3852 |

---
*Análise concluída em 1.99 segundos.*


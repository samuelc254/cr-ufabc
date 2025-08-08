# Análise Completa do Grafo: Elm

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 1,474 |
| **Arestas** | 3,781 |
| **Densidade** | 0.00174143 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 1,474 |
| **Componentes Fracamente Conectados (WCC)** | 1 |
| **Maior SCC** | 1 nós |
| **Maior WCC** | 1,474 nós |
| **Nós no Maior Componente** | 1,474 (100.00%) |
| **Arestas no Maior Componente** | 3,781 (100.00%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 5.13 |
| **Grau Máximo** | 1,467 |
| **Grau Mediano** | 3.00 |
| **In-Degree Médio** | 2.57 |
| **In-Degree Máximo** | 1,467 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 2.57 |
| **Out-Degree Máximo** | 16 |
| **Out-Degree Mediano** | 2.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
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
|------|---------|------------|
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
|------|-----|----------------|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `elm-lang/html` | 0.000281 |
| 2 | `elm-community/elm-test` | 0.000079 |
| 3 | `rtfeldman/elm-css` | 0.000044 |
| 4 | `elm-lang/svg` | 0.000032 |
| 5 | `elm-community/elm-check` | 0.000023 |
| 6 | `elm-lang/navigation` | 0.000018 |
| 7 | `Gizra/elm-essentials` | 0.000016 |
| 8 | `elm-tools/parser` | 0.000015 |
| 9 | `drathier/elm-graph` | 0.000014 |
| 10 | `RGBboy/websocket-server` | 0.000012 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.300517 |
| **Comunidades Detectadas (Louvain)** | 12 |
| **Modularidade** | 0.3852 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 0 |
| **Método** | Aproximado |
| **Componente Analisado** | 1 nós (0.1%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **1,474 nós** e **3,781 arestas**.
O diâmetro aproximado é **0**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 100.0% dos nós, 
com densidade de 0.001741.

---
*Análise concluída em 1.75 segundos.*
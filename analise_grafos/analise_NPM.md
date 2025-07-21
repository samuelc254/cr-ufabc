# Análise do Grafo: NPM

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 1,036,048 |
| **Arestas (Dependências)** | 11,134,428 |
| **Densidade do Grafo** | 0.00001037 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 4,316 |
| **Nós no Maior Componente (LCC)** | 1,022,526 (98.69%) |
| **Arestas no Maior Componente (LCC)** | 11,119,666 (99.87%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 10.75 | 10.75 | 21.49 |
| **Mediana** | 0.00 | 6.00 | 7.00 |
| **Máximo** | 189,564 | 1,000 | 189,648 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
| 1 | `mocha` | 189,564 |
| 2 | `eslint` | 177,187 |
| 3 | `typescript` | 128,457 |
| 4 | `chai` | 117,181 |
| 5 | `webpack` | 116,019 |
| 6 | `babel-core` | 111,274 |
| 7 | `babel-loader` | 99,117 |
| 8 | `react` | 95,439 |
| 9 | `lodash` | 93,109 |
| 10 | `jest` | 88,203 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|---|---|---|
| 1 | `sindresorhus.js` | 1,000 |
| 2 | `npm-bomb` | 999 |
| 3 | `1000-packages` | 999 |
| 4 | `all-of-them` | 989 |
| 5 | `digital-keyboard-demos` | 975 |
| 6 | `@hawkingnetwork/react-native-tab-view` | 921 |
| 7 | `@ericmcornelius/ease` | 905 |
| 8 | `vue-compment` | 895 |
| 9 | `nois-react-toast` | 873 |
| 10 | `@vuga/react-demo` | 846 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|---|---|---|
| 1 | `mocha` | 0.021679 |
| 2 | `eslint` | 0.014611 |
| 3 | `chai` | 0.007349 |
| 4 | `tslib` | 0.007247 |
| 5 | `typescript` | 0.006922 |
| 6 | `tape` | 0.006882 |
| 7 | `@types/node` | 0.006784 |
| 8 | `lodash` | 0.006597 |
| 9 | `tap` | 0.006303 |
| 10 | `rimraf` | 0.005755 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `mocha` | 0.003020 |
| 2 | `eslint` | 0.002245 |
| 3 | `typescript` | 0.001438 |
| 4 | `webpack` | 0.000729 |
| 5 | `electron` | 0.000685 |
| 6 | `@electron/get` | 0.000684 |
| 7 | `global-agent` | 0.000676 |
| 8 | `airtap` | 0.000657 |
| 9 | `antd` | 0.000655 |
| 10 | `anyproxy` | 0.000652 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.123555 |
| **Comunidades Detectadas (Louvain)** | 5,428 |
| **Modularidade** | 0.4848 |

---
*Análise concluída em 93969.64 segundos.*


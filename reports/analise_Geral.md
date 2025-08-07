# Análise do Grafo: Geral

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 1,758,429 |
| **Arestas (Dependências)** | 14,078,099 |
| **Densidade do Grafo** | 0.00000455 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 11,301 |
| **Nós no Maior Componente (LCC)** | 1,604,174 (91.23%) |
| **Arestas no Maior Componente (LCC)** | 13,504,283 (95.92%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 8.01 | 8.01 | 16.01 |
| **Mediana** | 0.00 | 4.00 | 5.00 |
| **Máximo** | 192,961 | 1,000 | 193,045 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
| 1 | `mocha` | 192,961 |
| 2 | `eslint` | 177,661 |
| 3 | `typescript` | 128,561 |
| 4 | `chai` | 117,227 |
| 5 | `webpack` | 116,054 |
| 6 | `babel-core` | 111,311 |
| 7 | `babel-loader` | 99,137 |
| 8 | `react` | 95,553 |
| 9 | `lodash` | 93,358 |
| 10 | `jest` | 88,218 |

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
| 10 | `org.springframework.boot:spring-boot-dependencies` | 856 |

## 4. Análise de Centralidade
_(Análise realizada em uma amostra de 200,000 nós do maior componente (Betweenness aproximado com k=1000))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|---|---|---|
| 1 | `mkdirp` | 0.019664 |
| 2 | `mock-fs` | 0.019409 |
| 3 | `eslint-plugin-import` | 0.016975 |
| 4 | `jest` | 0.016138 |
| 5 | `babel-core` | 0.014131 |
| 6 | `rspec` | 0.013571 |
| 7 | `webpack` | 0.012042 |
| 8 | `sinon` | 0.011489 |
| 9 | `istanbul` | 0.011411 |
| 10 | `@babel/preset-env` | 0.011333 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `rollup` | 0.000049 |
| 2 | `webpack` | 0.000046 |
| 3 | `async` | 0.000043 |
| 4 | `core-js` | 0.000027 |
| 5 | `eslint-plugin-import` | 0.000026 |
| 6 | `karma` | 0.000026 |
| 7 | `@babel/preset-env` | 0.000025 |
| 8 | `istanbul` | 0.000023 |
| 9 | `airtap` | 0.000021 |
| 10 | `redux` | 0.000019 |

---
*Análise concluída em 1554.93 segundos.*


# Análise Completa do Grafo: NPM

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 1,036,048 |
| **Arestas** | 11,134,428 |
| **Densidade** | 0.00001037 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 1,016,856 |
| **Componentes Fracamente Conectados (WCC)** | 4,316 |
| **Maior SCC** | 13,026 nós |
| **Maior WCC** | 1,022,526 nós |
| **Nós no Maior Componente** | 1,022,526 (98.69%) |
| **Arestas no Maior Componente** | 11,119,666 (99.87%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 21.49 |
| **Grau Máximo** | 189,648 |
| **Grau Mediano** | 7.00 |
| **In-Degree Médio** | 10.75 |
| **In-Degree Máximo** | 189,564 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 10.75 |
| **Out-Degree Máximo** | 1,000 |
| **Out-Degree Mediano** | 6.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
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
|------|---------|------------|
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
|------|-----|----------------|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `mocha` | 0.002967 |
| 2 | `eslint` | 0.002387 |
| 3 | `typescript` | 0.001337 |
| 4 | `webpack` | 0.000848 |
| 5 | `electron` | 0.000688 |
| 6 | `@electron/get` | 0.000687 |
| 7 | `global-agent` | 0.000681 |
| 8 | `airtap` | 0.000666 |
| 9 | `anyproxy` | 0.000658 |
| 10 | `antd` | 0.000658 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.123555 |
| **Comunidades Detectadas (Louvain)** | 5,428 |
| **Modularidade** | 0.4848 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 25 |
| **Método** | Aproximado |
| **Componente Analisado** | 13,026 nós (1.3%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **1,036,048 nós** e **11,134,428 arestas**.
O diâmetro aproximado é **25**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 98.7% dos nós, 
com densidade de 0.000010.

---
*Análise concluída em 71351.25 segundos.*
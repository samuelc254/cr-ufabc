# Análise Completa do Grafo: Geral

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 1,758,429 |
| **Arestas** | 14,078,099 |
| **Densidade** | 0.00000455 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 1,730,853 |
| **Componentes Fracamente Conectados (WCC)** | 11,301 |
| **Maior SCC** | 18,413 nós |
| **Maior WCC** | 1,604,174 nós |
| **Nós no Maior Componente** | 1,604,174 (91.23%) |
| **Arestas no Maior Componente** | 13,504,283 (95.92%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 16.01 |
| **Grau Máximo** | 193,045 |
| **Grau Mediano** | 5.00 |
| **In-Degree Médio** | 8.01 |
| **In-Degree Máximo** | 192,961 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 8.01 |
| **Out-Degree Máximo** | 1,000 |
| **Out-Degree Mediano** | 4.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
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
| 10 | `org.springframework.boot:spring-boot-dependencies` | 856 |

## 4. Análise de Centralidade
_(Análise realizada em uma amostra de 200,000 nós do maior componente (Betweenness aproximado com k=1000))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `typescript` | 0.035260 |
| 2 | `rimraf` | 0.022145 |
| 3 | `rake` | 0.019209 |
| 4 | `should` | 0.013553 |
| 5 | `husky` | 0.011594 |
| 6 | `nyc` | 0.011314 |
| 7 | `express` | 0.009337 |
| 8 | `debug` | 0.008063 |
| 9 | `karma` | 0.007316 |
| 10 | `prop-types` | 0.006701 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `typescript` | 0.000039 |
| 2 | `node-fetch` | 0.000015 |
| 3 | `karma` | 0.000014 |
| 4 | `gulp-rename` | 0.000013 |
| 5 | `husky` | 0.000012 |
| 6 | `jscs` | 0.000012 |
| 7 | `abort-controller` | 0.000012 |
| 8 | `express` | 0.000010 |
| 9 | `should` | 0.000008 |
| 10 | `range-parser` | 0.000005 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 30 |
| **Método** | Aproximado |
| **Componente Analisado** | 18,413 nós (1.0%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **1,758,429 nós** e **14,078,099 arestas**.
O diâmetro aproximado é **30**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 91.2% dos nós, 
com densidade de 0.000005.

---
*Análise concluída em 1541.54 segundos.*
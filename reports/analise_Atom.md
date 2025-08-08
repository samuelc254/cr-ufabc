# Análise Completa do Grafo: Atom

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 7,243 |
| **Arestas** | 17,128 |
| **Densidade** | 0.00032653 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 7,243 |
| **Componentes Fracamente Conectados (WCC)** | 222 |
| **Maior SCC** | 1 nós |
| **Maior WCC** | 6,770 nós |
| **Nós no Maior Componente** | 6,770 (93.47%) |
| **Arestas no Maior Componente** | 16,861 (98.44%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 4.73 |
| **Grau Máximo** | 840 |
| **Grau Mediano** | 2.00 |
| **In-Degree Médio** | 2.36 |
| **In-Degree Máximo** | 840 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 2.36 |
| **Out-Degree Máximo** | 162 |
| **Out-Degree Mediano** | 1.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `atom-space-pen-views` | 840 |
| 2 | `atom-package-deps` | 576 |
| 3 | `eslint` | 478 |
| 4 | `fs-plus` | 388 |
| 5 | `underscore-plus` | 372 |
| 6 | `atom-linter` | 266 |
| 7 | `coffeelint` | 247 |
| 8 | `jquery` | 241 |
| 9 | `lodash` | 239 |
| 10 | `request` | 220 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `nuclide` | 162 |
| 2 | `mstest2` | 70 |
| 3 | `mstest1` | 69 |
| 4 | `metasota-package-4` | 62 |
| 5 | `build-ibmstreams` | 53 |
| 6 | `etheratom` | 52 |
| 7 | `veda` | 50 |
| 8 | `touchbar-plus` | 44 |
| 9 | `prettier-atom` | 43 |
| 10 | `markdown-preview-plus` | 42 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `atom-space-pen-views` | 0.028087 |
| 2 | `atom-package-deps` | 0.017456 |
| 3 | `coffeelint` | 0.013775 |
| 4 | `underscore-plus` | 0.011199 |
| 5 | `jquery` | 0.009290 |
| 6 | `fs-plus` | 0.008387 |
| 7 | `eslint` | 0.007921 |
| 8 | `atom-linter` | 0.007648 |
| 9 | `request` | 0.006801 |
| 10 | `lodash` | 0.006387 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `atom-languageclient` | 0.000026 |
| 2 | `autocomplete-plus` | 0.000004 |
| 3 | `ionide-fsharp` | 0.000001 |
| 4 | `language-c` | 0.000001 |
| 5 | `jsfmt` | 0.000000 |
| 6 | `achievements` | 0.000000 |
| 7 | `atom-space-pen-views` | 0.000000 |
| 8 | `advanced-new-file` | 0.000000 |
| 9 | `touch` | 0.000000 |
| 10 | `mkdirp` | 0.000000 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.001505 |
| **Comunidades Detectadas (Louvain)** | 254 |
| **Modularidade** | 0.6067 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 0 |
| **Método** | Aproximado |
| **Componente Analisado** | 1 nós (0.0%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **7,243 nós** e **17,128 arestas**.
O diâmetro aproximado é **0**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 93.5% dos nós, 
com densidade de 0.000327.

---
*Análise concluída em 9.85 segundos.*
# Análise do Grafo: Atom

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 7,243 |
| **Arestas (Dependências)** | 17,128 |
| **Densidade do Grafo** | 0.00032653 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 222 |
| **Nós no Maior Componente (LCC)** | 6,770 (93.47%) |
| **Arestas no Maior Componente (LCC)** | 16,861 (98.44%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 2.36 | 2.36 | 4.73 |
| **Mediana** | 0.00 | 1.00 | 2.00 |
| **Máximo** | 840 | 162 | 840 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
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
|---|---|---|
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
|---|---|---|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `atom-languageclient` | 0.000039 |
| 2 | `remote-ftp` | 0.000004 |
| 3 | `autocomplete-plus` | 0.000004 |
| 4 | `zestyio-api-wrapper` | 0.000001 |
| 5 | `achievements` | 0.000000 |
| 6 | `atom-space-pen-views` | 0.000000 |
| 7 | `advanced-new-file` | 0.000000 |
| 8 | `touch` | 0.000000 |
| 9 | `mkdirp` | 0.000000 |
| 10 | `adwaita-pro-ui` | 0.000000 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.001505 |
| **Comunidades Detectadas (Louvain)** | 254 |
| **Modularidade** | 0.6067 |

---
*Análise concluída em 8.60 segundos.*


# Análise do Grafo: Rubygems

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 128,010 |
| **Arestas (Dependências)** | 578,076 |
| **Densidade do Grafo** | 0.00003528 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 366 |
| **Nós no Maior Componente (LCC)** | 127,085 (99.28%) |
| **Arestas no Maior Componente (LCC)** | 577,479 (99.90%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 4.52 | 4.52 | 9.03 |
| **Mediana** | 0.00 | 4.00 | 4.00 |
| **Máximo** | 67,698 | 220 | 67,703 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
| 1 | `rake` | 67,698 |
| 2 | `bundler` | 59,684 |
| 3 | `rspec` | 48,867 |
| 4 | `pry` | 11,179 |
| 5 | `rails` | 10,459 |
| 6 | `minitest` | 9,957 |
| 7 | `activesupport` | 9,846 |
| 8 | `simplecov` | 9,269 |
| 9 | `rubocop` | 7,460 |
| 10 | `sqlite3` | 7,260 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|---|---|---|
| 1 | `aws-sdk-resources` | 220 |
| 2 | `azure_sdk` | 136 |
| 3 | `rubysl` | 91 |
| 4 | `voluntary` | 82 |
| 5 | `backedup` | 82 |
| 6 | `workarea-core` | 81 |
| 7 | `hyrax` | 71 |
| 8 | `atreides` | 68 |
| 9 | `renalware-core` | 68 |
| 10 | `benmanns-atreides` | 67 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|---|---|---|
| 1 | `rake` | 0.069164 |
| 2 | `bundler` | 0.056957 |
| 3 | `rspec` | 0.043198 |
| 4 | `minitest` | 0.039396 |
| 5 | `rdoc` | 0.036265 |
| 6 | `rubocop` | 0.027407 |
| 7 | `hoe` | 0.025895 |
| 8 | `rspec-expectations` | 0.013112 |
| 9 | `activesupport` | 0.013100 |
| 10 | `coveralls` | 0.013083 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `rubocop` | 0.001069 |
| 2 | `parser` | 0.001001 |
| 3 | `simplecov` | 0.000706 |
| 4 | `docile` | 0.000691 |
| 5 | `github-markup` | 0.000677 |
| 6 | `github-linguist` | 0.000596 |
| 7 | `ast` | 0.000584 |
| 8 | `rake` | 0.000546 |
| 9 | `rest-client` | 0.000480 |
| 10 | `webmock` | 0.000441 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.197035 |
| **Comunidades Detectadas (Louvain)** | 420 |
| **Modularidade** | 0.3968 |

---
*Análise concluída em 2809.41 segundos.*


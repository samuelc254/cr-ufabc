# Análise Completa do Grafo: Rubygems

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 128,010 |
| **Arestas** | 578,076 |
| **Densidade** | 0.00003528 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 127,564 |
| **Componentes Fracamente Conectados (WCC)** | 366 |
| **Maior SCC** | 241 nós |
| **Maior WCC** | 127,085 nós |
| **Nós no Maior Componente** | 127,085 (99.28%) |
| **Arestas no Maior Componente** | 577,479 (99.90%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 9.03 |
| **Grau Máximo** | 67,703 |
| **Grau Mediano** | 4.00 |
| **In-Degree Médio** | 4.52 |
| **In-Degree Máximo** | 67,698 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 4.52 |
| **Out-Degree Máximo** | 220 |
| **Out-Degree Mediano** | 4.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
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
|------|---------|------------|
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
|------|-----|----------------|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `rubocop` | 0.001078 |
| 2 | `parser` | 0.001005 |
| 3 | `simplecov` | 0.000737 |
| 4 | `docile` | 0.000722 |
| 5 | `github-markup` | 0.000708 |
| 6 | `github-linguist` | 0.000624 |
| 7 | `ast` | 0.000584 |
| 8 | `rake` | 0.000571 |
| 9 | `rest-client` | 0.000471 |
| 10 | `webmock` | 0.000459 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.197035 |
| **Comunidades Detectadas (Louvain)** | 420 |
| **Modularidade** | 0.3968 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 17 |
| **Método** | Aproximado |
| **Componente Analisado** | 241 nós (0.2%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **128,010 nós** e **578,076 arestas**.
O diâmetro aproximado é **17**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 99.3% dos nós, 
com densidade de 0.000035.

---
*Análise concluída em 2700.12 segundos.*
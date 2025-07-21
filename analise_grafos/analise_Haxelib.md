# Análise do Grafo: Haxelib

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 638 |
| **Arestas (Dependências)** | 880 |
| **Densidade do Grafo** | 0.00216532 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 49 |
| **Nós no Maior Componente (LCC)** | 500 (78.37%) |
| **Arestas no Maior Componente (LCC)** | 751 (85.34%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 1.38 | 1.38 | 2.76 |
| **Mediana** | 0.00 | 1.00 | 2.00 |
| **Máximo** | 75 | 11 | 75 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
| 1 | `openfl` | 75 |
| 2 | `tink_core` | 34 |
| 3 | `hxnodejs` | 32 |
| 4 | `tink_macro` | 27 |
| 5 | `thx.core` | 17 |
| 6 | `lime` | 15 |
| 7 | `actuate` | 15 |
| 8 | `msignal` | 15 |
| 9 | `hscript` | 14 |
| 10 | `promhx` | 13 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|---|---|---|
| 1 | `prime` | 11 |
| 2 | `wighawag-game-utils` | 10 |
| 3 | `prime-css` | 9 |
| 4 | `ufront` | 8 |
| 5 | `ufront-client` | 8 |
| 6 | `prime-components` | 8 |
| 7 | `fonthx` | 7 |
| 8 | `ufront-ufadmin` | 6 |
| 9 | `ufront-uftasks` | 6 |
| 10 | `prime-display` | 6 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|---|---|---|
| 1 | `tink_core` | 0.058935 |
| 2 | `openfl` | 0.053499 |
| 3 | `tink_macro` | 0.028628 |
| 4 | `hxnodejs` | 0.025486 |
| 5 | `thx.core` | 0.013289 |
| 6 | `hscript` | 0.010954 |
| 7 | `react-native` | 0.009999 |
| 8 | `lime` | 0.009922 |
| 9 | `hxcpp` | 0.009180 |
| 10 | `monax` | 0.008624 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `tink_http` | 0.000238 |
| 2 | `hexinject` | 0.000213 |
| 3 | `hexannotation` | 0.000193 |
| 4 | `coconut.ui` | 0.000183 |
| 5 | `hexreflection` | 0.000165 |
| 6 | `tink_macro` | 0.000161 |
| 7 | `hexcore` | 0.000153 |
| 8 | `tink_io` | 0.000121 |
| 9 | `tink_syntaxhub` | 0.000108 |
| 10 | `tink_hxx` | 0.000078 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.068034 |
| **Comunidades Detectadas (Louvain)** | 65 |
| **Modularidade** | 0.8335 |

---
*Análise concluída em 0.61 segundos.*


# Análise Completa do Grafo: Haxelib

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 638 |
| **Arestas** | 880 |
| **Densidade** | 0.00216532 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 636 |
| **Componentes Fracamente Conectados (WCC)** | 49 |
| **Maior SCC** | 2 nós |
| **Maior WCC** | 500 nós |
| **Nós no Maior Componente** | 500 (78.37%) |
| **Arestas no Maior Componente** | 751 (85.34%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 2.76 |
| **Grau Máximo** | 75 |
| **Grau Mediano** | 2.00 |
| **In-Degree Médio** | 1.38 |
| **In-Degree Máximo** | 75 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 1.38 |
| **Out-Degree Máximo** | 11 |
| **Out-Degree Mediano** | 1.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
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
|------|---------|------------|
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
|------|-----|----------------|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
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
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.068034 |
| **Comunidades Detectadas (Louvain)** | 65 |
| **Modularidade** | 0.8335 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 1 |
| **Método** | Aproximado |
| **Componente Analisado** | 2 nós (0.3%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **638 nós** e **880 arestas**.
O diâmetro aproximado é **1**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 78.4% dos nós, 
com densidade de 0.002165.

---
*Análise concluída em 0.61 segundos.*
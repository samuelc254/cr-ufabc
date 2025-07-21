# Análise do Grafo: CPAN

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 32,975 |
| **Arestas (Dependências)** | 282,246 |
| **Densidade do Grafo** | 0.00025958 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 32 |
| **Nós no Maior Componente (LCC)** | 32,898 (99.77%) |
| **Arestas no Maior Componente (LCC)** | 282,194 (99.98%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 8.56 | 8.56 | 17.12 |
| **Mediana** | 0.00 | 5.00 | 6.00 |
| **Máximo** | 18,721 | 373 | 18,721 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
| 1 | `Test-More` | 18,721 |
| 2 | `ExtUtils-MakeMaker` | 17,110 |
| 3 | `perl` | 12,314 |
| 4 | `Test-Pod` | 6,215 |
| 5 | `strict` | 5,030 |
| 6 | `warnings` | 4,880 |
| 7 | `File-Spec` | 4,801 |
| 8 | `Module-Build` | 4,172 |
| 9 | `Carp` | 4,143 |
| 10 | `Test-Pod-Coverage` | 3,581 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|---|---|---|
| 1 | `Task-POE-All` | 373 |
| 2 | `Task-BeLike-MELO` | 310 |
| 3 | `Task-MojoliciousPlugins-PerlAcademy` | 283 |
| 4 | `Task-WebGUI` | 201 |
| 5 | `Task-MasteringPerl` | 191 |
| 6 | `Task-BeLike-LESPEA` | 177 |
| 7 | `Task-Cpanel-Core` | 167 |
| 8 | `Dist-Zilla-PluginBundle-Author-ETHER` | 162 |
| 9 | `Task-BeLike-BINGOS` | 159 |
| 10 | `RapidApp` | 149 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|---|---|---|
| 1 | `ExtUtils-MakeMaker` | 0.080544 |
| 2 | `Test-More` | 0.061821 |
| 3 | `perl` | 0.041400 |
| 4 | `File-Spec` | 0.020056 |
| 5 | `Data-Dumper` | 0.013795 |
| 6 | `File-Basename` | 0.013666 |
| 7 | `Encode` | 0.013302 |
| 8 | `Pod-Man` | 0.011712 |
| 9 | `Carp` | 0.011106 |
| 10 | `Test-Pod` | 0.008273 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `Dist-Zilla` | 0.002596 |
| 2 | `Module-Build` | 0.002488 |
| 3 | `Moose` | 0.002439 |
| 4 | `ExtUtils-Manifest` | 0.002301 |
| 5 | `Try-Tiny` | 0.001492 |
| 6 | `Dist-Zilla-Plugin-MetaProvides-Package` | 0.001152 |
| 7 | `Dist-Zilla-PluginBundle-Author-ETHER` | 0.001088 |
| 8 | `Test-Spelling` | 0.001007 |
| 9 | `Dist-Zilla-PluginBundle-DAGOLDEN` | 0.000976 |
| 10 | `Pod-Spell` | 0.000965 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.139627 |
| **Comunidades Detectadas (Louvain)** | 65 |
| **Modularidade** | 0.3815 |

---
*Análise concluída em 247.85 segundos.*


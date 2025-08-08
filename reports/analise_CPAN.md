# Análise Completa do Grafo: CPAN

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 32,975 |
| **Arestas** | 282,246 |
| **Densidade** | 0.00025958 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 32,476 |
| **Componentes Fracamente Conectados (WCC)** | 32 |
| **Maior SCC** | 420 nós |
| **Maior WCC** | 32,898 nós |
| **Nós no Maior Componente** | 32,898 (99.77%) |
| **Arestas no Maior Componente** | 282,194 (99.98%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 17.12 |
| **Grau Máximo** | 18,721 |
| **Grau Mediano** | 6.00 |
| **In-Degree Médio** | 8.56 |
| **In-Degree Máximo** | 18,721 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 8.56 |
| **Out-Degree Máximo** | 373 |
| **Out-Degree Mediano** | 5.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
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
|------|---------|------------|
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
|------|-----|----------------|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `Dist-Zilla` | 0.002673 |
| 2 | `Module-Build` | 0.002632 |
| 3 | `ExtUtils-Manifest` | 0.002481 |
| 4 | `Moose` | 0.002239 |
| 5 | `Dist-Zilla-Plugin-MetaProvides-Package` | 0.001190 |
| 6 | `Test-Spelling` | 0.001186 |
| 7 | `Try-Tiny` | 0.001178 |
| 8 | `Pod-Spell` | 0.001150 |
| 9 | `Dist-Zilla-PluginBundle-Author-ETHER` | 0.001130 |
| 10 | `Moo` | 0.001108 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.139627 |
| **Comunidades Detectadas (Louvain)** | 65 |
| **Modularidade** | 0.3815 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 13 |
| **Método** | Aproximado |
| **Componente Analisado** | 420 nós (1.3%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **32,975 nós** e **282,246 arestas**.
O diâmetro aproximado é **13**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 99.8% dos nós, 
com densidade de 0.000260.

---
*Análise concluída em 207.82 segundos.*
# Análise Completa do Grafo: Hex

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 5,706 |
| **Arestas** | 11,201 |
| **Densidade** | 0.00034409 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 5,703 |
| **Componentes Fracamente Conectados (WCC)** | 119 |
| **Maior SCC** | 4 nós |
| **Maior WCC** | 5,403 nós |
| **Nós no Maior Componente** | 5,403 (94.69%) |
| **Arestas no Maior Componente** | 11,000 (98.21%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 3.93 |
| **Grau Máximo** | 1,048 |
| **Grau Mediano** | 2.00 |
| **In-Degree Médio** | 1.96 |
| **In-Degree Máximo** | 1,048 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 1.96 |
| **Out-Degree Máximo** | 24 |
| **Out-Degree Mediano** | 2.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `poison` | 1,048 |
| 2 | `httpoison` | 893 |
| 3 | `jason` | 485 |
| 4 | `plug` | 445 |
| 5 | `ecto` | 351 |
| 6 | `timex` | 192 |
| 7 | `hackney` | 191 |
| 8 | `google_gax` | 168 |
| 9 | `cowboy` | 165 |
| 10 | `phoenix` | 137 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `ejabberd` | 24 |
| 2 | `fulib` | 24 |
| 3 | `islands_engine` | 21 |
| 4 | `rig` | 16 |
| 5 | `materia` | 16 |
| 6 | `riak_core_ng` | 15 |
| 7 | `riak_core_ng_up` | 15 |
| 8 | `sentinel` | 14 |
| 9 | `ex_admin_runtime` | 14 |
| 10 | `ami_models` | 14 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `poison` | 0.038199 |
| 2 | `hackney` | 0.031532 |
| 3 | `decimal` | 0.030116 |
| 4 | `httpoison` | 0.027000 |
| 5 | `plug` | 0.023849 |
| 6 | `jason` | 0.023641 |
| 7 | `ecto` | 0.013673 |
| 8 | `google_gax` | 0.011859 |
| 9 | `telemetry` | 0.010527 |
| 10 | `elixir_make` | 0.008372 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `hackney` | 0.000331 |
| 2 | `httpoison` | 0.000210 |
| 3 | `tesla` | 0.000188 |
| 4 | `google_gax` | 0.000140 |
| 5 | `timex` | 0.000075 |
| 6 | `plug` | 0.000075 |
| 7 | `idna` | 0.000056 |
| 8 | `tzdata` | 0.000053 |
| 9 | `phoenix` | 0.000049 |
| 10 | `jason` | 0.000030 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.040453 |
| **Comunidades Detectadas (Louvain)** | 151 |
| **Modularidade** | 0.6516 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 2 |
| **Método** | Aproximado |
| **Componente Analisado** | 4 nós (0.1%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **5,706 nós** e **11,201 arestas**.
O diâmetro aproximado é **2**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 94.7% dos nós, 
com densidade de 0.000344.

---
*Análise concluída em 7.11 segundos.*
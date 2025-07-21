# Análise do Grafo: Pypi

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 46,668 |
| **Arestas (Dependências)** | 126,759 |
| **Densidade do Grafo** | 0.00005820 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 577 |
| **Nós no Maior Componente (LCC)** | 45,180 (96.81%) |
| **Arestas no Maior Componente (LCC)** | 125,754 (99.21%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 2.72 | 2.72 | 5.43 |
| **Mediana** | 0.00 | 2.00 | 2.00 |
| **Máximo** | 9,459 | 120 | 9,459 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
| 1 | `requests` | 9,459 |
| 2 | `six` | 4,128 |
| 3 | `numpy` | 3,540 |
| 4 | `click` | 2,174 |
| 5 | `setuptools` | 1,851 |
| 6 | `python-dateutil` | 1,621 |
| 7 | `pyyaml` | 1,520 |
| 8 | `PyYAML` | 1,295 |
| 9 | `lxml` | 1,157 |
| 10 | `pandas` | 1,069 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|---|---|---|
| 1 | `cloudscript` | 120 |
| 2 | `c7n-azure` | 105 |
| 3 | `TEStribute` | 102 |
| 4 | `nucypher` | 96 |
| 5 | `cateye` | 72 |
| 6 | `mycloud-cli` | 71 |
| 7 | `cloudview` | 69 |
| 8 | `nova` | 68 |
| 9 | `ML-Navigator` | 68 |
| 10 | `rucio` | 63 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|---|---|---|
| 1 | `requests` | 0.044330 |
| 2 | `six` | 0.027790 |
| 3 | `numpy` | 0.017058 |
| 4 | `setuptools` | 0.010948 |
| 5 | `click` | 0.007997 |
| 6 | `python-dateutil` | 0.005665 |
| 7 | `django` | 0.005296 |
| 8 | `pyyaml` | 0.005135 |
| 9 | `Django` | 0.004968 |
| 10 | `pytz` | 0.004755 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `pytest` | 0.000004 |
| 2 | `boto3` | 0.000002 |
| 3 | `botocore` | 0.000002 |
| 4 | `ipython` | 0.000002 |
| 5 | `indy-node` | 0.000002 |
| 6 | `oslo.messaging` | 0.000002 |
| 7 | `importlib-metadata` | 0.000002 |
| 8 | `azureml-core` | 0.000002 |
| 9 | `Django` | 0.000001 |
| 10 | `indy-plenum` | 0.000001 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.038088 |
| **Comunidades Detectadas (Louvain)** | 625 |
| **Modularidade** | 0.5505 |

---
*Análise concluída em 98.08 segundos.*


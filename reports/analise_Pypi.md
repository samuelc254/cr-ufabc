# Análise Completa do Grafo: Pypi

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 46,668 |
| **Arestas** | 126,759 |
| **Densidade** | 0.00005820 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 46,642 |
| **Componentes Fracamente Conectados (WCC)** | 577 |
| **Maior SCC** | 4 nós |
| **Maior WCC** | 45,180 nós |
| **Nós no Maior Componente** | 45,180 (96.81%) |
| **Arestas no Maior Componente** | 125,754 (99.21%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 5.43 |
| **Grau Máximo** | 9,459 |
| **Grau Mediano** | 2.00 |
| **In-Degree Médio** | 2.72 |
| **In-Degree Máximo** | 9,459 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 2.72 |
| **Out-Degree Máximo** | 120 |
| **Out-Degree Mediano** | 2.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
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
|------|---------|------------|
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
|------|-----|----------------|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `pytest` | 0.000005 |
| 2 | `pantsbuild.pants` | 0.000004 |
| 3 | `Sphinx` | 0.000003 |
| 4 | `jupyter` | 0.000003 |
| 5 | `Django` | 0.000003 |
| 6 | `apache-airflow` | 0.000003 |
| 7 | `google-api-python-client` | 0.000003 |
| 8 | `neutron` | 0.000003 |
| 9 | `twine` | 0.000002 |
| 10 | `nbconvert` | 0.000002 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.038088 |
| **Comunidades Detectadas (Louvain)** | 625 |
| **Modularidade** | 0.5505 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 3 |
| **Método** | Aproximado |
| **Componente Analisado** | 4 nós (0.0%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **46,668 nós** e **126,759 arestas**.
O diâmetro aproximado é **3**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 96.8% dos nós, 
com densidade de 0.000058.

---
*Análise concluída em 112.84 segundos.*
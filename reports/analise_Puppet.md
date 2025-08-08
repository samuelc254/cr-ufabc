# Análise Completa do Grafo: Puppet

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 4,716 |
| **Arestas** | 9,623 |
| **Densidade** | 0.00043277 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 4,712 |
| **Componentes Fracamente Conectados (WCC)** | 54 |
| **Maior SCC** | 2 nós |
| **Maior WCC** | 4,566 nós |
| **Nós no Maior Componente** | 4,566 (96.82%) |
| **Arestas no Maior Componente** | 9,520 (98.93%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 4.08 |
| **Grau Máximo** | 3,422 |
| **Grau Mediano** | 2.00 |
| **In-Degree Médio** | 2.04 |
| **In-Degree Máximo** | 3,422 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 2.04 |
| **Out-Degree Máximo** | 75 |
| **Out-Degree Mediano** | 1.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `puppetlabs-stdlib` | 3,422 |
| 2 | `puppetlabs-concat` | 554 |
| 3 | `puppetlabs-apt` | 415 |
| 4 | `puppetlabs-inifile` | 216 |
| 5 | `puppetlabs-apache` | 171 |
| 6 | `puppetlabs-vcsrepo` | 160 |
| 7 | `puppetlabs-mysql` | 153 |
| 8 | `puppet-archive` | 149 |
| 9 | `puppetlabs-firewall` | 138 |
| 10 | `stahnma-epel` | 120 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `simp-simp_core` | 75 |
| 2 | `simp-simp` | 43 |
| 3 | `geoffwilliams-r_profile` | 42 |
| 4 | `pltraining-classroom_legacy` | 39 |
| 5 | `pltraining-classroom` | 32 |
| 6 | `maestrodev-maestro_nodes` | 20 |
| 7 | `gajdaw-symfony` | 20 |
| 8 | `cohdjn-cisecurity` | 20 |
| 9 | `fervid-secure_linux_cis` | 20 |
| 10 | `puppetlabs-openstack` | 18 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `puppetlabs-stdlib` | 0.275443 |
| 2 | `puppetlabs-translate` | 0.027495 |
| 3 | `puppetlabs-concat` | 0.024679 |
| 4 | `puppetlabs-apt` | 0.018501 |
| 5 | `puppetlabs-inifile` | 0.008108 |
| 6 | `example42-puppi` | 0.007752 |
| 7 | `puppet-archive` | 0.006643 |
| 8 | `puppetlabs-vcsrepo` | 0.005630 |
| 9 | `puppetlabs-apache` | 0.005320 |
| 10 | `stahnma-epel` | 0.005225 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `puppetlabs-concat` | 0.000036 |
| 2 | `geoffwilliams-r_profile` | 0.000026 |
| 3 | `puppetlabs-apt` | 0.000021 |
| 4 | `puppetlabs-apache` | 0.000014 |
| 5 | `puppetlabs-inifile` | 0.000012 |
| 6 | `camptocamp-systemd` | 0.000012 |
| 7 | `simp-rsync` | 0.000010 |
| 8 | `puppetlabs-powershell` | 0.000010 |
| 9 | `puppetlabs-mysql` | 0.000008 |
| 10 | `tarun4-chocolatey` | 0.000007 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.140082 |
| **Comunidades Detectadas (Louvain)** | 94 |
| **Modularidade** | 0.5360 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 1 |
| **Método** | Aproximado |
| **Componente Analisado** | 2 nós (0.0%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **4,716 nós** e **9,623 arestas**.
O diâmetro aproximado é **1**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 96.8% dos nós, 
com densidade de 0.000433.

---
*Análise concluída em 5.46 segundos.*
# Análise do Grafo: Puppet

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 4,716 |
| **Arestas (Dependências)** | 9,623 |
| **Densidade do Grafo** | 0.00043277 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 54 |
| **Nós no Maior Componente (LCC)** | 4,566 (96.82%) |
| **Arestas no Maior Componente (LCC)** | 9,520 (98.93%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 2.04 | 2.04 | 4.08 |
| **Mediana** | 0.00 | 1.00 | 2.00 |
| **Máximo** | 3,422 | 75 | 3,422 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
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
|---|---|---|
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
|---|---|---|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `puppetlabs-concat` | 0.000037 |
| 2 | `puppetlabs-apt` | 0.000022 |
| 3 | `puppetlabs-apache` | 0.000013 |
| 4 | `tarun4-chocolatey` | 0.000012 |
| 5 | `puppetlabs-inifile` | 0.000012 |
| 6 | `camptocamp-systemd` | 0.000008 |
| 7 | `puppetlabs-postgresql` | 0.000008 |
| 8 | `puppetlabs-powershell` | 0.000007 |
| 9 | `simp-simplib` | 0.000006 |
| 10 | `simp-nfs` | 0.000005 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.140082 |
| **Comunidades Detectadas (Louvain)** | 94 |
| **Modularidade** | 0.5360 |

---
*Análise concluída em 5.86 segundos.*


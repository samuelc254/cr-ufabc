# Análise Completa do Grafo: Homebrew

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 2,126 |
| **Arestas** | 4,189 |
| **Densidade** | 0.00092723 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 2,126 |
| **Componentes Fracamente Conectados (WCC)** | 45 |
| **Maior SCC** | 1 nós |
| **Maior WCC** | 2,023 nós |
| **Nós no Maior Componente** | 2,023 (95.16%) |
| **Arestas no Maior Componente** | 4,130 (98.59%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 3.94 |
| **Grau Máximo** | 401 |
| **Grau Mediano** | 2.00 |
| **In-Degree Médio** | 1.97 |
| **In-Degree Máximo** | 401 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 1.97 |
| **Out-Degree Máximo** | 28 |
| **Out-Degree Mediano** | 1.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `Pkg-config` | 401 |
| 2 | `Python` | 211 |
| 3 | `Autoconf` | 175 |
| 4 | `Java` | 168 |
| 5 | `Automake` | 157 |
| 6 | `Libtool` | 144 |
| 7 | `X11` | 139 |
| 8 | `Maco` | 111 |
| 9 | `Glib` | 95 |
| 10 | `Cmake` | 93 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `gstpluginsugly` | 28 |
| 2 | `gstpluginsgood` | 25 |
| 3 | `libav` | 22 |
| 4 | `fontforge` | 20 |
| 5 | `imagemagick` | 19 |
| 6 | `moc` | 18 |
| 7 | `mpd` | 18 |
| 8 | `openscenegraph` | 18 |
| 9 | `gource` | 16 |
| 10 | `gstpluginsbad` | 16 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `Python` | 0.039253 |
| 2 | `Java` | 0.036753 |
| 3 | `Pkg-config` | 0.030585 |
| 4 | `Maco` | 0.019052 |
| 5 | `X11` | 0.018079 |
| 6 | `Autoconf` | 0.012298 |
| 7 | `Xcode` | 0.012101 |
| 8 | `Cmake` | 0.011780 |
| 9 | `Python3` | 0.009563 |
| 10 | `Automake` | 0.009394 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `dockercloud` | 0.000000 |
| 2 | `Python` | 0.000000 |
| 3 | `aap` | 0.000000 |
| 4 | `abcde` | 0.000000 |
| 5 | `Vorbis-tool` | 0.000000 |
| 6 | `CdDiscid` | 0.000000 |
| 7 | `Mkcue` | 0.000000 |
| 8 | `Cdrtools` | 0.000000 |
| 9 | `Lame` | 0.000000 |
| 10 | `Flac` | 0.000000 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.000000 |
| **Comunidades Detectadas (Louvain)** | 61 |
| **Modularidade** | 0.6236 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 0 |
| **Método** | Aproximado |
| **Componente Analisado** | 1 nós (0.0%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **2,126 nós** e **4,189 arestas**.
O diâmetro aproximado é **0**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 95.2% dos nós, 
com densidade de 0.000927.

---
*Análise concluída em 1.93 segundos.*
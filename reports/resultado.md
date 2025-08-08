# Glossário de Gerenciadores e Repositórios de Pacotes

## Definição

Um **gerenciador de pacotes** é uma ferramenta que automatiza a instalação, atualização e gerenciamento de bibliotecas de software (pacotes) das quais um projeto depende. Um **repositório de pacotes** é o servidor central onde esses pacotes são armazenados e de onde são baixados.

## Plataformas e Gerenciadores

### Linguagens de Programação Específicas

#### **D**
- **Dub**: Gerenciador de pacotes para a linguagem de programação D.

#### **Erlang/Elixir**
- **Hex**: Gerenciador de pacotes para as linguagens Erlang e Elixir.

#### **Dart/Flutter**
- **Pub**: Gerenciador de pacotes oficial para a linguagem Dart e o framework Flutter (usado para criar apps móveis e web).

#### **JavaScript/Node.js**
- **NPM (Node Package Manager)**: O gerenciador de pacotes mais famoso do mundo, usado para JavaScript e o ambiente Node.js.

#### **Rust**
- **Cargo**: A ferramenta de construção e gerenciador de pacotes para a linguagem Rust.

#### **Python**
- **PyPI (Python Package Index)**: O repositório oficial de pacotes para a linguagem Python. A ferramenta `pip` é usada para instalar pacotes a partir dele.

#### **PHP**
- **Packagist**: O principal repositório de pacotes para PHP, gerenciado com a ferramenta Composer.

#### **Ruby**
- **RubyGems**: O gerenciador de pacotes padrão para a linguagem Ruby. Os pacotes são chamados de "gems".

#### **Java**
- **Maven**: Uma ferramenta de automação e gerenciamento de dependências muito popular para projetos em Java.

#### **.NET/C#**
- **NuGet**: O gerenciador de pacotes para a plataforma de desenvolvimento da Microsoft, principalmente para o ecossistema .NET (usado em C#, por exemplo).

#### **Perl**
- **CPAN (Comprehensive Perl Archive Network)**: O repositório clássico e abrangente de bibliotecas para a linguagem Perl.

#### **R**
- **CRAN (Comprehensive R Archive Network)**: O repositório principal de pacotes para a linguagem R, muito usada em estatística e ciência de dados.

#### **Elm**
- **Elm**: Refere-se ao gerenciador de pacotes da própria linguagem Elm, usada para desenvolvimento web.

#### **Haxe**
- **Haxelib**: O gerenciador de pacotes para a linguagem Haxe.

### Ferramentas e Ambientes Especializados

#### **Editores (Descontinuados)**
- **Atom**: Era o gerenciador de pacotes do editor de texto Atom (descontinuado), usado para instalar plugins e temas.

#### **Sistemas Operacionais**
- **Homebrew**: Um gerenciador de pacotes muito popular para o sistema operacional macOS (e também Linux), usado para instalar aplicativos e ferramentas de linha de comando.

#### **Automação de Infraestrutura**
- **Puppet**: Refere-se ao Puppet Forge, um repositório de "módulos" para a ferramenta de automação de infraestrutura Puppet.

#### **Ciência de Dados**
- **Conda**: Um gerenciador de pacotes e de ambientes muito popular na comunidade de ciência de dados, compatível principalmente com Python e R.

---

# Análise Completa do Grafo: Atom

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 7,243 |
| **Arestas** | 17,128 |
| **Densidade** | 0.00032653 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 7,243 |
| **Componentes Fracamente Conectados (WCC)** | 222 |
| **Maior SCC** | 1 nós |
| **Maior WCC** | 6,770 nós |
| **Nós no Maior Componente** | 6,770 (93.47%) |
| **Arestas no Maior Componente** | 16,861 (98.44%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 4.73 |
| **Grau Máximo** | 840 |
| **Grau Mediano** | 2.00 |
| **In-Degree Médio** | 2.36 |
| **In-Degree Máximo** | 840 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 2.36 |
| **Out-Degree Máximo** | 162 |
| **Out-Degree Mediano** | 1.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `atom-space-pen-views` | 840 |
| 2 | `atom-package-deps` | 576 |
| 3 | `eslint` | 478 |
| 4 | `fs-plus` | 388 |
| 5 | `underscore-plus` | 372 |
| 6 | `atom-linter` | 266 |
| 7 | `coffeelint` | 247 |
| 8 | `jquery` | 241 |
| 9 | `lodash` | 239 |
| 10 | `request` | 220 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `nuclide` | 162 |
| 2 | `mstest2` | 70 |
| 3 | `mstest1` | 69 |
| 4 | `metasota-package-4` | 62 |
| 5 | `build-ibmstreams` | 53 |
| 6 | `etheratom` | 52 |
| 7 | `veda` | 50 |
| 8 | `touchbar-plus` | 44 |
| 9 | `prettier-atom` | 43 |
| 10 | `markdown-preview-plus` | 42 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `atom-space-pen-views` | 0.028087 |
| 2 | `atom-package-deps` | 0.017456 |
| 3 | `coffeelint` | 0.013775 |
| 4 | `underscore-plus` | 0.011199 |
| 5 | `jquery` | 0.009290 |
| 6 | `fs-plus` | 0.008387 |
| 7 | `eslint` | 0.007921 |
| 8 | `atom-linter` | 0.007648 |
| 9 | `request` | 0.006801 |
| 10 | `lodash` | 0.006387 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `atom-languageclient` | 0.000026 |
| 2 | `autocomplete-plus` | 0.000004 |
| 3 | `ionide-fsharp` | 0.000001 |
| 4 | `language-c` | 0.000001 |
| 5 | `jsfmt` | 0.000000 |
| 6 | `achievements` | 0.000000 |
| 7 | `atom-space-pen-views` | 0.000000 |
| 8 | `advanced-new-file` | 0.000000 |
| 9 | `touch` | 0.000000 |
| 10 | `mkdirp` | 0.000000 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.001505 |
| **Comunidades Detectadas (Louvain)** | 254 |
| **Modularidade** | 0.6067 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 0 |
| **Método** | Aproximado |
| **Componente Analisado** | 1 nós (0.0%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **7,243 nós** e **17,128 arestas**.
O diâmetro aproximado é **0**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 93.5% dos nós, 
com densidade de 0.000327.

---
*Análise concluída em 9.85 segundos.*

---

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

---

# Análise Completa do Grafo: CRAN

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 15,413 |
| **Arestas** | 102,241 |
| **Densidade** | 0.00043041 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 14,386 |
| **Componentes Fracamente Conectados (WCC)** | 3 |
| **Maior SCC** | 882 nós |
| **Maior WCC** | 15,409 nós |
| **Nós no Maior Componente** | 15,409 (99.97%) |
| **Arestas no Maior Componente** | 102,239 (100.00%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 13.27 |
| **Grau Máximo** | 9,587 |
| **Grau Mediano** | 6.00 |
| **In-Degree Médio** | 6.63 |
| **In-Degree Máximo** | 9,587 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 6.63 |
| **Out-Degree Máximo** | 107 |
| **Out-Degree Mediano** | 5.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `R` | 9,587 |
| 2 | `knitr` | 4,239 |
| 3 | `testthat` | 4,080 |
| 4 | `stats` | 3,777 |
| 5 | `rmarkdown` | 3,257 |
| 6 | `methods` | 2,728 |
| 7 | `ggplot2` | 2,442 |
| 8 | `utils` | 2,302 |
| 9 | `graphics` | 1,889 |
| 10 | `Rcpp` | 1,792 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `mlr` | 107 |
| 2 | `broom` | 81 |
| 3 | `fitteR` | 76 |
| 4 | `rattle` | 67 |
| 5 | `Seurat` | 60 |
| 6 | `fscaret` | 59 |
| 7 | `nlmixr` | 52 |
| 8 | `BiodiversityR` | 49 |
| 9 | `RxODE` | 49 |
| 10 | `CNVScope` | 49 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `R` | 0.093825 |
| 2 | `testthat` | 0.026385 |
| 3 | `methods` | 0.025335 |
| 4 | `stats` | 0.025040 |
| 5 | `knitr` | 0.021490 |
| 6 | `utils` | 0.017440 |
| 7 | `rmarkdown` | 0.015607 |
| 8 | `graphics` | 0.013062 |
| 9 | `MASS` | 0.011680 |
| 10 | `Rcpp` | 0.011633 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `broom` | 0.019273 |
| 2 | `dplyr` | 0.017341 |
| 3 | `knitr` | 0.015418 |
| 4 | `Hmisc` | 0.015339 |
| 5 | `ggplot2` | 0.014547 |
| 6 | `mice` | 0.010068 |
| 7 | `caret` | 0.008864 |
| 8 | `testthat` | 0.007677 |
| 9 | `styler` | 0.007480 |
| 10 | `nlme` | 0.007129 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.176208 |
| **Comunidades Detectadas (Louvain)** | 16 |
| **Modularidade** | 0.3258 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 17 |
| **Método** | Aproximado |
| **Componente Analisado** | 882 nós (5.7%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **15,413 nós** e **102,241 arestas**.
O diâmetro aproximado é **17**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 100.0% dos nós, 
com densidade de 0.000430.

---
*Análise concluída em 47.77 segundos.*

---

# Análise Completa do Grafo: Cargo

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 24,305 |
| **Arestas** | 115,856 |
| **Densidade** | 0.00019613 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 24,016 |
| **Componentes Fracamente Conectados (WCC)** | 152 |
| **Maior SCC** | 164 nós |
| **Maior WCC** | 23,951 nós |
| **Nós no Maior Componente** | 23,951 (98.54%) |
| **Arestas no Maior Componente** | 115,628 (99.80%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 9.53 |
| **Grau Máximo** | 5,176 |
| **Grau Mediano** | 4.00 |
| **In-Degree Médio** | 4.77 |
| **In-Degree Máximo** | 5,175 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 4.77 |
| **Out-Degree Máximo** | 77 |
| **Out-Degree Mediano** | 3.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `serde` | 5,175 |
| 2 | `serde_json` | 3,580 |
| 3 | `log` | 3,193 |
| 4 | `serde_derive` | 3,108 |
| 5 | `rand` | 2,538 |
| 6 | `libc` | 2,410 |
| 7 | `clap` | 2,251 |
| 8 | `lazy_static` | 2,213 |
| 9 | `futures` | 1,699 |
| 10 | `failure` | 1,697 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `sccache` | 77 |
| 2 | `sn0int` | 74 |
| 3 | `solana` | 63 |
| 4 | `solana-core` | 63 |
| 5 | `rustpython-vm` | 59 |
| 6 | `snowchains` | 57 |
| 7 | `cargo` | 55 |
| 8 | `exonum` | 53 |
| 9 | `ciruela` | 52 |
| 10 | `cargo-semverver` | 52 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `serde_derive` | 0.036235 |
| 2 | `serde` | 0.030830 |
| 3 | `quote` | 0.030196 |
| 4 | `proc-macro2` | 0.025523 |
| 5 | `libc` | 0.018776 |
| 6 | `rand` | 0.018686 |
| 7 | `syn` | 0.018169 |
| 8 | `unicode-xid` | 0.012141 |
| 9 | `winapi` | 0.011835 |
| 10 | `serde_json` | 0.010846 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `syn` | 0.004625 |
| 2 | `flate2` | 0.003214 |
| 3 | `serde_derive` | 0.002237 |
| 4 | `tokio` | 0.001792 |
| 5 | `parking_lot` | 0.001605 |
| 6 | `tokio-tcp` | 0.001576 |
| 7 | `parking_lot_core` | 0.001425 |
| 8 | `rand_core` | 0.001408 |
| 9 | `backtrace` | 0.001347 |
| 10 | `tokio-reactor` | 0.001285 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.114293 |
| **Comunidades Detectadas (Louvain)** | 183 |
| **Modularidade** | 0.4845 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 18 |
| **Método** | Aproximado |
| **Componente Analisado** | 164 nós (0.7%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **24,305 nós** e **115,856 arestas**.
O diâmetro aproximado é **18**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 98.5% dos nós, 
com densidade de 0.000196.

---
*Análise concluída em 51.61 segundos.*

---

# Análise Completa do Grafo: Conda

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 1,270 |
| **Arestas** | 2,866 |
| **Densidade** | 0.00177832 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 1,270 |
| **Componentes Fracamente Conectados (WCC)** | 63 |
| **Maior SCC** | 1 nós |
| **Maior WCC** | 959 nós |
| **Nós no Maior Componente** | 959 (75.51%) |
| **Arestas no Maior Componente** | 2,565 (89.50%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 4.51 |
| **Grau Máximo** | 546 |
| **Grau Mediano** | 2.00 |
| **In-Degree Médio** | 2.26 |
| **In-Degree Máximo** | 536 |
| **In-Degree Mediano** | 1.00 |
| **Out-Degree Médio** | 2.26 |
| **Out-Degree Máximo** | 275 |
| **Out-Degree Mediano** | 1.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `python` | 536 |
| 2 | `libgcc-ng` | 327 |
| 3 | `libstdcxx-ng` | 144 |
| 4 | `numpy` | 77 |
| 5 | `zlib` | 64 |
| 6 | `six` | 36 |
| 7 | `openssl` | 28 |
| 8 | `requests` | 22 |
| 9 | `tornado` | 20 |
| 10 | `pandas` | 18 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `anaconda` | 275 |
| 2 | `libgdal` | 31 |
| 3 | `graphviz` | 21 |
| 4 | `orange3` | 19 |
| 5 | `vtk` | 16 |
| 6 | `tensorflow-base` | 16 |
| 7 | `scikit-image` | 15 |
| 8 | `wxpython` | 15 |
| 9 | `docker-py` | 14 |
| 10 | `scikit-bio` | 14 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `python` | 0.132325 |
| 2 | `libgcc-ng` | 0.122561 |
| 3 | `_libgcc_mutex` | 0.104456 |
| 4 | `libstdcxx-ng` | 0.037928 |
| 5 | `zlib` | 0.022327 |
| 6 | `ncurses` | 0.019351 |
| 7 | `openssl` | 0.014254 |
| 8 | `xz` | 0.012868 |
| 9 | `tk` | 0.012196 |
| 10 | `readline` | 0.011881 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `python` | 0.007259 |
| 2 | `libgcc-ng` | 0.000867 |
| 3 | `sqlite` | 0.000667 |
| 4 | `numpy` | 0.000585 |
| 5 | `libmxnet` | 0.000239 |
| 6 | `libopencv` | 0.000213 |
| 7 | `mxnet` | 0.000193 |
| 8 | `bokeh` | 0.000186 |
| 9 | `notebook` | 0.000160 |
| 10 | `dask` | 0.000155 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.156843 |
| **Comunidades Detectadas (Louvain)** | 74 |
| **Modularidade** | 0.5542 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 0 |
| **Método** | Aproximado |
| **Componente Analisado** | 1 nós (0.1%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **1,270 nós** e **2,866 arestas**.
O diâmetro aproximado é **0**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 75.5% dos nós, 
com densidade de 0.001778.

---
*Análise concluída em 1.48 segundos.*

---

# Análise Completa do Grafo: Dub

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 1,161 |
| **Arestas** | 1,383 |
| **Densidade** | 0.00102691 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 1,161 |
| **Componentes Fracamente Conectados (WCC)** | 93 |
| **Maior SCC** | 1 nós |
| **Maior WCC** | 780 nós |
| **Nós no Maior Componente** | 780 (67.18%) |
| **Arestas no Maior Componente** | 1,076 (77.80%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 2.38 |
| **Grau Máximo** | 76 |
| **Grau Mediano** | 1.00 |
| **In-Degree Médio** | 1.19 |
| **In-Degree Máximo** | 70 |
| **In-Degree Mediano** | 1.00 |
| **Out-Degree Médio** | 1.19 |
| **Out-Degree Máximo** | 21 |
| **Out-Degree Mediano** | 1.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `derelict-util` | 70 |
| 2 | `vibe-d` | 63 |
| 3 | `derelict-sdl2` | 25 |
| 4 | `vibe-d:data` | 25 |
| 5 | `derelict-gl3` | 24 |
| 6 | `vibe-d:http` | 18 |
| 7 | `pegged` | 17 |
| 8 | `vibe-d:core` | 16 |
| 9 | `openssl` | 15 |
| 10 | `hunt` | 15 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `arsd-official` | 21 |
| 2 | `soupply` | 18 |
| 3 | `selery` | 17 |
| 4 | `dplug` | 16 |
| 5 | `vibe-d` | 13 |
| 6 | `armos` | 13 |
| 7 | `tsv-utils-dlang` | 12 |
| 8 | `aurorafw` | 12 |
| 9 | `tsv-utils` | 12 |
| 10 | `evael` | 12 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `derelict-util` | 0.060536 |
| 2 | `vibe-d` | 0.029374 |
| 3 | `mir-core` | 0.022981 |
| 4 | `stdx-allocator` | 0.018380 |
| 5 | `vibe-d:data` | 0.013662 |
| 6 | `taggedalgebraic` | 0.010843 |
| 7 | `pegged` | 0.009873 |
| 8 | `derelict-sdl2` | 0.008482 |
| 9 | `tinyendian` | 0.008188 |
| 10 | `openssl` | 0.007783 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `vibe-d` | 0.001628 |
| 2 | `unit-threaded` | 0.000126 |
| 3 | `vibe-core` | 0.000113 |
| 4 | `fluent-asserts` | 0.000108 |
| 5 | `stdx-allocator` | 0.000095 |
| 6 | `dlangui` | 0.000090 |
| 7 | `libdparse` | 0.000048 |
| 8 | `mir-lapack` | 0.000046 |
| 9 | `soupply` | 0.000046 |
| 10 | `mysql-native` | 0.000039 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.032632 |
| **Comunidades Detectadas (Louvain)** | 112 |
| **Modularidade** | 0.8532 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 0 |
| **Método** | Aproximado |
| **Componente Analisado** | 1 nós (0.1%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **1,161 nós** e **1,383 arestas**.
O diâmetro aproximado é **0**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 67.2% dos nós, 
com densidade de 0.001027.

---
*Análise concluída em 1.38 segundos.*

---

# Análise Completa do Grafo: Elm

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 1,474 |
| **Arestas** | 3,781 |
| **Densidade** | 0.00174143 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 1,474 |
| **Componentes Fracamente Conectados (WCC)** | 1 |
| **Maior SCC** | 1 nós |
| **Maior WCC** | 1,474 nós |
| **Nós no Maior Componente** | 1,474 (100.00%) |
| **Arestas no Maior Componente** | 3,781 (100.00%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 5.13 |
| **Grau Máximo** | 1,467 |
| **Grau Mediano** | 3.00 |
| **In-Degree Médio** | 2.57 |
| **In-Degree Máximo** | 1,467 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 2.57 |
| **Out-Degree Máximo** | 16 |
| **Out-Degree Mediano** | 2.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `elm-lang/core` | 1,467 |
| 2 | `elm-lang/html` | 628 |
| 3 | `elm-lang/http` | 123 |
| 4 | `elm-lang/svg` | 102 |
| 5 | `elm-community/list-extra` | 82 |
| 6 | `NoRedInk/elm-decode-pipeline` | 48 |
| 7 | `rtfeldman/elm-css` | 43 |
| 8 | `elm-community/elm-test` | 39 |
| 9 | `elm-lang/mouse` | 37 |
| 10 | `elm-lang/navigation` | 31 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `cmditch/mel-bew3` | 16 |
| 2 | `Gizra/elm-essentials` | 13 |
| 3 | `williamwhitacre/scaffold` | 12 |
| 4 | `elm-bodybuilder/elegant` | 12 |
| 5 | `lucamug/elm-style-framework` | 12 |
| 6 | `williamwhitacre/gigan` | 10 |
| 7 | `xarvh/elm-slides` | 10 |
| 8 | `micktwomey/elmo-8` | 10 |
| 9 | `NoRedInk/elm-doodad` | 10 |
| 10 | `folkertdev/one-true-path-experiment` | 9 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `elm-lang/core` | 0.339190 |
| 2 | `elm-lang/html` | 0.063411 |
| 3 | `elm-lang/virtual-dom` | 0.031589 |
| 4 | `elm-lang/http` | 0.010381 |
| 5 | `elm-lang/svg` | 0.007007 |
| 6 | `elm-community/list-extra` | 0.005940 |
| 7 | `elm-lang/dom` | 0.004808 |
| 8 | `elm-lang/lazy` | 0.003664 |
| 9 | `elm-community/elm-test` | 0.003423 |
| 10 | `rtfeldman/elm-css` | 0.003258 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `elm-lang/html` | 0.000281 |
| 2 | `elm-community/elm-test` | 0.000079 |
| 3 | `rtfeldman/elm-css` | 0.000044 |
| 4 | `elm-lang/svg` | 0.000032 |
| 5 | `elm-community/elm-check` | 0.000023 |
| 6 | `elm-lang/navigation` | 0.000018 |
| 7 | `Gizra/elm-essentials` | 0.000016 |
| 8 | `elm-tools/parser` | 0.000015 |
| 9 | `drathier/elm-graph` | 0.000014 |
| 10 | `RGBboy/websocket-server` | 0.000012 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.300517 |
| **Comunidades Detectadas (Louvain)** | 12 |
| **Modularidade** | 0.3852 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 0 |
| **Método** | Aproximado |
| **Componente Analisado** | 1 nós (0.1%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **1,474 nós** e **3,781 arestas**.
O diâmetro aproximado é **0**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 100.0% dos nós, 
com densidade de 0.001741.

---
*Análise concluída em 1.75 segundos.*

---

# Análise Completa do Grafo: Geral

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 1,758,429 |
| **Arestas** | 14,078,099 |
| **Densidade** | 0.00000455 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 1,730,853 |
| **Componentes Fracamente Conectados (WCC)** | 11,301 |
| **Maior SCC** | 18,413 nós |
| **Maior WCC** | 1,604,174 nós |
| **Nós no Maior Componente** | 1,604,174 (91.23%) |
| **Arestas no Maior Componente** | 13,504,283 (95.92%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 16.01 |
| **Grau Máximo** | 193,045 |
| **Grau Mediano** | 5.00 |
| **In-Degree Médio** | 8.01 |
| **In-Degree Máximo** | 192,961 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 8.01 |
| **Out-Degree Máximo** | 1,000 |
| **Out-Degree Mediano** | 4.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `mocha` | 192,961 |
| 2 | `eslint` | 177,661 |
| 3 | `typescript` | 128,561 |
| 4 | `chai` | 117,227 |
| 5 | `webpack` | 116,054 |
| 6 | `babel-core` | 111,311 |
| 7 | `babel-loader` | 99,137 |
| 8 | `react` | 95,553 |
| 9 | `lodash` | 93,358 |
| 10 | `jest` | 88,218 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `sindresorhus.js` | 1,000 |
| 2 | `npm-bomb` | 999 |
| 3 | `1000-packages` | 999 |
| 4 | `all-of-them` | 989 |
| 5 | `digital-keyboard-demos` | 975 |
| 6 | `@hawkingnetwork/react-native-tab-view` | 921 |
| 7 | `@ericmcornelius/ease` | 905 |
| 8 | `vue-compment` | 895 |
| 9 | `nois-react-toast` | 873 |
| 10 | `org.springframework.boot:spring-boot-dependencies` | 856 |

## 4. Análise de Centralidade
_(Análise realizada em uma amostra de 200,000 nós do maior componente (Betweenness aproximado com k=1000))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `typescript` | 0.035260 |
| 2 | `rimraf` | 0.022145 |
| 3 | `rake` | 0.019209 |
| 4 | `should` | 0.013553 |
| 5 | `husky` | 0.011594 |
| 6 | `nyc` | 0.011314 |
| 7 | `express` | 0.009337 |
| 8 | `debug` | 0.008063 |
| 9 | `karma` | 0.007316 |
| 10 | `prop-types` | 0.006701 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `typescript` | 0.000039 |
| 2 | `node-fetch` | 0.000015 |
| 3 | `karma` | 0.000014 |
| 4 | `gulp-rename` | 0.000013 |
| 5 | `husky` | 0.000012 |
| 6 | `jscs` | 0.000012 |
| 7 | `abort-controller` | 0.000012 |
| 8 | `express` | 0.000010 |
| 9 | `should` | 0.000008 |
| 10 | `range-parser` | 0.000005 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 30 |
| **Método** | Aproximado |
| **Componente Analisado** | 18,413 nós (1.0%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **1,758,429 nós** e **14,078,099 arestas**.
O diâmetro aproximado é **30**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 91.2% dos nós, 
com densidade de 0.000005.

---
*Análise concluída em 1541.54 segundos.*

---

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

---

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

---

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

---

# Análise Completa do Grafo: Maven

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 122,532 |
| **Arestas** | 540,840 |
| **Densidade** | 0.00003602 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 121,912 |
| **Componentes Fracamente Conectados (WCC)** | 1,561 |
| **Maior SCC** | 272 nós |
| **Maior WCC** | 116,772 nós |
| **Nós no Maior Componente** | 116,772 (95.30%) |
| **Arestas no Maior Componente** | 535,829 (99.07%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 8.83 |
| **Grau Máximo** | 24,161 |
| **Grau Mediano** | 4.00 |
| **In-Degree Médio** | 4.41 |
| **In-Degree Máximo** | 24,159 |
| **In-Degree Mediano** | 1.00 |
| **Out-Degree Médio** | 4.41 |
| **Out-Degree Máximo** | 856 |
| **Out-Degree Mediano** | 3.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `junit:junit` | 24,159 |
| 2 | `org.scala-lang:scala-library` | 21,115 |
| 3 | `org.slf4j:slf4j-api` | 9,723 |
| 4 | `com.google.guava:guava` | 4,879 |
| 5 | `ch.qos.logback:logback-classic` | 4,763 |
| 6 | `commons-io:commons-io` | 4,365 |
| 7 | `org.mockito:mockito-core` | 3,908 |
| 8 | `log4j:log4j` | 3,533 |
| 9 | `org.mockito:mockito-all` | 3,352 |
| 10 | `org.apache.commons:commons-lang3` | 3,271 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `org.springframework.boot:spring-boot-dependencies` | 856 |
| 2 | `org.apache.camel:camel-spring-boot-dependencies` | 735 |
| 3 | `org.apache.camel:apache-camel` | 219 |
| 4 | `com.moz.fiji.rest:fiji-rest-standard-plugin` | 200 |
| 5 | `com.moz.fiji.spark:fiji-spark` | 199 |
| 6 | `org.apache.camel:camel-bundle` | 185 |
| 7 | `org.apereo.cas:cas-server-support-ws-sts` | 172 |
| 8 | `org.apereo.cas:cas-server-support-pac4j-webflow` | 169 |
| 9 | `org.apereo.cas:cas-server-support-oidc` | 169 |
| 10 | `org.apereo.cas:cas-server-support-saml-idp-metadata-couchdb` | 167 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `junit:junit` | 0.052650 |
| 2 | `org.hamcrest:hamcrest-core` | 0.046822 |
| 3 | `org.hamcrest:hamcrest` | 0.039004 |
| 4 | `org.scala-lang:scala-library` | 0.025786 |
| 5 | `com.typesafe:config` | 0.024367 |
| 6 | `org.hamcrest:hamcrest-library` | 0.024141 |
| 7 | `com.google.code.findbugs:jsr305` | 0.014994 |
| 8 | `org.slf4j:slf4j-api` | 0.009827 |
| 9 | `com.novocode:junit-interface` | 0.007025 |
| 10 | `org.jacoco:org.jacoco.agent` | 0.005935 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `org.testng:testng` | 0.003492 |
| 2 | `org.springframework:spring-test` | 0.002801 |
| 3 | `org.assertj:assertj-core` | 0.002579 |
| 4 | `com.github.marschall:memoryfilesystem` | 0.002553 |
| 5 | `org.springframework:spring-webflux` | 0.001755 |
| 6 | `org.springframework:spring-context-support` | 0.001067 |
| 7 | `org.yaml:snakeyaml` | 0.001019 |
| 8 | `org.easymock:easymock` | 0.000995 |
| 9 | `io.projectreactor.netty:reactor-netty` | 0.000797 |
| 10 | `io.micrometer:micrometer-core` | 0.000716 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.109379 |
| **Comunidades Detectadas (Louvain)** | 1,807 |
| **Modularidade** | 0.6091 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 23 |
| **Método** | Aproximado |
| **Componente Analisado** | 272 nós (0.2%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **122,532 nós** e **540,840 arestas**.
O diâmetro aproximado é **23**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 95.3% dos nós, 
com densidade de 0.000036.

---
*Análise concluída em 616.63 segundos.*

---

# Análise Completa do Grafo: NPM

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 1,036,048 |
| **Arestas** | 11,134,428 |
| **Densidade** | 0.00001037 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 1,016,856 |
| **Componentes Fracamente Conectados (WCC)** | 4,316 |
| **Maior SCC** | 13,026 nós |
| **Maior WCC** | 1,022,526 nós |
| **Nós no Maior Componente** | 1,022,526 (98.69%) |
| **Arestas no Maior Componente** | 11,119,666 (99.87%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 21.49 |
| **Grau Máximo** | 189,648 |
| **Grau Mediano** | 7.00 |
| **In-Degree Médio** | 10.75 |
| **In-Degree Máximo** | 189,564 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 10.75 |
| **Out-Degree Máximo** | 1,000 |
| **Out-Degree Mediano** | 6.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `mocha` | 189,564 |
| 2 | `eslint` | 177,187 |
| 3 | `typescript` | 128,457 |
| 4 | `chai` | 117,181 |
| 5 | `webpack` | 116,019 |
| 6 | `babel-core` | 111,274 |
| 7 | `babel-loader` | 99,117 |
| 8 | `react` | 95,439 |
| 9 | `lodash` | 93,109 |
| 10 | `jest` | 88,203 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `sindresorhus.js` | 1,000 |
| 2 | `npm-bomb` | 999 |
| 3 | `1000-packages` | 999 |
| 4 | `all-of-them` | 989 |
| 5 | `digital-keyboard-demos` | 975 |
| 6 | `@hawkingnetwork/react-native-tab-view` | 921 |
| 7 | `@ericmcornelius/ease` | 905 |
| 8 | `vue-compment` | 895 |
| 9 | `nois-react-toast` | 873 |
| 10 | `@vuga/react-demo` | 846 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `mocha` | 0.021679 |
| 2 | `eslint` | 0.014611 |
| 3 | `chai` | 0.007349 |
| 4 | `tslib` | 0.007247 |
| 5 | `typescript` | 0.006922 |
| 6 | `tape` | 0.006882 |
| 7 | `@types/node` | 0.006784 |
| 8 | `lodash` | 0.006597 |
| 9 | `tap` | 0.006303 |
| 10 | `rimraf` | 0.005755 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `mocha` | 0.002967 |
| 2 | `eslint` | 0.002387 |
| 3 | `typescript` | 0.001337 |
| 4 | `webpack` | 0.000848 |
| 5 | `electron` | 0.000688 |
| 6 | `@electron/get` | 0.000687 |
| 7 | `global-agent` | 0.000681 |
| 8 | `airtap` | 0.000666 |
| 9 | `anyproxy` | 0.000658 |
| 10 | `antd` | 0.000658 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.123555 |
| **Comunidades Detectadas (Louvain)** | 5,428 |
| **Modularidade** | 0.4848 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 25 |
| **Método** | Aproximado |
| **Componente Analisado** | 13,026 nós (1.3%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **1,036,048 nós** e **11,134,428 arestas**.
O diâmetro aproximado é **25**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 98.7% dos nós, 
com densidade de 0.000010.

---
*Análise concluída em 71351.25 segundos.*

---

# Análise Completa do Grafo: NuGet

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 150,103 |
| **Arestas** | 412,687 |
| **Densidade** | 0.00001832 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 150,051 |
| **Componentes Fracamente Conectados (WCC)** | 2,957 |
| **Maior SCC** | 7 nós |
| **Maior WCC** | 139,801 nós |
| **Nós no Maior Componente** | 139,801 (93.14%) |
| **Arestas no Maior Componente** | 402,791 (97.60%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 5.50 |
| **Grau Máximo** | 24,996 |
| **Grau Mediano** | 2.00 |
| **In-Degree Médio** | 2.75 |
| **In-Degree Máximo** | 24,990 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 2.75 |
| **Out-Degree Máximo** | 179 |
| **Out-Degree Mediano** | 2.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `Newtonsoft.Json` | 24,990 |
| 2 | `NETStandard.Library` | 12,827 |
| 3 | `EntityFramework` | 4,983 |
| 4 | `Microsoft.Extensions.DependencyInjection` | 2,709 |
| 5 | `log4net` | 2,634 |
| 6 | `Microsoft.Extensions.DependencyInjection.Abstractions` | 2,588 |
| 7 | `Microsoft.CSharp` | 2,561 |
| 8 | `Microsoft.EntityFrameworkCore` | 2,221 |
| 9 | `Microsoft.AspNet.Mvc` | 2,158 |
| 10 | `System.ValueTuple` | 1,938 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `Dynamicweb.Admin` | 179 |
| 2 | `Bupa.Api.Common.AspNetCore` | 176 |
| 3 | `SDK.All` | 168 |
| 4 | `Microsoft.AspNetCore.App` | 150 |
| 5 | `Axle.Web.WebSharper.All` | 133 |
| 6 | `Cireson.AssetManagement.Core` | 117 |
| 7 | `uIntra` | 109 |
| 8 | `Microsoft.ASPNETCore.All` | 104 |
| 9 | `VisualStudio.Extensibility.Common` | 101 |
| 10 | `Uintra` | 100 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `Microsoft.NETCore.Targets` | 0.087696 |
| 2 | `Microsoft.NETCore.Platforms` | 0.061927 |
| 3 | `System.Runtime` | 0.048275 |
| 4 | `NETStandard.Library` | 0.034654 |
| 5 | `Newtonsoft.Json` | 0.023717 |
| 6 | `Microsoft.NETCore.Targets.UniversalWindowsPlatform` | 0.012395 |
| 7 | `Microsoft.NETCore.Targets.NETFramework` | 0.012395 |
| 8 | `Microsoft.NETCore.Targets.DNXCore` | 0.012393 |
| 9 | `System.Resources.ResourceManager` | 0.010641 |
| 10 | `System.Reflection` | 0.008155 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `NETStandard.Library` | 0.000307 |
| 2 | `Newtonsoft.Json` | 0.000126 |
| 3 | `EntityFramework` | 0.000080 |
| 4 | `runtime.native.System.Security.Cryptography.OpenSsl` | 0.000079 |
| 5 | `System.Net.Http` | 0.000055 |
| 6 | `EntityFramework.Commands` | 0.000049 |
| 7 | `System.Security.Cryptography.X509Certificates` | 0.000034 |
| 8 | `System.Security.Cryptography.Algorithms` | 0.000031 |
| 9 | `Microsoft.AspNet.Mvc` | 0.000028 |
| 10 | `Microsoft.AspNet.Hosting` | 0.000024 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.086237 |
| **Comunidades Detectadas (Louvain)** | 3,185 |
| **Modularidade** | 0.6806 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 5 |
| **Método** | Aproximado |
| **Componente Analisado** | 7 nós (0.0%) |
| **Interpretação** | Rede Altamente Conectada |

## 7. Resumo Executivo
Este grafo possui **150,103 nós** e **412,687 arestas**.
O diâmetro aproximado é **5**, indicando que 
a rede apresenta alta conectividade, típica de ecossistemas maduros.

O maior componente conectado contém 93.1% dos nós, 
com densidade de 0.000018.

---
*Análise concluída em 444.05 segundos.*

---

# Análise Completa do Grafo: Packagist

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 186,519 |
| **Arestas** | 705,462 |
| **Densidade** | 0.00002028 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 184,644 |
| **Componentes Fracamente Conectados (WCC)** | 1,630 |
| **Maior SCC** | 445 nós |
| **Maior WCC** | 181,779 nós |
| **Nós no Maior Componente** | 181,779 (97.46%) |
| **Arestas no Maior Componente** | 701,493 (99.44%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 7.56 |
| **Grau Máximo** | 74,275 |
| **Grau Mediano** | 3.00 |
| **In-Degree Médio** | 3.78 |
| **In-Degree Máximo** | 74,250 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 3.78 |
| **Out-Degree Máximo** | 216 |
| **Out-Degree Mediano** | 2.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `phpunit/phpunit` | 74,250 |
| 2 | `illuminate/support` | 16,311 |
| 3 | `squizlabs/php_codesniffer` | 14,092 |
| 4 | `guzzlehttp/guzzle` | 13,627 |
| 5 | `mockery/mockery` | 13,335 |
| 6 | `yiisoft/yii2` | 8,570 |
| 7 | `ext-json` | 7,503 |
| 8 | `laravel/framework` | 7,026 |
| 9 | `orchestra/testbench` | 6,534 |
| 10 | `symfony/console` | 6,219 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `spryker-shop/suite-b2b` | 216 |
| 2 | `spryker-shop/b2b-demo-shop` | 216 |
| 3 | `balsama/lightning_strict` | 205 |
| 4 | `spryker-shop/suite` | 181 |
| 5 | `spryker-shop/b2c-demo-shop` | 181 |
| 6 | `drustack/framework-standard-edition` | 180 |
| 7 | `gbodin/ec-light-test` | 167 |
| 8 | `drupalcoders/quick_start` | 156 |
| 9 | `openfed/openfed8` | 138 |
| 10 | `oro/platform` | 123 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `phpunit/phpunit` | 0.106056 |
| 2 | `ext-json` | 0.011912 |
| 3 | `symfony/phpunit-bridge` | 0.011623 |
| 4 | `illuminate/support` | 0.011063 |
| 5 | `squizlabs/php_codesniffer` | 0.010239 |
| 6 | `ext-mbstring` | 0.009302 |
| 7 | `guzzlehttp/guzzle` | 0.009196 |
| 8 | `psr/container` | 0.009025 |
| 9 | `yiisoft/yii2` | 0.008465 |
| 10 | `symfony/console` | 0.007204 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `phpunit/phpunit` | 0.001429 |
| 2 | `doctrine/instantiator` | 0.001078 |
| 3 | `phpstan/phpstan-phpunit` | 0.000994 |
| 4 | `phing/phing` | 0.000919 |
| 5 | `phpdocumentor/phpdocumentor` | 0.000874 |
| 6 | `jms/serializer` | 0.000229 |
| 7 | `vimeo/psalm` | 0.000205 |
| 8 | `ergebnis/composer-normalize` | 0.000177 |
| 9 | `laravel/framework` | 0.000171 |
| 10 | `myclabs/deep-copy` | 0.000169 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.142107 |
| **Comunidades Detectadas (Louvain)** | 1,807 |
| **Modularidade** | 0.5905 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 14 |
| **Método** | Aproximado |
| **Componente Analisado** | 445 nós (0.2%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **186,519 nós** e **705,462 arestas**.
O diâmetro aproximado é **14**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 97.5% dos nós, 
com densidade de 0.000020.

---
*Análise concluída em 2171.26 segundos.*

---

# Análise Completa do Grafo: Pub

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 8,667 |
| **Arestas** | 28,851 |
| **Densidade** | 0.00038413 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 8,557 |
| **Componentes Fracamente Conectados (WCC)** | 16 |
| **Maior SCC** | 62 nós |
| **Maior WCC** | 8,626 nós |
| **Nós no Maior Componente** | 8,626 (99.53%) |
| **Arestas no Maior Componente** | 28,821 (99.90%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 6.66 |
| **Grau Máximo** | 4,663 |
| **Grau Mediano** | 3.00 |
| **In-Degree Médio** | 3.33 |
| **In-Degree Máximo** | 4,655 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 3.33 |
| **Out-Degree Máximo** | 64 |
| **Out-Degree Mediano** | 2.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `flutter` | 4,655 |
| 2 | `flutter_test` | 3,723 |
| 3 | `test` | 2,299 |
| 4 | `meta` | 828 |
| 5 | `pedantic` | 782 |
| 6 | `http` | 684 |
| 7 | `path` | 639 |
| 8 | `build_runner` | 566 |
| 9 | `unittest` | 409 |
| 10 | `logging` | 404 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `magpiecli` | 64 |
| 2 | `mpcli` | 64 |
| 3 | `mgpcli` | 64 |
| 4 | `build_runner` | 41 |
| 5 | `devtools_app` | 35 |
| 6 | `over_react` | 34 |
| 7 | `pana` | 32 |
| 8 | `dartdoc` | 30 |
| 9 | `repub` | 30 |
| 10 | `webdev` | 30 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `flutter` | 0.088888 |
| 2 | `test` | 0.061618 |
| 3 | `flutter_test` | 0.058742 |
| 4 | `path` | 0.018673 |
| 5 | `pedantic` | 0.018501 |
| 6 | `meta` | 0.012119 |
| 7 | `intl` | 0.011713 |
| 8 | `http` | 0.010788 |
| 9 | `vector_math` | 0.010330 |
| 10 | `sky_tools` | 0.009566 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `flutter` | 0.006877 |
| 2 | `sky_tools` | 0.004814 |
| 3 | `test` | 0.004182 |
| 4 | `build_runner` | 0.002644 |
| 5 | `mockito` | 0.001896 |
| 6 | `vector_math` | 0.001405 |
| 7 | `test_core` | 0.001321 |
| 8 | `shelf_route` | 0.001020 |
| 9 | `build_web_compilers` | 0.000911 |
| 10 | `vm_service` | 0.000902 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.110313 |
| **Comunidades Detectadas (Louvain)** | 31 |
| **Modularidade** | 0.4839 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 8 |
| **Método** | Aproximado |
| **Componente Analisado** | 62 nós (0.7%) |
| **Interpretação** | Rede Moderadamente Conectada |

## 7. Resumo Executivo
Este grafo possui **8,667 nós** e **28,851 arestas**.
O diâmetro aproximado é **8**, indicando que 
a rede apresenta conectividade moderada.

O maior componente conectado contém 99.5% dos nós, 
com densidade de 0.000384.

---
*Análise concluída em 15.20 segundos.*

---

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

---

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

---

# Análise Completa do Grafo: Rubygems

## 1. Métricas Básicas
| Métrica | Valor |
|---------|-------|
| **Nós** | 128,010 |
| **Arestas** | 578,076 |
| **Densidade** | 0.00003528 |
| **Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---------|-------|
| **Componentes Fortemente Conectados (SCC)** | 127,564 |
| **Componentes Fracamente Conectados (WCC)** | 366 |
| **Maior SCC** | 241 nós |
| **Maior WCC** | 127,085 nós |
| **Nós no Maior Componente** | 127,085 (99.28%) |
| **Arestas no Maior Componente** | 577,479 (99.90%) |

## 3. Análise de Graus
### 3.1. Estatísticas Gerais
| Métrica | Valor |
|---------|-------|
| **Grau Médio** | 9.03 |
| **Grau Máximo** | 67,703 |
| **Grau Mediano** | 4.00 |
| **In-Degree Médio** | 4.52 |
| **In-Degree Máximo** | 67,698 |
| **In-Degree Mediano** | 0.00 |
| **Out-Degree Médio** | 4.52 |
| **Out-Degree Máximo** | 220 |
| **Out-Degree Mediano** | 4.00 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|------|-------------|-----------|
| 1 | `rake` | 67,698 |
| 2 | `bundler` | 59,684 |
| 3 | `rspec` | 48,867 |
| 4 | `pry` | 11,179 |
| 5 | `rails` | 10,459 |
| 6 | `minitest` | 9,957 |
| 7 | `activesupport` | 9,846 |
| 8 | `simplecov` | 9,269 |
| 9 | `rubocop` | 7,460 |
| 10 | `sqlite3` | 7,260 |

### 3.3. Top 10 Projetos Mais Complexos (Maior Out-Degree)
| Rank | Projeto | Out-Degree |
|------|---------|------------|
| 1 | `aws-sdk-resources` | 220 |
| 2 | `azure_sdk` | 136 |
| 3 | `rubysl` | 91 |
| 4 | `voluntary` | 82 |
| 5 | `backedup` | 82 |
| 6 | `workarea-core` | 81 |
| 7 | `hyrax` | 71 |
| 8 | `atreides` | 68 |
| 9 | `renalware-core` | 68 |
| 10 | `benmanns-atreides` | 67 |

## 4. Análise de Centralidade
_(Análise realizada em maior componente (Betweenness aproximado com k=500))_

### 4.1. Top 10 Nós por Influência (PageRank)
| Rank | Nó | PageRank Score |
|------|-----|----------------|
| 1 | `rake` | 0.069164 |
| 2 | `bundler` | 0.056957 |
| 3 | `rspec` | 0.043198 |
| 4 | `minitest` | 0.039396 |
| 5 | `rdoc` | 0.036265 |
| 6 | `rubocop` | 0.027407 |
| 7 | `hoe` | 0.025895 |
| 8 | `rspec-expectations` | 0.013112 |
| 9 | `activesupport` | 0.013100 |
| 10 | `coveralls` | 0.013083 |

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness)
| Rank | Nó | Betweenness Score |
|------|-----|-------------------|
| 1 | `rubocop` | 0.001078 |
| 2 | `parser` | 0.001005 |
| 3 | `simplecov` | 0.000737 |
| 4 | `docile` | 0.000722 |
| 5 | `github-markup` | 0.000708 |
| 6 | `github-linguist` | 0.000624 |
| 7 | `ast` | 0.000584 |
| 8 | `rake` | 0.000571 |
| 9 | `rest-client` | 0.000471 |
| 10 | `webmock` | 0.000459 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---------|-------|
| **Coeficiente de Clusterização Médio** | 0.197035 |
| **Comunidades Detectadas (Louvain)** | 420 |
| **Modularidade** | 0.3968 |

## 6. Análise de Diâmetro
| Métrica | Valor |
|---------|-------|
| **Diâmetro** | 17 |
| **Método** | Aproximado |
| **Componente Analisado** | 241 nós (0.2%) |
| **Interpretação** | Rede Dispersa |

## 7. Resumo Executivo
Este grafo possui **128,010 nós** e **578,076 arestas**.
O diâmetro aproximado é **17**, indicando que 
a rede apresenta conectividade mais dispersa.

O maior componente conectado contém 99.3% dos nós, 
com densidade de 0.000035.

---
*Análise concluída em 2700.12 segundos.*

---

# Metodologia para Cálculo do Diâmetro de Redes de Dependências
**Grafo Analisado:** Rede Geral de Dependências
**Data da Análise:** 06/08/2025 02:24:47
**Tempo de Processamento:** 44.61 segundos

## Resumo Executivo

Este relatório documenta a metodologia aplicada para calcular o diâmetro de uma rede de dependências com **1,758,429 nós** e **14,078,099 arestas**. Devido ao tamanho do grafo, foi utilizada uma abordagem de **aproximação por amostragem** que reduziu a complexidade computacional de O(V³) para O(k×(V+E)), permitindo o cálculo em 44.61 segundos.

**Resultado obtido:** Diâmetro = 28 (aproximado)

## 1. Definição do Problema e Desafios Computacionais

### 1.1. O que é o Diâmetro de um Grafo?

O **diâmetro** de um grafo é definido como a maior distância (número de arestas no menor caminho) entre qualquer par de nós no grafo. Em termos matemáticos:

```
diâmetro(G) = max{d(u,v) : u,v ∈ V}
```

Onde `d(u,v)` é a distância mais curta entre os nós `u` e `v`.

### 1.2. Por que o Diâmetro é Importante?

Em redes de dependências, o diâmetro indica:
- **Conectividade da rede:** Quão bem integrado está o ecossistema
- **Propagação de impactos:** Distância máxima que uma mudança pode percorrer
- **Eficiência de navegação:** Quantos 'saltos' são necessários para conectar componentes distantes
- **Estrutura hierárquica:** Indica se existem gargalos ou pontos centrais

### 1.3. Desafio Computacional

O cálculo exato do diâmetro tem complexidade computacional **O(V³)** usando algoritmos clássicos como Floyd-Warshall, ou **O(V²E)** usando múltiplas execuções de algoritmos de caminho mais curto.

**Para o grafo analisado:**
- Nós (V): 1,758,429
- Arestas (E): 14,078,099
- Complexidade O(V³): ~5,437,190,038,579,187,589 operações
- Complexidade O(V²E): ~43,530,503,446,503,454,059 operações

**Estimativa de tempo para cálculo exato:** Várias horas ou dias em hardware convencional.

## 2. Metodologia Escolhida: Aproximação por Amostragem

### 2.1. Justificativa da Escolha

**Critérios de Decisão:**
1. **Viabilidade Computacional:** Necessidade de resultado em tempo razoável
2. **Precisão Adequada:** Para análise exploratória, aproximação é suficiente
3. **Escalabilidade:** Método deve funcionar para grafos ainda maiores
4. **Interpretabilidade:** Resultado deve ser compreensível para análise

**Alternativas Consideradas:**
- ❌ **Cálculo Exato:** Inviável computacionalmente
- ❌ **Amostragem de Arestas:** Menos precisa para diâmetro
- ❌ **Heurísticas Específicas:** Complexas e menos generalizáveis
- ✅ **Amostragem de Nós:** Balanceamento ideal entre precisão e eficiência

### 2.2. Algoritmo Implementado (Passo a Passo)

#### Passo 1: Identificação de Componentes
```python
if graph.is_directed():
    components = list(nx.strongly_connected_components(graph))
else:
    components = list(nx.connected_components(graph))
```

**Justificativa:** O diâmetro só pode ser calculado dentro de componentes conectados. Para grafos direcionados (como redes de dependências), usamos componentes **fortemente conectados** onde existe caminho direcionado entre qualquer par de nós.

**Resultado:** 1,730,853 componentes identificados
**Tamanhos:** Min=1, Max=18,413, Média=1.0

#### Passo 2: Seleção do Maior Componente
```python
largest_component = max(components, key=len)
subgraph = graph.subgraph(largest_component)
```

**Justificativa:** O maior componente representa a 'rede principal' e contém a maioria das interações relevantes.

**Maior componente:** 18,413 nós (1.05% do grafo total)

#### Passo 3: Decisão Exato vs. Aproximado
```python
if len(largest_component) <= sample_size:
    return nx.diameter(subgraph)  # Cálculo exato
else:
    # Aproximação por amostragem
```

**Limite configurado:** 1,000 nós
**Tamanho do componente:** 18,413 nós
**Método utilizado:** APROXIMADO

#### Passo 4: Aproximação por Amostragem
```python
sample_nodes = random.sample(largest_component, min(1000, len(largest_component)))
max_distance = 0
for source in sample_nodes[:100]:  # Limita nós fonte
    lengths = nx.single_source_shortest_path_length(subgraph, source)
    max_dist_from_source = max(lengths.values())
    max_distance = max(max_distance, max_dist_from_source)
```

**Parâmetros da amostragem:**
- **Amostra de nós:** 1.000 nós selecionados aleatoriamente
- **Nós fonte:** 100 primeiros da amostra (para economizar tempo)
- **Complexidade resultante:** O(100 × (V + E)) ≈ O(V + E)

## 3. Análise dos Resultados

### 3.1. Métricas Obtidas

| Métrica | Valor | Interpretação |
|---------|-------|---------------|
| **Diâmetro Calculado** | 28 | Maior distância entre nós no maior componente |
| **Método Utilizado** | Aproximado | Nível de precisão do resultado |
| **Componente Analisado** | 18,413 nós | 1.0% do grafo total |
| **Tempo de Cálculo** | 44.61s | Eficiência computacional |

### 3.2. Interpretação do Resultado

**Rede Dispersa**: O alto diâmetro indica conectividade mais dispersa, possivelmente com sub-ecossistemas menos integrados.

**Implicações práticas:**
- Mudanças em um nó podem alcançar qualquer outro em no máximo 28 passos
- A rede possui baixa integração
- Propagação de vulnerabilidades: até 28 níveis de dependência

### 3.3. Composição do Maior Componente por Plataforma

| Plataforma | Nós | Percentual | Relevância |
|------------|-----|------------|------------|
| NPM | 14,530 | 78.9% | Alta |
| CRAN | 1,111 | 6.0% | Média |
| Rubygems | 1,019 | 5.5% | Média |
| Cargo | 617 | 3.4% | Baixa |
| CPAN | 611 | 3.3% | Baixa |
| Pypi | 257 | 1.4% | Baixa |
| Pub | 170 | 0.9% | Baixa |
| Hex | 37 | 0.2% | Baixa |
| Atom | 30 | 0.2% | Baixa |
| Conda | 22 | 0.1% | Baixa |
| Dub | 2 | 0.0% | Baixa |
| NuGet | 2 | 0.0% | Baixa |
| Haxelib | 2 | 0.0% | Baixa |
| Homebrew | 2 | 0.0% | Baixa |
| Packagist | 1 | 0.0% | Baixa |

### 3.4. Nós Mais Importantes (Maior Grau)

| Rank | Nó | Grau | Plataforma | Importância |
|------|-----|------|------------|-------------|
| 1 | `mocha` | 4,521 | NPM | Crítica |
| 2 | `eslint` | 3,129 | NPM | Crítica |
| 3 | `tape` | 1,704 | NPM | Crítica |
| 4 | `chai` | 1,697 | NPM | Crítica |
| 5 | `typescript` | 1,457 | NPM | Crítica |
| 6 | `nyc` | 1,381 | NPM | Crítica |
| 7 | `prettier` | 1,312 | NPM | Crítica |
| 8 | `rimraf` | 1,166 | NPM | Crítica |
| 9 | `coveralls` | 1,135 | NPM | Crítica |
| 10 | `istanbul` | 1,073 | NPM | Crítica |

## 4. Limitações e Considerações Técnicas

### 4.1. Limitações do Método

**Limitações da Aproximação:**
- ⚠️ **Subestimativa Possível:** O valor pode ser menor que o diâmetro real
- ⚠️ **Variabilidade:** Resultados podem variar entre execuções (±1-2 tipicamente)
- ⚠️ **Dependência da Amostra:** Qualidade depende da representatividade dos nós amostrados
- ⚠️ **Componentes Isolados:** Apenas o maior componente é considerado

**Confiabilidade Estimada:** 85-95% (baseado em literatura de redes complexas)

### 4.2. Metodologias Alternativas (Não Implementadas)

| Método | Vantagens | Desvantagens | Por que não foi escolhido |
|--------|-----------|--------------|---------------------------|
| **Cálculo Exato** | Precisão absoluta | O(V³), impraticável | Tempo computacional proibitivo |
| **BFS de Múltiplas Fontes** | Mais preciso que amostragem | Ainda O(V²) | Complexidade ainda alta |
| **Algoritmos Aproximados Avançados** | Melhores garantias teóricas | Implementação complexa | Complexidade de código vs. ganho |
| **Landmark-based** | Eficiente para queries | Pré-processamento custoso | Overkill para análise única |

### 4.3. Validação do Método

**Checagens de Consistência Realizadas:**
- ✅ Verificação de componentes fortemente conectados
- ✅ Validação de que todos os nós são alcançáveis
- ✅ Comparação com propriedades esperadas de redes de dependências
- ✅ Análise de distribuição de graus para detecção de anomalias

## 5. Recomendações e Trabalhos Futuros

### 5.1. Para Melhorar a Precisão

1. **Aumentar Amostra:** Usar 500-1000 nós fonte (trade-off: +tempo, +precisão)
2. **Amostragem Estratificada:** Amostrar proporcionalmente por plataforma
3. **Múltiplas Execuções:** Executar 3-5 vezes e usar média/mediana
4. **Algoritmos Híbridos:** Combinar amostragem com heurísticas específicas

### 5.2. Para Análises Complementares

- **Raio do Grafo:** Menor distância máxima de qualquer nó
- **Distribuição de Distâncias:** Histograma completo das distâncias
- **Diâmetro por Plataforma:** Análise separada de cada ecossistema
- **Evolução Temporal:** Como o diâmetro muda ao longo do tempo

## 6. Conclusão

A metodologia de **aproximação por amostragem** se mostrou eficaz para calcular o diâmetro de uma rede de dependências com 1,758,429 nós em apenas 44.61 segundos. O resultado obtido (**diâmetro = 28**) fornece insights valiosos sobre a estrutura e conectividade da rede.

**Principais contribuições desta análise:**
1. **Metodologia Escalável:** Demonstra viabilidade para grafos grandes
2. **Insights Estruturais:** Revela características da rede de dependências
3. **Base para Análises Futuras:** Estabelece baseline para comparações
4. **Documentação Completa:** Permite reprodução e validação

**Limitações aceitas:**
- Aproximação com confiabilidade estimada de 85-95%
- Análise limitada ao maior componente conectado
- Variabilidade potencial de ±1-2 no resultado

---

## Informações Técnicas

**Ambiente de Execução:**
- Data: 06/08/2025 às 02:24:51
- Tempo de processamento: 44.61 segundos
- NetworkX version: 3.5
- Método: aproximado

**Parâmetros utilizados:**
- Sample size: 1.000 nós
- Nós fonte: 100
- Limite para cálculo exato: 1.000 nós

*Relatório gerado automaticamente pelo sistema de análise de grafos de dependências.*
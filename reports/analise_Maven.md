# Análise do Grafo: Maven

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 122,532 |
| **Arestas (Dependências)** | 540,840 |
| **Densidade do Grafo** | 0.00003602 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 1,561 |
| **Nós no Maior Componente (LCC)** | 116,772 (95.30%) |
| **Arestas no Maior Componente (LCC)** | 535,829 (99.07%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 4.41 | 4.41 | 8.83 |
| **Mediana** | 1.00 | 3.00 | 4.00 |
| **Máximo** | 24,159 | 856 | 24,161 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
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
|---|---|---|
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
|---|---|---|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `org.testng:testng` | 0.003586 |
| 2 | `org.springframework:spring-test` | 0.002837 |
| 3 | `org.assertj:assertj-core` | 0.002766 |
| 4 | `com.github.marschall:memoryfilesystem` | 0.002715 |
| 5 | `org.springframework:spring-webflux` | 0.001766 |
| 6 | `org.springframework:spring-context-support` | 0.001110 |
| 7 | `org.yaml:snakeyaml` | 0.001069 |
| 8 | `org.easymock:easymock` | 0.001046 |
| 9 | `io.projectreactor.netty:reactor-netty` | 0.000830 |
| 10 | `org.scalatest:scalatest_2.12` | 0.000778 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.109379 |
| **Comunidades Detectadas (Louvain)** | 1,807 |
| **Modularidade** | 0.6091 |

---
*Análise concluída em 624.92 segundos.*


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
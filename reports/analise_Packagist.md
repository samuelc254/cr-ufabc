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
# Análise do Grafo: NuGet

## 1. Métricas Gerais
| Métrica | Valor |
|---|---|
| **Nós (Projetos/Dependências)** | 150,103 |
| **Arestas (Dependências)** | 412,687 |
| **Densidade do Grafo** | 0.00001832 |
| **Grafo Direcionado** | Sim |

## 2. Análise de Conectividade
| Métrica | Valor |
|---|---|
| **Componentes Fracamente Conectados** | 2,957 |
| **Nós no Maior Componente (LCC)** | 139,801 (93.14%) |
| **Arestas no Maior Componente (LCC)** | 402,791 (97.60%) |

## 3. Análise de Graus (Popularidade e Complexidade)
### 3.1. Estatísticas Gerais de Grau
| Métrica | In-Degree (Popularidade) | Out-Degree (Complexidade) | Grau Total |
|---|---|---|---|
| **Média** | 2.75 | 2.75 | 5.50 |
| **Mediana** | 0.00 | 2.00 | 2.00 |
| **Máximo** | 24,990 | 179 | 24,996 |

### 3.2. Top 10 Dependências Mais Populares (Maior In-Degree)
| Rank | Dependência | In-Degree |
|---|---|---|
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
|---|---|---|
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
|---|---|---|
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

### 4.2. Top 10 Nós por Importância Estrutural (Betweenness Centrality)
| Rank | Nó | Betweenness Score |
|---|---|---|
| 1 | `NETStandard.Library` | 0.000298 |
| 2 | `Newtonsoft.Json` | 0.000104 |
| 3 | `runtime.native.System.Security.Cryptography.OpenSsl` | 0.000079 |
| 4 | `EntityFramework` | 0.000077 |
| 5 | `System.Net.Http` | 0.000054 |
| 6 | `EntityFramework.Commands` | 0.000046 |
| 7 | `Microsoft.NETCore.UniversalWindowsPlatform` | 0.000036 |
| 8 | `System.Security.Cryptography.X509Certificates` | 0.000034 |
| 9 | `Microsoft.AspNet.Mvc` | 0.000033 |
| 10 | `System.Security.Cryptography.Algorithms` | 0.000031 |

## 5. Análise Estrutural e de Comunidades
| Métrica | Valor |
|---|---|
| **Coeficiente de Clusterização Médio** | 0.086237 |
| **Comunidades Detectadas (Louvain)** | 3,185 |
| **Modularidade** | 0.6806 |

---
*Análise concluída em 508.99 segundos.*


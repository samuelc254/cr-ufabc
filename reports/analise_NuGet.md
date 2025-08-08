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
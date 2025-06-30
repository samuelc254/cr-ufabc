# Rede de Dependências em Projetos de Software

*Projeto final para a disciplina BCM-0506 - Comunicação e Redes (2025.2) da Universidade Federal do ABC (UFABC).*

---

## Sumário

- [Objetivos](#objetivos)
- [Motivação](#motivação)
- [Ferramentas](#ferramentas-de-software-plataformas-e-serviços-computacionais)
- [Dados](#dados)
- [Modelagem](#modelagem)
- [Resultados](#resultados)

---

## Objetivos

### Objetivo Geral
Analisar quais pacotes de um software são os mais críticos em um grande ecossistema.

### Objetivos Específicos
Descobrir quais bibliotecas formam a base sobre a qual milhares de outros projetos são construídos.

---

## Motivação

O projeto busca:
- Revelar as fundações invisíveis do software moderno e identificar pontos únicos de falha.
- Apontar como um problema em um pacote central pode impactar uma vasta gama de aplicações.

---

## Ferramentas de Software, Plataformas e Serviços Computacionais

Para a execução deste projeto, serão utilizadas as seguintes ferramentas:

- **Zenodo:** Repositório de dados de pesquisa de acesso aberto. Será utilizado para baixar o conjunto de dados públicos do Libraries.io, que contém as informações de dependência de milhões de pacotes de software e servirá como a fonte primária para a construção da rede.

- **Libraries.io:** Serviço online que cataloga metadados de pacotes de software de código aberto. É a fonte originária dos dados e sua base conceitual, fornecendo as relações que definirão os nós (pacotes) e as arestas (dependências) do nosso grafo.

- **Python (Linguagem de Programação):** Linguagem de programação de alto nível que será a principal ferramenta para a análise de dados e manipulação de redes, utilizando as seguintes bibliotecas:
  - **Pandas:** Para carregar, limpar e filtrar os arquivos do dataset, isolando o ecossistema de interesse e preparando os dados para a modelagem.
  - **NetworkX:** Para construir o grafo direcionado, calcular as métricas de centralidade (Grau, PageRank, Intermediação) e analisar a estrutura topológica da rede.

---

## Dados

### 5.1. Origem e Obtenção
Os dados necessários para este projeto serão obtidos de fontes públicas e abertas. A origem primária dos dados é o serviço **Libraries.io**, e a obtenção será feita através do repositório [Zenodo](https://zenodo.org/records/3626071).

### 5.2. Tamanho do Conjunto de Dados
Será feito um recorte do dataset com, as versões mais recentes dos pacotes para garantir uma estrutura relevante. Idealmente, o conjunto conterá milhares ou milhões de vértices. A filtragem poderá ser feita por critérios como popularidade, número de dependências ou linguagem de programação.

---

## Modelagem

### 6.1. Vértices
Cada vértice representará um pacote ou biblioteca de software individual (por exemplo, `express`, `react`, `numpy`, `pandas`).

### 6.2. Arestas
As arestas serão **direcionadas** e representarão uma relação de dependência: se o pacote A depende do pacote B, haverá uma aresta de A para B. Isso permite identificar quais pacotes são mais "dependidos" (alto grau de entrada) e quais dependem fortemente de outros (alto grau de saída).

---

## Resultados 

### Esperados
O projeto busca responder às seguintes questões:
- Quais pacotes têm o maior grau de entrada, sendo os mais reutilizados? 
- Quais bibliotecas representam pontos únicos de falha no ecossistema? 
- Qual é a estrutura da rede de dependências (hierárquica, hubs, modular)? 
- Quais pacotes podem ser considerados "infraestrutura crítica"? 
- Quais são os pacotes mais centrais na rede? 
- Um pequeno grupo de pacotes sustenta a maior parte do ecossistema? 
- Quais pacotes são mais vulneráveis devido à sua alta conectividade? 
- Como essas estruturas variam entre diferentes linguagens (ex: JavaScript vs. Python)?

### Preliminares
Desenvolvimento até 30/06/2025:
- 

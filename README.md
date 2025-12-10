# .MiniProjeto.ODS-

O projeto teve como **Objetivo Geral** desenvolver uma aplicação web interativa para analisar e visualizar dados relacionados aos Objetivos de Desenvolvimento Sustentável (ODS), com foco nos seguintes indicadores:

- **ODS 6 (Indicador 6.1.1):** Proporção da população que utiliza serviços de água potável gerenciados de forma segura.  
- **ODS 7 (Indicador 7.1.1):** Percentagem da população com acesso à eletricidade.

A aplicação foi planejada para permitir que o usuário explore de forma simples, autônoma e intuitiva o progresso dos países no acesso a serviços básicos essenciais.

---

## 2. Metodologia e Tecnologias

O desenvolvimento foi estruturado em quatro fases principais, utilizando uma stack voltada para ciência de dados e aplicações web.

### 2.1. Coleta e Pré-processamento de Dados

- **Fonte:** Arquivos `.xlsx` de repositórios públicos vinculados aos ODS.  
- **Ferramenta:** Biblioteca **Pandas (Python)**.  
- **Processos Realizados:**
  - **Padronização de nomes** de colunas (ex.: *GeoAreaName → País*, *TimePeriod → Ano*).
  - **Remoção de dados ausentes** com `df.dropna()`.
  - **Conversão de tipos numéricos** usando `pd.to_numeric` para garantir integridade das colunas *Ano* e *Valor*.

### 2.2. Análise Exploratória de Dados (EDA)

A EDA respondeu perguntas-chave sobre o comportamento dos indicadores, com destaque para:

- **Progresso Histórico:** cálculo do aumento percentual do ODS 7 (Acesso à Eletricidade) entre o primeiro e o último ano disponível para cada país.

### 2.3. Desenvolvimento e Visualização Web

- **Framework Web:** **Streamlit**, ideal para construir dashboards interativos rapidamente.  
- **Visualizações:** **Plotly Express**, que forneceu gráficos dinâmicos com tooltips e navegação fluida.

**Gráficos Implementados:**
- **Histograma:** mostra a distribuição geral do indicador em todos os países e anos.  
- **Gráfico de Barras:** apresenta um ranking dos países com base no valor mais recente disponível.

### 2.4. Hospedagem e Deploy

- Versionamento via **GitHub**.
- Deploy contínuo e gratuito através do **Streamlit Cloud**, permitindo acesso público imediato.

Link da aplicação:  
👉 **https://ktvrdmbg2tjkexdlbo3aoj.streamlit.app/**

---

## 3. Resultados e Análises da Aplicação

A aplicação final permite alternância entre indicadores dos ODS, seleção de países e visualização detalhada dos dados.

### 3.1. Distribuição dos Indicadores (Histograma)

- Para o **ODS 7**, os registros de País/Ano se concentram majoritariamente em torno de **84,17% ou mais**, mostrando que o acesso à eletricidade está em níveis elevados na maior parte dos países analisados.
- No **ODS 6**, a distribuição é mais dispersa, indicando variações maiores e desafios ainda significativos no acesso à água segura.

### 3.2. Progresso Histórico

A análise temporal revelou que os países com maior evolução no acesso à eletricidade ao longo dos anos foram:

- **Estados Unidos**
- **Suíça**
- **Bulgária**

Esses resultados indicam melhorias consistentes e impacto positivo de iniciativas recentes.

---

## 4. Conclusão e Reflexão Final

O projeto demonstrou como é possível construir uma solução simples, eficiente e interativa de **Business Intelligence**, integrando:

- Tratamento e limpeza de dados com **Pandas**  
- Visualização dinâmica com **Plotly**  
- Publicação ágil com **Streamlit**

O pré-processamento se mostrou a etapa mais trabalhosa, destacando a importância de dados limpos para análises confiáveis.

A aplicação publicada representa uma **prova de conceito** de como ferramentas de ciência de dados podem contribuir para monitorar e comunicar avanços em metas globais de sustentabilidade.

### 🔮 Possíveis Melhorias Futuras

- Inclusão de um **Mapa Interativo (Choropleth)** usando Plotly para análise geográfica dos indicadores.
- Adição de séries temporais dinâmicas.
- Comparações entre regiões ou blocos econômicos.

---

📌 **Acesse o Dashboard Completo:**  
https://ktvrdmbg2tjkexdlbo3aoj.streamlit.app/




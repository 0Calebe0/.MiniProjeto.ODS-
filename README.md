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
  - **Conversão de**



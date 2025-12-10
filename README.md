# .MiniProjeto.ODS-
Relatório Final: Desenvolvimento de Aplicação
Web para Monitoramento dos ODS 6 e 7
1. Introdução e Objetivos
O presente projeto teve como Objetivo Geral desenvolver uma aplicação web interativa
para analisar e visualizar dados relacionados aos Objetivos de Desenvolvimento
Sustentável (ODS), especificamente o ODS 6: Água Potável e Saneamento e o ODS 7:
Energia Limpa e Acessível. A meta era permitir que o usuário explorasse o progresso de
países no acesso a serviços básicos de forma autônoma e intuitiva.
O trabalho focou em dois indicadores críticos:
● ODS 6 (Indicador 6.1.1): Proporção da população que utiliza serviços de água
potável gerenciados de forma segura.
● ODS 7 (Indicador 7.1.1): Percentagem da população com acesso à eletricidade.
2. Metodologia e Tecnologias
O projeto seguiu uma metodologia estruturada em quatro fases principais, utilizando uma
stack tecnológica robusta e focada em ciência de dados:
2.1. Coleta e Pré-processamento de Dados
● Fonte e Formato: Os dados foram obtidos em arquivos .xlsx de fontes públicas
confiáveis (relatórios de ODS).
● Limpeza (Pandas): A biblioteca Pandas (Python) foi empregada para carregar e
transformar os dados. A fase de limpeza foi essencial e envolveu:
○ Renomeação: Padronização das colunas-chave para maior clareza
(GeoAreaName para Pais, TimePeriod para Ano e Value para Valor).
○ Tratamento de Ausentes: Remoção de registros incompletos (df.dropna()) e
conversão de tipos de dados (pd.to_numeric) para garantir que as colunas
Ano e Valor fossem estritamente numéricas, prevenindo erros nas análises
subsequentes.
2.2. Análise Exploratória de Dados (EDA)
A EDA utilizou o Pandas para responder a perguntas-chave. A análise de maior
profundidade foi a identificação do Progresso Histórico, onde foi calculado o diferencial
percentual de acesso à eletricidade (ODS 7) entre o primeiro e o último ano de registro para
cada país, demonstrando o avanço líquido ao longo do período coberto pelos dados.
2.3. Desenvolvimento e Visualização Web
● Web Framework: O framework Streamlit foi escolhido por sua capacidade de
transformar scripts Python em aplicações web interativas com poucas linhas de
código, ideal para o desenvolvimento rápido de dashboards orientados a dados.
● Visualização: A biblioteca Plotly Express foi utilizada para gerar gráficos dinâmicos
e com tooltips interativos, melhorando a experiência do usuário.
○ Histograma: Implementado como gráfico principal para visualizar a
distribuição de frequência dos valores, indicando em qual faixa de
porcentagem de acesso a maioria dos registros de País/Ano se concentra.
○ Gráfico de Barras: Implementado para criar um ranking claro dos países
com base no valor do indicador no ano mais recente disponível, facilitando a
comparação imediata.
2.4. Hospedagem e Deploy
O projeto foi versionado no GitHub e, em seguida, implantado de forma contínua e gratuita
na nuvem via Streamlit Cloud. Esta etapa garantiu a acessibilidade pública da aplicação e
a automatização do processo de build a partir do repositório Git.
3. Resultados e Análise Chave da Aplicação
A aplicação final permite a alternância imediata entre os ODS 6 e 7 e a seleção de múltiplos
países para comparação.
3.1. Insights da Distribuição (Histograma)
O Histograma revelou que, para o ODS 7 (Acesso à Eletricidade), uma grande parte dos
registros de País/Ano já se concentra em patamares de 84,17% . Isso sugere que o
indicador já está em níveis altos na maioria das observações. Já para o ODS 6 (Água
Segura), a distribuição pode ser mais dispersa, indicando que o acesso seguro à água
ainda é um desafio em um número maior de contextos.
3.2. Descobertas do Progresso Histórico
A análise mais aprofundada, visível na tabela de dados subjacente ou nos rankings,
demonstrou que as maiores evoluções no acesso à eletricidade (ODS 7) ao longo do
período de dados ocorreram em países que estavam partindo de uma base mais baixa. Os
dados revelaram que Estados Unidos, Suíça e Bulgária foram os que apresentaram o
maior aumento percentual em seu acesso à eletricidade, indicando um impacto positivo das
iniciativas e investimentos recentes.
4. Conclusão e Reflexão Final
O projeto demonstrou a capacidade de criar uma solução de Business Intelligence
simplificada, integrando com sucesso as etapas de manipulação, análise e visualização de
dados. O objetivo de desenvolver uma aplicação web interativa e baseada em dados reais
foi plenamente alcançado.
O principal aprendizado reside na robustez do Pandas para a limpeza de dados brutos e na
eficácia do Streamlit para prototipagem rápida. O desafio de tratar inconsistências nos
dados-fonte (como valores ausentes) reforçou a importância da etapa de
pré-processamento, que consumiu a maior parte do tempo de codificação.
A aplicação, acessível publicamente em https://ktvrdmbg2tjkexdlbo3aoj.streamlit.app/ é uma
prova de conceito de como as ferramentas de data science podem ser aplicadas para
monitorar e comunicar o progresso em relação a metas globais de desenvolvimento
sustentável.
Para futuras expansões, sugere-se a inclusão de um Mapa Interativo (Choropleth) do
Plotly para uma análise geográfica da distribuição dos indicadores.

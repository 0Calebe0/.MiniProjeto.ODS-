import streamlit as st
import pandas as pd
import plotly.express as px

# --- FUNÇÃO DE CARREGAMENTO E LIMPEZA DE DADOS ---
@st.cache_data
def load_data():
    # ... (O código de carregamento e limpeza de dados permanece o mesmo) ...
    df_ods6 = pd.read_excel('Indicador6.1.1.xlsx')
    df_ods7 = pd.read_excel('Indicador7.1.1.xlsx')

    def clean_and_rename(df):
        df = df.rename(columns={'GeoAreaName': 'Pais', 'TimePeriod': 'Ano', 'Value': 'Valor'})
        df.dropna(subset=['Pais', 'Ano', 'Valor'], inplace=True)
        df['Ano'] = pd.to_numeric(df['Ano'], errors='coerce').astype('Int64')
        df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
        df.dropna(subset=['Ano', 'Valor'], inplace=True)
        return df
    
    df_ods6 = clean_and_rename(df_ods6)
    df_ods7 = clean_and_rename(df_ods7)

    return df_ods6, df_ods7

df_ods6, df_ods7 = load_data()


# --- ESTRUTURA E INTERFACE STREAMLIT ---

st.set_page_config(layout="wide", page_title="Monitoramento ODS 6 & 7")
st.title('🌎 Monitoramento dos ODS 6 e 7')
st.markdown('### Água Potável e Saneamento | Energia Limpa e Acessível')

# 1. BARRA LATERAL (Filtros Interativos)
with st.sidebar:
    st.header("Filtros de Análise")
    
    ods_escolhido = st.selectbox(
        'Escolha o Objetivo de Desenvolvimento Sustentável (ODS):',
        ('ODS 6: Água e Saneamento', 'ODS 7: Energia Limpa')
    )

if ods_escolhido == 'ODS 6: Água e Saneamento':
    df_analise = df_ods6
    ods_titulo = 'ODS 6 - Proporção de Acesso à Água Potável Segura'
else:
    df_analise = df_ods7
    ods_titulo = 'ODS 7 - Percentagem da População com Acesso à Eletricidade'
    
st.header(ods_titulo)

# 2. FILTRO DE PAÍS (Multiseleção)
paises_disponiveis = sorted(df_analise['Pais'].unique().tolist())
paises_selecionados = st.multiselect(
    'Selecione os Países para Comparação (Use o filtro acima):', 
    paises_disponiveis, 
    # Para o Histograma, usaremos todos os países por padrão para ver a distribuição geral
    default=paises_disponiveis 
)

# Para o Histograma, vamos usar o DataFrame COMPLETO (df_analise) e não apenas o filtrado,
# a não ser que o usuário queira filtrar a distribuição por país.
# Vamos usar o df_filtrado para ser consistente com o filtro 'paises_selecionados'
df_filtrado = df_analise[df_analise['Pais'].isin(paises_selecionados)]

# 3. VISUALIZAÇÃO DE DADOS INTERATIVA
if not df_filtrado.empty:
    
    # --- HISTOGRAMA (NOVO GRÁFICO PRINCIPAL) ---
    st.subheader('🔔 Distribuição da Porcentagem de Acesso (Frequência)')
    
    # Cria o Histograma
    fig_hist = px.histogram(
        df_filtrado, 
        x='Valor', 
        # color='Pais', # Não vamos colorir por país, para evitar muitas cores no Histograma
        nbins=20, # Define 20 'baldes' ou classes para a distribuição
        title=f'Histograma de Valores de Acesso ({ods_escolhido})',
        labels={'Valor': 'Valor do Indicador (%)', 'count': 'Frequência (Nº de Registros País/Ano)'},
        histnorm='percent', # Mostra a altura das barras como porcentagem do total
        opacity=0.8
    )
    
    # Adiciona a linha de média (opcional, mas muito útil)
    media = df_filtrado['Valor'].mean()
    fig_hist.add_vline(x=media, line_width=2, line_dash="dash", line_color="red", 
                       annotation_text=f"Média Geral: {media:.2f}%")
                       
    st.plotly_chart(fig_hist, use_container_width=True)

    # --- GRÁFICO DE BARRAS (PARA COMPARAÇÃO NO ÚLTIMO ANO) ---
    st.subheader('📊 Comparação por País no Último Ano Disponível')

    # ... (O código do Gráfico de Barras permanece o mesmo) ...
    ultimo_ano = df_filtrado['Ano'].max()
    df_ultimo_ano = df_filtrado[df_filtrado['Ano'] == ultimo_ano]
    
    if not df_ultimo_ano.empty:
        df_ultimo_ano_agg = df_ultimo_ano.groupby('Pais')['Valor'].mean().reset_index()
        
        fig_bar = px.bar(
            df_ultimo_ano_agg.sort_values(by='Valor', ascending=False), 
            x='Valor', 
            y='Pais', 
            orientation='h', 
            title=f'Ranking de Países em {ultimo_ano} ({ods_escolhido})',
            labels={'Valor': 'Valor do Indicador (%)', 'Pais': 'País'},
            color='Valor', 
            color_continuous_scale=px.colors.sequential.Plasma 
        )
        fig_bar.update_layout(yaxis={'categoryorder':'total ascending'}) 
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info(f"Não há dados para o último ano ({ultimo_ano}) para os países selecionados.")


    # 4. TABELA DE DADOS DETALHADOS
    st.subheader('📋 Dados Detalhados')
    st.dataframe(
        df_filtrado[['Pais', 'Ano', 'Valor']].sort_values(by=['Ano', 'Valor'], ascending=[False, False]), 
        use_container_width=True
    )

else:
    st.warning('Por favor, selecione pelo menos um país para visualizar o progresso.')

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard ZettaLab - Pará", layout="wide")
st.title("📊 Dashboard Interativo - Desmatamento x Socioeconomia (Pará)")

@st.cache_data
def carregar_dados():
    df = pd.read_csv('saida/base_completa_merge.csv')
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['areakm'] = pd.to_numeric(df['areakm'], errors='coerce')
    df['idhm_2010'] = pd.to_numeric(df['idhm_2010'], errors='coerce')
    df['idhm_cat'] = df['idhm_cat'].astype(str)
    return df

df = carregar_dados()

# ==================== FILTROS ====================
st.sidebar.header("🎛️ Filtros")
st.sidebar.markdown("⚠️ O ano **2007** contém dados acumulados e pode distorcer a análise.")
st.sidebar.markdown("Desmarcado por padrão para garantir visualizações mais realistas.")

anos_unicos = sorted(df['year'].dropna().unique())
anos_default = [ano for ano in anos_unicos if ano > 2007]

anos = st.sidebar.multiselect("Ano(s) a considerar", options=anos_unicos, default=anos_default)
municipios = st.sidebar.multiselect("Município", sorted(df['municipio'].unique()), default=[])
categorias = st.sidebar.multiselect("Categoria de IDHM", ['Baixo', 'Médio', 'Alto'], default=['Baixo', 'Médio', 'Alto'])

df_filtros = df[df['year'].isin(anos)]
if municipios:
    df_filtros = df_filtros[df_filtros['municipio'].isin(municipios)]
if categorias:
    df_filtros = df_filtros[df_filtros['idhm_cat'].isin(categorias)]

if 2007 in anos:
    st.warning("⚠️ Cuidado: o ano de 2007 está incluído e pode distorcer os resultados. Use com critério.")

# ==================== MÉTRICAS ====================
col1, col2, col3 = st.columns(3)
col1.metric("🔍 Municípios Selecionados", df_filtros['municipio'].nunique())
col2.metric("🗓️ Intervalo de Anos", f"{min(anos)} - {max(anos)}")
col3.metric("🌳 Área Total Desmatada", f"{df_filtros['areakm'].sum():,.2f} km²")

# ==================== GRÁFICOS ====================
st.markdown("### 📈 Evolução do Desmatamento")
evolucao = df_filtros.groupby('year')['areakm'].sum().reset_index()
fig1, ax1 = plt.subplots()
sns.lineplot(data=evolucao, x='year', y='areakm', marker='o', ax=ax1)
ax1.set_title("Evolução da Área Total Desmatada (km²)")
ax1.set_ylabel("Área Desmatada (km²)")
st.pyplot(fig1)

st.markdown("### 🧠 Correlação: Indicadores vs Desmatamento")
variaveis = ['areakm', 'populacao_2022', 'pib_per_capita_2021', 'idhm_2010', 'desmatamento_per_capita']
correlacao = df_filtros[variaveis].corr()
fig2, ax2 = plt.subplots(figsize=(7, 5))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', ax=ax2)
st.pyplot(fig2)

st.markdown("### 📊 Área Desmatada por Categoria de IDHM")
df_barras = df_filtros.groupby('idhm_cat')['areakm'].sum().reset_index()
fig3, ax3 = plt.subplots()
sns.barplot(data=df_barras, x='idhm_cat', y='areakm', ax=ax3, palette='Set2')
ax3.set_ylabel("Área Desmatada (km²)")
ax3.set_xlabel("Categoria de IDHM")
ax3.set_title("Desmatamento Total por Categoria de IDHM")
st.pyplot(fig3)

st.markdown("### 🗂️ Tabela com Dados Filtrados")
st.dataframe(df_filtros[['municipio', 'year', 'areakm', 'pib_per_capita_2021', 'idhm_2010', 'idhm_cat']])

st.download_button(
    label="📥 Baixar CSV Filtrado",
    data=df_filtros.to_csv(index=False),
    file_name='dados_filtrados.csv',
    mime='text/csv'
)

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "987d0796-0519-4fae-9f44-c365bf708ff5",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mstreamlit\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mst\u001b[39;00m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mpandas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mseaborn\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01msns\u001b[39;00m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# ========== CONFIGURAÇÃO ==========\n",
    "st.set_page_config(page_title=\"Dashboard ZettaLab - Pará\", layout=\"wide\")\n",
    "st.title(\"📊 Dashboard Interativo - Desmatamento x Socioeconomia (Pará)\")\n",
    "\n",
    "# ========== LEITURA DO CSV ==========\n",
    "@st.cache_data\n",
    "def carregar_dados():\n",
    "    df = pd.read_csv('dados/base_completa_merge.csv')\n",
    "    df['year'] = pd.to_numeric(df['year'], errors='coerce')\n",
    "    df['areakm'] = pd.to_numeric(df['areakm'], errors='coerce')\n",
    "    df['idhm_2010'] = pd.to_numeric(df['idhm_2010'], errors='coerce')\n",
    "    df['idhm_cat'] = df['idhm_cat'].astype(str)\n",
    "    return df\n",
    "\n",
    "df = carregar_dados()\n",
    "\n",
    "# ========== FILTROS ==========\n",
    "st.sidebar.header(\"🎛️ Filtros\")\n",
    "anos = st.sidebar.multiselect(\"Ano\", sorted(df['year'].unique()), default=sorted(df['year'].unique()))\n",
    "municipios = st.sidebar.multiselect(\"Município\", sorted(df['municipio'].unique()), default=[])\n",
    "categorias = st.sidebar.multiselect(\"Categoria de IDHM\", ['Baixo', 'Médio', 'Alto'], default=['Baixo', 'Médio', 'Alto'])\n",
    "\n",
    "# Aplicar filtros\n",
    "df_filtros = df[df['year'].isin(anos)]\n",
    "if municipios:\n",
    "    df_filtros = df_filtros[df_filtros['municipio'].isin(municipios)]\n",
    "if categorias:\n",
    "    df_filtros = df_filtros[df_filtros['idhm_cat'].isin(categorias)]\n",
    "\n",
    "# ========== MÉTRICAS ==========\n",
    "col1, col2, col3 = st.columns(3)\n",
    "col1.metric(\"🔍 Municípios Selecionados\", df_filtros['municipio'].nunique())\n",
    "col2.metric(\"🗓️ Intervalo de Anos\", f\"{min(anos)} - {max(anos)}\")\n",
    "col3.metric(\"🌳 Área Total Desmatada\", f\"{df_filtros['areakm'].sum():,.2f} km²\")\n",
    "\n",
    "# ========== GRÁFICOS ==========\n",
    "st.markdown(\"### 📈 Evolução do Desmatamento\")\n",
    "evolucao = df_filtros.groupby('year')['areakm'].sum().reset_index()\n",
    "fig1, ax1 = plt.subplots()\n",
    "sns.lineplot(data=evolucao, x='year', y='areakm', marker='o', ax=ax1)\n",
    "ax1.set_title(\"Evolução da Área Total Desmatada (km²)\")\n",
    "ax1.set_ylabel(\"Área Desmatada (km²)\")\n",
    "st.pyplot(fig1)\n",
    "\n",
    "st.markdown(\"### 🧠 Correlação: Indicadores vs Desmatamento\")\n",
    "variaveis = ['areakm', 'populacao_2022', 'pib_per_capita_2021', 'idhm_2010', 'desmatamento_per_capita']\n",
    "correlacao = df_filtros[variaveis].corr()\n",
    "fig2, ax2 = plt.subplots(figsize=(7, 5))\n",
    "sns.heatmap(correlacao, annot=True, cmap='coolwarm', ax=ax2)\n",
    "st.pyplot(fig2)\n",
    "\n",
    "st.markdown(\"### 📊 Área Desmatada por Categoria de IDHM\")\n",
    "df_barras = df_filtros.groupby('idhm_cat')['areakm'].sum().reset_index()\n",
    "fig3, ax3 = plt.subplots()\n",
    "sns.barplot(data=df_barras, x='idhm_cat', y='areakm', ax=ax3, palette='Set2')\n",
    "ax3.set_ylabel(\"Área Desmatada (km²)\")\n",
    "ax3.set_xlabel(\"Categoria de IDHM\")\n",
    "ax3.set_title(\"Desmatamento Total por Categoria de IDHM\")\n",
    "st.pyplot(fig3)\n",
    "\n",
    "# ========== TABELA ==========\n",
    "st.markdown(\"### 🗂️ Tabela com Dados Filtrados\")\n",
    "st.dataframe(df_filtros[['municipio', 'year', 'areakm', 'pib_per_capita_2021', 'idhm_2010', 'idhm_cat']])\n",
    "\n",
    "# ========== DOWNLOAD ==========\n",
    "st.download_button(\n",
    "    label=\"📥 Baixar CSV Filtrado\",\n",
    "    data=df_filtros.to_csv(index=False),\n",
    "    file_name='dados_filtrados.csv',\n",
    "    mime='text/csv'\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2fd28369-03b1-4894-b0d2-dde49931148f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

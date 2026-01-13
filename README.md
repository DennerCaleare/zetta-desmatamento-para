# 🌱 Análise de Desmatamento no Pará
## Projeto-Based Learning em Data Science

> **Projeto de aprendizado prático que integrou dados de desmatamento (INPE) com indicadores socioeconômicos (IBGE) para explorar relações entre ambiental e desenvolvimento no Pará. Dashboard interativo + Notebooks Jupyter + Relatório PDF.**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://zetta-desmatamento-para.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Learning Project](https://img.shields.io/badge/Type-Research%20%26%20Learning-blue.svg)](#)

## 🚀 Acesso Rápido

**Explore os dados:** https://zetta-desmatamento-para.streamlit.app/

**Desenvolvedor:** Denner Caleare | [GitHub](https://github.com/DennerCaleare) | [LinkedIn](https://linkedin.com/in/dennercaleare)

---

## 🎉 História Deste Projeto

Quando comecei a estudar **Data Science**, quis aplicar o aprendizado em algo real. Baixei bases de dados públicas do INPE (desmatamento) e IBGE (dados socioeconômicos) e construí uma solução completa de análise.

**O que aprendi:**
- 📚 Pandas, NumPy, Plotly para EDA
- 🎯 Streamlit para criar dashboards
- 🗺️ GeoPandas para dados geoespaciais
- 📊 Criação de relatórios profissionais (PDF + HTML)
- 📝 Jupyter Notebooks para documentação de análise

## ✨ Entregaveis

### 📱 Dashboard Interativo
- Filtros por período (2008-2024)
- Visualização por município
- Gráficos de tendências de desmatamento
- Correlação com IDHM
- Export de dados filtrados

### 📚 Notebooks Jupyter
- `analise_governanca_para.ipynb` - Análise exploratória completa
- `zetta_relatorio_desmatamento_para.ipynb` - Relatório final
- Visualizações, insights e recomendações

### 📁 Saídas
- 📈 Dashboard HTML interativo
- 📄 Relatório em PDF
- 📂 Datasets processados em CSV

## 🛠️ Stack Técnico

```python
Python 3.8+         # Linguagem principal
Pandas 2.0+        # Manipulação de dados
NumPy               # Cálculos numéricos
Matplotlib          # Visualização estática
Plotly              # Gráficos interativos
Streamlit           # Dashboard web
GeoPandas           # Dados geoespaciais
Jupyter             # Notebooks
```

## 📂 Estrutura do Projeto

```
zetta-desmatamento-para/
├── dados/                                  # Dados brutos INPE + IBGE
│   ├── dados_ibge_para.xlsx
│   └── dados_desmatamento_para.csv
├── saida/                                 # Dados processados
│   └── base_completa_merge.csv
├── analise_governanca_para.ipynb        # Notebook de análise
├── zetta_relatorio_desmatamento_para.ipynb # Notebook de relatório
├── app.py                               # Dashboard Streamlit
├── dashboard_relatorio.html             # Relatório HTML
├── relatorio_final.pdf                  # Relatório PDF
├── requirements.txt                    # Dependências
└── README.md                           # Este arquivo
```

## 🚀 Como Usar

### 1. Acessar o Dashboard Online
```
https://zetta-desmatamento-para.streamlit.app/
```

### 2. Rodar Localmente
```bash
git clone https://github.com/DennerCaleare/zetta-desmatamento-para.git
cd zetta-desmatamento-para
pip install -r requirements.txt
streamlit run app.py
```

### 3. Explorar os Notebooks
```bash
jupyter notebook
# Abra analise_governanca_para.ipynb ou zetta_relatorio_desmatamento_para.ipynb
```

## 📊 Dados Utilizados

| Fonte | Descrição | Período |
|-------|-------------|----------|
| **INPE** | Desmatamento na Amazônia | 2008-2024 |
| **IBGE** | Indicadores socioeconômicos | 2010-2024 |
| **Scope** | Estado do Pará | 144 municípios |

## 📊 Principais Insights

🔍**Questões Respondidas:**
- Como o desmatamento varia temporalmente?
- Existe correlação entre desmatamento e IDHM?
- Quais municípios têm maior taxa de desmatamento?
- Como visualizar tendências por região?

## 🎓 Desenvolvido por

**Denner Caleare**

- 👋 Iniciando em Data Science
- 📚 Apaixonado por dados e sustentabilidade
- 🌟 Autor do ZettaLab Learning Program

**Contato:**
- [GitHub](https://github.com/DennerCaleare)
- [LinkedIn](https://linkedin.com/in/dennercaleare)

## 🌐 Tema

América Latina | Sustentabilidade | Desmatamento | Data Science | Análise Ambiental

## 📝 Licença

Projeto acadêmico de aprendizado. Dados públicos INPE + IBGE.

---

**Desenvolvido com ❤️ em Lavras, MG | ZettaLab - UFLA**

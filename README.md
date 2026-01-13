# 🌱 Análise de Desmatamento e Governança de Dados no Pará

> Projeto de análise exploratória integrando dados de desmatamento (INPE) com indicadores socioeconômicos (IBGE) para o estado do Pará.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://zetta-desmatamento-para.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Project Status](https://img.shields.io/badge/status-analysis%20complete-green.svg)](#)

## 🚀 Acesso Rápido

👉 **[Abrir Dashboard Online](https://zetta-desmatamento-para.streamlit.app/)**

## 📊 Sobre o Projeto

Projeto desenvolvido para o processo seletivo do **ZettaLab** (trilha de Governança de Dados) que explora a relação entre o desmatamento na Amazônia brasileira (estado do Pará) e os indicadores socioeconômicos de seus municípios.

### ✨ Funcionalidades

- 📅 Integração de dados de múltiplas fontes (INPE e IBGE)
- 📊 Análise exploratória com Python (Pandas, NumPy, Plotly)
- 📱 Dashboard interativo com filtros dinâmicos
- 📈 Visualizações de correlacão e tendências
- 📑 Relatório final em PDF e HTML
- 📋 Notebooks Jupyter com análise completa

## 💳 Objetivos

- ✍️ Integrar dados públicos de desmatamento (INPE) com dados socioeconômicos (IBGE)
- 📈 Realizar análise exploratória e gerar visualizações com Python
- 📱 Apresentar um dashboard interativo com filtros por ano, município e IDHM
- 📚 Produzir relatório final com insights e recomendações

## 🛠️ Tecnologias

```python
Python 3.8+         # Linguagem principal
Pandas              # Manipulação de dados
NumPy               # Cálculos numéricos
Matplotlib          # Visualização estática
Plotly              # Gráficos interativos
Streamlit           # Dashboard web
Jupyter             # Notebooks interativos
```

## 📂 Estrutura do Projeto

```
zetta-desmatamento-para/
├── dados/                                  # Dados brutos originais
│   ├── dados_ibge_para.xlsx              # Dados IBGE
│   └── dados_desmatamento_para.csv        # Dados INPE
├── saida/                                 # Dados tratados e processados
│   └── base_completa_merge.csv             # Dataset unificado
├── analise_governanca_para.ipynb        # Notebook da análise
├── zetta_relatorio_desmatamento_para.ipynb # Notebook do relatório
├── app.py                               # Dashboard Streamlit
├── dashboard_relatorio.html             # Relatório em HTML
├── relatorio_final.pdf                  # Relatório final em PDF
├── requirements.txt                    # Dependências
└── README.md                           # Este arquivo
```

## 📦 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/DennerCaleare/zetta-desmatamento-para.git
cd zetta-desmatamento-para
```

### 2. Criar ambiente virtual (opcional)

```bash
# Windows
python -m venv zetta-env
zetta-env\Scripts\activate

# macOS/Linux
python3 -m venv zetta-env
source zetta-env/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar o dashboard

```bash
streamlit run app.py
```

O dashboard abrirá automaticamente em [http://localhost:8501](http://localhost:8501/)

## 📋 Visualizar a Análise

Para ver toda a análise com gráficos e explicações:

```bash
jupyter notebook
```

Depois, abra `analise_governanca_para.ipynb`

## 📊 Dados e Fontes

| Fonte | Descrição | Link |
|-------|-------------|------|
| INPE | Desmatamento na Amazônia | [TerraBrasilis](http://terrabrasilis.dpi.inpe.br/) |
| IBGE | Indicadores socioeconômicos | [IBGE Cidades](https://www.ibge.gov.br/) |

## 📋 Principais Insights

- A análise explora correlações entre desmatamento e IDHM
- Dados de 2008-2024 para acompanhamento de tendências
- Métricas por município do estado do Pará
- Visualizações interativas para exploração de dados

## 📁 Saídas do Projeto

- 📈 Dashboard interativo (Streamlit)
- 📑 Relatório em PDF
- 📚 Notebooks Jupyter com análises
- 📊 Visualizações interativas (Plotly)
- 📂 Datasets processados em CSV

## 💡 Observações

- O ano de **2007** foi desmarcado por padrão (dados acumulados - distorções)
- Os dados do IBGE são estáticos (referência 2010-2024)
- O projeto funciona em qualquer SO com Python instalado

## 👨‍💻 Desenvolvido por

**Denner Caleare** | [GitHub](https://github.com/DennerCaleare) | [LinkedIn](https://linkedin.com/in/dennercaleare)

Como parte do processo seletivo para o **ZettaLab** - Programa de Governança de Dados

## 📝 Licença

Este projeto é de cáráter acadêmico e pode ser utilizado como referência para estudos e análises similares.

---

**Desenvolvido com ❤️ em Lavras, MG**

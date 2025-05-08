# 🌱 Projeto ZettaLab - Análise de Desmatamento e Indicadores Socioeconômicos no Pará

Este projeto foi desenvolvido como parte do processo seletivo para o ZettaLab (trilha de Governança de Dados) e tem como objetivo explorar a relação entre o desmatamento na Amazônia (Pará) e indicadores socioeconômicos dos municípios.

---

## 🧠 Objetivo

- Integrar dados públicos de desmatamento (INPE) com dados socioeconômicos (IBGE)
- Realizar análise exploratória e gerar visualizações com Python
- Apresentar um dashboard interativo com filtros por ano, município e IDHM

---

## 🗂️ Estrutura do Projeto

```
zetta-desmatamento-para/
├── dados/                          # Dados brutos
│   ├── dados_ibge_para.xlsx
│   └── dados_desmatamento_para.csv
├── saida/                          # Base tratada e pronta para análise
│   └── base_completa_merge.csv
├── app.py                          # Dashboard Streamlit
├── analise_governanca_para.ipynb  # Notebook com a análise completa
├── relatorio_final.pdf             # Relatório descritivo final
├── README.md                       # Este arquivo
└── requirements.txt                # Dependências do projeto
```

---

## ⚙️ Como executar o projeto

### 1. Instalar o Python (>= 3.8)
- [Python para Windows/macOS/Linux](https://www.python.org/downloads/)

### 2. (Opcional) Criar um ambiente virtual

```bash
# Windows
python -m venv zetta-env
zetta-env\Scripts\activate

# macOS/Linux
python3 -m venv zetta-env
source zetta-env/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar o dashboard

```bash
streamlit run app.py
```

> Isso abrirá automaticamente o dashboard no navegador: http://localhost:8501

---

## 📊 Visualizar a análise no Jupyter

Se preferir ver toda a análise com gráficos e explicações passo a passo:

```bash
# Rodar Jupyter
jupyter notebook
```

Depois, abra o arquivo `analise_governanca_para.ipynb`

---

## 📥 Fontes de Dados

- [INPE - PRODES/TerraBrasilis](http://terrabrasilis.dpi.inpe.br/)
- [IBGE - Cidades e Indicadores](https://www.ibge.gov.br/)

---

## 📌 Observações

- O ano de **2007** foi desmarcado por padrão por conter dados acumulados (distorções).
- Os dados do IBGE são estáticos (referência 2010–2024).
- O projeto pode ser executado em qualquer sistema operacional com Python instalado.

---

## 🤝 Contato

Este projeto foi desenvolvido por Denner Gabriel Ramos Caleare para o ZettaLab.

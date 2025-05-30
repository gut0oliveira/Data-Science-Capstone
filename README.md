# Data-Science-Capstone

## Previsão de Arquivos Maliciosos usando Machine Learning

Este projeto é uma aplicação desenvolvida com **Streamlit** para realizar previsões de ataques cibernéticos com base em modelos de Machine Learning.

---

## 🚀 Funcionalidades

- Upload de arquivos CSV com dados de tráfego de rede.
- Detecção automática do tipo de classificação: Binária ou Multiclasse.
- Escolha de modelos de ML previamente treinados.
- Visualização dos resultados com gráficos.
- Interface interativa.

---

## 🧩 Requisitos

Certifique-se de ter instalado:

- Python 3.8+
- pip
- [JupyterLab](https://jupyter.org/install) (opcional)
- Os seguintes pacotes Python:
```bash
pip install streamlit pandas numpy joblib matplotlib seaborn scikit-learn xgboost streamlit-lottie os datetime requests
```

---

## 📁 Estrutura de Diretórios

```
Data-Science-Capstone/
│
├── notebooks/
│   └── 1-data-preprocessing.ipynb         # Coleta e Preparação dos Dados
│   └── 2-exploratory-data-analysis.ipynb  # Análise Exploratória dos Dados
│   └── 3-feature-engineering              # Engenharia de Features
│   └── 4-ml-models                        # Modelagem ML
│   └── modelos.pkl                        # Modelos treinados
│
├── scripts/
│   ├── app.py                             # Aplicação Streamlit
│   └── visuals.py                         # Funções visuais do app
│
├── requirements.txt                       # Pacotes necessários
├── README.md                              # Este arquivo
```

---

## ▶️ Como Executar a Aplicação

Você pode rodar a aplicação de duas maneiras:

### 1. Usando o terminal do JupyterLab

1. Abra o **JupyterLab**
2. Vá em: `File > New > Terminal`
3. No terminal, navegue até a pasta do script:

```bash
cd caminho/para/a/pasta/scripts
streamlit run app.py
```

4. Copie o link exibido no terminal (geralmente http://localhost:8501) e abra no navegador.

### 2. Usando o terminal comum do sistema

1. Abra o terminal ou prompt de comando
2. Navegue até a pasta do projeto:

```bash
cd caminho/para/a/pasta/scripts
```

3. Rode o Streamlit:

```bash
streamlit run app.py
```

---

## 📌 Observações

- O arquivo `modelos.pkl` precisa estar dentro da pasta `Notebooks/` para o app funcionar corretamente.
- Apenas arquivos `.csv` são aceitos.

---

## 👨‍💻 Desenvolvedor

- **Nome**: Augusto Oliveira  
- **RA**: 22153474



# 🛠️ Instruções de Instalação e Execução

## ✅ Clonando o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio/scripts
```

## 📦 Instalando Dependências

Recomenda-se criar um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
```

## ⚠️ Atenção: Download Manual Necessário

O arquivo `modelos.pkl` (com os modelos treinados) não pode ser enviado ao GitHub devido ao limite de 25MB.

➡️ Baixe o arquivo aqui: [LINK_DO_GOOGLE_DRIVE]

Depois de baixar, coloque o arquivo dentro da pasta `notebooks/` do projeto.

## ▶️ Rodando a Aplicação

```bash
streamlit run app.py
```

Abra o link exibido no terminal (geralmente http://localhost:8501) no navegador.

---

✅ Pronto! Agora você pode fazer upload de um arquivo CSV para testar os modelos de Machine Learning.


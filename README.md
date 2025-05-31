<h1 align="center">Data Science Capstone</h1>

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
- Os seguintes pacotes Python:
```bash
pip install streamlit pandas numpy joblib matplotlib seaborn scikit-learn xgboost streamlit-lottie os datetime requests
```

---

## 📁 Estrutura do Projeto

```
Data-Science-Capstone/
├── amostras/
│   └── amostra_1.csv                      # Amostra de Teste 1
│   └── amostra_2.csv                      # Amostra de Teste 2
│   └── amostra_3.csv                      # Amostra de Teste 3
│   └── amostra_4.csv                      # Amostra de Teste 4
│   └── amostra_5.csv                      # Amostra de Teste 5
│   └── amostra_6.csv                      # Amostra de Teste 6
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
├── README.md                              # Este arquivo
├── requirements.txt                       # Pacotes necessários
```

---

## 🛠️ Como Instalar e Executar

### 1. Clone o repositório

```bash
git clone https://github.com/gut0oliveira/data-science-capstone.git
cd data-science-capstone
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Baixe o arquivo de modelos (.pkl)
⚠️ Atenção: O arquivo `modelos.pkl` não pode ser enviado ao GitHub devido ao limite de 25MB.

➡️ Baixe o arquivo aqui: [Drive](https://drive.google.com/drive/folders/1jXfISmh7TDFaJjiEeeAgV-KyDmYKl2jx?usp=drive_link)

Depois de baixar, coloque o arquivo dentro da pasta `/notebooks` do projeto.

### 4. Navegue até a pasta /scripts do projeto:

- Clique com o botão direito na pasta `/scripts` e selecione `Copy Path`
- Abra o terminal e cole digite o código abaixo:
```bash
cd caminho/copiado/para/a/pasta/scripts
```

### 5. Rode o Streamlit:

Após acessar a pasta `/scripts`, coloque esse código abaixo no terminal:
```bash
streamlit run app.py
```
Abra o link gerado no navegador (http://localhost:...) para interagir com a aplicação.

---

## 📌 Observações

- O arquivo `modelos.pkl` precisa estar dentro da pasta `/notebooks` para o app funcionar corretamente.
- Apenas arquivos `.csv` são aceitos.

✅ Pronto! Agora você pode fazer upload de um arquivo CSV para testar os modelos de Machine Learning.

---
## 👨‍💻 Desenvolvedor

- **Nome**: Augusto Oliveira Silva
- **Curso**: Ciência da Computação
- **RA**: 22153474

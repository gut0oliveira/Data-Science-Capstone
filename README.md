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

## 📁 Estrutura do Projeto

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

## 🛠️ Como Instalar e Executar

### 1. Clone o repositório

```bash
git clone https://github.com/augusto-oliveira/data-science-capstone.git
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

### 4. Navegue até a pasta do projeto:

- Clique com o botão direito na pastas `/Script` e selecione `Copy Path`
- Abra o terminal e cole digite o código abaixo:

```bash
cd caminho/copiado/para/a/pasta/scripts
```

### 5. Rode o Streamlit:

Após acessar a pasta `/Scripts`, coloque esse código abaixo no terminal:
```bash
streamlit run app.py
```

Abra o link gerado no navegador (http://localhost:...) para interagir com a aplicação.

---

## 📌 Observações

- O arquivo `modelos.pkl` precisa estar dentro da pasta `/Notebooks` para o app funcionar corretamente.
- Apenas arquivos `.csv` são aceitos.

---

## 👨‍💻 Desenvolvedor

- **Nome**: Augusto Oliveira Silva
- **Curso**: Ciência da Computação
- **RA**: 22153474

✅ Pronto! Agora você pode fazer upload de um arquivo CSV para testar os modelos de Machine Learning.

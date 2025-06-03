<h1 align="center">Data Science Capstone</h1>
<h2 align="center">Previsão de Arquivos Maliciosos usando Machine Learning</h2>

Este projeto é uma aplicação **Streamlit** feita para realizar previsões de ataques cibernéticos com base em modelos de Machine Learning.

## 🚀 Funcionalidades

- Upload de arquivos CSV com dados de tráfego de rede.
- Detecção automática do tipo de classificação: Binária ou Multiclasse.
- Escolha de modelos de ML previamente treinados.
- Visualização dos resultados com gráficos.
- Interface interativa.

## 🧩 Requisitos

Certifique-se de ter instalado:

- Ter instalado na máquina o Python 3.8+;
- Ter instalado na máquina o Pip (instalação normalmente ocorre junto com o python);
- Ter o Git/Github instalado na máquina;
- Ter feito o download do arquivo modelos.pkl e colocado o mesmo na pasta /notebooks;
- Os dados de teste devem estar no formato .csv.
- Os seguintes pacotes Python:
```bash
pip install streamlit pandas numpy joblib matplotlib seaborn scikit-learn xgboost streamlit-lottie os datetime requests
```

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

## 🛠️ Como Instalar e Executar

### 1. Clone o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/gut0oliveira/data-science-capstone.git
cd data-science-capstone
```


### 2. Instale as dependências
Depois de executar os códigos acima, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### 3. Baixe o arquivo de (`modelos .pkl`)

```bash
⚠️ATENÇÃO⚠️
O arquivo modelos.pkl tem aproximadamente 111MB.
O GitHub não permite arquivos desse tamanho, então ele está hospedado externamente.
```
- Clique aqui para baixar o arquivo: <a href="https://drive.google.com/uc?export=download&id=1wWmQbKhzWJxsIQc_MfjYCEfkIgvdvHi2" target="_blank">modelos.pkl</a>

- Após o download, coloque o arquivo dentro da pasta `/notebooks` do projeto.

### 4. Acesse a pasta /scripts do projeto:

No terminal, navegue até a pasta onde está o arquivo `app.py`. Exemplo:

```bash
cd notebooks/scripts
```
Ou copie o caminho absoluto da pasta `/scripts` e cole no terminal assim:
```bash
cd "C:\Users\SeuUsuario\Documents\GitHub\data-science-capstone\notebooks\scripts"
```

### 5. Rode o Streamlit:

Execute o seguinte comando:
```bash
streamlit run app.py
```
O navegador será aberto automaticamente em `http://localhost:8501`, onde você poderá interagir com a aplicação.

## 📌 Observações

- O arquivo `modelos.pkl` precisa estar dentro da pasta `/notebooks` para o app funcionar corretamente.
- Apenas arquivos `.csv` são aceitos.

## Aplicação

Caso voc~e tenha feito todos os passos corretamente, você verá uma tela como essa abaixo:

![image](https://github.com/user-attachments/assets/55744db9-be76-4eef-ba8b-abe72ded8d08)


✅ Pronto! Agora você pode fazer upload de um arquivo CSV para testar os modelos de Machine Learning.

---
## 👨‍💻 Desenvolvedor

- **Nome**: Augusto Oliveira Silva
- **Curso**: Ciência da Computação
- **RA**: 22153474

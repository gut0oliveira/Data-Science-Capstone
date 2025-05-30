# Data-Science-Capstone

# 📊 Previsão de Arquivos Maliciosos usando Machine Learning

Este projeto é uma aplicação desenvolvida com **Streamlit** para realizar previsões de ataques cibernéticos com base em modelos de Machine Learning treinados com dados de tráfego de rede de 2017.

---

## 🚀 Funcionalidades

- Upload de arquivos CSV com dados de tráfego de rede
- Detecção automática do tipo de classificação: binária ou multiclasse
- Escolha de modelos de ML previamente treinados
- Visualização dos resultados com gráficos de barras e pizza (binário) ou mapa de calor (multiclasse)
- Interface interativa em modo dark

---

## 🧩 Requisitos

Certifique-se de ter instalado:

- Python 3.8+
- pip
- [JupyterLab](https://jupyter.org/install) (opcional)
- Os seguintes pacotes Python:

```bash
pip install streamlit pandas joblib matplotlib seaborn scikit-learn xgboost streamlit-lottie
```

---

## 📁 Estrutura de Diretórios

```
Capstone-Data-Science-Project/
│
├── notebooks/
│   └── modelos.pkl               # Modelos treinados salvos com joblib
│
├── scripts/
│   ├── app.py                    # Aplicação Streamlit principal
│   └── visuals.py                # Funções visuais para o app
│
├── README.md                     # Este arquivo
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

- O arquivo `modelos.pkl` precisa estar dentro da pasta `notebooks/` para o app funcionar corretamente.
- O aplicativo detecta automaticamente o tipo de modelo (binário ou multiclasse) com base na coluna `Tipos de Ataques`.
- Apenas arquivos `.csv` são aceitos.

---

## 👨‍💻 Desenvolvedor

- **Nome**: Augusto Oliveira  
- **RA**: 22153474

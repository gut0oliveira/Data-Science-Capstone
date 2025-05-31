import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os
from visuals import aplicar_estilo, titulo, upload_arquivo, rodape, sidebar_info

aplicar_estilo()

titulo("Previsão de Arquivos Maliciosos usando ML")

# Carrega arquivo modelos.pkl
@st.cache_resource
def carregar_modelos():
    caminho = "../notebooks/modelos.pkl"
    if not os.path.exists(caminho):
        st.warning("Arquivo de modelo não encontrado. Baixe e coloque o 'modelos.pkl' na pasta /Notebooks.")
    return joblib.load(caminho)

dados_modelos = carregar_modelos()

# Upload do arquivo CSV
arquivo = upload_arquivo()

if arquivo is not None:
    try:
        df = pd.read_csv(arquivo)
        st.success("Arquivo carregado com sucesso! ✅")
        st.dataframe(df.head(5))

        if 'Tipos de Ataques' not in df.columns:
            st.warning("Atenção: a coluna 'Tipos de Ataques' não foi encontrada.")
            tipo = st.radio("Qual modelo você deseja usar?", ("Binário", "Multiclasse"))
        else:
            n_classes = df['Tipos de Ataques'].nunique(dropna=True)
            tipo = "Multiclasse" if n_classes > 2 else "Binário"
            st.warning(f"Tipo de classificação definida como: **{tipo}**")
            df = df.drop(columns=["Tipos de Ataques"])

        modelos_binarios = {
            "Regressão Logística": dados_modelos["modelo_reg_2017"],
            "Support Vector Machine": dados_modelos["modelo_svm_2017"],
        }
        modelos_multiclasse = {
            "Random Forest": dados_modelos["modelo_rf_2017"],
            "K-Nearest Neighbours": dados_modelos["modelo_knn_2017"],
            "XGBoost": dados_modelos["modelo_xgb_2017"],
        }

        # Caixa de seleção
        st.subheader("Escolha o Modelo de Machine Learning")
        if tipo == "Binário":
            modelo_nome = st.selectbox("Selecione o modelo binário:", list(modelos_binarios.keys()))
            modelo = modelos_binarios[modelo_nome]
        else:
            modelo_nome = st.selectbox("Selecione o modelo multiclasse:", list(modelos_multiclasse.keys()))
            modelo = modelos_multiclasse[modelo_nome]

        # Previsão
        if st.button("🔍 Realizar Previsão"):
            with st.spinner("Gerando previsões..."):
                previsoes = modelo.predict(df)
                probabilidades = modelo.predict_proba(df)

                st.success("Previsões concluídas com sucesso! ✅")
                if tipo == "Binário":
                    st.subheader("Resultados - Classificação Binária")

                    df_resultados = pd.DataFrame({
                        "Benigno": probabilidades[:, 0],
                        "Malicioso": probabilidades[:, 1],
                        "Previsão": previsoes
                    })

                    st.dataframe(df_resultados)

                    contagem = df_resultados["Previsão"].value_counts().sort_index()

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("Distribuição das Previsões")
                        fig_bar, ax_bar = plt.subplots(figsize=(4, 3))
                        
                        bars = ax_bar.bar(contagem.index.astype(str), contagem.values, color=['darkgreen', 'darkred'])
                        ax_bar.set_xlabel("Classes")
                        ax_bar.set_ylabel("Probabilidade")
                        ax_bar.set_xticks([0, 1])
                        ax_bar.set_xticklabels(["Benigno", "Malicioso"])
                        ax_bar.grid(axis='y', linestyle='--', alpha=0.4)

                        y_max = contagem.values.max()
                        for bar in bars:
                            yval = bar.get_height()
                            ax_bar.text(
                                bar.get_x() + bar.get_width() / 2.0,
                                yval + (y_max * 0.05), 
                                f'{int(yval)}',
                                ha='center',
                                va='bottom'
                            )
                        ax_bar.set_ylim(0, y_max + y_max * 0.15)
                        st.pyplot(fig_bar)

                        with col2:
                            st.subheader("Proporção das Previsões")
                            fig_pie, ax_pie = plt.subplots(figsize=(4, 3))
                            
                            classes_encontradas = contagem.index.tolist()
                            nomes_classes = {0: "Benigno", 1: "Malicioso"}
                            cores_classes = {0: "darkgreen", 1: "darkred"}

                            labels = [nomes_classes[i] for i in classes_encontradas]
                            cores = [cores_classes[i] for i in classes_encontradas]

                            ax_pie.pie(
                                contagem.values,
                                labels=labels,
                                autopct='%1.1f%%',
                                startangle=90,
                                colors=cores,
                                textprops={'color': 'white'},
                            )
                            ax_pie.axis('equal')
                            st.pyplot(fig_pie)

                else:
                    st.subheader("Resultados - Classificação Multiclasse")
                    labels = modelo.classes_
                    df_resultados = pd.DataFrame(probabilidades, columns=[f"{label}" for label in labels])
                    df_resultados["Previsão"] = previsoes
                    st.dataframe(df_resultados)

                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("Distribuição das Previsões")
                        contagem_mc = df_resultados["Previsão"].value_counts().sort_index()
                        fig1, ax1 = plt.subplots(figsize=(6, 4))

                        bars = ax1.bar(contagem_mc.index.astype(str), contagem_mc.values, color='darkred')
                        ax1.set_xlabel("Classes")
                        ax1.set_ylabel("Frequência")
                        ax1.grid(axis='y', linestyle='--', alpha=0.4)

                        y_max_mc = contagem_mc.values.max()
                        y_pad = max(y_max_mc * 0.15, 50)
                        for bar in bars:
                            yval = bar.get_height()
                            ax1.text(
                                bar.get_x() + bar.get_width() / 2.0,
                                yval + (y_pad * 0.2),
                                f'{int(yval)}',
                                ha='center',
                                va='bottom'
                            )

                        ax1.set_ylim(0, y_max_mc + y_pad)
                        fig1.tight_layout(pad=0.1, w_pad=1, h_pad=0.5)
                        st.pyplot(fig1)

                    with col2:
                        st.subheader("Mapa de Calor de Probabilidades")
                        n_amostras = min(20, len(df_resultados))
                        fig2, ax2 = plt.subplots(figsize=(6, 4))
                        sns.heatmap(df_resultados.iloc[:n_amostras, :-1], annot=True, cmap="OrRd", fmt=".2f", ax=ax2)
                        ax2.set_xlabel("Classes")
                        ax2.set_ylabel("Amostras")
                        fig2.tight_layout()
                        st.pyplot(fig2)

    except Exception as error:
        st.error(f"Erro ao processar o arquivo: {error}")

rodape("Augusto Oliveira", "22153474")
sidebar_info()

import pandas as pd
import joblib
import os

modelos = joblib.load(r"C:\Users\augus\Capstone-Data-Science-Project\notebooks\modelos.pkl")

path_arquivos = r"C:\Users\augus\Capstone-Data-Science-Project\arquivos"

index = 1

# BINÁRIO

X_bin = modelos.get("X_2017_bin")
y_bin = modelos.get("y_2017_bin")
cols_bin = modelos.get("colunas_2017_bin")

df_bin = pd.DataFrame(X_bin, columns=cols_bin[:-1])
df_bin["Tipos de Ataques"] = y_bin

for i in range(1, 6):
    amostra_bin = df_bin.sample(100, random_state=100 + i)
    amostra_bin.to_csv(os.path.join(path_arquivos, f"amostra_{index}.csv"), index=False)
    index += 1

# MULTICLASSE

X_multi = modelos.get("X_2017_multi")
y_multi = modelos.get("y_2017_multi")
cols_multi = modelos.get("colunas_2017_multi")

df_multi = pd.DataFrame(X_multi, columns=cols_multi[:-1])
df_multi["Tipos de Ataques"] = y_multi

for i in range(1, 6):
    amostra_multi = df_multi.sample(100, random_state=200 + i)
    amostra_multi.to_csv(os.path.join(path_arquivos, f"amostra_{index}.csv"), index=False)
    index += 1

print("Amostras geradas com sucesso!")

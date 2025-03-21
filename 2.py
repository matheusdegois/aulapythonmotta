import pandas as pd

df = pd.read_csv("dados_tratados.csv")

media_salarial = df["Salário"].mean()
pessoas_salario_maior = df[df["Salário"] > media_salarial].shape[0]
print(f"\nNúmero de pessoas com salário maior que a média geral: {pessoas_salario_maior}")




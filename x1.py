import pandas as pd

df = pd.read_csv("dados.csv")

print("Dados originais:")
print(df)

print("\nVerificando valores ausentes:")
print(df.isnull().sum())

df["Salário"] = df["Salário"].fillna(df["Salário"].mean())

df["Salário"] = pd.to_numeric(df["Salário"])

print("\nEstatísticas da tabela:")
print(df.describe())

print("\nPessoas com idade maior que 25 anos:")
print(df[df["Idade"] > 25])

media_salarial = df["Salário"].mean()
print(f"\nMédia salarial: R$ {media_salarial:.2f}")

quantidade_sp = df[df["Cidade"] == "São Paulo"].shape[0]
print(f"\nQuantidade de pessoas de São Paulo: {quantidade_sp}")

df_ordenado = df.sort_values(by="Salário", ascending=False)
print("\nTabela ordenada por salário:")
print(df_ordenado)

def classificar_salario(valor):
    if valor <= 3500:
        return "Baixo"
    elif 3500 < valor <= 5000:
        return "Médio"
    else:
        return "Alto"

df["Classificação"] = df["Salário"].apply(classificar_salario)

print("\nTabela com classificação salarial:")
print(df)

df.to_csv("dados_tratados.csv", index=False)
print("\nDados tratados salvos com sucesso!")



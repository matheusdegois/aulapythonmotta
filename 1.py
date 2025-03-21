import pandas as pd

df = pd.read_csv("dados.csv")

media_idade = df["Idade"].mean()
print(f"\nMédia da idade: {media_idade:.0f} anos.")


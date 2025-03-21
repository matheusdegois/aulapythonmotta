import pandas as pd

df = pd.read_csv("dados.csv")

pessoa_mais_jovem = df.loc[df["Idade"].idxmin()]
print("\nPessoa mais jovem:")
print(pessoa_mais_jovem)
import pandas as pd
import numpy as np

Test_1 = np.array([1, 2, 3])
Test_2 = np.array([[10, 20, 30], [40, 50, 60]])
print(f'Caso1:\n{Test_1}')
print(f'Caso2:\n{Test_2}')

# Operações
print("--" * 20)
print(Test_1 + 10)
print("--" * 20)
print(Test_2 * 3)
print("--" * 20)
print(Test_1 + Test_2) #Broadcasting
print(Test_2.sum()) # Soma de todos os elementos de B

# Pandas
# Dataframe vazio
df = pd.DataFrame()

# Adição de colunas
df["Bandas"] = ["RHCP", "Metallica", "Nirvana"]
df["Gêneros"] = ["Rock", "Metal", "Grunge"]
df["Ouvintes (em milhões)"] = [9.9, 10.5, 6.9]
print(df)

#Salvar em csv
df.to_csv("BandasExemplos.csv", index=False, encoding="utf-8")
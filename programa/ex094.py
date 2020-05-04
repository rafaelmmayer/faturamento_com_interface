import pandas as pd

df = pd.read_excel('FATURAMENTO_vs2.xlsx')
cell = df.at[2, 'Preço']
print(cell)
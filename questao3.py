# Questão 3
# Dado o arquivo invoices.csv escreva um serviço que computa a média de faturamento de cada conta
# (account) nos últimos três e seis meses retroativos à Jan/2020.
# Quando não há dados suficientes na janela de 3 ou 6 meses o serviço registra a entrada como NaN (null).
# A saída esperada é a seguinte:

import pandas as pd

df_csv = pd.read_csv('invoices.csv')
df_final = pd.DataFrame(columns=['customer', 'account', 'avg_invoices_last_3_months', 'avg_invoices_last_6_months'])

contas = df_csv.account.unique()

index = 0
for conta in contas:
    df_temp = df_csv[df_csv['account'] == conta]
    ordenate = df_temp.sort_values(['account', 'month'], ascending=[True, False])

    valor3mes = 'NaN'
    if len(ordenate['invoice'].head(3)) == 3:
        valor3mes = "{:.2f}".format(ordenate['invoice'].head(3).sum() / 3)

    valor6mes = 'NaN'
    if len(ordenate['invoice'].head(6)) == 6:
        valor6mes = "{:.2f}".format(ordenate['invoice'].head(6).sum() / 6)

    df_final.loc[index] = [ordenate['customer'].unique(),
                           conta,
                           valor3mes,
                           valor6mes]
    index += 1

print(df_final)


# Questão 2
# Suponha que você está explorando dados de cobrança de chatbots de Jan/2020 e
# tem em mãos dois conjuntos de dados pré-processados.
# O primeiro armazena os clientes e respectivos chatbots utilizados naquele mês.

import pandas as pd
import numpy as np

clientes = {'customer_id': [7494212, 7494212, 1475185, 6946725, 6946725],
            'chatbot_id': [1000, 2000, 3000, 4000, 5000],
            'chatbot_type':['Pesquisa de satisfação', 'Confirmação de agendamento',
                            'Negociação de dívida', 'Segunda via de fatura',
                            'Pesquisa de satisfação']}

cobranca = {'cost': [200.0, 100.0, 1000.0, 50.0, 400.0, 200.0, 1000],
            'chatbot_id': [1000, 2000, 3000, 4000, 5000, 5000, 3000]}

## cria data frames
dfclie = pd.DataFrame(data=clientes)
dfcob = pd.DataFrame(data=cobranca)

## concatena os dataframes realizando sum por chatbot_id
concat = pd.concat([dfclie, dfcob])
group = concat.groupby(['chatbot_id'], as_index=False)
sum = group.agg(np.sum)
result = sum[['customer_id', 'chatbot_id', 'cost']]

clientes = result[result['cost'] > 500]

print(clientes)


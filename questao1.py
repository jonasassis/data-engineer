#### 	Questão 1

# Um plataforma de comunicação registra eventos de execuções de chatbots.
# Escreva um serviço que computa quantos clientes executaram entre 1000 e 2000 chatbots.

import pandas as pd

d = {'customer_id': [7494212, 7494212, 1475185, 6946725, 6946725, 6946725],
     'chatbot_id': [1000, 2000, 3000, 1400, 5000, 6000],
     'event_date_time':[1535308430, 1535308433, 1535308444, 1535308475, 1535308476, 1535308477]}

df = pd.DataFrame(data=d)

df1000 = df[df['chatbot_id'] >= 1000]
df2000 = df[df['chatbot_id'] <= 2000]

print(len(df2000))
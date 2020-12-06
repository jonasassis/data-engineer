# 	Questão 4

# Uma plataforma de comunicação fornece fluxos de conversação (chatbots)
# entre outras funcionalidades. O data lake desta plataforma armazena
# valores informados pelos usuários em um formato semiestruturado (JSON)
# particionado por hora:
import pandas as pd
import json

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

dfhour13 = pd.read_json('hour=13.json')
dfhour14 = pd.read_json('hour=14.json')
concat = pd.concat([dfhour13, dfhour14])
group = concat.groupby(['customer', 'flow', 'session'])

for key, item in group:

    df_temp = group.get_group(key)
    columns = list(df_temp.columns)
    count = 0
    listContent = []
    listResult = []
    columns_fix = ['customer', 'flow', 'session', 'first_answer_dt', 'last_answer_dt']

    for index, row in df_temp.iterrows():

        # first aswers
        if count == 0:
            listResult.append(row["customer"])
            listResult.append(row["flow"])
            listResult.append(row["session"])
            listResult.append(str(row["timestamp"]))

        # last datetime
        if count == len(df_temp)-1:
            listResult.append(str(row["timestamp"]))

        count += 1
        jsonDumps = json.dumps(row["content"])
        jsonContent = json.loads(jsonDumps)
        listContent.append(jsonContent)

        pdContent = pd.DataFrame(listContent)
        dicionario = dict()

        for x in range(0, len(pdContent.index)):
            for y in range(0, len(pdContent.columns)):
                if not pd.isnull(pdContent.iat[x, y]):
                    dicionario[y] = pdContent.iat[x, y]

    columns_fix.extend(pdContent.columns)

    for value in range(0,len(dicionario)):
        listResult.append(dicionario[value])

    dicFinal = dict()
    for x in range(0, len(columns_fix)):
        dicFinal[columns_fix[x]] =  str(listResult[x])

    pdFinal = pd.DataFrame([dicFinal])

    print(pdFinal)
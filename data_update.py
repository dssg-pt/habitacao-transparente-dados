import pymongo
import pandas as pd
import datetime
import os 


# Get MongoDB credentials from environment variables
mongo_user = os.getenv('MONGO_USER')
mongo_pass = os.getenv('MONGO_PASS')
mongo_server = os.getenv('MONGO_SERVER')

print("mongo_user: ", mongo_user)

# load data
client = pymongo.MongoClient(f"mongodb+srv://{mongo_user}:{mongo_pass}@{mongo_server}/")
database_names = client.list_database_names()
db = client["habitacao-transparente"]
collection = db['user-data']
cursor = collection.find()
documents = list(cursor)
df = pd.DataFrame(documents)

# clean data
df['ano_nascimento_interval'] = pd.cut(df['ano-nascimento'], bins=range(1900, datetime.datetime.now().year + 5, 5), right=False)
df['nacionalidade_pt'] = df['nacionalidade'].apply(lambda x: 'portuguesa' if x == 'portugal' else 'nao-portuguesa')

colsToKeep = ['situacao-habitacional', 'distrito', 'concelho',
       'area-util', 'tipo-casa', 'tipologia', 
       #'ano_nascimento_interval','nacionalidade_pt', 
       'rendimento-anual', 'num-pessoas-nao-dependentes',
       'num-pessoas-dependentes', 'situacao-profissional', 'educacao',
       'satisfacao', 'percentagem-renda-paga',
       'valor-mensal-renda', 'ano-inicio-arrendamento',
       'rendimento-arrendamento', 'estrategia-arrendamento',
       'insatisfacao-motivos', 'valor-compra', 'ano-compra',
       'estado-conservacao', 'estrategia-compra',
       'rendimento-liquido-anual-individual-na-compra',
       'rendimento-liquido-anual-conjunto-na-compra', 'ano-heranca-aquisicao',
       'rendimento-liquido-anual-individual-na-aquisicao',
       'rendimento-heranca-conjunto', 'estado-conservacao-heranca']
#df[colsToKeep]

df.rename(columns={'ano_nascimento_interval': 'ano-nascimento'}, inplace=True)
df.rename(columns={'nacionalidade_pt': 'nacionalidade'}, inplace=True)
df['nacionalidade'].replace('_', '-', regex=True, inplace=True)

# save data
df[colsToKeep].to_csv('dados_new.csv')

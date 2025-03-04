from sqlalchemy import create_engine, text
import pandas as pd

user = 'root'
password = '1234'
host = '127.0.0.1'
port = 3306
database = 'online_movie_rating'

connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'

#connect to database
engine = create_engine(connection_string)

def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    return sql_script

sql_script = read_sql_file('test.sql')

# with engine.connect() as connection:
#     for statement in sql_script.split(';'):
#         statement = statement.strip()
#         if statement:  # Only execute non-empty statements
#             connection.execute(text(statement))

df = pd.read_csv('Top_25_Gainers.csv')
print("Writing to MySQL Database")
with engine.connect() as connection:
    df.to_sql('test', connection, index=False, chunksize=10000)


print('Script executed succesfully')


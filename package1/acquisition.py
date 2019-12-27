# The first step in data cleaning is to import all libraries needed:
import pandas as pd
from sqlalchemy import create_engine

def acquisition(file):
    # using the relative path to create the engine:
    eng = create_engine('sqlite:///../data/raw/almsasantos.db')
    business_info = pd.read_sql_table('business_info', con=eng)
    personal_info = pd.read_sql_table('personal_info', con=eng)
    rank_info = pd.read_sql_table('rank_info', con=eng)
    df = pd.merge(pd.merge(business_info, personal_info, on='id'), rank_info, on='id')
    df.to_csv(file)

def reading_csv(acquisition_file):
    print('Reading csv file ...')
    df = pd.read_csv(acquisition_file)
    return df

acquisition('df_acquisition')

print(reading_csv('df_acquisition'))
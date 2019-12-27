import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('web')
colors = ['burlywood', 'yellowgreen', 'gold', 'r', 'orangered', 'mediumvioletred', 'skyblue', 'navy', 'grey', 'black']
def num_billionaires_per_country(df):
    # Which country has maximum numbers of billionaires??
    df['country'].value_counts()[:30].plot(kind='bar', width=0.9, figsize=(20,10), color = colors)
    plt.xlabel('Country (Top 30)')
    plt.ylabel('Number of billionaires')
    plt.title('Number of billionaires per country')
    return plt.show()

def male_female_ratio(df):
    # Male to female ratio based on the total of dollares
    male_female_ratio = df.groupby('gender')['worth(BUSD)'].sum().sort_values(ascending=False)/100

    # In this case we will represent that variable in a pie chart:
    gender = ['Male', 'Female']
    colors = ['skyblue', 'hotpink']
    male_female_ratio.plot(kind='pie', labels = gender, colors = colors, startangle=90, shadow=True, figsize=(20,10),  autopct='%.2f')
    plt.title('Male-Female ratio')
    return plt.show()

def more_even_country(df):
    # Which country has the greatest share in terms of total money held by its billionaires??
    colors = ['burlywood', 'yellowgreen', 'gold', 'r', 'orangered', 'mediumvioletred', 'skyblue', 'navy', 'grey', 'black']
    total_per_country = df.groupby('country')['worth(BUSD)'].sum().sort_values(ascending=False)[:15]
    total_per_country.plot(kind='bar', width=0.92, figsize=(20,10), color = colors)
    plt.xlabel('Country (Top 15)')
    plt.ylabel('Billions of dollars')
    plt.title('Top 15 countries which held more money')
    return plt.show()

def profitable_work_field(df):
    # Top 10 most profitable field of work
    most_profitable_work_field = df.groupby('work_field')['worth(BUSD)'].sum().sort_values(ascending=False)[:15]
    most_profitable_work_field.plot(kind='bar', width=0.92, figsize=(20,10), color = colors)
    plt.xlabel('Work field (Top 15)')
    plt.ylabel('Billions of dollars')
    plt.title('Top 10 most profitable fields of work')
    return plt.show()

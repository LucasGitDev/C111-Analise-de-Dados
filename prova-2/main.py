import matplotlib.pyplot as plt
from os import path
import pandas as pd


"""Crie um Bar Plot que ilustre qual o país mais feliz e o mais infeliz do mundo
segundo este dataset;"""
def q1(df: pd.DataFrame):
    happiest_country = df.loc[df['Ladder score'].idxmax()]
    unhappiest_country = df.loc[df['Ladder score'].idxmin()]
    print(happiest_country)
    print(unhappiest_country)
    plt.bar([f'Happiest: {happiest_country["Country name"]}', f'Unhappiest: {unhappiest_country["Country name"]}'], [
            happiest_country['Ladder score'], unhappiest_country['Ladder score']])
    plt.show()

"""Mostre em um Pie Plot as regiões dos 20 países mais felizes deste dataset;"""
def q2(df: pd.DataFrame):
    # pegar os 20 países mais felizes
    happiest_countries = df.nlargest(20, 'Ladder score')
    happiest_countries = happiest_countries.groupby('Regional indicator').size()
    plt.pie(happiest_countries, labels=happiest_countries.index)
    plt.show()

"""Mostre em um Scatter Plot os 5 países mais felizes da América Latina e Caribe. O
tamanho do marcador de cada país deve ser definido se baseando na respectiva
renda per capita de cada um deles (faça os devidos ajustes para auxiliar na melhor
visibilidade dos pontos);"""
def q3(df: pd.DataFrame):
    happiest_countries = df.loc[df['Regional indicator']
                                == 'Latin America and Caribbean']
    happiest_countries = happiest_countries.nlargest(5, 'Ladder score')
    plt.scatter(happiest_countries['Ladder score'], happiest_countries['Log GDP per capita'],
                s=happiest_countries['Log GDP per capita']*1000, c='red', alpha=0.5,)
    plt.show()


"""Apresente um Bar Plot que compare a "liberdade de se fazer escolhas de vida" do
Brazil com a média de "liberdade de se fazer escolhas de vida" dos países da
América Latina e Caribe."""

def q4(df: pd.DataFrame):
    brazil = df.loc[df['Country name'] == 'Brazil']
    latin_america = df.loc[df['Regional indicator']
                           == 'Latin America and Caribbean']
    latin_america = latin_america['Freedom to make life choices'].mean()

    brazil_value = brazil['Freedom to make life choices'].values[0]

    print(brazil_value)
    print(latin_america)
    
    plt.bar(['Brazil', 'Latin America and Caribbean'],
            [brazil_value, latin_america])
    plt.show()


def obtain_path(file_name='world_happiness.csv'):
    return path.join(path.dirname(__file__), file_name)


def main():
    df = pd.read_csv(obtain_path(), delimiter=',', header=0,)
    # q1(df)
    # q2(df)
    # q3(df)
    q4(df)

if __name__ == "__main__":
    main()

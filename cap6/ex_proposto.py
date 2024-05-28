import pandas as pd
from os import path
import matplotlib.pyplot as plt


"""
1. Por meio do Dataset space.csv, trace um grafico em barras 
mostrando quantas empresas Espaciais os EUA e a CHINA possuem; 

Dica: apos realizar os devidos condicionais no dataset para cada
um dos paises, utilize do método unique() para retirar resultados 
repetidos. 
"""


def q1(df: pd.DataFrame):
    print('Empresas Espaciais dos EUA e da China')
    us_companies = df[df['Location'].str.contains(
        'USA')]['Company Name'].unique()
    china_companies = df[df['Location'].str.contains(
        'China')]['Company Name'].unique()

    print(f'Empresas dos EUA: {us_companies.size}')
    print(f'Empresas da China: {china_companies.size}')
    print(f'Total: {us_companies.size + china_companies.size}')

    plt.bar(['EUA', 'China'], [us_companies.size, china_companies.size])
    plt.show()


"""
2. Por meio do Dataset paises.csv, trace dois graficos de linhas 
em um mesmo plano cartesiano, um mostrando a taxa de mortalidade 
(Deathrate) e outro a taxa de natalidade (Birthrate) dos paises da
America do Norte (NORTHERN AMERICA);  Dica: apos realizar o condicional 
no dataset para pegar os paises da América do Norte,  vocé ja podera chamar 
o método plot, passando como argumento para ele slicings sobre o  dataset 
resultante do condicional.  
"""


def q2(df: pd.DataFrame):
    print('Taxa de Natalidade e Mortalidade dos paises da America do Norte')
    north_america = df[df['Region'].str.strip() == 'NORTHERN AMERICA']

    north_america.plot(x='Country', y=['Birthrate', 'Deathrate'])
    plt.show()


def obtain_path(file_name='space.csv'):
    return path.join(path.dirname(__file__), file_name)


def main():
    df = pd.read_csv(obtain_path(), delimiter=';', header=0,)
    # header = ['Num' 'Company Name' 'Location' 'Datum' 'Detail' 'Status Rocket' 'Cost' 'Status Mission']
    q1(df)
    dfCountries = pd.read_csv(obtain_path(
        file_name='paises.csv'), delimiter=';', header=0,)
    q2(dfCountries)


if __name__ == "__main__":
    main()

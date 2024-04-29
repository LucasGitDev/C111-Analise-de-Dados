import pandas as pd
from os import path


# Quais os paises da oceania
def q1(df: pd.DataFrame):
    print('Paises da Oceania')
    countries_from_oceania = df[df['Region'].str.strip()
                                == 'OCEANIA']['Country']
    
    print(countries_from_oceania)
    print(f'Total de paises: {countries_from_oceania.size}')


#Mostre a media de alfabetização (Literacy (%)) do planeta
def q2(df: pd.DataFrame):
    print('Media de alfabetização do planeta')
    print(f'Media de alfabetização: {df["Literacy (%)"].mean()}%')


# nome e a regiao do pais que possui maior populaçao
def q3(df: pd.DataFrame):
    print('Pais com maior população')
    country = df[df['Population'] == df['Population'].max()].iloc[0]
    print(f'Pais: {country["Country"]}')
    print(f'Regiao: {country["Region"]}')


"""
4, Busque 0 nome de todos os paises do dataset que nao possuem costa maritima 
(Coastline (coast/area ratio) == 0) e guarde-os em um novo arquivo chamado noCoast.csv;
Dica: apos realizar os filtros, use do auxilio da funçao to_csv; 
"""
def q4(df: pd.DataFrame):
    print('Paises sem costa maritima')
    no_coast = df[df['Coastline (coast/area ratio)'].astype(float) == 0]
    no_coast.to_csv(obtain_path('noCoast.csv'), index=False)
    print(no_coast['Country'])
    

def obtain_path(file_name='paises.csv'):
    return path.join(path.dirname(__file__), file_name)


def main():
    df = pd.read_csv(obtain_path(), delimiter=';', header=0,)
    q1(df)
    q2(df)
    q3(df)
    q4(df)
    
    
if __name__ == "__main__":
    main()
import numpy as np
from os import path

"""Faça um slicing no dataset para mostrar apenas o País (Country), Região
(Region), População (Population) e Area (Area (sq. mi.)) dos países contidos
nele;"""

def q1(dataset: np.ndarray) -> np.ndarray:
    return dataset[:, 0:4]


"""Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo
este dataset;"""
def q2(dataset: np.ndarray) -> np.ndarray:
    return np.unique(dataset[:, 1])


"""Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo
este dataset;"""
def q3(dataset: np.ndarray) -> float:
    return np.mean(dataset[:, get_column_index('Literacy (%)')].astype(float))


"""Conte quantos países são da América do Norte (NORTHERN AMERICA)
segundo este dataset;
"""
def q4(dataset: np.ndarray) -> int:
    north_american_countries = dataset[1:][np.char.find(dataset[1:, 1], 'NORTHERN AMERICA') != -1]
    return len(north_american_countries)




"""Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB)
possui a maior renda per capita (GDP ($ per capita));"""
def q5(dataset: np.ndarray) -> str:
    latin_american_countries = dataset[1:][np.char.find(
        dataset[1:, 1], 'LATIN AMER. & CARIB') != -1]
    gdp_column_index = get_column_index('GDP ($ per capita)')
    gdp_column = latin_american_countries[:, gdp_column_index].astype(float)
    max_gdp_index = np.argmax(gdp_column)
    return latin_american_countries[max_gdp_index, 0]



def get_column_index(column_name: str) -> int:
    return np.where(header == column_name)[0][0]


def obtain_path():
    return path.join(path.dirname(__file__), 'paises.csv')


def main():
    global header
    header = np.loadtxt(obtain_path(), delimiter=';',
                        dtype=str, encoding='utf-8', max_rows=1)
    dataset: np.ndarray = np.loadtxt(
        obtain_path(), delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

    print('#' *30)
    print('# Questão 1')
    print(q1(dataset))
    print('#' *30)
    print('# Questão 2')
    regions = q2(dataset)
    print(f'Existem {len(regions)} regiões no dataset')
    print(regions)
    print('#' *30)
    print('# Questão 3')
    print(f'{q3(dataset):.2f}%')
    print('#' *30)
    print('# Questão 4')
    print(q4(dataset))
    print('#' *30)
    print('# Questão 5')
    print(q5(dataset))
    print('#' *30)
    
    
        
if __name__ == '__main__':
    main()
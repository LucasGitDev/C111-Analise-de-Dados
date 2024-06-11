import numpy as np
from os import path


# Mostre o quanto ($) a empresa Google valorizou de 2021 para 2022;
def q1(dataset: np.ndarray) -> np.ndarray:
    googleRow = dataset[dataset[:, 0] == 'Google']
    google2022 = float(googleRow[0, column_index('Brand Value ($M) in 2022')])
    google2021 = float(googleRow[0, column_index('Brand Value ($M) in 2021')])
    print(f'Google 2022: {google2022}')
    print(f'Google 2021: {google2021}')
    return google2022 - google2021


# Mostre quantas marcas neste dataset possuem a palavra “Group” em seu nome;
def q2(dataset: np.ndarray) -> np.ndarray:
    return np.sum(['Group' in brand for brand in dataset[:, 0]])


# Mostre o nome e qual seria o valor de mercado das 5 primeiras empresas deste dataset em 2023 caso tivessem um aumento de 10%
def q3(dataset: np.ndarray) -> np.ndarray:
    first_five = dataset[:5]
    for row in first_five:
        print(f'{row[0]}: {float(row[column_index("Brand Value ($M) in 2022")]) * 1.1}')


"""Faça um Slicing no dataset e extraia apenas as colunas "nome da marca, por quem foi
fundada e o ano que ela foi fundada". Em seguida, mostre apenas o nome das empresas
fundadas depois dos anos 2000;"""
def q4(dataset: np.ndarray) -> np.ndarray:
    sliced = dataset[:, [0, column_index(
        'Founded By/How it was founded'), column_index('Founded In')]]
    filtered = sliced[sliced[:, 2] > '2000']
    return filtered[:, 0]


"""Busque os diferentes anos em que as empresas foram fundadas. Em seguida, mostre em
qual ano mais empresas abriram as portas."""
def q5(dataset: np.ndarray) -> np.ndarray:
    years = dataset[:, column_index('Founded In')]
    unique_years, counts = np.unique(years, return_counts=True)
    return unique_years[np.argmax(counts)]


def get_full_path():
    return path.join(path.dirname(__file__), 'brands.csv')


def column_index(column_name: str) -> int:
    return np.where(header == column_name)[0][0]


def main():
    global header
    header = np.loadtxt(get_full_path(), delimiter=';',
                        dtype=str, encoding='utf-8', max_rows=1)
    dataset: np.ndarray = np.loadtxt(
        get_full_path(), delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

    print('#'*10)
    print('Q1')
    print(q1(dataset))
    print('#'*10)
    print('Q2')
    print(q2(dataset))
    print('#'*10)
    print('Q3')
    q3(dataset)
    print('#'*10)
    print('Q4')
    print(q4(dataset))
    print('#'*10)
    print('Q5')
    print(q5(dataset))
    print('#'*10)

if __name__ == "__main__":
    main()

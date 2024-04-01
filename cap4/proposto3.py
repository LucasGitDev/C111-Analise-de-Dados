import numpy as np
import os


"""1. Apresente a porcentagem de quantas missOes deram certo;"""


def q1(dataset: np.ndarray):
    status_mission_column_index = get_column_index(header, 'Status Mission')
    status_mission_column = dataset[:, status_mission_column_index].flatten()
    success_missions = np.where(status_mission_column == 'Success')[0]
    success_rate = len(success_missions) / len(status_mission_column) * 100
    print(f'{success_rate:.2f}%')


"""2. Qual a média de gastos de uma missão espacial se baseando em missões que 
possuam valores disponíveis (> 0)? """


def q2(dataset: np.ndarray):
    cost_column_index = get_column_index(header, 'Cost')
    cost_column = dataset[:, cost_column_index].flatten()
    cost_column_filtered = cost_column[cost_column.astype(float) > 0]
    cost_column_filtered = cost_column_filtered.astype(float)
    average_cost = np.mean(cost_column_filtered)
    print(f'{average_cost:.2f}')
    pass


"""3. Encontre quantas missOes espaciais neste DataSet foram realizadas pelos
Estados Unidos (EUA); """


def q3(dataset: np.ndarray):
    location_column_index = get_column_index(header, 'Location')
    location_column = dataset[:, location_column_index].flatten()
    location_with_only_last_word = np.array(
        [location.split()[-1] for location in location_column])
    us_missions = np.where(location_with_only_last_word == 'USA')[0]
    print(len(us_missions))


"""4. Encontre qual foi a missão mais cara realizada pela Empresa "Spacex"; """


def q4(dataset: np.ndarray):
    company_name_column_index = get_column_index(header, 'Company Name')
    cost_column_index = get_column_index(header, 'Cost')
    company_name_column = dataset[:, company_name_column_index].flatten()
    cost_column = dataset[:, cost_column_index].flatten()

    spacex_missions = np.where(company_name_column == 'SpaceX')[0]
    spacex_costs = cost_column[spacex_missions].astype(float)

    max_cost_mission_index = np.argmax(spacex_costs)

    most_expensive_mission_row = dataset[spacex_missions[max_cost_mission_index]]

    print(most_expensive_mission_row)


"""5. Mostre o nome das empresas que ja realizaram Miss6es Espaciais juntamente
com suas respectivas quantidades de missões (use o for no final para mostrar 
as informacoes). """


def q5(dataset: np.ndarray):
    company_name_column_index = get_column_index(header, 'Company Name')
    company_name_column = dataset[:, company_name_column_index].flatten()
    unique_companies, unique_companies_counts = np.unique(
        company_name_column, return_counts=True)
    for company, count in zip(unique_companies, unique_companies_counts):
        print(company, count)


def obtain_path():
    return os.path.join(os.path.dirname(__file__), 'space.csv')


def get_column_index(header: np.ndarray, column_name: str) -> int:
    return np.where(header == column_name)


def main():
    global header
    header = np.loadtxt(obtain_path(), delimiter=';',
                        dtype=str, encoding='utf-8', max_rows=1)
    dataset: np.ndarray = np.loadtxt(
        obtain_path(), delimiter=';', dtype=str, encoding='utf-8', skiprows=1)
    # header = ['Num' 'Company Name' 'Location' 'Datum' 'Detail' 'Status Rocket' 'Cost' 'Status Mission']

    print('#' * 30)
    print('#' * 14, 'Q1', 14 * '#')
    q1(dataset)
    print()
    print('#' * 30)
    print('#' * 14, 'Q2', 14 * '#')
    q2(dataset)
    print()
    print('#' * 30)
    print('#' * 14, 'Q3', 14 * '#')
    q3(dataset)
    print()
    print('#' * 30)
    print('#' * 14, 'Q4', 14 * '#')
    q4(dataset)
    print()
    print('#' * 30)
    q5(dataset)
    print()


if __name__ == '__main__':
    main()

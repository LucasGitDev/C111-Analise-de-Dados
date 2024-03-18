import numpy as np

""""1. Crie um array de floats com 10 elementos positivos e negativos 
entre 0 e 1. Em seguida, multiplique seus valores por 100 e crie um novo 
vetor apenas com a parte inteira destes numeros; (use seed(5) antes) """
def q1():
    np.random.seed(5)
    arr = np.random.randn(10)
    print(arr)
    arr = np.floor(arr * 100)
    return arr

"""2. 
Crie uma matriz de tamanho 4x4 formada por numeros aleatórios 
inteiros entre 1 e 50; (use seed(10) antes) 
    """
def q2():
    np.random.seed(10)
    arr = np.random.randint(1, 51, (4, 4))
    print(arr)
    return arr

"""3. 
Mostre o resultado da média de cada linha e cada coluna da matriz gerada 
pela questao 2, e em seguida, apresente o maior valor das médias para 
as linhas e também para as colunas; 
"""

def q3(arr: np.ndarray):
    print(arr)
    print('Media das linhas:', arr.mean(axis=1))
    print('Media das colunas:', arr.mean(axis=0))
    print('Maior media das linhas:', arr.mean(axis=1).max())
    print('Maior media das colunas:', arr.mean(axis=0).max())
    return arr.mean(axis=1).max(), arr.mean(axis=0).max()


"""4.
Baseado na matriz gerada na questão 2, mostre a quantidade de 
aparições de cada um dos numeros na mesma. 
Em seguida, mostre apenas os numeros que aparecem 2 vezes. """
def q4(arr: np.ndarray):
    unique = np.unique(arr.flatten(), return_counts=True)
    my_dict = dict(zip(unique[0], unique[1]))
    print('Quantidade de aparições de cada número:', my_dict)
    print('Numeros que aparecem 2 vezes:', (unique[0][unique[1] == 2]))
    return np.where(np.bincount(arr.flatten()) == 2)[0]


def main():
    print('#' * 30)
    print('#'* 14, 'Q1', 14 * '#')
    print(q1())
    print('#' * 30)
    print()
    print('#' * 30)
    print('#'* 14, 'Q2', 14 * '#')
    arr = q2()
    print('#' * 30)
    print()
    print('#' * 30)
    print('#'* 14, 'Q3', 14 * '#')
    q3(arr)
    print('#' * 30)
    print()
    print('#' * 30)
    print('#' * 14, 'Q4', 14 * '#')
    q4(arr)
    print('#' * 30)
    print()
    
    
    
if __name__ == "__main__":
    main()
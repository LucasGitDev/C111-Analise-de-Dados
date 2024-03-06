import numpy as np


# Crie um array com 21 elementos com valores linearmente espaçados entre 0 e 1
def q1():
    arr = np.linspace(0, 1, 21)
    print(arr)


# Crie dois arrays: um de números pares de 0 até 51 e outro também de números pares 100 até 50.
# Em seguida, concatene os dois arrays e mostre o resultado ordenado.
def q2():
    arr1 = np.arange(0, 52, 2)
    arr2 = np.arange(100, 49, -2)
    arr3 = np.concatenate((arr1, arr2))
    arr3 = np.sort(arr3)
    print(arr3)
    return arr3


# Ordene o array anterior de forma decrescente.
def q3(arr):
    arr = np.sort(arr)[::-1]
    print(arr)
    return arr


# Crie uma matriz formada somente por uns de tamanho 3x4. Em seguida, transforme-a em um Array 1-D.
def q4():
    arr = np.ones((3, 4))
    arr = arr.flatten()
    print(arr)
    return arr


# Crie uma matriz identidade de tamanho qualquer. Extraia seu número de linhas e colunas,
# multiplique-os, e diga se esta matriz poderia se tornar um vetor com número par ou impar de elementos.
def q5():
    matriz = np.identity(5)
    print("Matriz: ", matriz)
    linhas, colunas = matriz.shape
    print("Linhas * Colunas = ", linhas * colunas)
    is_even = (linhas * colunas) % 2 == 0
    print("par" if is_even else "ímpar")


def main():
    print('#'*10, 'Questão 1', '#'*10)
    q1()
    print('#'*30)
    print('#'*10, 'Questão 2', '#'*10)
    response = q2()
    print('#'*30)
    print('#'*10, 'Questão 3', '#'*10)
    q3(response)
    print('#'*30)
    print('#'*10, 'Questão 4', '#'*10)
    q4()
    print('#'*30)
    print('#'*10, 'Questão 5', '#'*10)
    q5()
    print('#'*30)


if __name__ == '__main__':
    main()

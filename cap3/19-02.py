def tupla():
    nomes = ("Goku", "Vegeta", "Trunks", "Gohan")
    print("TUPLA:")

    print("Nome do primeiro personagem:")
    print(nomes[0])

    print("Nome de todos os personagens anteriores ao indice 2:")
    print(nomes[:2])

    print("Nome dos personagens centrais:")
    print(nomes[1:3])

    print("Printando o Trunks buscando pela esquerda:")
    print(nomes[-2])

    print("Definição de tupla: ")
    print("Tupla é uma coleção de objetos que não pode ser alterada")
    print("-----------------------------------------------------------------")


def lista():
    nomes = ["Goku", "Vegeta", "Trunks", "Gohan"]
    print("LISTA:")
    print("Adicionando Piccolo a lista:")
    nomes.append("Piccolo")
    print(nomes)

    print("Atualizando o nome do Gohan para Goten:")
    nomes[3] = "Goten"
    print(nomes)

    print("Removendo o Trunks da lista:")
    nomes.remove("Trunks")
    print(nomes)

    print("Definição de lista: ")
    print("Lista é uma coleção de objetos que pode ser alterada")
    print("-----------------------------------------------------------------")


def conjuntos():
    nomes = {"Goku", "Vegeta", "Trunks", "Gohan"}
    print("CONJUNTO:")
    print(nomes)

    print("Adicionando Piccolo ao conjunto:")
    nomes.add("Piccolo")
    print(nomes)

    print("Adicionando Goku novamente ao conjunto:")
    print("Conjuntos não guardam valores duplicados")

    print("Removendo o Trunks do conjunto:")
    nomes.remove("Trunks")
    print(nomes)

    print("Definição de conjunto: ")
    print(
        "Conjunto é uma coleção de objetos que pode ser alterada (Add e Delete apenas) e não guarda valores duplicados"
    )
    print("-----------------------------------------------------------------")


def dicionarios():
    personagens = {
        "Goku": "Saiyajin",
        "Vegeta": "Saiyajin",
        "Trunks": "Saiyajin",
        "Gohan": "Saiyajin",
    }
    print("DICIONÁRIO:")
    print("A raça do Goku é:")
    print(personagens["Goku"])

    print("Adicionando Piccolo ao dicionário:")
    personagens["Piccolo"] = "Namekuseijin"
    print(personagens)

    print("Atualizando a raça do Gohan para Humano:")
    personagens["Gohan"] = "Humano"
    print(personagens)

    print("Removendo o Trunks do dicionário:")
    del personagens["Trunks"]
    print(personagens)

    print("Definição de dicionário: ")
    print(
        "Dicionário é uma coleção de objetos que pode ser alterada e não guarda valores duplicados"
    )
    print("-----------------------------------------------------------------")


if __name__ == "__main__":
    tupla()
    lista()
    conjuntos()
    dicionarios()
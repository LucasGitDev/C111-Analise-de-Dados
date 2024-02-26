
def q1():
    print('-'*10, 'Q1', '-'*10)
    campeonato_mundial = [
        {
            'nome': 'Barcelona',
            'pontos': 39,
            'jogos': 19,
        }, {
            'nome': 'Real Madrid',
            'pontos': 38,
            'jogos': 19,
        }, {
            'nome': 'Atletico Madrid',
            'pontos': 38,
            'jogos': 19,
        }, {
            'nome': 'Valencia',
            'pontos': 37,
            'jogos': 19,
        }, {
            'nome': 'Sevilla',
            'pontos': 36,
            'jogos': 19,
        },
    ]
    
    print('Apenas os 3 primeiros colocados:')
    for time in campeonato_mundial[:3]:
        print(f'{time["nome"]}: {time["pontos"]} pontos')
    print('-'*30)
    
    print('Os últimos 2 colocados:')
    for time in campeonato_mundial[-2:]:
        print(f'{time["nome"]}: {time["pontos"]} pontos')
    print('-'*30)
    
    print('Times em ordem alfabética:')
    for time in sorted(campeonato_mundial, key=lambda time: time['nome']):
        print(f'{time["nome"]}: {time["pontos"]} pontos')
    print('-'*30)
    
    print('Qual posição do Barcelona?')
    # use filter
    barcelona = list(filter(lambda time: time['nome'] == 'Barcelona', campeonato_mundial))
    print(f'Barcelona está na {campeonato_mundial.index(barcelona[0]) + 1}ª posição')

def q2():
    print('-'*10, 'Q2', '-'*10)
    loja1_modelos = ['Redmi Note 8', 'Redmi Note 9', 'Redmi Note 10', 'Redmi Note 11']
    loja2_modelos = ['Redmi Note 9', 'Redmi Note 10', 'Redmi Note 11', 'Redmi Note 12']
    
    print('Modelos que estão nas duas lojas:')
    lista = list(filter(lambda modelo: modelo in loja2_modelos, loja1_modelos))
    print(lista)
    print('-'*30)
    
    print('Modelos existentes no total:')
    lista = list(set(loja1_modelos + loja2_modelos))
    print(lista)
    print('-'*30)
    

def q3():
    print('-'*10, 'Q3', '-'*10)
    aluno = {}
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
    
    if aluno['media'] >= 60:
        print(f'{aluno["nome"]} está aprovado')
        aluno['situacao'] = 'Aprovado'
    else:
        print(f'{aluno["nome"]} está reprovado')
        aluno['situacao'] = 'Reprovado'
    
    print(aluno)
    print('-'*30)

if __name__ == '__main__':
    q1()
    q2()
    q3()

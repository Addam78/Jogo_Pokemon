import random
import time


##listando os pokemons
print('jogo do pokemon')

print('Bem vindo ao jogo pokemon, estes são os pokemons para escolha')

pokemons={
        'Pokemon1':['Nome:''Charmander','Life:' '180hp','Atack:' '85'],
        'Pokemon2':['Nome:''Squartle','Life:' '200hp','Atack:' '70'],
        'Pokemon3':['Nome:''Bulbassauro','Life:' '230hp','Atack:' '65'],

          }

for n,k in pokemons.items():
    print(n,k)

##REgra para escolha do Pokemon
escolha=input('Escolha seu pokemon ')
while True:
    if escolha=='1':
        print(pokemons['Pokemon1'])
        escolha=pokemons['Pokemon1']
        break
    elif escolha=='2':
        print(pokemons['Pokemon2'])
        escolha=pokemons['Pokemon2']
        break
    elif escolha =='3':
        print(pokemons['Pokemon3'])
        escolha = pokemons['Pokemon3']
        break
    else:
        print('Escolha uma opção valida por favor ')
        escolha = input('Escolha seu pokemon ')

print('Otima escolha de pokemon')
for n in escolha:
    print(n)

##Criando Pokemons do oponente
print('*'*20)
pokemonscom={'Pokemonscom1':['Nome:Onix','Life:300hp','Atack:60'],
             'Pokemonscom2':['Nome:Miau','Life:250hp' ,'Atack:45',],
             'Pokemonscom3':['Nome:Raichu','Life:280hp','Atack:90']}


##Escolhendo pokemon do oponente
adversario=''
dado=list(range(0,3))
dado=(random.choice(dado))

if dado==0:
    print('Seu adversario é')
    adversario=pokemonscom['Pokemonscom1']
    for n in pokemonscom['Pokemonscom1']:
        print(n)
elif dado==1:
    print('Seu adversario é')
    adversario = pokemonscom['Pokemonscom2']
    for n in pokemonscom['Pokemonscom2']:
        print(n)
elif dado==2:
    print('Seu adversario é')
    adversario = pokemonscom['Pokemonscom3']
    for n in pokemonscom['Pokemonscom3']:
        print(n)

print('*'*15)

print(f'Muito bom o pokemon do principal é {escolha} e o pokemon do oponente é {adversario}')

##Inicio da batalha##
print('Muito bem, hora de iniciar a batalha, primeiro vamos ver que vai começar,sera definido'
      ' da seguinte forma o jogador Principal  sera par, e o Oponente sera impar', 
      'serão lançados dois dados, se resultar em par Jogador princiapl inicia, se resultar em impar,'
      'o Oponente inicia a batalha ')

##Sorteando quem vai iniciar a batalha
dado_1=list(range(1,6))
dado_2=list(range(1,6))


sorte_1=random.choice(dado_1)
sorte_2=random.choice(dado_2)

t=sorte_1+sorte_2
print(f' O Resultado do lancamento dos dados foi {t}')


##Função de ataque paara player principal
def ataque_principal():

    life=(adversario[1])
    life_oponente=int((life[5:8]))
    vida_adversario_atual =[]
    lifes=(escolha[1])
    life_principal=int(lifes[5:8])
    c=10

    while c>=0:
        print('TUrno do player principal'.upper())
        dano = random.choice(list(range(5,95)))  ##Universal player principal
        decidir=input('1-Atacar ou 2- Item de recuperação de 10%Hp ')
        if decidir=='1':
            life_oponente-=dano
            print(f'O player principal ataca essa é a vida atual do oponente {life_oponente}')
            if life_oponente<=0:
                print('O player principal venceu')
                break
        else:
            print('Vida +10%')
            acrescimo_vida=life_principal*10/100
            life_principal+=acrescimo_vida
            print(f' essa é a vida atual do player princiapl {life_principal}')


        print('=-='*25)
        print('Turno do adversario'.upper()) ###Turno adversario


        print('1-Atacar ou 2- Item de recuperação de 10%Hp') ##Ataque adversario
        danos = random.choice(list(range(5, 95)))
        adversario_decidi = random.randint(1,2)
        print(adversario_decidi)
        if adversario_decidi==1:
            life_principal-=danos
            print(f'adversario ataca, essa é avida atual do player principal {life_principal}')

            if life_principal<0:
                print('O adversario venceu')
                break

        else:
            print('VIda +10%')
            acrescimo_vida_oponente=life_oponente*10/100
            life_oponente+=acrescimo_vida_oponente
            print(f'essa é a vida atual do oponente{life_oponente}')

        print('=-='*25)


##Função de atque para adversario
def oponente_ataque():
    life = (adversario[1])
    life_oponente = int((life[5:8]))
    vida_adversario_atual = []
    lifes = (escolha[1])
    life_principal = int(lifes[5:8])
    c = 10

    while c>0:
        print('1-Atacar ou 2- Item de recuperação de 10%Hp')
        danos = random.choice(list(range(5, 95)))
        adversario_decidi = random.randint(1,2)
        print(adversario_decidi)
        if adversario_decidi == 1:
            life_principal -= danos
            print(f'adversario atacar essa é avida atual do player principal {life_principal}')

            if life_principal < 0:
                print('O adversario venceu')
                break
            # vida_jogador_principal_atual=vida_jogador_principal_atual-random.choice(list(range(0,95)))
        else:
            print('VIda +10%')
            acrescimo_vida_oponente = life_oponente * 10 / 100
            life_oponente += acrescimo_vida_oponente
            print(f'O oponente recuperou a vida {life_oponente}')

        print('=-='*25)
        print('Turno do player principal'.upper())

        dano = random.choice(list(range(5, 95)))  ##Universal player principal
        decidir = input('1-Atacar ou 2- Item de recuperação de 10%Hp')
        if decidir == '1':
            life_oponente -= dano
            print(f'player principal ataca essa é a vida atual do oponente {life_oponente}')
            if life_oponente <= 0:
                print('O player principal venceu')
                break
        else:
            print('Vida +10%')
            acrescimo_vida = life_principal * 10 / 100
            life_principal += acrescimo_vida
            print(life_principal)


        print('=-='*25)
        print('Turno do adversario'.upper())


if t%2==0:
    print('Jogador principal inicia a partida')
    ataque_principal()

else:
    print('Vez do oponente')
    oponente_ataque()
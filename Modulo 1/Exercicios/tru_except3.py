lista=['gabriel,','joao','otavio']
indice= int(input('digite o indice que voce quer acessar'))

try:
    print(lista[indice])
except:
    print('o nome que voce esat acessando nao existe')
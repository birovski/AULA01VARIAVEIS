contador = int(input("Digite um número: ")) 

while contador <= 5:
    print(contador)
    contador = contador + 1

senha = "123"


#Atividade 01

print("Atividade 01:")
num = 1
while num <=10:
    print(num)
    num = num + 1

#atividade 02

print("Atividade 02:")
num2 = 1
num3 = 1
while num2 < 100:
    num2 = num2 + 1
    num3 = num3 + num2

print(num3)

#atividade 03

print("Atividade 03:")
tabuada = int(input("digite um número: "))
mult = 1

while mult <= 10:
    result = tabuada * mult
    print(f"{tabuada} x {mult} = {result}")
    mult += 1

#atividade 04

print("Atividade 04:")
contagem = 10
while contagem >= 1:
    print(contagem)
    contagem -= 1

print("Feliz ano novo")

#atividade 05

print("Atividade 05:")
num4 = int(input("Digite um número para que seja feita a contagem de um até ele: "))
cont2 = 1
while cont2 <= num4:
    if cont2 % 2 != 0:
        print(cont2)
    cont2 += 1


#atividade 06

print("Atividade 06:")

soma = 0
num6 = 0
while num6 >= 0:
    num6 = int(input("Digite um número positivo para somar ou um negativo para sair: "))
    if num6 > 0:
        soma += num6
    else:
        print(f"A soma dos números positivos é: {soma}")


#atividade 07

print("Atividade 07:")

#atividade 08

print("Atividade 08:")

tabuada3 = int(input("digite um número para calcular a tabuada dos multiplos de 3: "))
mult3 = 1

while mult <= 10:
   result = tabuada * mult
   print(f"{tabuada} x {mult} = {result}")
   mult += 1

# crie um  programa que solicite a senha do usuário com limite de tentativas = 3
# encerre quando ultrapassar as 3 tentativas

senha = "123"
tentativas = 0
totaltentativas = 3
insert = input("Digite a senha: ")
while insert != senha:
    print(f"Senha incorreta, você ainda tem {totaltentativas - tentativas}")
    tentativas += 1
    insert = input("Digite a senha: ")
    if tentativas >= totaltentativas:
        print("Tentativas esgotadas")
        break
if insert == senha:
    print("Acesso concedido")
    
# FAZER AS DEMAIS ATIVIDADES
# ESTUDAR WHILE TRUE
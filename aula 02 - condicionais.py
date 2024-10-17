#teste: str = 20
#print(type(teste))

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
peso = int(input("Qual a seu peso? "))
altura = float(input("Qual a seu altura? "))
imc = peso/altura**2
print(f"Meu nome é {nome} e tenho {idade} anos, meço {altura:.2f}m, peso {peso}kg e meu IMC é {imc:.1f}")

# Operadores de comparação

nome2 = input("Qual o seu nome? ")
idade2 = int(input("Qual a sua idade? "))
peso2 = int(input("Qual a seu peso? "))
altura2 = float(input("Qual a seu altura? "))
imc2 = peso2/altura2**2
print(f"Meu nome é {nome2} e tenho {idade2} anos, meço {altura2:.2f}m, peso {peso2}kg e meu IMC é {imc2:.1f}")

print(f"O IMC de {nome} é igual ao de {nome2}? ", imc == imc2)
print(f"O IMC de {nome} é diferente do de {nome2}? ", imc != imc2)
print(f"O IMC de {nome} é maior que o de {nome2}? ", imc > imc2)
print(f"O IMC de {nome} é menor que o de {nome2}? ", imc < imc2)

#Operadores logicos

# nomemaiordeidade = idade>=18
# passouexame = True
# habilitacao = nomemaiordeidade and passouexame

#Operadores de atribuicao

x = 10
x += 5
print(x)

#operadores de associacao

# atividade 01

print(f"Idade de {nome} é maior que idade de {nome2} ", idade>idade2)
print(f"Idade de {nome} é menor que idade de {nome2} ", idade<idade2)
print(f"Idade de {nome} é igual a idade de {nome2} ", idade==idade2)

# atividade 02

print(f"Nome de {nome} é igual a nome de {nome2} ", idade==idade2)

# atividade 03

# nomemaiordeidade = idade>=18
# passouexame = True
# habilitacao = nomemaiordeidade and passouexame

# atividade 04

nota=float(input(f"A nota de {nome} é:" ))
nota2=float(input(f"A nota de {nome2} é:" ))
aprovado=6
print(f"{nome} está aprovado? ", nota>=aprovado)
print(f"{nome2} está aprovado? ", nota2>=aprovado)

#atividade 05

preco=float(input("Insira o preço: "))
desconto=preco*0.05
preco-=desconto
print=(f"O preço com desconto é {preco}")

#atividade 06

quantidade=(int(input("Insira a quantidade de produtos que quer comprar com desconto: ")))
preco*=quantidade
print=(f"O preço de {quantidade} produtos é {preco}")

#atividade 07

frase=input("Insira uma frase: ")
palavra=input("Digite uma palavra: ")
#falta terminar

#atividade 08

#estrutura condicional IF, ELIF, ELSE

if idade >= 60:
    print(f"{nome} é idoso.")
elif idade >=18:
    print(f"{nome} não é idoso, mas é maior de idade.")
else:
    print(f"{nome} é menor de idade.")

#atividade do IMC

if imc <= 18:
    print(f"{nome} é MAGRO VÉI")
elif imc < 25:
    print(f"{nome} é NORMAL")
elif imc < 30:
    print(f"{nome} tem SOBREPESO")
elif imc < 35:
    print(f"{nome} é OBESO GRAU 1")
elif imc < 40:
    print(f"{nome} é OBESO GRAU 2")
else:
    print(f"{nome} é UMA BALEIA")
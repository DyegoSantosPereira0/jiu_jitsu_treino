idade = int(input("idade:"))
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

soma = 0 
for i in range(1 , 6):
    soma += 1
print("soma total:", soma)

nomes = []
for i in range(3):
    nome = input("digite um nome:")
    nomes.append(nome)

alunos = {"joao":8.5, "maria": 9.0 }
nome = input("nome do aluno: ")
print("nota", alunos.get(nome, "aluno não encontrado"))

idade = int(input("idade:"))
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

soma = 0 
for i in range(1,6):
    soma += i
print("soma total:", soma)

nomes = []
for i in range(3):
    nome = input("digite um nome:")
    nomes.append(nome)

alunos = {"joao": 8.5, "maria": 9.0}
nome = input("nome do aluno:")
print("nota", alunos.get(nome, "aluno não encontrado"))

idade = int(input("idade:"))
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

soma = 0 
for i in range(1,6):
    soma += print("soma total:", soma)

nomes = []
for i in range(3):
    nome = input("digite um nome:")
    nomes.append(nome)

alunos = {"joao": 8.5, "maria": 9.0}
nome = input("nome do aluno: ")
print("nota:", alunos.get(nome, "aluno não encontrado"))

idade = int(input("idade:"))
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

soma = []
for i in range(3):
    nome = input("digite um nome:")
    nomes.append("nome")

alunos = {"joao": 8.5 , "maria": 9.0}
nome = input("nome do aluno:")
print("nota:", alunos.get(nome, "alunos não encontrado"))

idade = int(input("idade:"))
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

soma = 0 
for i in range(1, 6):
    soma += i
print("soma total:", soma)

nome = []
for i in range(3):
    nome = input("digite um nome:")
    nomes.append(nome)

alunos = {"joao": 8.5 , "maria": 9.0}
nome = input("digite um nome:")
print("nota:", alunos.get(nome, "aluno não encontrado"))

idade = int(input("idade:"))
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

soma = 0
for i in range(1, 6):
    soma += i 
print("soma total:", soma)

nomes = []
for i in range(3):
    nome = input("digite um nome:")
    nomes.append(nome)

alunos = {"joao": 8.5, "maria": 9.0}
nome = input("nome do aluno:")
print("nota:", alunos.get(nome, "aluno não encontrado"))

idade = int(input("idade:"))
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

soma = 0
for i in range(1,6):
    soma+= i
print("soma total:", soma)

nomes = []
for i in range(3):
    nome = input("digite um nome:")
    nomes.append(nome)

alunos = {"joao": 8.5, "maria": 9.0}
nome = input("nome de aluno:")
print("nota:", alunos.get(nome, "aluno não encontrado"))

idade = int(input("idade:"))
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

soma = 0
for i in range(1, 6):
    soma += i
print("soma total:", soma)

nomes = []
for i in range(3):
 nome = input("digite um nome:")
 nomes.append(nome)

alunos = {"joao": 8.5, "maria":9.0}
nome = input("nome do aluno:")
print("nota:", alunos.get(nome, "aluno não encontrado"))

idade = int(input("idade:"))
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

soma = 0
for i in range(1, 6):
    soma += i
print("soma total:", soma)

nomes = []
for i in range(3):
    nome = input("digite um nome")
    nomes.append(nome)

alunos = {"joao": 8.5, "maria": 9.0}
nome = input("nopme do aluno:")
print("nota", alunos.get(nome, "aluno não encontrado"))

idade = int(input(idade))
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

soma = 0 
for i in range(1,6):
    soma+= i
print("soma total:", soma)

nomes = []
for i in range(3):
    nome = input("digite um nome:")
    nomes.append(nome)

idade = int(input("idade:"))
if idade>= 18 :
    print("maior de idade")
else:
    print("menor de idade")

soma = 0 
for i in range(1, 6):
    soma += i
print("soma total:", soma)

#-----------------------------------------------

clientes = {}

while True:
    print("1 - cadastrar cliente")
    print("2 - registrar compra")
    print("3 - listar clientes")
    print("4- ver compras de um cliente")
    print("5 - sair")

    opcao = ("escolha:")
    
    if opcao == "1":
        nome = input("nome")
        idade = int(input("idade:"))
        email = input("email:")
        clientes[nome] = {"idade": idade, "email": email, "compras":[]}
    
    elif opcao == "2":
        nome = input("nome do cliente:")
        if nome in clientes:
            compra = input("descriçao da compra:")
            clientes[nome]["compras"].append(compra)
        else:
            print("cliente não encontrado.")

    elif opcao == "3":
        for nome in clientes:
            print(f"{nome} ({clientes[nome]["idade"]} anos) - ({clientes[nome]["email"]})")
    
    elif opcao == "2":
        nome = input("nome do clientes:")
        if nome in clientes:
            compra = input("descrição da compra:")
            clientes[nome]["compra"].append(compra)
        else:
            print("cliente não encontrado")

    elif opcao == "":
       nome = input("nome do cliente:")
       if nome in clientes:
           print("compras:", clientes[nome]["compras"])
       else:
           print("cliente não encontrado.")

    elif opcao == "5":
        break
    else:
        print("opcão invalida")

clientes = {}

while True:
    print("1 - cadastrar clientes")
    print("2 - registrar compra")
    print("3 - listar clientes")
    print("4 - ver compras de um cliente")
    print("5 - sair")

    opcao = input("escolha:")

    if opcao == "1":
        nome = input("nome:")
        idade = int(input("idade:"))
        email = input("email:")
        clientes[nome] = {"idade": idade, "email": email, "compras": []}

    elif opcao == "2":
        nome = input("nome do cliente:")
        if nome in clientes:
            compra = input("descrição da compra:")
            clientes[nome]["compras".append(compra)]
        else:
            print("cliente não encontrado.")

    elif opcao == "3":
        for nome in clientes:
            print(f"{nome} ({clientes[nome]["idade"]} anos) - ({clientes[nome]["email"]})")
    elif opcao == "4":
        nome = input("nome do cliente:")
        if nome in clientes:
            print("compra:", clientes[nome]["compras"])
        else:
            print("clientes não encontrado.")
    elif opcao == "5":
        break
    else:
      print("opcao invalida.")

clientes = {}

while True:
    print("1 - cadastrar cliente")
    print("2 - registrar compra")
    print("3 - listar clientes")
    print("4 - ver compras de um cliente")
    print("5 - sair")

    opcao = input("escolha:")

    if opcao == "1":
        nome = input("nome:")
        idade = int(input("idade:"))
        email = input("email:")
        clientes[nome] = {"idade": idade, "email": email, "compras": []}

    elif opcao == "2":
        nome = input("nome de cliente:")
        idade = int(input("idade:"))
        email = input("email:")
        clientes[nome] = {"idade": idade, "email":email, "compra":[]}

    elif opcao == "2":
        nome = input("nome do cliente")
        if nome in clientes:
            compra = input("descriçao da compra:")
            clientes[nome]["compra"].append(compra)
        else:
            print("cliente não encontrado.")

    elif opcao == "5":
        break
    else:
        print("opcao invalida.")

clientes = {}

while True:
    print("1 - cadastrar clientes")
    print("2 - registrar compra")
    print("3 - listar clientes")
    print("4 - ver compras de um cliente")
    print("5 - sair")

    opcao = input("escolha:")

    if opcao == "1":
        nome = input("nome:")
        idade = int(input("idade:"))
        email = input("email:")
        clientes[nome] = {"idade": idade, "email": email, "compras": []}

    elif opcao == "2":
        nome = input("nome do cliente:")
        if nome in clientes:
            compra = input("descriçao da compra:")
            clientes[nome]["compras"].append(compra)
        else:
            print("cliente não encontrado.")

    elif opcao == "3":
        for nome in clientes:
            print(f"{nome} ({clientes[nome]["idade"]} anos) - {clientes[nome]["email"]}")

    elif opcao == "4":
        nome = input("nome do cliente:")
        if nome in clientes:
            print("compra:", clientes[nome]["compras"])
        else:
            print("cliente não encontrado.")

    elif opcao == "5":
        break
    else:
        print("opcao invalida.")

    
clientes = {}

while True:
    print("1 - cadastrar clientes")
    print("2 - registrar compra")
    print("3 - listar clientes")
    print("4 - ver compras de im cliente")
    print("5 - sair")

    opcao = input("escolha:")

    if opcao == "1":
        nome = input("nome:")
        idade = int(input("idade:"))
        email = input("email:")
        clientes[nome] = {"idade": idade, "email": email, "compras": []}

    elif opcao == "2":
        nome = input("nome do cliente:")
        if nome in clientes:
            compra = input("descricao da compra:")
            clientes[nome]["compras"].append(compra)
        else:
            print("cliente não encontrado.")

    elif opcao == "3":
        for nome in clientes:
            print(f"{nome} ({clientes[nome]["idade"]} anos) - {clientes[nome]["email"]}")
    elif opcao == "4":
        nome = input("nome do cliente:")
        if nome in clientes:
            print("compra:", clientes[nome]["compras"])
        else:
            print("cliente não encontrado") 
    elif opcao == "5":
        break
    else:
        print("opcao ivalida.")
          

def saudacao():
    print("ola! bem-vindo ao python")
    saudacao()

def ola(nome):
    print(f"ola´, {nome}")
ola("maria")

def somar (a, b):
    return a + b
resultado = somar(5,3)
print("resultado:", resultado)
 
def saudacao():
    print("ola, bem vindo ao python")
saudacao()

def ola(nome):
    print(f"ola, {nome}!")
ola("maria")

def somar(a, b):
    return a + b
resulta = somar(5, 3)
print("resultado:", resultado)

def saudacao():
    print("ola, bem-vindo ao python")
saudacao()

def ola(nome):
    print(f"ola, {nome}")
ola("maria")

def somar(a, b):
    return a + b
resultado = somar(5,3)
print("resultado", resultado)

def saudacao():
    print("ola bem-vindo ao python")
saudacao()

def ola(nome):
    print(f"ola, {nome}")
ola("maria")

def somar(a,b):
    return a+b
resultado = somar(5,3)
print("resultado:", resultado)

def saudacao():
    print("ola bem-vindo ao python")
saudacao()

def ola(nome):
    print(f"olá, {nome}")
ola("maria")

def somar(a,b):
    return a + b
resultado = somar(5, 3)
print("resultado:", resultado)

def saudacao():
    print("ola bem-vindo ao python")
saudacao()

def ola(nome):
    print(f"ola, {nome}")
ola("maria")

def somar(a,b):
    return a + b 
resultado = somar(5,3)
print("resultado", resultado)

def saudacao():
    print("ola bem-vinda ao python")
saudacao()

def ola(nome):
    print(f"ola, {nome}")
ola("maria")

def somar(a,b):
    return a + b
resultado = somar(5,3)
print("resultado:", resultado)

def saudacao():
    print("ola bem-vindo ao python")
saudacao()

def ola(nome):
    print(f"ola, {nome}")
ola("maria")

def somar(a,b):
    return a+b
resultado = somar(5,3)
print("resultado:", resultado)

def saudacao():
    print("ola bem-vindo ao python")
saudacao()

def ola(nome):
    print(f"ola", {nome})
ola("maria")

def somar(a,b):
    return a + b
resultado = somar(5, 3)
print("resultado:", resultado)

def saudacao():
    print("ola! bem-vindo ao python")
saudacao()

def ola(nome):
    print(f"ola, {nome}")
ola("maria")

def somar(a, b):
    return a + b
resultado = somar(5, 3)
print("resultado:", resultado)

def saudacao():
    print("ola bem-vindo ao python.")
saudacao()

def ola(nome):
    print(f"ola, {nome}")
ola("maria")

def somar(a,b):
    return a+b
resultado = somar(5,3)
print("resultado:", resultado)

def saudacao():
    print("ola bem-vindo ao python")
saudacao()

def ola(nome):
    print(f"ola, {nome}")
ola("maria")

def somar(a,b):
    return a + b
resultado = somar(5,3)
print("resultado", resultado)

def saudacao():
    print("ola bem-vindo ao python")
saudacao()

def ola(nome):
    print(f"Olá, {nome}!")
ola("maria")

def somar(a,b):
    return a+b
resultado = somar(5,3)
print("resultado:", resultado)

def somar(a , b):
    return a + b 
print(somar(10,20))

def eh_par(n):
    return n % 2 == 0
print(eh_par(4))
print(eh_par(5))

def saudacao():
    print("ola bem-vindo ao python")
saudacao()

def ola(nome):
    print(f"ola, {nome}")
ola("maria")

def somar(a,b):
    return a+b
resultado = somar(5, 3)
print("resultado:", resultado)

def saudacao():
    print("ola bem-vindo ao python.")
saudacao()

def ola(nome):
    print(f"ola, {nome}")
    ola("maria")
def somar(a,b):
    return a+b
resultado = somar(5,3)
print("resultado", resultado)

def saudacao():
    print("ola bemvinda ao python")
saudacao()

def ola(nome):
    print(f"ola, {nome}")
ola("maria")

def somar(a,b):
    return a + b
resultado = somar(5,3)
print("resultado", resultado)

def saudacao():
    print("ola bem vindo ao python")
saudacao()

def ola(nome):
    print(f'ola, {nome}')
ola("maria")

def somar(a, b):
    return (a + b)
resultado = somar(5, 3)
print("resultado", resultado)

#-------------------------------------------------------

def soma(a,b):
    return a + b
print(somar(10,20))

def eh_par(n):
    return n%2 == 0
print(eh_par(4))
print(eh_par(5))

def boas_vindas(nome):
    print(f"seja bem-vindo , {nome}")
boas_vindas("lucas")

def somar(a,b):
    return a + b
print(somar(10, 20))

def eh_par(n):
    return n%2 == 0
print(eh_par(4))
print(eh_par(5))

def boas_vindas(note):
    print(f"seja bem-vindo, {nome}")
boas_vindas("lucas")

def somar(a,b):
    return a + b
print(somar(10,20))

def eh_par(n):
    return n%2 == 0
print(eh_par(4))
print(eh_par(5))

def boas_vindas(nome):
    print(f"seja bem-vindo, {nome}")
boas_vindas("lucas")

def somar(a,b):
    return a + b
print(somar(10,20))

def eh_par(n):
    return n%2 == 0
print((eh_par(4)))
print(eh_par(5))

def boas_vindas(nome):
    print(f"seja bem-vindo, {nome}")
boas_vindas("lucas")

def somar(a,b):
    return a + b
print(somar(10,20))

def eh_par(n):
    return n%2 == 0
print(eh_par(4))
print(eh_par(5))

def boas_vindas(nome):
    print(f"seja bem vindo, {nome}")
boas_vindas("lucas")

def somar (a,b):
    return a + b
print(somar(10,20))

def eh_par(n):
    return n%2 == 0
print(eh_par(4))
print(eh_par(5))

def boas_vindas(nome):
    print(f"seja bem-vindo, {nome}")
boas_vindas("lucas")

def somar(a,b):
    return a + b
print(somar(10,20))

def eh_par(n):
    return n%2 == 0
print(eh_par(4))
print(eh_par(5))

def boas_vindas(nome):
    print(f"seja bem-vindo, {nome}")
boas_vindas("lucas")

def somar(a,b):
    return a + b
print(somar(10,20))

def eh_par(n):
    return n%2 == 0
print(eh_par(4))
print(eh_par(5))

def boas_vindas(nome):
    print(f"seja bem-vindo, {nome}")
boas_vindas("lucas")

def somar(a,b):
    return a + b 
print(somar(10,20))

def eh_par(n):
    return n%2 == 0
print(eh_par(4))
print(eh_par(5))

def boas_vindas(nome):
    print(f"seja bem-vindo, {nome}")
boas_vindas("lucas")

def somar(a,b):
    return a + b
print(somar(10,20))

def eh_par(n):
    return n%2 ==0
print(eh_par(4))
print(eh_par(5))

def boas_vindas(nome):
    print(f"seja bemvindo, {nome}")
boas_vindas('lucas')

#--------------------------------------------------------

def media(n1,n2,n3):
    return (n1+n2+n3) / 3

def tabuada(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

def cortar_vogais(palavras):
    vogais = "aeiou"
    cont = 0
    for letra in palavras.lower():
        if letra in vogais:
            cont += 1
    return cont

def senha_forte(senha):
    return len(senha) >= 8 and any(c.isdigit() for c in senha) and any(c.isupper() for c in senha)
print(senha_forte("python123"))

def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def media(n1,n2,n3):
    return (n1,n2,n3) / 3

def tabuada(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

def contar_vogais(palavra):
    vogais = "aeiou"
    cont = 0
    for letra in palavra.lower():
        if letra in vogais:
            cont += 1
    return cont

def contar_vogais(palavra):
    vogais = "aeiou"
    cont = 0
    for letra in vogais:
        cont += 1
    return cont

def media(n1,n2,n3):
    return(n1+n2+n3) / 3

def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def contar_vogais(palavra):
    vogais = "aeiou"
    cont = 0
    for letra in palavra.lower():
        if letra in vogais:
                cont += i
    return cont

def media(n1,n2,n3):
    return(n1,n2,n3) / 3

def tabuada(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

def media (n1,n2,n3):
    return(n1+n2+n3) / 3

def tabuada(n):
    for i in range(1,11):
        print(f"{n}x{i} = {n*i}")

def media(n1,n2,n3):
    return(n1+n2+n3) / 3

def media(n1,n2,n3):
    return(n1+n2+n3) / 3

def tabuada(n):
    for i in range(1, 11):
        print(f"{n}x{i} = {n*i}")

def senha_forte(senha):
    tem_8_digitos = len(senha) >=8
    tem_numero = any(c.isdigit() for c in senha)
    tem_maiuscula = any(c.isupper() for c in senha)
    return tem_8_digitos and tem_numero and tem_maiuscula
print(senha_forte("python123"))
print(senha_forte("python"))
print(senha_forte("py123"))
print(senha_forte("PYTHON123"))

def senha_forte(senha):
    print("tamanho suficiente:", len(senha) >= 8)
    print("contem numero:", any(c.isdigit() for c in senha))
    print("contem letra maiuscula", any(c.isupper() for c in senha))
    return len(senha) >= 8 and any(c.isdigit() for c in senha) and any(c.isupper() for c in senha)
senha_forte("abc123")

def senha_forte(senha):
    tem_8_digitos = len(senha) >= 8
    tem_numero = any(c.isdigit() for c in senha)
    tem_maiscula = any(c.isupper() for c in senha)
    return tem_8_digitos and tem_numero and tem_maiscula
print(senha_forte("Python123"))
print(senha_forte("python"))
print(senha_forte("py123"))
print(senha_forte("PYTHON123"))

def senha_forte(senha):
    print("tamanho suficiente:", len(senha) >= 8)
    print("contem numero:", any(c.isdigit() for c in senha))
    print("contem letra maiscula:", any(c.isupper() for c in senha))
    return(len(senha) >= 8 and any(c.isdigit() for c in senha) and any(c.isupper() for c in senha))

def senha_forte(senha):
    tem_8_digitos = len(senha) >= 8
    tem_numero = any(c.isdigit() for c in senha)
    tem_maiuscula = any(c.isupper() for c in senha)
    return tem_8_digitos and tem_numero and tem_maiuscula
print(senha_forte("Python123"))
print(senha_forte("python"))
print(senha_forte("py123"))
print(senha_forte("PYTHON123"))

def senha_forte(senha):
    print("tamanho suficiente", len(senha) >= 8)
    print("contem numero:", any(c.isdigit() for c in senha))
    print("conteud letra maiuscula:", any(c.isupper() for c in senha))
    return ( len(senha) >= 8 and any(c.isdigit() for c in senha) and any(c.isupper() for c in senha))
senha_forte("abc123")

def senha_forte(senha):
    print("tamanho sufuciente", len(senha) >= 8)
    print("contem numero:", any(c.isdigit() for c in senha))
    print("contem letra maiscula:", any(c.isupper() for c in senha))
    return len(senha) >= 8 and any(c.isdigit() for c in senha) and any(c.isupper() for c in senha)

senha_forte("abc123")

def senha_forte(senha):
    print("tamanho suficiente", len(senha) >= 8)
    print("contem numero", any(c.isdigit() for c in senha))
    print("contem letra maiscula:", any(c.isupper() for c in senha))
    return(len(senha) >= 8 and any(c.isdigit() for c in senha) and any(c.isupper() for c in senha))
senha_forte("abc123")

def somar(a,b): return a + b
def subtrair(a,b): return a - b
def multiplicar(a,b): return a * b 
def dividir( a ,b): 
    if b == 0: 
     return "erro: divisao por zero"
     return a / b


while True:
    print("1 - somar")
    print("2 - subtrair")
    print("3 - multiplicar")
    print("4 - dividir")
    print("5 - sair")
    op = input("escolha:")

    if op == "5":
        break

    n1 = float(input("numero 1: "))
    n2 = float(input("numero 2:"))

    if op == "1":
        print("resultados", somar(n1, n2))
    elif op == "2":
        print("resultado", subtrair(n1,n2))
    elif op == "3":
       print("resultado", multiplicar(n1,n2))
    elif op == "4":
        print("resultado", dividir(n1,n2))
    else:
        print("opção invalida") 


def somar(a, b): return a + b
def subtrair(a,b): return a - b
def multiplicar(a,b): return a*b 
def dividir(a, b):
    if b == 0:
        return "erro: divisao por zero"
    return a / b 

while True:
    print("1 - somar")
    print("2 - subtrair")
    print("3 - multiplicar")
    print("4 - sividir")
    print("5 - sair")
    op = input("escolha:")

    if op == "5":
        break

    n1 = float(input("numero 1:"))
    n2 = float(input("numero 2:"))

    if op == "1":
        print("resultado:", somar(n1, n2))
    elif op == "2":
        print("resultado", subtrair(n1,n2))
    elif op == "3":
        print("resultado", multiplicar(n1,n2))
    elif op == "4":
        print("resultado:", dividir(n1,n2))
    else:
        print("opcao invalida.")

def contar_vogais(palavra):
    vogais = "aeiou"
    cont = 0
    for letra in palavra.lower():
        if letra in vogais:
            cont += 1
    return cont

def contar_vogais(palavra):
    vogais = "aeiou"
    cont = 0
    for letra in palavra.lower():
        if letra in vogais:
            cont += 1
    return cont

def senha_forte(senha):
    tem_8_digitos = len(senha) >=8
    tem_numero = any(c.isdigit() for c in senha)
    tem_maiscula = any(c.isupper() for c in senha)
    return tem_8_digitos and tem_numero and tem_maiscula
print(senha_forte("python123"))
print(senha_forte("python"))
print(senha_forte("py123"))
print(senha_forte("PYTHON123"))
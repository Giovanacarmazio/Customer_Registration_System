matriz = [["nome", 0, "CPF"], ["nome", 0, "CPF"]]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if coluna == 0:
            matriz[linha][coluna] = input("digite o nome do usuario: ")
        elif coluna == 1:
            matriz[linha][coluna] = input("digite a idade: ")
        else:
            matriz[linha][coluna] = input("digite o CPF: ")

arq = open("loja.txt", "w")
print("-"*40, file=arq)
print("|Nome\t|Idade\t|CEP\t|", file=arq)

arq.close()
arq = open("loja.txt", "a")
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print("|", end="", file=arq)
        print(matriz[linha][coluna], end="\t", file=arq)
    print("|", file=arq)

print("-"*40, file=arq)
arq.close()

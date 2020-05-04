frase = "1      4 Cafe com leite"
codigo, produto = frase.split("      ", 1)
quantidade, produto = produto.split(" ", 1)

print(codigo)
print(quantidade)
print(produto)

soma = int(quantidade) + int(codigo)

print(soma)
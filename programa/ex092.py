from datetime import datetime

pessoa = {}

pessoa['nome'] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
idade = datetime.now().year - nasc
pessoa['idade'] = idade
pessoa['carteira de trabalho'] = int(input("Carteira de trabalho: "))

if pessoa['carteira de trabalho'] != 0:
    pessoa['ano de contratacao'] = int(input("Ano de contratacao: "))
    pessoa['salario'] = int(input("Salario: "))

print("-="*30)
for k, v in pessoa.items():
    print(f'{k}: {v}')


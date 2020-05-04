aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]} '))

if aluno['média'] >= 7:
    aluno['situacao'] = "aprovado"
else:
    aluno['situacao'] = "reprovado"

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

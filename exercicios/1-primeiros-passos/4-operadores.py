ano_nascimento = 1989
ano_formatura = 2024
ano_atual = 2024

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
#print(ano_formatura - ano_nascimento)

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print("Ano formatura > Ano Nascimento? ", ano_formatura > ano_nascimento)
print("Ano formatura < Ano Nascimento? ", ano_formatura < ano_nascimento)
print("Ano formatura <= Ano Nascimento? ", ano_formatura <= ano_nascimento)
print("Ano formatura = Ano Nascimento? ", ano_formatura == ano_nascimento)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print(bool(ano_formatura < ano_nascimento))
print(bool(ano_formatura < ano_nascimento or ano_formatura == ano_atual))
print(bool((ano_formatura > ano_nascimento) and (ano_formatura == ano_atual)))
print(bool(ano_formatura < ano_nascimento and ano_formatura == ano_atual))

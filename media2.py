# Programa para calcular a média de um aluno

print("=== SISTEMA DE NOTAS ===")

# Entrada de dados
nome = input("Digite o nome do aluno: ")
disciplina = input("Digite o nome da disciplina: ")

av1 = float(input("Digite a nota da AV1: "))
av2 = float(input("Digite a nota da AV2: "))
av3 = float(input("Digite a nota da AV3: "))

# Cálculo da média
media = (av1 + av2 + av3) / 3

# Verificação da situação
if media >= 7:
    situacao = "APROVADO"
elif media >= 4:
    situacao = "PROVA FINAL"
else:
    situacao = "REPROVADO"  

# Exibição dos resultados
print("\n=== RESULTADOS ===")
print(f"Aluno: {nome}")
print(f"Disciplina: {disciplina}")
print(f"AV1: {av1:.2f}")
print(f"AV2: {av2:.2f}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
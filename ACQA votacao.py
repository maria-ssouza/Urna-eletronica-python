# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

# Inicialização das variáveis para contar os votos de cada candidato, nulos e em branco
votos_rogerio = 0
votos_marcus = 0
votos_fernanda = 0
votos_alice = 0
votos_nulos = 0
votos_branco = 0
total_votos = 0  # Conta o total de votos válidos, nulos e em branco

# Exibe a tabela de códigos para o usuário
print("Códigos de votação:")
print("1 - Rogério")
print("2 - Marcus")
print("3 - Fernanda")
print("4 - Alice")
print("5 - Nulo")
print("6 - Branco")
print("0 - Encerrar votação")

# Loop para receber os votos até que o usuário digite 0
while True:
    voto = int(input("Digite o número do candidato: "))
    if voto == 0:
        break  # Encerra a votação
    elif voto == 1:
        votos_rogerio += 1  # Adiciona um voto para Rogério
    elif voto == 2:
        votos_marcus += 1   # Adiciona um voto para Marcus
    elif voto == 3:
        votos_fernanda += 1 # Adiciona um voto para Fernanda
    elif voto == 4:
        votos_alice += 1    # Adiciona um voto para Alice
    elif voto == 5:
        votos_nulos += 1    # Adiciona um voto nulo
    elif voto == 6:
        votos_branco += 1   # Adiciona um voto em branco
    else:
        print("Código inválido! Tente novamente.")  # Caso o código não exista
        continue  # Volta para o início do loop sem contar o voto
    total_votos += 1  # Soma 1 ao total de votos

# Calcula as porcentagens de votos nulos e em branco, se houver votos
if total_votos > 0:
    perc_nulos = (votos_nulos / total_votos) * 100
    perc_branco = (votos_branco / total_votos) * 100
else:
    perc_nulos = perc_branco = 0

# Cria um dicionário para facilitar a identificação do vencedor
candidatos = {
    "Rogério": votos_rogerio,
    "Marcus": votos_marcus,
    "Fernanda": votos_fernanda,
    "Alice": votos_alice
}
# O vencedor é o candidato com maior número de votos
vencedor = max(candidatos, key=candidatos.get)
votos_vencedor = candidatos[vencedor]
perc_vencedor = (votos_vencedor / total_votos) * 100 if total_votos > 0 else 0

# Exibe o resultado final da eleição
print("\nRESULTADO DA ELEIÇÃO:")
print(f"Total de votos para Rogério: {votos_rogerio}")
print(f"Total de votos para Marcus: {votos_marcus}")
print(f"Total de votos para Fernanda: {votos_fernanda}")
print(f"Total de votos para Alice: {votos_alice}")
print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_branco}")
print(f"Percentual de votos nulos: {perc_nulos:.2f}%")
print(f"Percentual de votos em branco: {perc_branco:.2f}%")
print(f"O candidato vencedor foi: {vencedor}")
print(f"Percentual de votos do vencedor: {perc_vencedor:.2f}%")
input("\nPressione Enter para encerrar...")
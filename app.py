# Coleta as informações do usuário
nome_aparelho = input("Digite o nome do aparelho (ex.: Geladeira): ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# Calcule o consumo mensal em kWh
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Exibe o resultado formatado
print("-" * 40)
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")

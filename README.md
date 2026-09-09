# Calculadora de Consumo de Energia Elétrica 

Este é um programa simples em Python desenvolvido para calcular o consumo mensal estimado de energia elétrica (em kWh) de um determinado eletrodoméstico ou aparelho eletrônico.

# Funcionalidades

- **Coleta de Dados**: Solicita o nome do aparelho, a potência em watts (W) e a média de horas de uso diário.
- **Cálculo Automático**: Aplica a fórmula padronizada para calcular o consumo mensal em quilowatts-hora (kWh).
- **Exibição Formatada**: Exibe os resultados organizados de forma limpa e com arredondamento para duas casas decimais.

#Fórmula Utilizada
O consumo mensal é calculado utilizando a seguinte equação:
consumo_mensal = (potencia * horas_dia * 30) / 1000

#Como Executar o Programa
1. baixe o repositório** para a sua máquina local.
2. Abra o terminal ou prompt de comando na pasta onde o arquivo `.py` está salvo.
3. Execute o programa digitando:

# Exemplo
Digite o nome do aparelho (ex.: Geladeira): Geladeira
Digite a potência do aparelho em watts (W): 150
Digite o tempo médio de uso diário em horas: 24
----------------------------------------
Aparelho: Geladeira
Consumo estimado: 108.00 kWh/mês
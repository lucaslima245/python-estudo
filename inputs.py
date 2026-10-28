faturamento = float(input("preencha o faturamento"))

faturamento = faturamento.replace(",",".")
faturamento = float(faturamento)

custo = 600

lucro = faturamento - custo
print(lucro)



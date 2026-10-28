email = "EMAILFALSO@GMAIL.COM"

print(len(email)) #mostra o tanto de caracteres

posicao = email.find("@") #mostra posicao do caractere
print(posicao)

print(email[0:8]) #mostra o caractere

print(email[0:posicao]) #do comeco ate a posicao do  @


#formatacao numerica

faturamento = 1_000_000
custo = 600
lucro = faturamento - custo
margem = lucro / faturamento



texto = f"o lucro foi de RS{lucro:,.2f} e o faturamento foi de RS{faturamento:,}"

print(texto)
print(f"a margem e {margem:.1%}")
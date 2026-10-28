email = "EMAILFALSO@GMAIL.COM"

print(len(email)) #mostra o tanto de caracteres

posicao = email.find("@") #mostra posicao do caractere
print(posicao)

print(email[0:8]) #mostra o caractere

print(email[0:posicao]) #do comeco ate a posicao do  @
    #Calculo de idade



#input usuario    
try:
    Ano_nasceu =  int(input("Digite sua data de nascimento: "))
    Ano_atual = int(input("Digite o ano atual: "))
except ValueError:
    print("Valor inválido, digite um número inteiro.")
    exit()

#Processamento da idade

Idade = (Ano_atual - Ano_nasceu)

print("Sua idade é: " , Idade , "anos.")





#Processamento da idade

Idade = (Ano_atual - Ano_nasceu)

print("Sua idade é: " , Idade , "anos.")


#Verificação se é maior ou menor de idade
if (Idade>18):
    print("Você é maior de idade.")


elif (Idade<18):
    print("Você é menor de idade.")

else:
    print("Você tem exatamente 18 anos.")
    
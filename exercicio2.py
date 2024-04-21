letra = input("Insira o sexo 'F'   OU   'M'")

if letra == "F":
    sexo = "feminino"
elif letra == "M":
    sexo = "masculino"
else: 
    sexo = "inválido"

print(f"O sexo digitado foi {sexo}")
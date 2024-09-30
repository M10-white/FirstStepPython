first_name = input('Votre Prénom ? ')
last_name = input('Votre Nom ? ')

age = int(input('Ton age ? '))
print('Bonjour', first_name, last_name, ', tu as ', age, ' ans !')

if age >= 18 :
    status = input("Tu es Majeur")
else:
    status = input("Tu es Mineur")

print("Récapitulons :")
report = [first_name, last_name, str(age) + ' ans', status]
i = 0
while i < len(report):
    print(report[i])
    i += 1
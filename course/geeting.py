first_name = input('Votre Prénom ? ')
last_name = input('Votre Nom ? ')

age = int(input('Ton age ? '))
print('Bonjour', first_name, last_name, ', tu as ', age, ' ans !')

if age >= 18 :
    print("Tu es Majeur")
else:
    print("Tu es Mineur")
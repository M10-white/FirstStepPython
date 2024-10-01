first_name = input('Votre Prénom ? ')
last_name = input('Votre Nom ? ')

age = int(input('Ton age ? '))
print('Bonjour', first_name, last_name, ', tu as ', age, ' ans !')

if age >= 18 :
    status = input("Tu es Majeur")
else:
    status = input("Tu es Mineur")

input("Récapitulons :")
report = [first_name, last_name, str(age) + ' ans', status]
i = 0
while i < len(report):
    print(report[i])
    i += 1

user = {
   "first_name": "John",
   "last_name": "Doe",
   "age": str(20) + ' ans',
   "email" : "john.doe@yahoo.fr"
}  
input('Je me présente:')
for val in user.values():

    print(val)
user['age'] = str(3250) + ' ans'
input('Oups ...')
input('J\'ai fait une erreur ...')
for val in user.values():

    print(val)
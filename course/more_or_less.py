import random
secret = random.randint(0,100)

difficulty = int(input('Choisir une difficulté: 1-Facile  2-Moyen  3-Difficile '))
max = 100

if difficulty == 1:
    max = 10 
elif difficulty == 2:
    max = 100
else:
    max = 1000

secret = random.randint(0,max)
user_number = int(input(f'Veuillez entrer un nombre entre 0 et {max}: '))
attempts = 1
while secret != user_number:
    if secret < user_number:
        print('C\'est plus petit')
    else:
        print('C\'est plus grand')
    
    user_number = int(input(f'Veuillez entrer un nombre entre 0 et {max}: '))
    attempts = attempts + 1

print(f'Bravo, vous avez trouvé le nombre secret {secret} en {attempts} essais ! ')
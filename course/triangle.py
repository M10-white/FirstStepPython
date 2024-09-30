first_side = float(input('Veuillez entrer la longueur du premier côté : '))
second_side = float(input('Veuillez entrer la longueur du second côté : '))
third_side = float(input('Veuillez entrer la longueur du troisième côté : '))

if first_side == second_side == third_side:
    print('Le triangle est équilatéral')
elif first_side == second_side or first_side == second_side or second_side == third_side:
    print('Le triangle est isocèle')
else:
    print ('Le triangle est quelconque')
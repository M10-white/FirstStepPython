nb_to_en = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}

result = ""

print("Entrez un numéro de téléphone : ")
phone_number = input(">>> ")
for nb in phone_number :
    result += nb_to_en.get(nb, '[Caractère non mappé]') + " "

print(result)
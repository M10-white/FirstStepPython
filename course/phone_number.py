fr_to_en = {
"chat" : "cat",
"chien" : "dog",
"oiseau" : "bird"
}

word_fr = input("Entrez un mot en français : ")
if word_fr in fr_to_en.keys() :
    print(f"Traduction : {fr_to_en[word_fr]}")
else :
    print("Traduction non disponible")
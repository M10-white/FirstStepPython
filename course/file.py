oceans = [
   "Southern",
   "Artic"
]
with open("file.txt", "a") as f:
   for ocean in oceans :
     f.write(ocean)
     f.write("\n")

f = open("file.txt", "r")

print(f.read())

f.close()
#/usr/bin/python3

'''Votre programme prend en entrée une chaine de caractère. Il devra effectuer des opérations sur cette dernière à partir d'une clé qui est "robinson c'est le meilleur"

Explication technique : si la chaine est inférieure à la clé, alors on réduit la clé pour qu'elle ait le bon nombre de
caractères (ex : chaine: "bjr" donc clé: "rob") si elle est trop longue on recommence au début de
la clé (ex : chaine: "...truc avant" donc "...robinson c". Les opérations seront d'abord une converstiob en ET binaire
et ensuite en XOR. Il faudra donner le résultat sous forme d'une chaine de caractères. (pas 00100 mais ajdh3r)

vous devrez vérifier que votre valeur finale soit < ou = à 32  si c'est le cas alors vous lui ajoutée 32. 
Si elle est égale à 127 vous lui enlevée 2 et si elle est entre 32 et 126 alors vous ne changez rien.'''

final_result = ""
key = "robinson c'est le meilleur"
usr = input("Enter text : ")

if len(usr) < len(key):
  key = key[:len(usr)]
else:
  for i in range(len(usr)):
    key += key[i]
  key = key[26:len(key)] # 26 -> key's len

for _ in range(len(key)):
    and_result = ""
    # AND comparaison bin_usr & key
    bin_key = "0" + "".join(format(ord(key[_]), "b"))
    bin_usr = "0" + "".join(format(ord(usr[_]), "b"))
    if len(bin_key) == 7:
        bin_key = "0" + bin_key
    if len(bin_usr) == 7:
        bin_usr = "0" + bin_usr
    for x in range(8): # len(bin_...)
        if int(bin_key[x]) + int(bin_usr[x]) > 1:
            and_result += "1"
        else:
            and_result += "0"

    # XOR comparaison AND(bin_usr & bin_key) & bin_key
    xor_result = ""
    for i in range(8):
        if (and_result[i] == "0" and bin_key[i] == "0") or (and_result[i] == "1" and bin_key[i] == "1"):
            xor_result += "0"
        else:
            xor_result += "1"

    xor_result = int(xor_result, 2)

    if xor_result <= 33:
        xor_result += 33
    elif xor_result == 127:
        xor_result -= 2

    final_result += chr(xor_result)

print("Result     : " + final_result)

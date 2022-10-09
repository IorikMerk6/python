#Famil = input("Фамилия:").capitalize()
#name = input("Имя:").capitalize()
#otchestvo = input("Отчество:").capitalize()
#print (Famil, name[0] + ".", otchestvo[0] + ".")
#print (f"{Famil} {name[0]}. {otchestvo[0]}.")
#lst = x.split(",")
#lst.pop(0)
#print(lst)
#hrase = input("VVedite frazy")
#find = input("Find")
#replace = input("Replace")
#print(hrase.replace(find , replace))
#phrase = input("Vvedite frazy:")
#print(phrase.replace("йо", "ё"))
#alphabet = {
 ##    "а": "Су-25",
 #   "б": "Су-34",
 #   "в": "Миг-29",
 #   "г": "Су-24",
 #   "д": "Миг-31",

#}
#x = input("Введи фразу для транслитика")
#rus = ""
#for letter in x:
  #  rus = rus + alphabet[letter]
#priemailnt(rus)
email = input("Введите почту:")
login = email.split("@")[0]
Domen = email.split("@")[1]
print("Логин: ", login)
print("Доman: ", Domen)
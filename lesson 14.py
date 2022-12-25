#d1 = {"Антон","Антон","ы"}
#print(d1)
#d1.pop
#print(d1)
#phrase = "Маша, а ты где?Маша загорает, а за ней едет мама Маша".lower()
#nigger = list("!,.?")
#phrase_cleared = ""
#d = {}
#for azerbaidjan in phrase:
#    if azerbaidjan not in nigger:
#        phrase_cleared += azerbaidjan
#print(phrase_cleared)
#l = phrase_cleared.split(" ")
#print(l)
#for kakish in l:
#    if kakish not in d:
#        d[kakish] = 1
  #  else:
  #      d[kakish] += 1
#print(d)
#ass = 0
#d = {"Хлеб": 1000,
   # "Молоко дочи милк" : 1.5,
  #  "Сырок БЮ Саня" : 47,
 #   "БМП 1" : 12000,
 #    }
 #3

# phrase = "Маша, а ты где?Маша загорает, а за ней едет мама Маша".lower()
# nigger = list("!,.?")
# phrase_cleared = ""
# d = {}
# for azerbaidjan in phrase:
#    if azerbaidjan not in nigger:
#        phrase_cleared += azerbaidjan
# print(phrase_cleared)
# l = phrase_cleared.split(" ")
# print(l)
# for kakish in l:
#     if kakish not in d:
#         d[kakish] = 1
#     else:
#         d[kakish] += 1
# print(d)
# maxi = max(d.values())
# for (key, values) in d.items():
#     if values == maxi:
#         print(f"ключ: {key,}, значение {values} ")
# 34
e = {
    "Ключ 1":2,
    "Ключ 2":5,
    6:2,
    ".!.":3,
}

# one = 1
# two = 2
# one, two = two, one
# print(one,two)
e["Ключ 1"], e["Ключ 2"] = e["Ключ 2"], e["Ключ 1"]
print(e["Ключ 1"], e["Ключ 2"])
e["new_key"] = "new_value"
print(e)


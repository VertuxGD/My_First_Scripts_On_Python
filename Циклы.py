num = str(input("Введи слово: "))
for j in num:
    if j == 'a':
        break
    print (j * 2, end = '')
else:
    print()
    print ("Буквы a нету в слове")
a=input()
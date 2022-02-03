l = []
lis = [1, 2, 3, 'x', 3.46, 12.55, ['S', 't', 'r', 'o', 'k', 'a']]
print ("Таблица lis: ")
print (lis)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print ()
print (a)

b = [64, 0]
print ("Таблица b: ")
print ()
print (b)
l.append (12)
l.append (45)
l.extend (b)
l.insert (0, 'Лол')
print ("Таблица l: ")
print ()
print (l)

o=input()

l.remove (45)
print ()
print (l)
l.pop ()

o=input()

print ()
print (l)
print ("Индекс номера 12 в таблице l: ")
print (l.index (12))
print ("Значений 'Лол' в таблице l: ")
print (l.count ('Лол'))
k=[34, 78, 13, 124, 2, 4, 113, 100, 35]
k.sort ()

o=input()

print ("Таблица k: ")
print ()
print (k)
k.reverse ()
print ()
print (k)

o=input()

l.clear ()
print ("Таблица l: ")
print ()
print (l)

o=input()
def func (mounth):
    for i in range (13):
        if i == mounth:
            return "Да, такой месяц есть."
        else:
            continue
    else:
        return "Нет, такого месяца нет."
t = func (int(input('Введите номер месяца: ')))
print (t)
#Классы. Практическое применение

class Castle:
    def __init__ (self, height, length, width, population, name):
       self.height=height
       self.length=length
       self.width=width
       self.population=population
       self.name=name
    def Create_Height (self, height_number):
        self.height+=height_number
    def Create_Length (self, length_number):
        self.length+=length_number
    def Create_Width (self, width_number):
        self.width+=width_number
    def Create_Population (self, population_number):
        self.population+=population_number
    def Create_Name (self, name_of):
         self.name=name_of
    def Create_All (self):
        self.Create_Height (int (input('Введите высоту замка: ')))
        self.Create_Length (int (input('Введите длину замка: ')))
        self.Create_Width (int (input('Введите ширину замка: ')))
        self.Create_Population (int (input('Введите население замка: ')))
        self.Create_Name (input('Введите имя замка: '))

Castle_1=Castle (0, 0, 0, 0, '')
Castle_2=Castle (0, 0, 0, 0, '')

#Как не надо:
#Castle_1.Create_Height (int (input('Введите высоту замка: ')))
#Castle_1.Create_Length (int (input('Введите длину замка: ')))
#Castle_1.Create_Width (int (input('Введите ширину замка: ')))
#Castle_1.Create_Population (int (input('Введите население замка: ')))
#Castle_1.Create_Name (input('Введите имя замка: '))

#Как надо:
Castle_1.Create_All ()

print ('Параметры замка ',Castle_1.name, ': ', Castle_1.height, Castle_1.length, Castle_1.width, Castle_1.population)
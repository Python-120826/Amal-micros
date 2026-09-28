class Animal:
    def init(self, name):
        self.name = name
class Bird(Animal):
    def init(self, name, color,obitanie,razmah, food):
        super().init(name)
        self.color = color
        self.obitanie = obitanie
        self.razmah = razmah
        self.food = food
class Mlekopitayushee(Animal):
    def init(self, name, color,obitanie, razmer, food):
        super().init(name)
        self.color = color
        self.obitanie = obitanie
        self.razmer = razmer
        self.food = food
class Reptiliya(Animal):
    def init(self, name, obitanie,cheshuya, razmer, food):
        super().init(name)
        self.obitanie = obitanie
        self.cheshuya = cheshuya
        self.razmer = razmer
        self.food = food
orel = Bird(Animal)("Орел", "коричневый","лес", "1 метра", "птица")
kuritsa = Bird(Animal)("Курица", "Белый", "Ферма", "5 метра", "зерно")
krisa = Mlekopitayushee(Animal)("Крыса", "Серый", "Города", "Маленький", "Всеядна")
obezyana = Mlekopitayushee(Animal)("Обезьяна", "Коричневый", "Джунгли", "Средний", "Фрукты")
zmeya = Reptiliya(Animal)("Змея", "Пустыня", "Мелкая", "Длинная", "Мыши")
hameleon = Reptiliya(Animal)("Хамелеон", "тропики", "Гладкая", "маленький", "рептилия")
print(orel.name, orel.color, orel.obitanie, orel.razmah, orel.food)
print(kuritsa.name, kuritsa.color, kuritsa.obitanie, kuritsa.razmah, kuritsa.food)
print(krisa.name, krisa.color, krisa.obitanie, krisa.razmer, krisa.food)
print(obezyana.name, obezyana.color, obezyana.obitanie, obezyana.razmer, obezyana.food)
print(zmeya.name, zmeya.obitanie, zmeya.cheshuya, zmeya.razmer, zmeya.food)
print(hameleon.name, hameleon.obitanie, hameleon.cheshuya, hameleon.razmer, hameleon.food)
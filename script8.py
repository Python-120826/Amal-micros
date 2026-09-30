#номер 1 #

class COMPS:
    def init(self, owner, ram , cpu, hdd, gpu):
        self.owner = owner
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
        self.gpu = gpu

def __gt__ (self, other ):
   print (self.ram > other.ram)

pc = COMPS ('behzod', 16, 'i9', 1024, 'rtx 5080')
pc2 = COMPS ('Saif', 2, 'i9', 1024, "RTX 5080")

print(pc.ram > pc2.ram)












#номер 2 #

class Animal:
    pass
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
class fish (Animal):
    def init(self, name, obitanie, color, food):
        super ().init (name)
        self.obitanie = obitanie
        self.color = color
        self.food = food
orel = Bird(Animal)("Орел", "коричневый", "лес", "1 метра", "птица")
kuritsa = Bird(Animal)("Курица", "Белый", "Ферма", "5 метра", "зерно")
krisa = Mlekopitayushee(Animal)("Крыса", "Серый", "Города", "Маленький", "Всеядна")
obezyana = Mlekopitayushee(Animal)("Обезьяна", "Коричневый", "Джунгли", "Средний", "Фрукты")
zmeya = Reptiliya(Animal)("Змея", "Пустыня", "Мелкая", "Длинная", "Мыши")
hameleon = Reptiliya(Animal)("Хамелеон", "тропики", "Гладкая", "маленький", "рептилия")
clown = fish (Animal) (' клоун', ' вода', 'рыжий', 'коралы' )
belaya_shark = fish (Animal) ('белая акула ', 'серо-белый', 'рыбы,тюлени')
print(orel.name, orel.color, orel.obitanie, orel.razmah, orel.food)
print(kuritsa.name, kuritsa.color, kuritsa.obitanie, kuritsa.razmah, kuritsa.food)
print(krisa.name, krisa.color, krisa.obitanie, krisa.razmer, krisa.food)
print(obezyana.name, obezyana.color, obezyana.obitanie, obezyana.razmer, obezyana.food)
print(zmeya.name, zmeya.obitanie, zmeya.cheshuya, zmeya.razmer, zmeya.food)
print(hameleon.name, hameleon.obitanie, hameleon.cheshuya, hameleon.razmer, hameleon.food)
print(clown.name, clown.color,clown.obitanie, clown.color, clown.food)
print(belaya_shark.name, belaya_shark.color,belaya_shark.obitanie, belaya_shark.color, clown.food)


#номер 3 #

class figura:
    def init(self, name):
        self.name = name
        super().init(name)
class treugolnik(figura):
         def init(self, name, a,b,c, P, S):
             super().init(name)
             self.name = name
             self.a = a
             self.b = b
             self.c = c
             self.P = P
             self.S = S
class chetirehgolnik(figura):
    def init(self, name, a,c, P, S):
        super().init(name)
        self.name = name
        self.a = a
        self.c = c
        self.P = P
        self.S = S

class circle(figura):
    def init(self, name,R,P,S):
        super().init(name)
        self.name = name
        self.R = R
        self.P = P
        self.S = S
treugolnik = treugolnik(figura)( 'треугольник' 'a', 'b', 'c', 'P= a+b+c', 'S=(a+b+c):2')
chetirehgolnik = chetirehgolnik(figura)('четырехугольник''a','c', "P = a+c)2", 'S = 1/2 d1 d2')
circle = circle(figura) ('круг', 'R', 'P=c= 2pr', 'S= pr2')
print(treugolnik.name,treugolnik.a,treugolnik.b,treugolnik.c,treugolnik.P,treugolnik.S)
print(chetirehgolnik.name, chetirehgolnik.a,chetirehgolnik.c, chetirehgolnik.P,chetirehgolnik.S)
print(circle.name,circle.R,circle.P,circle.S)

# 6
class Shaxs:
    def __init__(self, ism):
        self.ism = ism

    def salom(self):
        print("Shaxs ismi kiritilmoqda")

class Oqituvchi(Shaxs):
    def __init__(self, ism, fan):
        super().__init__(ism)
        self.fan = fan

    def salom(self):
        super().salom()
        print(f"ismi: {self.ism}")
        print(f"fani: {self.fan}")

s1 = Oqituvchi("Azamat", "IT-Python")
s1.salom()

# 7
class Kitob:
    def __init__(self, nomi):
        self.nomi = nomi

    def info(self):
        print("Kitob nomi")

class Darslik(Kitob):
    def __init__(self, nomi, fan):
        super().__init__(nomi)
        self.fan = fan

    def info(self):
        super().info()
        print(f"darslik nomi: {self.nomi}")
        print(f"fani: {self.fan}")

d1 = Darslik("SQL", "Informatika")
d1.info()

# 8
class Avto:
    def __init__(self, nomi):
        self.nomi = nomi

    def yurish(self):
        print("Avto nomi")

class ElektroAvto(Avto):
    def __init__(self, nomi, quvvat):
        super().__init__(nomi)
        self.quvvat = quvvat
        print(f"nomi: {self.nomi}")
        print(f"quvvat: {self.quvvat}")

e1 = ElektroAvto("L9", "100%")
e1.yurish()

# 9
class Kompyuter:
    def __init__(self, cpu):
        self.cpu = cpu

    def info(self):
        print("cpu yaratilmoqda")

class Noutbuk(Kompyuter):
    def __init__(self, cpu, batareya):
        super().__init__(cpu)
        self.batareya = batareya

    def info(self):
        super().info()
        print(f"cpu: {self.cpu}")
        print(f"batareyasi: {self.batareya}")

n1 = Noutbuk(16, "100%")
n1.info()

# 10
class Oyinchi:
    def __init__(self, ism):
        self.ism = ism

    def info(self):
        print("ismi chiqmoqda")

class ProOyinchi(Oyinchi):
    def __init__(self, ism, reyting):
        super().__init__(ism)
        self.reyting = reyting

    def info(self):
        print(f"ismi: {self.ism}")
        print(f"reytingi: {self.reyting}")

p1 = ProOyinchi("Jamshid", 100)
p1.info()

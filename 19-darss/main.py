class Shaxs:
    def __init__(self, ism, familiya, o_yili, o_tyili):
        self.ism = ism
        self.familiya = familiya
        self.o_yili = o_yili
        self.o_tyili = o_tyili
    def info(self):
        info = f"ism: {self.ism}, familiyasi: {self.familiya}, o_yili: {self.o_yili}, o_tyili: {self.o_tyili}"
        return info

class Talaba(Shaxs):
    def __init__(self, ism, familiya, o_yili, o_tyili, id, manzil, bosqich=1):
        super().__init__(ism, familiya, o_tyili, o_yili)
        self.id = id
        self.bosqich = bosqich
        self.manzil = manzil

    def get_id(self):
        return self.id
    
    def info(self):
        info = f"ism: {self.ism}, familiyasi: {self.familiya}, o_yili: {self.o_yili}, o_tyili: {self.o_tyili}, id raqami: {self.id}"
        return info
    
class Manzil:
    def __init__(self, uy, kocha, shaxar, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.shaxar = shaxar
        self.viloyat = viloyat
        
    def manzil_info(self):
        info = f"{self.viloyat}, {self.shaxar}, {self.kocha}, {self.uy}"
        return info
    
class Til:
    def __init__(self, rus_tili, ingliz_tili):
        self.rus_tili = rus_tili
        self.ingliz_tili = ingliz_tili

t_manzil = Manzil(34, 'amir temur', 'shax', 'fergana')
talaba1 = Talaba('ali', 'aliyev', 1999, 1990, 12, t_manzil)
tili = Til('rus tili', 'ingliz tili')

print(talaba1.info())
print(f"Manzili: {talaba1.manzil.manzil_info()}")
print(f"nechta tilni bilasiz: {tili.rus_tili}")
print(f"nechta tilni bilasiz: {tili.ingliz_tili}")

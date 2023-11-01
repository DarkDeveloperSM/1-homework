class Shaxs: 
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def get_info(self):
        info = f"{self.ism}, {self.familiya} {self.yosh} yosh"
        return info

class Kishi(Shaxs):
    def __init__(self, ism, familiya, yosh, id, bosqich, manzil):
        super().__init__(ism, familiya, yosh)
        self.manzil = manzil
        self.id = id
        self.bosqich = bosqich

    def get_kishi(self):
        info = f"{self.manzil}, {self.id} {self.bosqich}"
        return info
    
class Manzil:
    def __init__(self, uy, kocha, shaxar, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.shaxar = shaxar
        self.viloyat = viloyat
    def manzil_info(self):
         info = f"{self.viloyat} viloyati, {self.shaxar} shaxri, {self.kocha} ko'chasi, {self.uy}-uy"
         return info

t_manzil = Manzil(46, 'turkiston', 'kokand', 'fargona')
shaxs = Kishi('asdfgh', 'asdf', 24, 'asdfg', 46, 12)
print(f"Manzili: {shaxs.manzil.ma}")

print(shaxs.info())

class Mashina:
    def __init__(self, nomi, yili, model):
        self.nomi = nomi
        self.yili = yili
        self.model = model
    def info(self):
        info = f"ism: {self.nomi}, yili: {self.yili}, model: {self.model},"
        return info

class Mashina2:
    def __init__(self, nomi, yili, model, rangi, kompanyasi,yurgan):
        super().__init__(nomi, yili, model)
        self.rangi = rangi
        self.kompanyasi = kompanyasi
        self.yurgan = yurgan
    
class Mashina3:
    def __init__(self, balon, salon, tanirovka):
        self.balon = balon
        self.salon =salon
        self.tanirovka = tanirovka

    def info1(self):
        info1 = f"balon: {self.balon}, salon: {self.salon}, tanirovka: {self.tanirovka}"
        return info1
    
class Mashina4:    
    def __init__(self, yengil_m, ogir_m, katta):
        self.yengil_m = yengil_m
        self.ogir_m = ogir_m
        self.katta = katta

    def info2(self):
        info2 =f"yengil_m: {self.yengil_m}, ogir_m: {self.ogir_m}, katta: {self.katta}"
        return info2

    def get_rangi(self):
        return self.rangi
    def get_kompanyasi(self):
        return self.kompanyasi
    def get_yurgan(self):
        return self.yurgan
    
amal = True

while amal:
    input1 = input('nomini kiriting: ')
    input2 = input('yilini kiriting: ')
    input3 = input('modelini kiriting: ')    
    input4 = input('yana qoshishni xoxlaysizmi xa/yoq: ')

    if input4 == 'yoq':
        amal = False
    else:
        input1 = input('nomini kiriting: ')
        input2 = input('yilini kiriting: ')
        input3 = input('modelini kiriting: ')    
        input4 = input('yana qoshishni xoxlaysizmi xa/yoq: ')

    mashina1 = Mashina(input1, input2, input3 )
    print(mashina1.info())
    
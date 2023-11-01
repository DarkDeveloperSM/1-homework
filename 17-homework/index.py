class Mashina:
    def __init__(self,nomi,yili,rangi, model):
        self.nomi = nomi
        self.yili = yili
        self.rangi = rangi
        self.model = model
    def set_name(self, newism):
        self.nomi = newism
        return self.nomi
    def set_yili(self, newyili):
        self.nomi = newyili
        return self.yili
    def set_rangi(self, newrangi):
        self.nomi = newrangi
        return self.rangi
    def set_model(self, newmodel):
        self.nomi = newmodel
        return self.model
    def fun(self):
        return f"nomi: {self.nomi}, yili: {self.yili}, rangi: {self.rangi}, model: {self.model}"
    
    def get_name(self):
        return self.nomi
    def get_name(self):
        return self.yili
    def get_name(self):
        return self.rangi
    def get_name(self):
        return self.model

mashina1 = Mashina('manlibu', 2023, 'qora', 'premium')
# mashina1.set_name('captiva')
# mashina1.set_yili(2000)
# mashina1.set_rangi('oq')
mashina1.set_model()

print(mashina1.fun())
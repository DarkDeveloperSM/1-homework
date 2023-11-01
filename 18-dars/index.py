class Kitoblar:
    def __init__(self, nomi, yili, yozuvchi, bet):
        self.nomi = nomi
        self.yili = yili
        self.yozuvchi = yozuvchi
        self.bet = bet

    def set_neme(self, new_name):
        self.nomi = new_name
        return self.nomi
    def set_yili(self, new_yili):
        self.yili = new_yili
        return self.yili
    def set_yozuvchi(self, new_yozuvchi):
        self.yozuvchi = new_yozuvchi
        return self.yozuvchi
    def set_bet(self, new_bet):
        self.bet = new_bet
        return self.bet
    
    def kitob1(self):
        return f"nomi: {self.nomi}, yili: {self.yili}, yozuvchi: {self.yozuvchi}, bet: {self.bet}"
    
        
    def get_name(self):
        return self.nomi
    def get_yili(self):
        return self.yili
    def get_yozuvchi(self):
        return self.yozuvchi
    def get_bet(self):
        return self.bet
    
    
kitob = Kitoblar('robert', 2000, 'kiosaki', 300)
kitob.set_neme('hamsa')
kitob.set_yili(200)
kitob.set_yozuvchi('alisher navoiy')
kitob.set_bet(200)
print(kitob.kitob1()) 
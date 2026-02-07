class Hero :
    def __init__(self, nama, hp_awal):
        self.nama = nama
        # Hp ini bersifat private
        self.__hp = hp_awal
        
        # MEMBUAT Getter
    def get_hp (self) :
            return self.__hp
        # MEMBUAT Setter untuk mengubah nilai hp
    def set_hp (self, hp_baru) :
            # if hp_baru < 0 :
            #     self.__hp = 0
            # elif hp_baru >= 1000 :
            #     print("lu nge cheat dongo")
            #     self.__hp =999
            # else :
                self.__hp = hp_baru
                
    def attack (self, damage) :
            sisa_hp = self.get_hp()- damage
            self.set_hp(sisa_hp)
            print(f"{self.nama} terkena serangan {damage} sisa HP : {self.get_hp()}")
            
# -- uji serang --
hero1 = Hero("Gloo",100)

hero1.set_hp(-100)
print(hero1.get_hp())
#print(f"Mencoba akses paksa: {hero1._Hero__hp}")



            
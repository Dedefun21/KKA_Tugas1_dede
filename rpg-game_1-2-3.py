class Hero:
    # constructor akan dijalankan saat Hero baru dibuat
    def __init__(self, name, hp, attack_power,):
        self.name = name # Nama Hero
        self.hp = hp # Nyawa (Health Point)
        self.attack_power = attack_power # Kekuatan Serangan
        
    # pemakaian getter
   
    
    # pemakaian setter
    
    
    
    # method untuk melakukan penyerangan
    def attack(self,lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.damage(self.attack_power)
    # method untuk menerima serangan
    def damage(self, damage,):
        self.hp -= damage
       
        print(f"{self.name} terkena serangan {damage} HP tersisa {self.hp}")

# Method untuk menampilkan info hero
    def kabar(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")
        
#Anak darri kelas Hero
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana,  ):
        # memanggil constuctor dari kelas induk yaitu (Hero)
        super().__init__(name, hp, attack_power, )
        self.mana = mana
    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")
    #kekuatan khusus mage
    def skill_fire(self,lawan):
        if self.mana >=20:
            print(f"{self.name}, menggunakan skill fire ke {lawan.name}!")
            self.mana -=20
            lawan.damage(self.attack_power * 2) #powernya 2x lipat
        else:
            print(f"{self.name} gagal skill mana low")
# -- Main program baru --
print("=== upadate hero baru ===")

Valir = Mage("Valir", 200, 20, 100)
balmond = Hero("Balmond", 300, 25)

Valir.info()
balmond.kabar()


# -- Main Program --

# Membuat Object (Instansiasi)
hero1 = Hero("Belerick", 500, 15)
hero2 = Hero("Beatrix", 120, 20)

# Memanggil Method
hero1.kabar()
hero2.kabar()
#jika hero 1 diubah point hp nya menjadi 500
print("hp diubah", hero1.hp, hero1.name)

# output Hero: 
# Hero: Belerick | HP: 500 | Power: 15
# Hero: Beatrix | HP: 120 | Power: 20

# output dari pertarungan
print("==== Ready fight ====")
hero1.attack(hero2)
hero2.attack(hero1)


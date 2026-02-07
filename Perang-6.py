# Parent Class
class Hero:
    def __init__(self, nama):
        self.nama = nama
    def attack(self):
        print("Hero menyerang dengan tangan kosong.")
        
    # Child Class 1
class Mage(Hero):
    def attack(self):
     print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")
# Child Class 2
class Marksman(Hero):
    def shoot(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")
# Child Class 3
class Fighter(Hero):
    def attack(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")
        
class Support(Hero):
    def attack(self):
        print(f"{self.nama} (Support) melakukan Healing")        

# -- Penerapan Polymorphism --

pasukan = [
    Mage("Valir"),
    Marksman("Miya"),
    Fighter("Alucard"),
    Fighter("Lapu"),
    Support("Estes")
]
print("--- PERANG DIMULAI ---")
# Satu perintah loop, tapi respon berbeda-beda (Polymorphism)
for War in pasukan:
    War.attack()
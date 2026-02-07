from abc import ABC, abstractmethod

# Interface / Abstarct class

class Games(ABC):
    @abstractmethod
    def attack(self,target):
        pass
    def info(self):
        pass
    
# implementasi pada kelas konkret
class Hero(Games):
    def __init__(self,nama):
        self.nama = nama
    def attack(self, target):
        print(f"Hero {self.nama} menyerang {target}!")
    def info(self):
        print(f"My name is {self.nama}")

class Monster(Games):
    def __init__(self,jenis):
        self.jenis = jenis
        
    # implementasi yang dilakukan oleh monster
    def attack(self,target):
        print(f"Monster {self.jenis} menghantam {target}!")
        
    def info(self):
        print(f"Saya adalah monster {self.jenis}")     
        
# pengujian

h= Hero("Badang")
m = Monster("Patrick")

h.info
m.info
h.attack("Patrick")
m.attack("Badang")

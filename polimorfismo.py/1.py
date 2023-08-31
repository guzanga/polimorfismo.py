class AnimalAquatico:
    def nadando(self):
        pass
    
class tartaruga (AnimalAquatico):
    def nadando(self):
        print("splash...splash...")

class peixe(AnimalAquatico):
    def nadando(self):
        print("shua...shua...")
        
peixe1 = peixe()
peixe1.nadando()

tartaruga1 = tartaruga()
tartaruga1.nadando()
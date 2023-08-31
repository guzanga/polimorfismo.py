class calculo:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def calcular(self):
        pass

class mult(calculo):
    def __init__(self,num1, num2):
        super().__init__(num1, num2)
    def calcular(self):
        print(self.num1 * self.num2)
        
class soma(calculo):
    def __init__(self,num1, num2):
        super().__init__(num1, num2)
    def calcular(self):
        print(self.num1 + self.num2) 

class sub(calculo):
    def __init__(self,num1, num2):
        super().__init__(num1, num2)
    def calcular(self):
        print(self.num1 - self.num2) 
        
class div(calculo):
    def __init__(self,num1, num2):
        super().__init__(num1, num2)
    def calcular(self):
        print(self.num1 / self.num2) 

calc1 = div(90,20)
calc1.calcular()
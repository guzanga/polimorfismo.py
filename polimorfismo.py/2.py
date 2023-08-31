class item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        def calc_valor(self):
            pass
            
class produto(item):
    def __init__(self,nome,preco, quantidade):
        super().__init__(nome,preco)
        self.quantidade = quantidade
    
    def calc_valor(self):
        print(self.preco * self.quantidade)
        
class serviço(item):
    def __init__(self,nome,preco, horas):
        super().__init__(nome,preco)
        self.horas = horas
    
    def calc_valor(self):
        print (self.preco * self.horas)
        
p1 = serviço("vaso",10,2)
p1.calc_valor()
        
# primeira forma do polimorfismo
# o pass é um modelo de acao que posso usar depois
class profissao:
    def acao(self):
        pass

# aqui eu alterei a função pass para uma outra
class estudante(profissao):
    def acao(self):
        print("estudando...")
    
# aqui eu chamei a função da classe filho, atribui esta classe a um objeto e após eu chamei a função 
aluno1 = estudante()
aluno1.acao()


# segunda forma de se usar o polimorfismo

class prifisões:
    def acoes(self):
        return "a atividade é:"
    
class estudantes(prifisões):
    def acoes(self):
        print(super().acoes(),"estudar")
        
aluno2 = estudantes()
aluno2.acoes()
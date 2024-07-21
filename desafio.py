class Vendedor():
    def __init__(self,nome):
        self.nome =  nome
        self.vendas = 0

    def vendeu(self,vendas):
        self.vendas =  vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome, 'Bateu a meta')
        else:
            print('não bateu a meta')

vendedor1 = Vendedor('Lucas')
vendedor1.vendeu(200)
vendedor1.bateu_meta(300)

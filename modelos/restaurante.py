from modelos.avaliacao import Avaliacao

class Restaurante:  # Define a classe Restaurante
    restaurantes = []  # Lista para armazenar todas as instâncias de restaurantes criadas

    def __init__(self, nome, categoria, ano):  # Método inicializador da classe
        self._nome = nome.title()  # Atributo nome do restaurante
        self.categoria = categoria.upper()  # Atributo categoria do restaurante
        self.ano = ano  # Atributo ano de fundação do restaurante
        self._ativo = False  # Atributo privado por conta do "_" no nome, indicando se o restaurante está ativo (inicialmente False)
        self._avaliacao = []
        Restaurante.restaurantes.append(self)  # Adiciona a nova instância à lista de restaurantes

    def __str__(self):  # Método que retorna uma representação em string da instância
        return f'{self._nome} | {self.categoria} | {self.ativo} | {self.ano}'  # Formata e retorna os atributos da instância
    
    @classmethod
    def listar_restaurantes(cls):  # Método para listar todos os restaurantes
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Ano'.ljust(25)} |{'Avaliacão'.ljust(25)}| {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:  # Percorre a lista de restaurantes
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ano.ljust(25)} |{str(restaurante.media_avaliacao).ljust(25)}| {restaurante.ativo}')  # Imprime as informações do restaurante

    def listar_avaliacao():
        for avaliacao in avaliacao:
            print(f'{avaliacao.ljust(25)}')

    @property  # Define um método como uma propriedade
    def ativo(self):  # Propriedade que retorna o status ativo do restaurante
        return 'verdadeiro' if self._ativo else 'falso'  # Retorna 'verdadeiro' se _ativo for True, caso contrário 'falso'
    def alterar_status(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self,avaliacao):
        #avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)
        return media
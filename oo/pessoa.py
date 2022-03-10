class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=47,):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_De_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    pek = Pessoa(nome='Pek')
    paulo = Pessoa(pek, nome='Paulo')
    print(Pessoa.cumprimentar(paulo))
    print(id(paulo))
    print(paulo.cumprimentar())
    print(paulo.nome)
    print(paulo.idade)
    for filho in paulo.filhos:
        print(filho.nome)
    paulo.sobrenome = 'José'
    del paulo.filhos
    paulo.olhos = 1
    del paulo.olhos
    print(paulo.__dict__)
    print(pek.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(paulo.olhos)
    print(pek.olhos)
    print(id(Pessoa.olhos)), print(id(paulo.olhos)), print(id(pek.olhos))
    print(Pessoa.metodo_estatico(), paulo.metodo_estatico())
    print(Pessoa.nome_e_atributo_De_classe(), paulo.nome_e_atributo_De_classe())
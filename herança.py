class programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes
    @likes.setter
    def likes(self, new_like):
        self._likes = new_like

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def curtir(self):
        self.likes += 1

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}'

class playlist:
    def __init__(self, nome, programa):
        self.nome = nome
        self.programa = programa

    def __getitem__(self, item):
        return self.programa[item]
    @property
    def listagem(self):
        return self.programa

    def __len__(self):
        return len(self.programa)

class filme(programa):

    def __init__(self, nome, ano, duracao):
        super().__init__( nome, ano,)
        self.duracao = duracao

        def __str__(self):
            return f'{self._nome} - {self.ano} - {self.duracao} - {self._likes}'

class serie(programa):
    def __init__(self, nome, ano, temp):
        super().__init__( nome, ano,)
        self.temp = temp

        def __str__(self):
            return f'{self._nome} - {self.ano} - {self.temp} - {self._likes}'

vingadores = filme("vinga:2", 2018, 120)
demolidor = filme("demolidor", 2012, 80)
atlanta = serie("atlanta", 2018, 3)
todo = serie("Todo mundo odeia o chris)", 2000, 1000)

atlanta.curtir()
atlanta.curtir()
vingadores.curtir()
demolidor.curtir()
todo.curtir()

filmes_e_series = [vingadores, atlanta, demolidor, todo]
fds = playlist("fds", filmes_e_series)

print(f"{len(fds.listagem)}")

for programa in fds:
    print(programa)

print(demolidor in fds)

len(fds)
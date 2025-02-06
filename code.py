import heapq

class Livros:
    def __init__(self, livro, genero, autor):
        self.livro = livro
        self.genero = genero
        self.autor = autor
        self.disponibilidade = True

    def emprestar(self):
        self.disponibilidade = False

    def devolver(self):
        self.disponibilidade = True

    def retornando_resultados(self):
        if self.disponibilidade:
            return f"O livro {self.livro} está disponível.", f"Gênero: {self.genero}", f"Autor: {self.autor}"
        else:
            return f"O livro {self.livro} não está disponível."


class Usuario:
    def __init__(self, nome, Id):
        self.nome = nome
        self.Id = Id
        self.historico = []

    def colocando_no_historico(self, *livro_guardado):
        for livro in livro_guardado:
            self.historico.append(livro)
        return [str(livro) for livro in self.historico]


    def retornando_resultados_usuario(self):
        livros_str = ", ".join(livro.livro for livro in self.historico)
        return f"O usuário {self.nome} de ID {self.Id}",f"guardou os seguintes livros: {livros_str}" 

    def similirariedade(self, livroa, varios_livrob):
        similirariedade = 0
        if livroa.genero == varios_livrob.genero:
            similirariedade += 1
        if livroa.autor == varios_livrob.autor:
            similirariedade += 1
        return similirariedade

    def recomendacao(heap, livro_principal, livro_alternativos):
        for livro in livro_alternativos:
            similiridade = livro_principal.similirariedade[livro]
            heapq.heappush(heap, (similiridade, livro))

    def retornando_resultados_recomendacao(heap):
        recomendacao_livro = []
        while heap:
            similiraridade, livro = heapq.heappop(heap)
            recomendacao_livro.append((similiraridade, livro.livro))
        return recomendacao_livro

heap = []

livros_escolhidos_1 = Livros("O Senhor dos Aneis", "Fantasia", "J. R. R. Tolkien") 
livros_escolhidos_2 = Livros("Harry Potter", "Fantasia", "J. K. Rowling")
livros_escolhidos_3 = Livros("O Pequeno Príncipe", "Infantil", "Antoine de Saint-Exupéry")

usuarios_1 = Usuario("João", 1)
usuarios_2 = Usuario("Maria", 2)
usuarios_3 = Usuario("Pedro", 3)

usuarios_1.colocando_no_historico(livros_escolhidos_1)
usuarios_1.colocando_no_historico(livros_escolhidos_2)
usuarios_1.colocando_no_historico(livros_escolhidos_3)

print(livros_escolhidos_1.retornando_resultados(),livros_escolhidos_2.retornando_resultados(), livros_escolhidos_3.retornando_resultados())
print(usuarios_1.retornando_resultados_usuario())

verdadeiras_recomendacoes = Usuario.retornando_resultados_recomendacao(heap)
print(f"Recomendações com base no livro escolhido: {livros_escolhidos_1.livro}")
for similiridade, livro,livro in verdadeiras_recomendacoes:
    print(f"Similirariedade: {similiridade}, Livro: {livro}. Similar a : {livros_escolhidos_3.livro}")

print(usuarios_1.similirariedade(livros_escolhidos_1, livros_escolhidos_2))
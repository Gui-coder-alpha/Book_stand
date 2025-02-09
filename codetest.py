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
            return f"O livro {self.livro} está disponível.", f"Gênero: {self.genero}", f"Autor: {self.autor}"
        else:
            return f"O livro {self.livro} não está disponível."

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
        return f"O usuário {self.nome} de ID {self.Id} guardou os seguintes livros: {livros_str}"

    def calcular_similaridade(self, livroa, livrob):
        similaridade = 0
        if livroa.genero == livrob.genero:
            similaridade += 1
        if livroa.autor == livrob.autor:
            similaridade += 1
        return similaridade

    def recomendacao(self, heap, livro_principal, livros_alternativos):
        for livro in livros_alternativos:
            similaridade = self.calcular_similaridade(livro_principal, livro)
            heapq.heappush(heap, (similaridade, livro))

    def retornando_resultados_recomendacao(self, heap):
        recomendacao_livro = []
        while heap:
            similaridade, livro = heapq.heappop(heap)
            recomendacao_livro.append((similaridade, livro.livro))
        return recomendacao_livro

# Criação de livros
livros_escolhidos_1 = Livros("O Senhor dos Aneis", "Fantasia", "J. R. R. Tolkien") 
livros_escolhidos_2 = Livros("Harry Potter", "Fantasia", "J. K. Rowling")
livros_escolhidos_3 = Livros("O Pequeno Príncipe", "Infantil", "Antoine de Saint-Exupéry")

# Criação de usuário
usuarios_1 = Usuario("João", 1)

# Adicionando livros ao histórico do usuário
usuarios_1.colocando_no_historico(livros_escolhidos_1, livros_escolhidos_2, livros_escolhidos_3)

# Exibindo resultados dos livros e histórico
print(livros_escolhidos_1.retornando_resultados(), livros_escolhidos_2.retornando_resultados(), livros_escolhidos_3.retornando_resultados())
print(usuarios_1.retornando_resultados_usuario())

# Recomendação com MinHeap
heap = []
usuarios_1.recomendacao(heap, livros_escolhidos_1, [livros_escolhidos_2, livros_escolhidos_3])
verdadeiras_recomendacoes = usuarios_1.retornando_resultados_recomendacao(heap)
print(f"Recomendações com base no livro escolhido: {livros_escolhidos_1.livro}")
for similaridade, livro in verdadeiras_recomendacoes:
    print(f"Similaridade: {similaridade}, Livro: {livro}")

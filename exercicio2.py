# Feito por Daniel Gama - RU:4121047
class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None


class TabelaHash:
    def __init__(self):
        self.tabela = [
            None
        ] * 10  # Inicializa a tabela hash com 10 posições, todas None

    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10

    def inserir(self, sigla, nomeEstado):
        indice = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nomeEstado)
        if self.tabela[indice] is None:
            self.tabela[indice] = novo_nodo
        else:
            novo_nodo.proximo = self.tabela[indice]
            self.tabela[indice] = novo_nodo

    def imprimir(self):
        for i, head in enumerate(self.tabela):
            print(f"Posição {i}:", end=" ")
            atual = head
            while atual:
                print(atual.sigla, end=" -> ")
                atual = atual.proximo
            print("None")


# Criando a tabela hash
tabela_hash = TabelaHash()

# Saída de Console 1 de 3
print("Tabela Hash antes de inserir qualquer informação:")
tabela_hash.imprimir()

# Lista dos estados
estados = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
]

# Inserindo os estados na tabela hash
for sigla, nome in estados:
    tabela_hash.inserir(sigla, nome)

# Saída de Console 2 de 3
print("\nTabela Hash após inserir os 26 estados e o Distrito Federal - DF:")
tabela_hash.imprimir()

# Estado fictício com meu nome
tabela_hash.inserir("DG", "Daniel Gama")

# Saída de Console 3 de 3
print(
    "\nTabela Hash após inserir os 26 estados, Distrito Federal – DF e o estado fictício:"
)
tabela_hash.imprimir()
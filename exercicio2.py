class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10  # EXIGÊNCIA DE CÓDIGO 1 de 7

    def funcao_hash(self, sigla):
        if sigla == 'DF':
            return 7  # Regra especial para o Distrito Federal
        else:
            return (ord(sigla[0]) + ord(sigla[1])) % 10  # Regra de hash geral

    def inserir(self, sigla, nomeEstado):
        posicao = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nomeEstado)
        novo_nodo.proximo = self.tabela[posicao]
        self.tabela[posicao] = novo_nodo  # EXIGÊNCIA DE CÓDIGO 3 de 7

    def imprimir(self):
        for i in range(10):  # EXIGÊNCIA DE CÓDIGO 4 de 7
            print(f"Posição {i}: ", end="")
            atual = self.tabela[i]
            while atual is not None:
                print(f"{atual.sigla} ({atual.nomeEstado}) -> ", end="")
                atual = atual.proximo
            print("None")

def inserir_estados(tabela):
    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
        ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
        ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
        ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
        ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
    ]

    for sigla, nome in estados:
        tabela.inserir(sigla, nome)

def inserir_estado_ficticio(tabela, sigla, nomeEstado):
    tabela.inserir(sigla, nomeEstado)  # EXIGÊNCIA DE CÓDIGO 7 de 7

# Execução do programa
tabela = TabelaHash()

print("Tabela Hash inicial (sem inserções):")
tabela.imprimir()  # EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3

inserir_estados(tabela)

print("\nTabela Hash após inserção dos estados e Distrito Federal:")
tabela.imprimir()  # EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3

inserir_estado_ficticio(tabela, "BK", "Bruno Kostiuk")

print("\nTabela Hash após inserção dos estados, Distrito Federal e estado fictício:")
tabela.imprimir()  # EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3

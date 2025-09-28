""" Hiago De Araujo Dantas Teixeira
    RA: 139001

    Link para o vídeo de apresentação:
    https://youtu.be/6n8vHRCkltE """

from dataclasses import dataclass
from copy import deepcopy

Terra: int = -1

@dataclass
class tipoItem:
    """Representa um item da pilha."""
    valor: int | str | float = None

class criaPilhaEstatica():
    """Representa uma pilha estática."""
    def __init__(self, maxTam: int)->None:
        self.maxTam: int = maxTam
        self.itens: list = maxTam*[tipoItem()]
        self.posTopo: int = Terra
        self.opSuc: bool = False

    def vazia(self)->bool:
        return self.posTopo==Terra
    
    def cheia(self)->bool:
        return self.posTopo==self.maxTam-1

    def opSucesso(self)->bool:
        return self.opSuc

    def empilha(self, item: tipoItem)->None:
        if self.cheia():
            self.opSuc=False
        else:
            self.posTopo+=1
            self.itens[self.posTopo]=deepcopy(item)
            self.opSuc=True

    def desempilha(self)->tipoItem:
        if self.vazia():
            self.opSuc=False
            return tipoItem()
        else:
            self.posTopo-=1
            self.opSuc=True
            return deepcopy(self.itens[self.posTopo+1])
    
    def itemTopo(self)->tipoItem:
        if self.vazia():
            self.opSuc=False
            return tipoItem()
        else:
            self.opSuc=True
            return deepcopy(self.itens[self.posTopo])
        
    def exibe(self)->None:
        if self.vazia():
            print("\nPilha Vazia!\n")
        else:
            print("\nPilha:\n")
            for i in range(self.posTopo+1):
                print(self.itens[i].valor," ")
        
    def esvazia(self)->None:
        self.posTopo=Terra

    def __str__(self)->str:
        pilha=""
        for i in range(self.posTopo+1):
            pilha+=str(self.itens[i].valor)
        return pilha
    
    def __len__(self)->int:
        return self.posTopo+1

    def __getitem__(self, ind)->int | str | float:
        return self.itens[ind].valor

def verificar_balanceamento(expressao: str) -> str:
    """ Verifica se os parênteses, colchetes e chaves em uma expressão
    matemática estão corretamente balanceados."""

    abre = "([{"
    fecha = ")]}"
    
    pilha = criaPilhaEstatica(len(expressao)) # o tamanho máximo da pilha estática é o len da expressão (o tamanho da expressão)

    for i in range(len(expressao)):
        caracter = expressao[i] # guarda o elemento que está na posição 'i' da nossa expressão
        
        if caracter in abre:
            item = tipoItem(caracter) # guardamos o caracter de abertura utilizando a classe 'tipoItem'
            pilha.empilha(item) # empilhamos esse valor

        elif caracter in fecha:
            if pilha.vazia(): # se a pilha está vazia, signfica que não empilhamos nenhum caracter de abertura
                return print("\n[ERRO] Expressão inválida!\n", f"O caractere de fechamento '{caracter}' na posição {i} não possui um caractere de abertura correspondente.")

            item_topo = pilha.desempilha() # tira do topo um caracterter abre 
            topo_valor = item_topo.valor # guarda apenas o valor desse caracter
            
            abre_esperado = ''
            if caracter == ')':
                abre_esperado = '('
            elif caracter == ']':
                abre_esperado = '['
            elif caracter == '}':
                abre_esperado = '{'

            if topo_valor != abre_esperado: # se o valor de fechamento que guardamos não corresponde com o 'abre_esperado', signfica que não está balanceado
                return print("\n[ERRO] Expressão inválida!\n", f"O caractertere de fechamento '{caracter}' na posição {i} não corresponde ao caractertere de abertura '{topo_valor}'.")

    if pilha.vazia(): # se após o for a pilha ficar vazia, a pilha está balanceada
        return print("\n[SUCESSO] A expressão está corretamente balanceada!")
    else: # caso sobre caracteres de abertura, a pilha está desbalanceada
        return print("\n[ERRO] Expressão inválida!\n", f"Há caracterteres de abertura que não foram fechados: {str(pilha)}")

if __name__ == "__main__":
    print("---------------------------------------------------------")
    print("  Verificador de Balanceamento de Expressões Matemáticas ")
    print("---------------------------------------------------------")
 

    while True:
        exp = input("Digite a expressão (ou 'sair' para terminar): ")
        if exp == 'sair':
            break
        
        verificar_balanceamento(exp)
        print("-" * 50)
""" Hiago De Araujo Dantas Teixeira
    RA: 139001

    Link para o vídeo de apresentação:
    https://youtu.be/d5aVZKnt2Sc """

import random
import time
import os
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Cliente:
    """Representa um cliente com nome, tempo de atendimento e momento de chegada."""
    nome: str
    tempo_atendimento: int
    giro_chegada: int

@dataclass
class tipoItem:
    """Representa um item genérico da fila, que conterá um Cliente."""
    valor: Cliente = None

class criaFilaEstaticaCircular():
    """Representa uma fila estática circular."""

    def __init__(self, maxTam: int):
        self.maxTam: int = maxTam
        self.itens: list = maxTam * [tipoItem()]
        self.posPrimeiro = 0
        self.posUltimo = -1
        self.numItens = 0
        self.opSuc = False

    def vazia(self) -> bool:
        return self.numItens == 0
    
    def cheia(self) -> bool:
        return self.numItens == self.maxTam

    def opSucesso(self) -> bool:
        return self.opSuc

    def enfileira(self, item: tipoItem) -> None:
        if self.cheia():
            self.opSuc = False
        else:
            self.posUltimo = (self.posUltimo + 1) % self.maxTam
            self.itens[self.posUltimo] = deepcopy(item)
            self.opSuc = True
            self.numItens += 1

    def desenfileira(self) -> tipoItem:
        if self.vazia():
            self.opSuc = False
            return None
        self.opSuc = True
        item: tipoItem = self.itens[self.posPrimeiro]
        self.posPrimeiro = (self.posPrimeiro+1) % self.maxTam
        self.numItens-=1
        return deepcopy(item)
    
    def decrementa_tempo_primeiro(self) -> int:
        """Decrementa o tempo de atendimento do primeiro cliente da fila e retorna o novo tempo."""
        if self.vazia():
            return -1
        cliente_na_frente = self.itens[self.posPrimeiro].valor # Pega o cliente que está no caixa
        if cliente_na_frente.tempo_atendimento > 0:
            cliente_na_frente.tempo_atendimento -= 1 # A cada giro, decrementa 1 no seu tempo de atendimento
        return cliente_na_frente.tempo_atendimento # Retorna o tempo atualizado

    def itemPrimeiro(self) -> tipoItem:
        if self.vazia():
            self.opSuc = False
            return tipoItem()
        self.opSuc = True
        item = self.itens[self.posPrimeiro]
        return deepcopy(item)

def ler_maxFila(mensagem: str) -> int:
    """ Lê e valida a capacidade máxima da fila a partir da entrada do usuário. """
    while True:
        valor_str = input(mensagem)
        
        try:
            valor_int = int(valor_str) #Tenta converter a string em int
            if valor_int > 0:
                return valor_int
            else:
                print("Erro: A capacidade da fila deve ser um número positivo (maior que zero).")

        except ValueError:
            print(f"Erro: '{valor_str}' não é um número inteiro válido. Por favor, tente novamente.")
        
    
def ler_probabilidade(mensagem: str) -> float:
    """Lê e valida uma probabilidade (entre 0.0 e 1.0) de entrada na fila a partir da entrada do usuário"""
    while True:
        prob_str = input(mensagem)
        
        try:
            prob_float = float(prob_str) #Tenta converter a string em float
            if prob_float >= 0.0 and prob_float <= 1.0:
                return prob_float
            else:
                print("Erro: A probabilidade da entrada na fila deve ser um número entre 0.0 e 1.0.")

        except ValueError:
            print(f"Erro: '{prob_str}' não é um número decimal válido. Por favor, tente novamente.")

def exibe_simulacao(fila: criaFilaEstaticaCircular, giro_atual: int, tempo_total: int, estatisticas: dict):
    """Limpa a tela e exibe o estado atual da simulação."""
    os.system('cls' if os.name == 'nt' else 'clear') # É uma função da biblioteca 'os' que executa um comando diretamente no terminal para limpar a tela.
    print("===================================================")
    print("      SIMULADOR DE FILA DE ATENDIMENTO  ")
    print("===================================================")
    print(f"Tempo decorrido: {giro_atual} de {tempo_total} giros.")
    print(f"Clientes na fila: {fila.numItens} de {fila.maxTam} | Atendidos: {estatisticas['clientes_atendidos']}")
    print("-" * 50)

    print("CAIXA: ", end="")
    if fila.vazia():
        print("Livre")
    else:
        cliente_atendido = fila.itemPrimeiro().valor
        print(f"Atendendo [{cliente_atendido.nome}: {cliente_atendido.tempo_atendimento} giros restantes]")

    print("FILA: ", end="[ ")
    if fila.numItens > 1: # Se tem 1 pessoa na fila ela está no caixa
        pos = (fila.posPrimeiro + 1) % fila.maxTam
        for i in range(fila.numItens - 1):
            cliente = fila.itens[pos].valor
            print(f"({cliente.nome}:{cliente.tempo_atendimento})", end=" ")
            pos = (pos + 1) % fila.maxTam
    print("]")
    print("-" * 50)

if __name__ == "__main__":
    maxFila = ler_maxFila("Digite a capacidade máxima da fila: ")
    probEntrada = ler_probabilidade("Digite a probabilidade de chegada de um cliente (0.0 a 1.0): ",)
    totalGiros = ler_maxFila("Digite o tempo total de simulação (em giros de loop): ")

    fila = criaFilaEstaticaCircular(maxFila)
    
    giros = 0
    estatisticas = {
        "clientes_atendidos": 0,
        "soma_tempo_espera": 0
    }

    while giros < totalGiros or fila.vazia() != True: # Continua o loop enquanto giros < totalGiros ou enquanto a fila não estiver vazia.
        
        exibe_simulacao(fila, giros, totalGiros, estatisticas)

        if giros < totalGiros:
            if random.random() < probEntrada: # Verifica se a probabilidade de entrar é menor que a probabilidade sorteada
                if not fila.cheia():    
                    novo_nome = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    novo_tempo = random.randint(2, 8) # O tempo pode ser entre 2 a 8
                    novo_cliente = Cliente(nome=novo_nome, tempo_atendimento=novo_tempo, giro_chegada=giros)
                    fila.enfileira(tipoItem(valor=novo_cliente)) # Enfileiramos nosso novo cliente
                    print(f"Chegada: Cliente {novo_nome} entrou na fila.")
                else:
                    print("Fila cheia! Cliente não pôde entrar.")

        if not fila.vazia():
            tempo_restante = fila.decrementa_tempo_primeiro()
            
            if tempo_restante == 0:
                cliente_saindo = fila.desenfileira().valor
                print(f"Atendimento concluído: Cliente {cliente_saindo.nome} saiu.")
                
                estatisticas["clientes_atendidos"] += 1
                tempo_de_espera = giros - cliente_saindo.giro_chegada
                estatisticas["soma_tempo_espera"] += tempo_de_espera
        
        giros += 1
        time.sleep(1) 

    print("\n\n===================================================")
    print("             FIM DA SIMULAÇÃO ")
    print("===================================================")
    
    total_atendidos = estatisticas["clientes_atendidos"]
    if total_atendidos > 0:
        tempo_medio_espera = estatisticas["soma_tempo_espera"] / total_atendidos
        print(f"Total de clientes atendidos: {total_atendidos}")
        print(f"Tempo médio de espera na fila: {tempo_medio_espera:.2f} giros")
    else:
        print("Nenhum cliente foi atendido na simulação.")
    
    print(f"Tempo total para finalizar todos os atendimentos: {giros} giros.")
    print("===================================================")
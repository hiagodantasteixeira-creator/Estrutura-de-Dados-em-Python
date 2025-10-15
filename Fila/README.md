# Simulador de Fila de Atendimento em Python
Este projeto implementa uma simulação de uma fila de atendimento de clientes, como a de um caixa de supermercado, utilizando uma estrutura de dados de fila estática circular em Python. A simulação exibe o estado da fila em tempo real no terminal e, ao final, calcula estatísticas de desempenho.

## __🎥 Vídeo de Apresentação__
Para uma demonstração e explicação detalhada do projeto, assista ao vídeo no YouTube:

https://youtu.be/d5aVZKnt2Sc

## ✨ Funcionalidades
* Estrutura de Fila Circular: Utiliza uma implementação de fila estática circular para gerenciar os clientes, garantindo um uso eficiente da memória.

* Simulação Parametrizável: O usuário pode definir os parâmetros iniciais da simulação:

* Capacidade máxima da fila.

* Probabilidade de chegada de um novo cliente a cada "giro".

* Tempo total de simulação (em "giros").

* Visualização em Tempo Real: A cada "giro" de tempo, o estado atual da fila, o cliente sendo atendido no caixa e o tempo restante são exibidos no terminal.

* Geração Aleatória: A chegada de novos clientes e o tempo de atendimento necessário para cada um são determinados de forma aleatória, tornando cada simulação única.

* Relatório Final: Ao término da simulação, o programa exibe um resumo com:

* O total de clientes atendidos.

* O tempo médio de espera na fila.

* O tempo total decorrido até que o último cliente fosse atendido.

## ⚙️ Como Funciona
O fluxo principal da simulação ocorre em um laço que representa a passagem do tempo em "giros":

Chegada de Clientes: A cada giro, o programa sorteia um número. Se este número for menor que a probabilidade de chegada definida pelo usuário, um novo cliente é criado (com um nome e tempo de atendimento aleatórios) e entra na fila, caso ela não esteja cheia.

Atendimento no Caixa: O cliente no início da fila é atendido. A cada giro, seu tempo de atendimento restante é decrementado em uma unidade.

Saída de Clientes: Quando o tempo de atendimento de um cliente chega a zero, ele é removido da fila (desenfileirado), e as estatísticas de atendimento são atualizadas.

Atualização da Tela: O terminal é limpo e o estado atual da simulação é reexibido.

O processo continua até que o tempo total de simulação tenha passado e a fila esteja completamente vazia.

## 🚀 Como Executar
Para rodar este projeto, você só precisa ter o Python 3 instalado em sua máquina.

Clone o repositório para sua máquina local:

git clone https://github.com/seu-usuario/seu-repositorio.git
Navegue até o diretório do projeto:

cd seu-repositorio
Execute o script Python:

python FilaCircular.py
O programa solicitará que você insira os parâmetros da simulação. Por exemplo:

Digite a capacidade máxima da fila: 5
Digite a probabilidade de chegada de um cliente (0.0 a 1.0): 0.7
Digite o tempo total de simulação (em giros de loop): 20
Após inserir os dados, a simulação começará no seu terminal.


RA: 139001

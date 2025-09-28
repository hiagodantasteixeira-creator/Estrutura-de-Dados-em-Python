# Verificador de Balanceamento de Expressões com Pilha Estática

## 📖 Descrição

Este projeto é uma implementação em Python de um verificador de balanceamento de delimitadores (parênteses, colchetes e chaves) em expressões matemáticas. O núcleo do projeto é uma **Pilha Estática**, uma estrutura de dados fundamental, que foi criada do zero para gerenciar os caracteres de abertura e garantir que cada um deles seja corretamente fechado.

O objetivo é demonstrar na prática o uso do princípio **LIFO (Last-In, First-Out)** de uma pilha para resolver um problema clássico da ciência da computação. O programa é interativo e permite que o usuário insira múltiplas expressões para validação.

* **Autor:** Hiago De Araujo Dantas Teixeira
* **Vídeo de Apresentação:** [Link para o vídeo](https://youtu.be/6n8vHRCkltE)
  * o vídeo tinha como restrição não passar de 10 minutos 

## ✨ Funcionalidades

* **Implementação de Pilha Estática:** O projeto contém a classe `criaPilhaEstatica` com todas as operações essenciais, como:
    * `empilha(item)`: Adiciona um item ao topo.
    * `desempilha()`: Remove um item do topo.
    * `itemTopo()`: Retorna o item do topo sem removê-lo.
    * `vazia()`: Verifica se a pilha está vazia.
    * `cheia()`: Verifica se a pilha atingiu sua capacidade máxima.
* **Validador Interativo:** Permite ao usuário inserir expressões via terminal e recebe feedback instantâneo se a expressão é válida ou não.
* **Mensagens de Erro Detalhadas:** Em caso de erro, o programa informa exatamente qual foi o problema e em que posição da expressão ele ocorreu, como:
    * Caractere de fechamento sem um de abertura.
    * Caracteres de abertura e fechamento que não correspondem (ex: `([)]`).
    * Caracteres de abertura que nunca foram fechados.

## 🧠 Conceitos de Estrutura de Dados Aplicados

* **Pilhas (Stacks):** O conceito central do projeto. A pilha é utilizada para armazenar os caracteres de abertura (`(`, `[`, `{`) à medida que são encontrados na expressão.
* **Princípio LIFO (Last-In, First-Out):** Quando um caractere de fechamento (`)`, `]`, `}`) é encontrado, o último caractere de abertura que foi inserido na pilha é o primeiro a ser removido para a verificação. Se o par corresponder, o processo continua; caso contrário, a expressão está desbalanceada.

## ⚙️ Como Funciona a Lógica de Verificação

A função `verificar_balanceamento` percorre a expressão caractere por caractere:
1.  Se encontra um caractere de **abertura** (`(`, `[`, `{`), ele é **empilhado** (`push`).
2.  Se encontra um caractere de **fechamento** (`)`, `]`, `}`), o algoritmo verifica:
    * Se a pilha está vazia. Se estiver, significa que há um fechamento sem uma abertura correspondente, e a expressão é inválida.
    * Se a pilha não está vazia, o topo é **desempilhado** (`pop`) e comparado com o caractere de fechamento atual. Se não formarem um par válido (ex: `[` e `)`), a expressão é inválida.
3.  Ao final do percurso, se a **pilha estiver vazia**, significa que todos os caracteres de abertura foram corretamente fechados, e a expressão está **balanceada**. Se ainda restarem itens na pilha, significa que há aberturas que não foram fechadas, e a expressão é **inválida**.

## 🚀 Como Executar o Projeto

1.  **Pré-requisitos:**
    * É necessário ter o **Python 3** instalado.

2.  **Clone o repositório (ou baixe o arquivo):**
    * Salve o arquivo `BalanceamentoPilha.py` em uma pasta no seu computador.

3.  **Execute o arquivo via terminal:**
    * Abra um terminal ou prompt de comando.
    * Navegue até a pasta onde você salvou o arquivo:
        ```bash
        cd caminho/para/a/pasta
        ```
    * Execute o script com o seguinte comando:
        ```bash
        python BalanceamentoPilha.py
        ```

4.  **Interaja com o programa:**
    * O terminal exibirá uma mensagem de boas-vindas.
    * Digite a expressão que deseja verificar e pressione Enter.
    * O resultado (sucesso ou erro) será exibido.
    * Para finalizar, digite `sair` e pressione Enter.

### Exemplos de Uso

* **Entrada Válida:** `({[a+b]*c})`
    * **Saída:** `[SUCESSO] A expressão está corretamente balanceada!`

* **Entrada Inválida:** `(a+[b)`
    * **Saída:** `[ERRO] Expressão inválida! Há caracteres de abertura que não foram fechados: ([`

* **Entrada Inválida:** `a+b)`
    * **Saída:** `[ERRO] Expressão inválida! O caractere de fechamento ')' na posição 3 não possui um caractere de abertura correspondente.`

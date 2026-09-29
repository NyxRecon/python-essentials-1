# 🎩 Escrevendo uma Lista Simples

Um exercício desenvolvido em **Python** como parte das atividades do curso **Python Essentials 1**, da **Cisco Networking Academy**.

Neste desafio, uma lista contendo cinco números é utilizada para praticar operações básicas de manipulação de listas.

O programa permite substituir o elemento central por um número informado pelo usuário, remover o último elemento e, por fim, verificar quantos elementos permanecem na lista.

## 🎯 Objetivo

Praticar os seguintes conceitos de Python:

* Listas
* Índices
* Acesso e alteração de elementos
* Entrada de dados com `input()`
* Conversão de `string` para `int`
* Exclusão de elementos com `del`
* Função `len()`

## ⚙️ Como funciona

O programa começa com uma lista contendo cinco números:

```python
hat_list = [1, 2, 3, 4, 5]
```

### 1️⃣ Substituindo o elemento do meio

O usuário informa um número inteiro:

```python
hat_sub = int(input("Escolha um número para substituir o número do meio: "))
```

Como as listas em Python começam no índice `0`, o elemento do meio da lista `[1, 2, 3, 4, 5]` está no índice `2`.

Por isso, ele é substituído utilizando:

```python
hat_list[2] = hat_sub
```

### 2️⃣ Removendo o último elemento

Depois, o último elemento da lista é removido utilizando `del`:

```python
del hat_list[4]
```

### 3️⃣ Verificando o tamanho da lista

Por fim, a função `len()` é utilizada para descobrir quantos elementos permanecem na lista:

```python
len(hat_list)
```

## 💻 Código

```python
# Escrevendo uma lista simples

hat_list = [1, 2, 3, 4, 5]

# Etapa 1: substituir o número do meio
print(hat_list)

hat_sub = int(input(
    "Escolha um número para substituir o número do meio: "
))

hat_list[2] = hat_sub

print("Essa é a nova lista:", hat_list)

# Etapa 2: remover o último elemento
del hat_list[4]

print("O último número da lista foi deletado:", hat_list)

# Etapa 3: imprimir o comprimento atual da lista
print(
    "Comprimento atual da lista:",
    len(hat_list),
    "itens."
)
```

## 🖥️ Exemplo de execução

```text
[1, 2, 3, 4, 5]

Escolha um número para substituir o número do meio: 10

Essa é a nova lista: [1, 2, 10, 4, 5]

O último número da lista foi deletado: [1, 2, 10, 4]

Comprimento atual da lista: 4 itens.
```

## 🧠 O que aprendi

Este exercício ajudou a reforçar como trabalhar com **listas em Python** e como seus elementos podem ser acessados e modificados individualmente.

Também pratiquei:

* Criação de listas;
* Indexação de elementos;
* Alteração de valores dentro de uma lista;
* Remoção de elementos;
* Contagem de elementos;
* Recebimento e conversão de dados informados pelo usuário.

## 🔎 Conceito principal

Um ponto importante aprendido neste exercício foi o funcionamento dos **índices das listas**.

Em Python, a contagem começa em `0`:

```text
Índice:    0  1  2  3  4
Valor:    [1, 2, 3, 4, 5]
```

Por isso, o número do meio (`3`) está no índice `2`.

Depois da substituição, por exemplo, a lista pode ficar:

```text
[1, 2, 10, 4, 5]
```

Após remover o último elemento:

```text
[1, 2, 10, 4]
```

E o `len()` retorna:

```text
4
```

## 🎓 Curso

**Python Essentials 1 — Cisco Networking Academy**

Este projeto faz parte das atividades práticas realizadas durante meus estudos de fundamentos de Python.

---

🐍 **Mais um exercício concluído na minha jornada de aprendizado em Python e Cybersecurity.**


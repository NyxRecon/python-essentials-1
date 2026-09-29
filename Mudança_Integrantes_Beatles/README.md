# 🎸 Documentando a Mudança de Integrante dos Beatles com Listas

Um exercício desenvolvido em **Python** como parte das atividades do curso **Python Essentials 1**, da **Cisco Networking Academy**.

Neste desafio, a proposta é simular mudanças na formação dos **Beatles** utilizando uma lista e diferentes operações de manipulação de dados.

O exercício trabalha desde a criação de uma lista vazia até a adição, remoção e inserção de integrantes em posições específicas.

## 🎯 Objetivo

Praticar os seguintes conceitos de Python:

* Criação de listas;
* Método `append()`;
* Método `insert()`;
* Instrução `del`;
* Loop `for`;
* Função `range()`;
* Função `len()`;
* Entrada de dados com `input()`;
* Manipulação de elementos por índice.

## ⚙️ Como funciona

O exercício é dividido em cinco etapas.

### 1️⃣ Criando uma lista vazia

Primeiro, é criada uma lista chamada `beatles`:

```python
beatles = []
```

### 2️⃣ Adicionando os primeiros integrantes

Os três primeiros integrantes são adicionados utilizando o método `append()`:

```python
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
```

Nesse momento, a lista contém:

```text
['John Lennon', 'Paul McCartney', 'George Harrison']
```

### 3️⃣ Adicionando novos integrantes

Um loop `for` é utilizado para solicitar ao usuário os nomes de **Stu Sutcliffe** e **Pete Best**.

```python
for _ in range(2):
    nome = input(
        "Digite o nome do membro que você deseja adicionar, "
        "Stu Sutcliffe ou Pete Best: "
    )
    beatles.append(nome)
```

O método `append()` adiciona cada novo nome ao final da lista.

### 4️⃣ Removendo integrantes

Depois, `del` é utilizado para remover Stu Sutcliffe e Pete Best da lista:

```python
del beatles[4]
del beatles[3]
```

A ordem é importante porque, ao remover um elemento, os índices dos elementos seguintes são alterados.

### 5️⃣ Adicionando Ringo Starr

Por fim, o método `insert()` é utilizado para adicionar **Ringo Starr** no início da lista:

```python
beatles.insert(0, "Ringo Starr")
```

O índice `0` representa a primeira posição da lista.

## 💻 Código

```python
# Documentando a mudança de integrante dos Beatles com lista

# Etapa 1
beatles = []
print("Etapa 1:", beatles)

# Etapa 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)

# Etapa 3
for _ in range(2):
    nome = input(
        "Digite o nome do membro que você deseja adicionar, "
        "Stu Sutcliffe ou Pete Best: "
    )
    beatles.append(nome)

print("Etapa 3:", beatles)

# Etapa 4
del beatles[4]
del beatles[3]
print("Etapa 4:", beatles)

# Etapa 5
beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)

# Verificando o tamanho da lista
print(
    "O fabuloso Beatles é composto por",
    len(beatles),
    "integrantes!"
)
```

## 🖥️ Exemplo de execução

```text
Etapa 1: []

Etapa 2: ['John Lennon', 'Paul McCartney', 'George Harrison']

Digite o nome do membro que você deseja adicionar, Stu Sutcliffe ou Pete Best: Stu Sutcliffe

Digite o nome do membro que você deseja adicionar, Stu Sutcliffe ou Pete Best: Pete Best

Etapa 3: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Stu Sutcliffe', 'Pete Best']

Etapa 4: ['John Lennon', 'Paul McCartney', 'George Harrison']

Etapa 5: ['Ringo Starr', 'John Lennon', 'Paul McCartney', 'George Harrison']

O fabuloso Beatles é composto por 4 integrantes!
```

## 🧠 O que aprendi

Este exercício ajudou a entender que listas podem ser **modificadas durante a execução do programa**, permitindo adicionar, remover e reorganizar seus elementos.

Também pratiquei:

* Criação de listas vazias;
* Adição de elementos com `append()`;
* Inserção de elementos em posições específicas com `insert()`;
* Exclusão de elementos utilizando `del`;
* Percorrer repetições com `for`;
* Utilização de `range()` para controlar repetições;
* Contagem de elementos com `len()`;
* Acesso aos elementos através de índices.

## 🔎 Conceito principal

Um dos principais aprendizados deste exercício foi entender a diferença entre `append()` e `insert()`.

### `append()`

Adiciona um elemento **ao final** da lista:

```python
beatles.append("George Harrison")
```

### `insert()`

Permite escolher **em qual posição** o elemento será inserido:

```python
beatles.insert(0, "Ringo Starr")
```

Nesse caso, `0` indica a primeira posição da lista.

Também foi possível observar como a utilização de `del` altera os índices dos elementos restantes.

## 🎓 Curso

**Python Essentials 1 — Cisco Networking Academy**

Este projeto faz parte das atividades práticas realizadas durante meus estudos de fundamentos de Python.

---

🐍 **Mais um exercício concluído na minha jornada de aprendizado em Python e Cybersecurity.**


# 🔮 Adivinhe o Número Secreto

Um pequeno jogo desenvolvido em **Python** como parte dos exercícios do curso **Python Essentials 1**, da **Cisco Networking Academy**.

Neste desafio, o usuário precisa descobrir um número secreto definido pelo programa. Enquanto o número informado estiver incorreto, o programa continuará solicitando novas tentativas por meio de um **loop `while`**.

## 🎯 Objetivo

Praticar conceitos fundamentais da linguagem Python, principalmente:

* Variáveis
* Entrada de dados com `input()`
* Conversão de dados com `int()`
* Estruturas condicionais
* Loop `while`
* Operadores de comparação
* Função `print()`
* Strings com múltiplas linhas utilizando aspas triplas

## ⚙️ Como funciona

O programa define inicialmente o número secreto:

```python
secret_number = 777
```

Em seguida, solicita ao usuário que informe um número inteiro.

Enquanto o número informado for diferente do número secreto, o programa exibe uma mensagem e solicita uma nova tentativa:

```python
while numero_escolhido != secret_number:
    print("Ha ha! Você está preso no meu loop!")
    numero_escolhido = int(input("Digite aqui o número escolhido: "))
```

Quando o usuário finalmente informa o número correto, o loop é encerrado e o programa exibe uma mensagem de sucesso:

```python
print("Muito bem, trouxa! Você está livre agora.")
```

## 💻 Exemplo de execução

```text
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+

Digite aqui o número escolhido: 100
Ha ha! Você está preso no meu loop!

Digite aqui o número escolhido: 500
Ha ha! Você está preso no meu loop!

Digite aqui o número escolhido: 777
Muito bem, trouxa! Você está livre agora.
```

## 📚 O que pratiquei

Este exercício ajudou a reforçar principalmente o funcionamento dos **loops `while`** e das **condições de repetição**.

Também pratiquei:

* Recebimento de dados do usuário;
* Conversão de `string` para `int`;
* Comparação entre valores;
* Controle de fluxo;
* Repetição de comandos até que uma condição seja satisfeita;
* Formatação de mensagens no terminal.

## 🧠 Conceito principal

O ponto central do exercício é entender que o `while` continua executando um bloco de código **enquanto sua condição for verdadeira**.

Neste caso:

```python
while numero_escolhido != secret_number:
```

O loop continua enquanto o número escolhido pelo usuário for **diferente** do número secreto.

Quando:

```text
numero_escolhido == secret_number
```

a condição deixa de ser verdadeira e o loop termina.

## 🎓 Curso

**Python Essentials 1 — Cisco Networking Academy**

Este projeto faz parte das atividades práticas realizadas durante meus estudos de fundamentos de Python.

---

🐍 **Mais um exercício concluído na minha jornada de aprendizado em Python e Cybersecurity.**


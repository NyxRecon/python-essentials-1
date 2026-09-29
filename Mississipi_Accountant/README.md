# ⏱️ Contando Mississippi com `for`

Um pequeno programa desenvolvido em **Python** como parte dos exercícios do curso **Python Essentials 1**, da **Cisco Networking Academy**.

Neste exercício, o objetivo é utilizar um loop `for` para realizar uma contagem de 1 a 5, exibindo a palavra **"Mississippi"** a cada iteração e adicionando uma pausa de um segundo entre os números.

Ao finalizar a contagem, o programa exibe a mensagem:

> **"Pronto ou não, aqui vou eu!"**

## 🎯 Objetivo

Praticar conceitos fundamentais de Python, principalmente:

* Loop `for`
* Função `range()`
* Função `print()`
* Módulo `time`
* Função `time.sleep()`
* Controle de repetição

## ⚙️ Como funciona

Primeiro, o módulo `time` é importado:

```python
import time
```

Em seguida, o loop `for` utiliza `range(1, 6)` para gerar os números de **1 até 5**:

```python
for contagem in range(1, 6):
    print(contagem, "Mississippi!")
    time.sleep(1)
```

O `time.sleep(1)` faz o programa aguardar **1 segundo** antes de passar para a próxima iteração.

Depois que o loop termina, a mensagem final é exibida:

```python
print("Pronto ou não, aqui vou eu!")
```

## 💻 Código

```python
# Contando Mississippi com for

import time

for contagem in range(1, 6):
    print(contagem, "Mississippi!")
    time.sleep(1)

print("Pronto ou não, aqui vou eu!")
```

## 🖥️ Exemplo de execução

```text
1 Mississippi!
2 Mississippi!
3 Mississippi!
4 Mississippi!
5 Mississippi!
Pronto ou não, aqui vou eu!
```

A cada número, o programa aguarda aproximadamente um segundo antes de continuar a contagem.

## 🧠 O que aprendi

Este exercício ajudou a reforçar o conceito de **loops `for`** e como utilizá-los para executar uma determinada ação várias vezes.

Também pratiquei:

* Utilização de `range()` para definir uma sequência numérica;
* Iteração com `for`;
* Importação de módulos em Python;
* Utilização de `time.sleep()` para criar intervalos de tempo;
* Organização de um pequeno programa utilizando repetição.

## 🔎 Conceito principal

O trecho:

```python
range(1, 6)
```

gera os valores:

```text
1
2
3
4
5
```

O número `6` não é incluído na sequência.

Assim, o `for` percorre cada valor e executa o bloco de código uma vez para cada número.

## 🎓 Curso

**Python Essentials 1 — Cisco Networking Academy**

Este projeto faz parte das atividades práticas realizadas durante meus estudos de fundamentos de Python.

---

🐍 **Mais um exercício concluído na minha jornada de aprendizado em Python e Cybersecurity.**


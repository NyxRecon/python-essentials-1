# 📅 Verificador de Ano Bissexto em Python

Projeto desenvolvido durante o curso **Python Essentials 1**, da **Cisco Networking Academy**, como parte dos exercícios de prática de lógica de programação e estruturas condicionais em Python.

## 🎯 Sobre o projeto

O programa recebe um ano informado pelo usuário e verifica se ele é:

* **Ano bissexto**
* **Ano comum**
* Ou se está **fora do período do calendário gregoriano**

A lógica utilizada segue as regras do calendário gregoriano, considerando anos a partir de **1582**.

## 🧠 Regras utilizadas

Um ano é considerado **bissexto** quando:

1. É divisível por 4;
2. Mas não é divisível por 100;

**ou**

3. É divisível por 400.

Exemplos:

* `2024` → ano bissexto
* `2025` → ano comum
* `1900` → ano comum
* `2000` → ano bissexto

Além disso, anos anteriores a 1582 são considerados fora do período do calendário gregoriano utilizado pelo exercício.

## 💻 Código

```python
# Descobrindo se um ano é bissexto

year = int(input("Digite um ano: "))

if year < 1582:
    print("Não está dentro do período do calendário gregoriano")
else:
    if year % 4 != 0:
        print("Ano comum")
    elif year % 100 != 0:
        print("Ano bissexto")
    elif year % 400 != 0:
        print("Ano comum")
    else:
        print("Ano bissexto")
```

## 🔎 Conceitos praticados

Neste exercício, pratiquei:

* `input()` para receber dados do usuário;
* `int()` para converter a entrada em número inteiro;
* `if`, `elif` e `else` para estruturas condicionais;
* operador `%` (módulo) para verificar divisibilidade;
* operador `!=` para comparação;
* estruturas condicionais aninhadas;
* aplicação de regras lógicas na resolução de problemas.

## 🧪 Exemplos de execução

### Exemplo 1

```text
Digite um ano: 2024
Ano bissexto
```

### Exemplo 2

```text
Digite um ano: 2025
Ano comum
```

### Exemplo 3

```text
Digite um ano: 1900
Ano comum
```

### Exemplo 4

```text
Digite um ano: 2000
Ano bissexto
```

### Exemplo 5

```text
Digite um ano: 1500
Não está dentro do período do calendário gregoriano
```

## 📚 Curso

**Python Essentials 1 — Cisco Networking Academy**

Este exercício faz parte das atividades práticas realizadas durante o curso, com foco no desenvolvimento de fundamentos de programação e lógica utilizando Python.

---

**Tecnologia:** Python 🐍
**Curso:** Python Essentials 1 — Cisco Networking Academy
**Nível:** Iniciante


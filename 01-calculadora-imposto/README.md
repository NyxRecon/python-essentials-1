# Calculadora de Imposto de Renda

## Objetivo

Desenvolver um programa capaz de calcular o imposto de renda com base em uma regra progressiva de tributação.

O programa recebe a renda anual do usuário e calcula o imposto devido considerando:

* Rendas de até 85.528 unidades monetárias: aplicação de 18% sobre a renda com dedução fixa.
* Rendas acima de 85.528 unidades monetárias: aplicação de uma taxa de 32% sobre o valor excedente, somada a uma parcela fixa.
* Caso o cálculo resulte em um valor negativo, o imposto deve ser considerado como zero.
* O resultado final deve ser arredondado para um número inteiro.

## Conceitos praticados

* Entrada de dados com `input()`
* Conversão de tipos com `float()`
* Estruturas condicionais (`if` e `else`)
* Operadores matemáticos
* Uso da função `round()`
* Validação de valores negativos

## Solução

```python
# Calculadora de imposto

renda = float(input("Informe sua renda: "))

if renda <= 85528:
    tax = renda * 0.18 - 556.02
else:
    valor_tributavel = renda - 85528
    tax = valor_tributavel * 0.32 + 14839.02

tax = round(tax, 0)

if tax <= 0:
    tax = 0

print("A taxa é:", tax, "thalers")
```

## Exemplos de execução

### Caso 1: Renda abaixo do limite de tributação

**Entrada:**

```text
10000
```

**Saída:**

```text
A taxa é: 1244.0 thalers
```

---

### Caso 2: Renda acima do limite de tributação

**Entrada:**

```text
100000
```

**Saída:**

```text
A taxa é: 19470.0 thalers
```

## Aprendizados

Este exercício ajudou a praticar estruturas condicionais e lógica de decisão, simulando um problema real de cálculo financeiro.

Também reforçou a importância de validar resultados antes da exibição, evitando valores inconsistentes como impostos negativos.

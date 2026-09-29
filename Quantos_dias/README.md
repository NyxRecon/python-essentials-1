# 🐍 Quantos dias? — escrevendo e usando suas próprias funções

Neste exercício, o desafio foi criar uma função capaz de determinar a quantidade de dias de um determinado mês, considerando também a regra dos anos bissextos.

💻 **O que pratiquei:**

* Criação e utilização de funções em Python
* Funções com múltiplos argumentos
* Reutilização da função `is_year_leap()`
* Estruturas condicionais `if / elif / else`
* Listas e indexação
* Validação de valores de entrada
* Tratamento específico para fevereiro em anos bissextos
* Testes automatizados com diferentes combinações de ano e mês

🔎 Um dos pontos importantes do exercício foi fazer com que a função não retornasse um resultado incorreto quando o mês informado estivesse fora do intervalo válido de `1` a `12`.

Também utilizei uma lista contendo a quantidade de dias de cada mês, tornando o código mais simples e evitando várias condições desnecessárias.

### 💻 Código completo

```python
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    else:
        if is_year_leap(year) and month == 2:
            return 29
        else:
            return month_days[month - 1]


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]

    print(yr, mo, "->", end="")

    result = days_in_month(yr, mo)

    if result == test_results[i]:
        print("OK")
    else:
        print("Fracassado")
```

### 🧪 Resultado dos testes

```text
1900 2 -> OK
2000 2 -> OK
2016 1 -> OK
1987 11 -> OK
```

📚 Mais um exercício concluído durante meus estudos de **Python Essentials 1 — Cisco Networking Academy**, fortalecendo minha base em lógica de programação, funções e estruturas condicionais em Python.




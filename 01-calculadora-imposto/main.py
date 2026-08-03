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

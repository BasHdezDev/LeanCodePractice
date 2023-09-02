import calculator
import amortization
import extraAmount

print("\n¡Bienvenido!, qué tipo de cálculo desea hacer?\n")

print("1. Una compra con tarjeta de crédito y calcular el total de intereses")
print("2. Plan de amortización")
print("3. Plan de amortización con abono extra")
election = int(input("\n\nEscriba el número de su elección: "))

if election == 1:
    Amount = float(input("Especifique el monto a pagar: "))
    Interest = float(input("Especifique la tasa de interés actual: "))
    Payment = int(input("Especifique a cúantas cuotas pagará el monto: "))
    print(calculator.monthly_bills(Amount, Interest, Payment))
if election == 2:
    Amount = float(input("Especifique el monto a pagar: "))
    Interest = float(input("Especifique la tasa de interés actual: "))
    Payment = int(input("Especifique a cúantas cuotas pagará el monto: "))
    print(amortization.ModelCalculator(Amount, Interest, Payment).amortization())
if election == 3:
    Amount = float(input("Especifique el monto a pagar: "))
    Interest = float(input("Especifique la tasa de interés actual: "))
    Payment = int(input("Especifique a cúantas cuotas pagará el monto: "))
    numero_cuota_a_abonar = int(input("Especifique en qué cuota va a hacer un abono extra: "))
    abonoextra = float(input("Especifique de cúanto será el abono extra: "))
    print(extraAmount.ModelExtraAmount(Amount, Interest, Payment).amortization_extra_amount(numero_cuota_a_abonar, abonoextra))


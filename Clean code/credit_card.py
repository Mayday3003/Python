def calcular_cuota(valor_compra, tasa_interes, numero_cuotas):
    interes_mensual = tasa_interes / 12 / 100
    pago_mensual = valor_compra + interes_mensual/(1-(1+interes_mensual)**-numero_cuotas)
    return pago_mensual


def main():
    valor_compra = float(input('Ingrese el valor de la compra: '))
    tasa_interes = float(input('Ingrese la tasa de interés: '))
    numero_cuotas = int(input('Ingrese el número de cuotas: '))
    cuota = calcular_cuota(valor_compra, tasa_interes, numero_cuotas)
    print(f'El valor de la cuota mensual es: {cuota}')
    

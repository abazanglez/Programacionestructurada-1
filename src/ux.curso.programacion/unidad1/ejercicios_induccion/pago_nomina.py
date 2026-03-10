#1. Ejercicio de induccion: pagono de nomina 
numero_horas = float (input("Ingrese el numero de horas trabajadas:"))
tarifa_hora = float(input("Ingrese la tarifa por hora:"))
nombre_empleado = input("Ingrese el nombre del empleado:")
 
#Las horas superiores a 35 se pagan como extras

if numero_horas > 35:
    horas_extra = numero_horas -35
    pago_bruto = (35 * tarifa_hora) + (horas_extra *tarifa_hora *1.5)
else:
    pago_bruto = numero_horas * tarifa_hora

#calculo de impuesto 

if pago_bruto <=2000:
    impuesto = 0
elif pago_bruto <= 2200:
    impuesto = (pago_bruto - 2000) * 0.20
else:
    impuesto = (pago_bruto - 2220) * 0.30 + 220 *0.20

pago_neto = pago_bruto - impuesto

#mostrar resultados 

print(f"Empleado: {nombre_empleado}")
print(f"Pago bruto: ${pago_bruto:.2f}")
print(f"Impuesto: ${impuesto:.2f}")
print(f"Pago bruto: ${pago_bruto:.2f}")
print("=== SIMULADOR DE PRÉSTAMO (SISTEMA FRANCÉS) ===")
print("Ingrese el monto del préstamo solicitado ($):")
capitalInicial = int(input())
print("Ingrese la Tasa Nominal Anual TNA (%) (Ejemplo: 53):")
tna = int(input())
print("Ingrese el plazo de devolución (en meses):")
plazo = int(input())
i = (tna / 100) / 12
cuotaPura = capitalInicial * (i * (1 + i) * plazo) / ((1 + i) * plazo - 1)
mes = 1
saldoInicial = capitalInicial
totalDevuelto = 0
costoFinanciero = 0
print("Mes | Saldo Inicial | Interés Puro | IVA (21%) | Amortización | Cuota Total | Saldo Final")
print("----------------------------------------------------------------------------------------")
while mes <= plazo:
    interesMes = saldoInicial * i
    ivaInteres = interesMes * 0.21
    amortizacion = cuotaPura - interesMes
    cuotaTotal = amortizacion + interesMes + ivaInteres
    saldoFinal = saldoInicial - amortizacion
    totalDevuelto = totalDevuelto + cuotaTotal
    costoFinanciero = costoFinanciero + interesMes + ivaInteres
    print(mes, "   | $", round(saldoInicial), "          | $", round(interesMes), "        | $", round(ivaInteres), "     | $", round(amortizacion), "       | $", round(cuotaTotal), "       | $", round(saldoFinal))
    saldoInicial = saldoFinal
    mes = mes + 1
print("----------------------------------------------------------------------------------------")
print("Cantidad total de dinero devuelta al banco:", round(totalDevuelto))
print("Costo financiero neto por intereses es", round(costoFinanciero))
print("* Ejecución Finalizada. *")
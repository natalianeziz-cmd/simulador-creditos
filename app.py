from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def calcular_simulador(capital_inicial, tna, plazo):
    """
    Calcula el simulador de préstamo usando el sistema francés
    """
    try:
        capital_inicial = float(capital_inicial)
        tna = float(tna)
        plazo = int(plazo)
        
        if capital_inicial <= 0 or tna <= 0 or plazo <= 0:
            return {"error": "Los valores deben ser mayores a 0"}
        
        # Tasa mensual
        i = (tna / 100) / 12
        
        # Cuota pura (sin IVA)
        if i == 0:
            cuota_pura = capital_inicial / plazo
        else:
            cuota_pura = capital_inicial * (i * (1 + i) ** plazo) / ((1 + i) ** plazo - 1)
        
        mes = 1
        saldo_inicial = capital_inicial
        total_devuelto = 0
        costo_financiero = 0
        detalles = []
        
        while mes <= plazo:
            interes_mes = saldo_inicial * i
            iva_interes = interes_mes * 0.21
            amortizacion = cuota_pura - interes_mes
            cuota_total = amortizacion + interes_mes + iva_interes
            saldo_final = saldo_inicial - amortizacion
            
            total_devuelto += cuota_total
            costo_financiero += interes_mes + iva_interes
            
            detalles.append({
                "mes": mes,
                "saldo_inicial": round(saldo_inicial, 2),
                "interes": round(interes_mes, 2),
                "iva": round(iva_interes, 2),
                "amortizacion": round(amortizacion, 2),
                "cuota_total": round(cuota_total, 2),
                "saldo_final": round(max(0, saldo_final), 2)
            })
            
            saldo_inicial = saldo_final
            mes += 1
        
        return {
            "success": True,
            "capital_inicial": round(capital_inicial, 2),
            "tna": tna,
            "plazo": plazo,
            "cuota_pura": round(cuota_pura, 2),
            "total_devuelto": round(total_devuelto, 2),
            "costo_financiero": round(costo_financiero, 2),
            "detalles": detalles
        }
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calcular', methods=['POST'])
def calcular():
    data = request.json
    capital = data.get('capital')
    tna = data.get('tna')
    plazo = data.get('plazo')
    
    resultado = calcular_simulador(capital, tna, plazo)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

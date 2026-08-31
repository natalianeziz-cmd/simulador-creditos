// Elementos del DOM
const form = document.getElementById('simuladorForm');
const loading = document.getElementById('loading');
const resultados = document.getElementById('resultados');
const error = document.getElementById('error');

// Event Listeners
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    await enviarSimulacion();
});

// Obtener valores del formulario
function obtenerDatos() {
    return {
        capital: document.getElementById('capital').value,
        tna: document.getElementById('tna').value,
        plazo: document.getElementById('plazo').value
    };
}

// Enviar simulación al servidor
async function enviarSimulacion() {
    const datos = obtenerDatos();

    // Validaciones básicas
    if (!datos.capital || !datos.tna || !datos.plazo) {
        mostrarError('Por favor completa todos los campos');
        return;
    }

    // Mostrar loading
    loading.style.display = 'flex';
    resultados.style.display = 'none';
    error.style.display = 'none';

    try {
        const response = await fetch('/api/calcular', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(datos)
        });

        const resultado = await response.json();

        if (resultado.error) {
            mostrarError(resultado.error);
        } else {
            mostrarResultados(resultado);
        }
    } catch (err) {
        mostrarError('Error al conectar con el servidor: ' + err.message);
    } finally {
        loading.style.display = 'none';
    }
}

// Mostrar resultados
function mostrarResultados(datos) {
    // Llenar resumen
    document.getElementById('resCapital').textContent = '$' + formatoMoneda(datos.capital_inicial);
    document.getElementById('resCuota').textContent = '$' + formatoMoneda(datos.cuota_pura);
    document.getElementById('resTotalDevuelto').textContent = '$' + formatoMoneda(datos.total_devuelto);
    document.getElementById('resCostoFinanciero').textContent = '$' + formatoMoneda(datos.costo_financiero);
    document.getElementById('resTNA').textContent = datos.tna.toFixed(2);
    document.getElementById('resPlazo').textContent = datos.plazo;

    // Llenar tabla
    const tbody = document.getElementById('cuotasBody');
    tbody.innerHTML = '';

    datos.detalles.forEach(cuota => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${cuota.mes}</td>
            <td>$${formatoMoneda(cuota.saldo_inicial)}</td>
            <td>$${formatoMoneda(cuota.interes)}</td>
            <td>$${formatoMoneda(cuota.iva)}</td>
            <td>$${formatoMoneda(cuota.amortizacion)}</td>
            <td><strong>$${formatoMoneda(cuota.cuota_total)}</strong></td>
            <td>$${formatoMoneda(cuota.saldo_final)}</td>
        `;
        tbody.appendChild(tr);
    });

    // Mostrar sección de resultados
    resultados.style.display = 'block';
    error.style.display = 'none';

    // Scroll a resultados
    setTimeout(() => {
        resultados.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
}

// Mostrar error
function mostrarError(mensaje) {
    document.getElementById('errorMsg').textContent = mensaje;
    error.style.display = 'block';
    resultados.style.display = 'none';
    error.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Formatear números a moneda
function formatoMoneda(numero) {
    return numero.toLocaleString('es-AR', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}

// Resetear formulario
function resetForm() {
    form.reset();
    resultados.style.display = 'none';
    error.style.display = 'none';
    document.getElementById('capital').focus();
}

// Focus en primer input al cargar
window.addEventListener('load', () => {
    document.getElementById('capital').focus();
});

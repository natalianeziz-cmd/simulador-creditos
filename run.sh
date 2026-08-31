#!/bin/bash

# Script para ejecutar la aplicacion en Mac/Linux

echo ""
echo "========================================"
echo "Simulador de Creditos"
echo "========================================"
echo ""

# Activar entorno virtual si existe
if [ -d "venv" ]; then
    echo "Activando entorno virtual..."
    source venv/bin/activate
else
    echo "Entorno virtual no encontrado"
    echo "Ejecuta primero: bash setup.sh"
    exit 1
fi

# Ejecutar la aplicacion
echo ""
echo "Iniciando aplicacion..."
echo ""
python app.py

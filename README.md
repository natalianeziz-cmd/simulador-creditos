# 💰 Simulador de Créditos

**Educación Financiera en tu Bolsillo**

Aplicación web para simular préstamos usando el sistema de amortización francés con IVA.

## 🚀 Características

- ✅ Simulador de préstamos con sistema francés
- ✅ Cálculo automático de cuotas con IVA (21%)
- ✅ Tabla detallada mes a mes
- ✅ Interfaz moderna y responsiva
- ✅ Fácil de usar

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🔧 Instalación Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/natalianeziz-cmd/simulador-creditos.git
cd simulador-creditos
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

**En Windows:**
```bash
venv\Scripts\activate
```

**En Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```bash
python app.py
```

### 6. Abrir en tu navegador

Va a `http://localhost:5000` en tu navegador

## 🌐 Despliegue Online (GRATIS)

### Opción 1: Render (Recomendado)

1. Ve a [render.com](https://render.com)
2. Crea una cuenta gratuita
3. Conecta tu repositorio de GitHub
4. Selecciona "Web Service"
5. Configura:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
6. ¡Deploy!

### Opción 2: Railway

1. Ve a [railway.app](https://railway.app)
2. Conecta tu GitHub
3. Selecciona este repositorio
4. ¡Deploy automático!

### Opción 3: Heroku

1. Crea archivo `Procfile` con:
   ```
   web: gunicorn app:app
   ```
2. Push a Heroku

## 📊 Cómo funciona

1. **Ingresa tus datos:**
   - Monto del préstamo
   - Tasa Nominal Anual (TNA)
   - Plazo en meses

2. **El sistema calcula:**
   - Cuota mensual pura
   - IVA sobre intereses
   - Amortización
   - Saldo pendiente

3. **Visualiza:**
   - Resumen de tu préstamo
   - Tabla completa mes a mes
   - Costo total del financiamiento

## 📁 Estructura del Proyecto

```
simulador-creditos/
├── app.py                 # Backend Flask
├── requirements.txt       # Dependencias
├── templates/
│   └── index.html        # HTML principal
└── static/
    ├── style.css         # Estilos CSS
    └── script.js         # JavaScript
```

## 💡 Ejemplo de Uso

**Ingreso:**
- Monto: $50,000
- TNA: 53%
- Plazo: 60 meses

**Resultado:**
- Cuota mensual: $1,234.56
- Total a devolver: $74,073.60
- Costo financiero: $24,073.60

## 📱 Responsivo

Funciona perfectamente en:
- ✅ Computadoras
- ✅ Tablets
- ✅ Smartphones

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de abrir un issue o enviar un pull request.

## 📄 Licencia

MIT License - Libre para usar y modificar

## 👩‍💻 Autor

**Natalia** - [GitHub](https://github.com/natalianeziz-cmd)

---

**¡Esperamos que te sea útil para tu educación financiera!** 💰📚

# 🤖 El Consultor de IA: Generador de Casos de Negocio

Una aplicación web interactiva construida con Streamlit que te ayuda a crear casos de negocio profesionales para proyectos de IA. Utiliza múltiples proveedores de IA (Gemini, Groq, OpenRouter) para generar borradores de alta calidad para cada sección de tu caso de negocio.

---

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Despliegue](#-despliegue)
- [Uso de la Aplicación](#-uso-de-la-aplicación)
- [Personalización Avanzada](#-personalización-avanzada)
- [Solución de Problemas](#-solución-de-problemas)
- [Preguntas Frecuentes](#-preguntas-frecuentes)

---

## ✨ Características

- **Múltiples Proveedores de IA**: Soporta Gemini, Groq y OpenRouter
- **Generación de Casos de Negocio**: Crea borradores profesionales en 4 áreas clave:
  - Definición del problema de negocio
  - Propuesta de solución de IA
  - Análisis de beneficios y ROI
  - Identificación de riesgos y estrategias de mitigación
- **Interfaz Intuitiva**: Diseño por pestañas con campos guiados
- **Flexibilidad de Modelos**: Cambia entre diferentes modelos de IA para comparar resultados
- **Transparencia**: Visualiza los prompts enviados a las APIs

---

## 🔧 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

### Software Necesario

1. **Python 3.8 o superior**
   - Verifica tu versión: `python --version` o `python3 --version`
   - Descarga desde: https://www.python.org/downloads/

2. **pip** (gestor de paquetes de Python)
   - Normalmente viene incluido con Python
   - Verifica: `pip --version` o `pip3 --version`

3. **Editor de texto** (recomendado)
   - Visual Studio Code, Sublime Text, Notepad++, o cualquier editor de tu preferencia

### Claves de API

Necesitarás al menos UNA de las siguientes claves de API (puedes usar todas si lo deseas):

1. **Google Gemini API Key**
   - Obtén tu clave en: https://makersuite.google.com/app/apikey
   - Es gratuita con límites generosos

2. **Groq API Key**
   - Regístrate en: https://console.groq.com
   - Ofrece acceso gratuito a modelos open-source

3. **OpenRouter API Key**
   - Regístrate en: https://openrouter.ai/
   - Proporciona acceso a múltiples modelos, algunos gratuitos

---

## 📥 Instalación

### Paso 1: Descomprimir el Archivo

1. Localiza el archivo `.zip` descargado
2. Descomprímelo en una ubicación de tu preferencia
3. Deberías ver una estructura similar a:
   ```
consultor-ia/
├── consultor-ia.py
|--- requirements.txt
|---Readme.md
├── .env        ← Debe estar aquí
└── venv/
   ```

### Paso 2: Abrir Terminal en la Carpeta del Proyecto

**En Windows:**
- Abre la carpeta del proyecto en el Explorador de Archivos
- Mantén presionada la tecla `Shift` y haz clic derecho en un espacio vacío
- Selecciona "Abrir ventana de PowerShell aquí" o "Abrir ventana de comandos aquí"

**En macOS/Linux:**
- Abre Terminal
- Navega a la carpeta: `cd /ruta/a/tu/carpeta/consultor-ia`

### Paso 3: Crear un Entorno Virtual (Recomendado)

Un entorno virtual mantiene las dependencias del proyecto aisladas.

```bash
# Crear entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

Verás que tu terminal ahora muestra `(venv)` al inicio de la línea.

### Paso 4: Instalar Dependencias

Instala todas las bibliotecas necesarias:

```bash
pip install streamlit google-generativeai openai python-dotenv
```

**Verificación:** Ejecuta `pip list` para confirmar que se instalaron:
- streamlit
- google-generativeai
- openai
- python-dotenv

---

## ⚙️ Configuración

### Paso 1: Crear el Archivo de Variables de Entorno

1. En la carpeta del proyecto, crea un archivo llamado `.env` (sin extensión)
2. Abre el archivo con tu editor de texto
3. Agrega las siguientes líneas:

```env
GEMINI_API_KEY=tu_clave_de_gemini_aqui
GROQ_API_KEY=tu_clave_de_groq_aqui
OPENROUTER_API_KEY=tu_clave_de_openrouter_aqui
```

### Paso 2: Configurar tus Claves de API

Reemplaza los valores de ejemplo con tus claves reales:

**Ejemplo con Gemini:**
```env
GEMINI_API_KEY=AIzaSyB1234567890abcdefghijklmnopqrstuvwx
GROQ_API_KEY=
OPENROUTER_API_KEY=
```

**Notas importantes:**
- **NO** agregues espacios alrededor del signo `=`
- **NO** uses comillas alrededor de las claves
- Puedes dejar vacías las claves que no uses
- Si solo tienes una clave, la aplicación funcionará igualmente
- **NUNCA** compartas este archivo ni subas tus claves a repositorios públicos

### Paso 3: Verificar la Configuración

Asegúrate de que tu archivo `.env` está en el mismo directorio que `consultor-ia`:

```
consultor-ia/
├── consultor-ia.py
|--- requirements.txt
|---Readme.md
├── .env        ← Debe estar aquí
└── venv/
```

---

## 🚀 Despliegue

### Ejecución Local (Desarrollo)

1. Asegúrate de que tu entorno virtual está activado (deberías ver `(venv)` en el terminal)

2. Ejecuta la aplicación:
   ```bash
   streamlit run consultor-ia.py
   ```

3. La aplicación se abrirá automáticamente en tu navegador en:
   - URL local: `http://localhost:8501`

4. Si no se abre automáticamente, copia y pega la URL mostrada en el terminal

### Detener la Aplicación

- En el terminal, presiona `Ctrl + C`

### Reiniciar la Aplicación

- Simplemente ejecuta de nuevo: `streamlit run consultor-ia.py`

---

## 🎯 Uso de la Aplicación

### Flujo de Trabajo Básico

1. **Selecciona tu Proveedor de IA**
   - En el panel lateral izquierdo, elige entre Gemini, Groq u OpenRouter
   - Solo verás los proveedores para los que configuraste claves de API

2. **Elige un Modelo Específico**
   - Cada proveedor ofrece diferentes modelos
   - Modelos recomendados para comenzar:
     - Gemini: `gemini-2.5-flash` (rápido y eficiente)
     - Groq: `deepseek-r1-distill-llama-70b` (excelente calidad)
     - OpenRouter: `deepseek/deepseek-chat-v3.1:free` (gratuito)

3. **Trabaja por Pestañas**

   **Pestaña 1: Problema de Negocio**
   - Define el área de negocio afectada
   - Describe el problema actual con detalle
   - Explica el impacto negativo que genera
   - Establece el nivel de urgencia
   - Haz clic en "Generar Borrador del Problema"

   **Pestaña 2: Solución de IA**
   - Selecciona el tipo de solución de IA
   - Describe cómo funcionará tu solución
   - Especifica la tecnología o plataforma
   - Indica la complejidad técnica
   - Haz clic en "Generar Borrador de la Solución"

   **Pestaña 3: Beneficios y ROI**
   - Ingresa la inversión inicial estimada
   - Define los costes anuales de operación
   - Estima el ahorro o ingreso anual esperado
   - Especifica el tiempo de implementación
   - Describe beneficios cualitativos
   - Haz clic en "Generar Análisis de Beneficios y ROI"
   - La app calculará automáticamente el ROI y el payback

   **Pestaña 4: Riesgos y Mitigación**
   - Marca los riesgos relevantes para tu proyecto
   - Añade riesgos específicos adicionales
   - Describe tus estrategias de mitigación
   - Haz clic en "Generar Análisis de Riesgos"

4. **Revisa y Refina**
   - Lee el borrador generado
   - Copia el texto para editarlo en tu documento
   - Expande "Para los curiosos" para ver el prompt utilizado
   - Prueba con diferentes modelos para comparar resultados

### Consejos de Uso

- **Sé específico**: Cuanto más detalle proporciones, mejor será el borrador generado
- **Itera**: No dudes en modificar los campos y regenerar el contenido
- **Compara modelos**: Diferentes modelos tienen diferentes estilos y enfoques
- **Personaliza**: Los borradores son puntos de partida, no productos finales

---

## 🎨 Personalización Avanzada

### Modificar los Modelos Disponibles

Para agregar o cambiar modelos, edita el diccionario `API_PROVIDERS` en `consultor-ia`:

```python
API_PROVIDERS = {
    "Gemini": {
        "api_key": GEMINI_API_KEY,
        "models": [
            "gemini-2.5-pro",      # Puedes agregar más modelos aquí
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite"
        ],
        "client_config": None
    },
    # ... otros proveedores
}
```

**Modelos disponibles por proveedor:**

**Gemini (Google):**
- `gemini-2.5-pro` - Modelo más potente
- `gemini-2.5-flash` - Equilibrio velocidad/calidad
- `gemini-2.5-flash-lite` - Más rápido y económico
- Consulta: https://ai.google.dev/gemini-api/docs/models

**Groq:**
- `openai/gpt-oss-120b`
- `meta-llama/llama-4-maverick-17b-128e-instruct`
- `deepseek-r1-distill-llama-70b`
- Consulta: https://console.groq.com/docs/models

**OpenRouter:**
- `deepseek/deepseek-r1-0528:free`
- `deepseek/deepseek-chat-v3.1:free`
- `qwen/qwen3-coder:free`
- `moonshotai/kimi-k2:free`
- Consulta: https://openrouter.ai/models

### Personalizar los Prompts del Sistema

Cada sección utiliza un prompt del sistema diferente. Puedes modificarlos para ajustar el tono y estilo:

**Ejemplo - Modificar el prompt del analista de ROI:**

Busca en `consultor-ia` la línea que dice:
```python
system_prompt = "Eres un analista financiero especializado en la evaluación de proyectos tecnológicos..."
```

Cámbiala por:
```python
system_prompt = "Eres un CFO con 20 años de experiencia. Hablas de forma directa y concisa, enfocándote en métricas clave..."
```

### Ajustar la Temperatura de Generación

La temperatura controla la creatividad de las respuestas (0 = conservador, 2 = muy creativo).

Busca esta línea en la función `generar_contenido_ia`:
```python
temperature=0.7,
```

Cámbiala según tus necesidades:
- `0.3` - Respuestas más predecibles y conservadoras
- `0.7` - Balance (valor por defecto)
- `1.2` - Respuestas más creativas y variadas

### Agregar Nuevos Campos de Entrada

**Ejemplo: Agregar un campo para "Stakeholders Clave"**

1. En la pestaña correspondiente, agrega:
```python
stakeholders = st.text_input("Stakeholders Clave", "CEO, CFO, Director de Operaciones")
```

2. Incluye la variable en el prompt de usuario:
```python
user_prompt = f"""
...
- Stakeholders: {stakeholders}
...
"""
```

### Modificar las Áreas de Negocio

Busca la línea con `st.selectbox("Área de Negocio Impactada"` y modifica la lista:

```python
area_negocio = st.selectbox(
    "Área de Negocio Impactada", 
    [
        "Marketing y Ventas",
        "Operaciones y Logística",
        "Tu Nueva Área",  # ← Agrega aquí
        "Otra Área"       # ← O aquí
    ]
)
```

### Cambiar el Estilo Visual

Modifica la configuración de página al inicio de `consultor-ia.py`:

```python
st.set_page_config(
    page_title="Tu Título Personalizado",
    page_icon="🚀",  # Cambia el emoji
    layout="wide",   # o "centered"
    initial_sidebar_state="expanded"  # o "collapsed"
)
```

---

## 🔍 Solución de Problemas

### Problema: "ModuleNotFoundError: No module named 'streamlit'"

**Solución:**
```bash
# Asegúrate de que tu entorno virtual está activado
# Luego instala las dependencias:
pip install streamlit google-generativeai openai python-dotenv
```

### Problema: "Clave de API no encontrada"

**Causas comunes:**
1. El archivo `.env` no está en la carpeta correcta
2. El nombre de la variable está mal escrito
3. Hay espacios alrededor del signo `=`

**Solución:**
- Verifica que `.env` está en el mismo directorio que `consultor-ia`
- Asegúrate de que no hay espacios: `GEMINI_API_KEY=tu_clave` (correcto)
- NO uses: `GEMINI_API_KEY = tu_clave` (incorrecto)

### Problema: "Error con la API de [Proveedor]"

**Posibles causas:**
1. La clave de API es inválida o expiró
2. Alcanzaste el límite de uso gratuito
3. El modelo especificado no existe o cambió de nombre

**Solución:**
- Verifica tu clave en el panel del proveedor
- Revisa los límites de tu cuenta
- Prueba con un modelo diferente

### Problema: La aplicación no se abre en el navegador

**Solución:**
- Copia manualmente la URL del terminal (usualmente `http://localhost:8501`)
- Verifica que no tienes otra instancia de Streamlit corriendo
- Prueba con otro puerto: `streamlit run consultor-ia.py --server.port 8502`

### Problema: "Address already in use"

**Solución:**
```bash
# El puerto 8501 ya está en uso
# Opción 1: Detén la aplicación anterior (Ctrl+C)
# Opción 2: Usa otro puerto
streamlit run consultor-ia.py --server.port 8502
```

### Problema: Los cambios en el código no se reflejan

**Solución:**
- Streamlit recarga automáticamente, pero a veces necesitas:
  1. Presionar `R` en la interfaz de Streamlit
  2. O refrescar el navegador (F5)
  3. O reiniciar completamente: Ctrl+C, luego `streamlit run consultor-ia.py`

---

## ❓ Preguntas Frecuentes

### ¿Puedo usar solo un proveedor de IA?

Sí, absolutamente. Solo configura la clave de API del proveedor que desees usar. La aplicación detectará automáticamente qué proveedores están disponibles.

### ¿Los datos que ingreso se envían a internet?

Sí, cuando generas un borrador, tu información se envía a la API del proveedor seleccionado (Gemini, Groq u OpenRouter). Lee las políticas de privacidad de cada proveedor para más detalles.

### ¿Puedo usar esta aplicación sin conexión a internet?

No, la aplicación requiere conexión a internet para comunicarse con las APIs de IA.

### ¿Cuánto cuesta usar esta aplicación?

La aplicación en sí es gratuita. Los costes dependen del proveedor de IA:
- **Gemini**: Tiene un tier gratuito generoso
- **Groq**: Ofrece acceso gratuito con límites
- **OpenRouter**: Tiene modelos gratuitos y de pago

### ¿Puedo comercializar los casos de negocio generados?

Sí, los contenidos generados son tuyos. Sin embargo, revisa los términos de servicio de cada proveedor de IA.

### ¿Cómo actualizo la aplicación si hay cambios?

Descarga la nueva versión, reemplaza el archivo `consultor-ia`, pero **mantén tu archivo `.env`** con tus claves.

### ¿Puedo personalizar completamente los prompts?

Sí, todos los prompts están en el código fuente (`consultor-ia`). Puedes modificarlos para ajustarlos a tus necesidades específicas.

### ¿Esta aplicación almacena mi información?

No, la aplicación no guarda ningún dato. Toda la información existe solo durante tu sesión activa.

### ¿Puedo agregar más pestañas o secciones?

Sí, puedes duplicar y modificar las pestañas existentes para agregar nuevas secciones a tu caso de negocio.

### ¿Qué hago si el modelo no está generando buenos resultados?

1. Proporciona más detalles en los campos de entrada
2. Prueba con un modelo diferente
3. Ajusta los prompts del sistema para mayor especificidad
4. Modifica la temperatura de generación

---

## 📚 Recursos Adicionales

- **Streamlit Documentation**: https://docs.streamlit.io/
- **Google Gemini API Docs**: https://ai.google.dev/docs
- **Groq Documentation**: https://console.groq.com/docs
- **OpenRouter API Docs**: https://openrouter.ai/docs

---

## 👨‍💻 Soporte y Contribuciones

Este proyecto fue creado para el curso "Integración de IA en el Entorno Empresarial" por Ángel Arias.

Para preguntas o sugerencias, contacta al instructor del curso.

---

## 📝 Licencia

Este proyecto es material educativo del curso mencionado, no está permitida su venta. Consulta con el instructor sobre los términos de uso y redistribución.

---

**¡Felicidades! Ya estás listo para crear casos de negocio profesionales con IA. 🚀**
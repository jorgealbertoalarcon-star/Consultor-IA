import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI

# --- CONFIGURACIÓN DE PÁGINA (DEBE SER LO PRIMERO) ---
st.set_page_config(
    page_title="El Consultor de IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CARGA DE CLAVES Y CONFIGURACIÓN DE MODELOS ---
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Diccionario de proveedores y sus modelos
API_PROVIDERS = {
    "Gemini": {
        "api_key": GEMINI_API_KEY,
        "models": ["gemini-2.5-pro", "gemini-2.5-flash", "gemini-2.5-flash-lite"],
        "client_config": None
    },
    "Groq": {
        "api_key": GROQ_API_KEY,
        "models": ["openai/gpt-oss-120b", "meta-llama/llama-4-maverick-17b-128e-instruct", "deepseek-r1-distill-llama-70b"],
        "client_config": {"base_url": "https://api.groq.com/openai/v1"}
    },
    "OpenRouter": {
        "api_key": OPENROUTER_API_KEY,
        "models": ["deepseek/deepseek-r1-0528:free", "deepseek/deepseek-chat-v3.1:free", "qwen/qwen3-coder:free", "moonshotai/kimi-k2:free"],
        "client_config": {"base_url": "https://openrouter.ai/api/v1", "default_headers": {"HTTP-Referer": "http://localhost", "X-Title": "Curso IA Udemy"}}
    },
}

# --- FUNCIÓN DE GENERACIÓN DE CONTENIDO UNIFICADA ---
def generar_contenido_ia(provider, model, system_prompt, user_prompt, imagen=None):
    """Llama a la API del proveedor seleccionado para generar contenido."""
    config = API_PROVIDERS.get(provider)
    if not config or not config["api_key"]:
        st.error(f"🚨 Clave de API para {provider} no encontrada. Por favor, configúrala en tu archivo .env.")
        return None

    try:
        if provider == "Gemini":
            if imagen:
                st.warning("El análisis de imágenes no está implementado en este laboratorio específico para Gemini. Ignorando la imagen.")
            
            genai.configure(api_key=config["api_key"])
            gemini_model = genai.GenerativeModel(
                model_name=model,
                system_instruction=system_prompt
            )
            response = gemini_model.generate_content(user_prompt)
            return response.text
        
        elif provider in ["Groq", "OpenRouter"]:
            if imagen:
                st.warning(f"El proveedor {provider} no soporta análisis de imágenes. Ignorando la imagen.")
            
            client = OpenAI(api_key=config["api_key"], **config["client_config"])
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                model=model,
                temperature=0.7,
            )
            return chat_completion.choices[0].message.content

    except Exception as e:
        st.error(f"Ha ocurrido un error con la API de {provider}: {e}")
        return None

# --- UI DE LA APLICACIÓN ---
with st.sidebar:
    st.title("🔧 Panel de Control")
    st.markdown("Selecciona el 'cerebro' de IA que quieres usar.")
    
    providers_con_key = [p for p, c in API_PROVIDERS.items() if c["api_key"]]
    if not providers_con_key:
        st.error("No se ha configurado ninguna API Key en el archivo .env")
        st.stop()
        
    selected_provider = st.selectbox("Proveedor de IA:", providers_con_key)
    
    available_models = API_PROVIDERS[selected_provider]["models"]
    selected_model = st.selectbox("Modelo Específico:", available_models)
    
    st.markdown("---")
    st.title("📘 Guía del Laboratorio")
    st.markdown("""
    ¡Bienvenido al **Consultor de IA**! Esta herramienta te ayudará a generar borradores para tu **Caso de Negocio de IA**.
    
    **¿Cómo funciona?**
    1.  Elige un proveedor y modelo de IA en el Panel de Control.
    2.  Navega por las pestañas y rellena los campos.
    3.  Haz clic en "Generar Borrador".
    4.  Compara los resultados entre diferentes modelos.
    """)
    st.markdown("---")
    st.success(f"✅ Usando {selected_provider} con el modelo:\n`{selected_model}`")
    st.markdown("---")
    st.caption('Creado para el curso "Integración de IA en el Entorno Empresarial" por Ángel Arias')

st.title("🤖 El Consultor de IA: Generador de Casos de Negocio")
st.markdown("Transforma tus ideas en un Caso de Negocio profesional. Completa los campos y deja que la IA que elijas te ayude a redactar.")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["🎯 1. Problema de Negocio", "💡 2. Solución de IA", "💰 3. Beneficios y ROI", "⚠️ 4. Riesgos y Mitigación"])

# ========== PESTAÑA 1: PROBLEMA DE NEGOCIO ==========
with tab1:
    st.header("🎯 Define el Problema que quieres Resolver")
    st.info("Un buen Caso de Negocio empieza con un 'dolor' claro y medible.")
    
    col1, col2 = st.columns(2)
    with col1:
        area_negocio = st.selectbox("Área de Negocio Impactada", ["Marketing y Ventas", "Operaciones y Logística", "Finanzas y Contabilidad", "Recursos Humanos", "I+D y Producto", "Soporte al Cliente"])
    with col2:
        urgencia = st.select_slider("Nivel de Urgencia del Problema", ["Baja", "Media", "Alta", "Crítica"], value="Alta")

    problema_actual = st.text_area("Describe el Problema Actual (Sé específico)", "El equipo de soporte al cliente tarda en promedio 48 horas en dar una primera respuesta a los tickets, lo que genera una baja puntuación de satisfacción (NPS).", height=100)
    impacto_negativo = st.text_area("Describe el Impacto Negativo (financiero, de eficiencia, de reputación)", "Esto provoca que un 15% de los clientes con problemas no repitan la compra y genera una sobrecarga de trabajo en el equipo de soporte.", height=100)

    if st.button("Generar Borrador del Problema", key="btn_problema", type="primary"):
        if problema_actual and impacto_negativo:
            system_prompt = "Eres un consultor de estrategia de negocio experto en la redacción de casos de negocio para proyectos de IA. Tu tono es profesional, claro y orientado a resultados."
            user_prompt = f"""
            Analiza la siguiente información y redacta una sección formal y convincente de "Problema de Negocio" para un caso de negocio:
            - Área: {area_negocio}
            - Problema: {problema_actual}
            - Impacto: {impacto_negativo}
            - Urgencia: {urgencia}

            Elabora un párrafo convincente que explique el problema, su impacto tangible y la necesidad de actuar.
            """
            
            with st.spinner(f"🧠 {selected_provider} está redactando el borrador..."):
                borrador = generar_contenido_ia(selected_provider, selected_model, system_prompt, user_prompt)
                if borrador:
                    st.subheader(f"Borrador Sugerido por {selected_provider} ({selected_model}):")
                    st.markdown(borrador)
                    with st.expander("🤓 Para los curiosos: Ver el Prompt enviado"):
                        st.code(user_prompt, language="markdown")
        else:
            st.warning("Por favor, completa todos los campos para generar el borrador.")

# ========== PESTAÑA 2: SOLUCIÓN DE IA ==========
with tab2:
    st.header("💡 Propón tu Solución de IA")
    st.info("Aquí defines QUÉ tecnología de IA usarás y CÓMO resolverá el problema.")
    
    col1, col2 = st.columns(2)
    with col1:
        tipo_ia = st.selectbox("Tipo de Solución de IA", [
            "Procesamiento de Lenguaje Natural (NLP)",
            "Visión por Computadora",
            "Aprendizaje Automático (ML) - Predicción",
            "Chatbot / Asistente Virtual",
            "Automatización Inteligente (RPA + IA)",
            "Sistema de Recomendación",
            "Otra"
        ])
    with col2:
        complejidad = st.select_slider("Complejidad Técnica Estimada", ["Baja", "Media", "Alta"], value="Media")
    
    descripcion_solucion = st.text_area("Describe tu Solución de IA (¿Qué hace? ¿Cómo funciona?)", "Implementar un chatbot con IA generativa que responda automáticamente a las preguntas frecuentes de los clientes y derive solo los casos complejos al equipo humano.", height=100)
    tecnologia = st.text_input("Tecnología o Plataforma que usarás", "API de Google Gemini Pro integrada con nuestro sistema de tickets (Zendesk)")
    
    if st.button("Generar Borrador de la Solución", key="btn_solucion", type="primary"):
        if descripcion_solucion and tecnologia:
            system_prompt = "Eres un arquitecto de soluciones de IA experto. Tu objetivo es describir una solución tecnológica de forma clara y concisa para una audiencia de negocio, destacando el valor y la viabilidad."
            user_prompt = f"""
            Analiza la siguiente información y redacta una sección formal y convincente de "Solución de IA Propuesta" para un caso de negocio:
            - Tipo de IA: {tipo_ia}
            - Descripción: {descripcion_solucion}
            - Tecnología: {tecnologia}
            - Complejidad: {complejidad}

            Elabora una descripción clara de la solución, explicando cómo la IA resolverá el problema de negocio identificado. Incluye los componentes clave y el valor diferencial de esta aproximación.
            """
            
            with st.spinner(f"🧠 {selected_provider} está diseñando la solución..."):
                borrador = generar_contenido_ia(selected_provider, selected_model, system_prompt, user_prompt)
                if borrador:
                    st.subheader(f"Borrador Sugerido por {selected_provider} ({selected_model}):")
                    st.markdown(borrador)
                    with st.expander("🤓 Para los curiosos: Ver el Prompt enviado"):
                        st.code(user_prompt, language="markdown")
        else:
            st.warning("Por favor, completa todos los campos para generar el borrador.")

# ========== PESTAÑA 3: BENEFICIOS Y ROI ==========
with tab3:
    st.header("💰 Estima los Beneficios y el Retorno de la Inversión (ROI)")
    st.info("Cuantifica el valor que generará tu proyecto de IA.")
    
    col1, col2 = st.columns(2)
    with col1:
        inversion_estimada = st.number_input("Inversión Inicial Estimada (€)", min_value=0, value=25000, step=1000)
        costes_anuales = st.number_input("Costes Anuales de Operación (€)", min_value=0, value=8000, step=500)
    with col2:
        ahorro_anual = st.number_input("Ahorro o Ingreso Anual Esperado (€)", min_value=0, value=90000, step=1000)
        tiempo_implementacion = st.slider("Tiempo de Implementación (meses)", 1, 24, 4)
    
    beneficios_cualitativos = st.text_area("Beneficios Cualitativos (mejora de satisfacción, imagen de marca, etc.)", "Mejora radical de la experiencia del cliente con soporte 24/7. Liberación del equipo humano para enfocarse en tareas de alto valor. Posicionamiento de la marca como innovadora.", height=100)
    
    if st.button("Generar Análisis de Beneficios y ROI", key="btn_roi", type="primary"):
        roi_simple = ((ahorro_anual - costes_anuales) / inversion_estimada) * 100 if inversion_estimada > 0 else 0
        payback = inversion_estimada / (ahorro_anual - costes_anuales) if (ahorro_anual - costes_anuales) > 0 else 999
        
        st.metric("ROI Anual Estimado (simple)", f"{roi_simple:.1f}%")
        st.metric("Periodo de Recuperación (Payback)", f"{payback:.1f} años" if payback < 999 else "No rentable")
        
        system_prompt = "Eres un analista financiero especializado en la evaluación de proyectos tecnológicos. Tu objetivo es justificar una inversión de forma clara y convincente, combinando métricas financieras con valor estratégico."
        user_prompt = f"""
        Analiza la siguiente información y redacta una sección formal y convincente de "Beneficios y ROI" para un caso de negocio:
        - Inversión inicial: {inversion_estimada}€
        - Costes anuales: {costes_anuales}€
        - Ahorro/Ingreso anual: {ahorro_anual}€
        - Tiempo de implementación: {tiempo_implementacion} meses
        - ROI anual calculado: {roi_simple:.1f}%
        - Payback: {payback:.1f} años
        - Beneficios cualitativos: {beneficios_cualitativos}

        Elabora una sección que presente tanto los beneficios cuantitativos como cualitativos de manera convincente. Destaca el valor de negocio de esta inversión y justifica su rentabilidad.
        """
        
        with st.spinner(f"🧠 {selected_provider} está analizando el valor..."):
            borrador = generar_contenido_ia(selected_provider, selected_model, system_prompt, user_prompt)
            if borrador:
                st.subheader(f"Borrador Sugerido por {selected_provider} ({selected_model}):")
                st.markdown(borrador)
                with st.expander("🤓 Para los curiosos: Ver el Prompt enviado"):
                    st.code(user_prompt, language="markdown")

# ========== PESTAÑA 4: RIESGOS Y MITIGACIÓN ==========
with tab4:
    st.header("⚠️ Identifica los Riesgos y cómo Mitigarlos")
    st.info("Todo proyecto tiene riesgos. Identifícalos y propón soluciones.")
    
    st.subheader("Selecciona los Riesgos Relevantes para tu Proyecto")
    
    col1, col2 = st.columns(2)
    with col1:
        riesgo_tecnico = st.checkbox("Riesgo Técnico (la tecnología no funciona como se esperaba)", value=True)
        riesgo_datos = st.checkbox("Riesgo de Calidad de Datos (datos insuficientes o de mala calidad)", value=True)
        riesgo_costes = st.checkbox("Riesgo de Sobrecostes (el proyecto excede el presupuesto)", value=False)
    with col2:
        riesgo_adopcion = st.checkbox("Riesgo de Adopción (los usuarios no usan la solución)", value=True)
        riesgo_regulatorio = st.checkbox("Riesgo Regulatorio o Ético (privacidad, sesgos, compliance)", value=True)
    
    riesgos_adicionales = st.text_area("Otros Riesgos Específicos de tu Proyecto", "El chatbot podría dar respuestas incorrectas ('alucinaciones'), dañando la confianza del cliente.", height=80)
    
    mitigaciones = st.text_area("Estrategias de Mitigación que implementarás", "Realizar una fase piloto de 3 meses, capacitar al equipo de soporte para trabajar en colaboración con el chatbot, implementar un sistema de escalado humano robusto y auditar las respuestas del bot.", height=100)
    
    if st.button("Generar Análisis de Riesgos", key="btn_riesgos", type="primary"):
        riesgos_seleccionados = []
        if riesgo_tecnico: riesgos_seleccionados.append("Riesgo Técnico")
        if riesgo_datos: riesgos_seleccionados.append("Riesgo de Calidad de Datos")
        if riesgo_adopcion: riesgos_seleccionados.append("Riesgo de Adopción")
        if riesgo_regulatorio: riesgos_seleccionados.append("Riesgo Regulatorio/Ético")
        if riesgo_costes: riesgos_seleccionados.append("Riesgo de Sobrecostes")
        
        system_prompt = "Eres un director de proyectos de IA con amplia experiencia. Tu especialidad es anticipar problemas y crear planes de contingencia robustos. Tu tono debe transmitir preparación y confianza, no alarma."
        user_prompt = f"""
        Analiza la siguiente información y redacta una sección formal y convincente de "Riesgos y Estrategias de Mitigación" para un caso de negocio:
        - Riesgos principales identificados: {', '.join(riesgos_seleccionados)}
        - Riesgos adicionales específicos: {riesgos_adicionales if riesgos_adicionales else "Ninguno especificado"}
        - Estrategias de mitigación generales: {mitigaciones}

        Elabora una sección que presente los riesgos de manera honesta pero constructiva, y que demuestre que el equipo tiene un plan sólido para gestionarlos.
        """
        
        with st.spinner(f"🧠 {selected_provider} está evaluando los riesgos..."):
            borrador = generar_contenido_ia(selected_provider, selected_model, system_prompt, user_prompt)
            if borrador:
                st.subheader(f"Borrador Sugerido por {selected_provider} ({selected_model}):")
                st.markdown(borrador)
                with st.expander("🤓 Para los curiosos: Ver el Prompt enviado"):
                    st.code(user_prompt, language="markdown")

# ========== FOOTER ==========
st.markdown("---")
st.markdown("### 💡 Próximos Pasos")
st.info("""
**¡Excelente trabajo!** Ahora que tienes los borradores de tu Caso de Negocio:
1. **Revisa** cada sección y personalízala con tu conocimiento del negocio.
2. **Valida** los números y supuestos con tu equipo.
3. **Combina** todas las secciones en un documento único.
4. **Presenta** tu Caso de Negocio a los stakeholders.

Recuerda: La IA es tu copiloto, pero tú eres quien toma las decisiones finales.
""")
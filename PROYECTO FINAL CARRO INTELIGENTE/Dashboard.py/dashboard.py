from streamlit_autorefresh import st_autorefresh
import streamlit as st

# ======================================
# CONFIG
# ======================================

st.set_page_config(
    page_title="Carro Inteligente",
    page_icon="🚗",
    layout="centered"
)
st_autorefresh(interval=1000, key="refresco")

# ======================================
# ESTILOS
# ======================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #334155);
}

h1 {
    text-align: center;
    color: white;
}

h2, h3 {
    color: white;
}

.card {
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: white;
    margin-bottom: 20px;
}

.estado {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ======================================
# TITULO
# ======================================

st.title("🚗 Carro Inteligente")

st.caption(
    "Proyecto Integrador | Arduino UNO + TCS3200 + L293D + Python + Streamlit"
)

st.markdown(
    "<h3 style='text-align:center;'>Sistema Inteligente de Detección de Colores</h3>",
    unsafe_allow_html=True
)

# ======================================
# COLOR
# ======================================

import serial
import time

@st.cache_resource
def conectar_arduino():

    try:
        arduino = serial.Serial("COM4", 9600, timeout=1)
        time.sleep(2)
        return arduino

    except:
        return None

if "color_actual" not in st.session_state:
    st.session_state.color_actual = "SIN DATOS"

arduino = conectar_arduino()
st.write("Arduino:", arduino)
st.write("Bytes disponibles:", arduino.in_waiting)



if arduino:

    try:

        datos = arduino.read(arduino.in_waiting)

       # st.write("RAW:", datos)

        linea = datos.decode(
            errors="ignore"
        )
       #  st.write("TEXTO:",linea)

       # st.write("DEBUG VERDE:", "Color detectado: VERDE" in linea)
       # st.write("DEBUG AZUL:", "Color detectado: AZUL" in linea)
       # st.write("DEBUG ROJO:", "Color detectado: ROJO" in linea)

        if "Color detectado: NEGRO" in linea:
            st.session_state.color_actual = "NEGRO"

        elif "Color detectado: BLANCO" in linea:
            st.session_state.color_actual = "BLANCO"

        elif "Color detectado: ROJO" in linea:
            st.session_state.color_actual = "ROJO"

        elif "Color detectado: VERDE" in linea:
            st.session_state.color_actual = "VERDE"

        elif "Color detectado: AZUL" in linea:
            st.session_state.color_actual = "AZUL"
        #st.write("COLOR SESSION:", st.session_state.color_actual)

    except Exception as e:

        st.write("ERROR:", e)

st.markdown("---")

st.subheader("🎨 Indicador Visual de Color")

color = st.session_state.color_actual
#st.write("COLOR ACTUAL VISUAL:", color)
#st.success(f"ENTRÉ A LA ZONA VISUAL - {color}")
#st.write("ANTES DEL IF")

if color == "VERDE":

    st.markdown("""
    <div class='card'
    style='background:linear-gradient(135deg,#16a34a,#22c55e);'>
    🟢<br><br>
    COLOR DETECTADO<br><br>
    VERDE
    </div>
    """, unsafe_allow_html=True)

elif color == "ROJO":

    st.markdown("""
    <div class='card'
    style='background:linear-gradient(135deg,#b91c1c,#ef4444);'>
    🔴<br><br>
    COLOR DETECTADO<br><br>
    ROJO
    </div>
    """, unsafe_allow_html=True)

elif color == "AZUL":

    st.markdown("""
    <div class='card'
    style='background:linear-gradient(135deg,#1d4ed8,#3b82f6);'>
    🔵<br><br>
    COLOR DETECTADO<br><br>
    AZUL
    </div>
    """, unsafe_allow_html=True)

elif color == "NEGRO":

    st.markdown("""
    <div class='card'
    style='background:linear-gradient(135deg,#111827,#374151);'>
    ⚫<br><br>
    COLOR DETECTADO<br><br>
    NEGRO
    </div>
    """, unsafe_allow_html=True)

elif color == "BLANCO":

    st.markdown("""
    <div class='card'
    style='background:white;color:black;'>
    ⚪<br><br>
    COLOR DETECTADO<br><br>
    BLANCO
    </div>
    """, unsafe_allow_html=True)

# ======================================
# FUNCIONALIDADES
# ======================================

st.markdown("---")

st.subheader("⚙️ Funcionalidades Implementadas")

st.write("🎨 Detección de colores mediante sensor TCS3200")
st.write("🚗 Control de movimiento mediante driver L293D")
st.write("🎙️ Control por voz desarrollado en Python")
st.write("💻 Interfaz web desarrollada con Streamlit")
st.write("🤖 Chatbot informativo del proyecto")

# ======================================
# ESTADO DEL SISTEMA
# ======================================

st.markdown("---")

st.subheader("📡 Estado del Sistema")

col1, col2 = st.columns(2)

with col1:
    st.success("✅ Arduino UNO")
    st.success("✅ Sensor TCS3200")
    st.success("✅ Driver L293D")

with col2:
    st.success("✅ Dashboard Streamlit")
    st.success("✅ Control por Voz")
    st.success("✅ Chatbot")

# ======================================
# CHATBOT
# ======================================

st.markdown("---")

st.subheader("🤖 Chatbot del Proyecto")

st.markdown("""
**Preguntas sugeridas:**

- ¿Qué sensor utiliza?
- ¿Cómo funciona Arduino?
- ¿Qué hace el L293D?
- ¿Cómo funciona el proyecto?
- ¿Para qué sirve el control por voz?
""")

pregunta = st.text_input(
    "Haz una pregunta sobre el proyecto"
)

if pregunta:

    pregunta = pregunta.lower()

    if "sensor" in pregunta:

        st.success(
            "El proyecto utiliza un sensor TCS3200 para la detección de colores."
        )

    elif "arduino" in pregunta:

        st.success(
            "Arduino UNO procesa la información recibida del sensor y ejecuta las acciones programadas."
        )

    elif "motor" in pregunta:

        st.success(
            "Los motores DC permiten el desplazamiento del vehículo."
        )

    elif "l293d" in pregunta:

        st.success(
            "El driver L293D controla el sentido de giro y la potencia enviada a los motores."
        )

    elif "voz" in pregunta:

        st.success(
            "El sistema incorpora control por voz desarrollado en Python."
        )

    elif "funciona" in pregunta:

        st.success(
            "El sensor detecta colores, Arduino procesa la información y ejecuta acciones según la lógica programada."
        )

    elif "color" in pregunta:

        st.success(
            "El sensor TCS3200 identifica colores mediante la medición de componentes RGB."
        )

    else:

        st.warning(
            "Pregunta no registrada en la base de conocimientos."
        )

# ======================================
# PIE
# ======================================

st.markdown("---")

st.info(
    "🚗 Proyecto Final | Arduino + Python + Streamlit + TCS3200 + L293D"
)


import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key="sk-23435310c79b450b96dd66f2a6d85214",
    base_url="https://api.deepseek.com"
)

st.title("🤖 Chatbot de Semiconductores 2026")

pregunta = st.text_input("Escribe tu pregunta:")

if pregunta:
    p = pregunta.lower()

    if "innovacion" in p:
        st.write("La innovación en educación con semiconductores permite el uso de Arduino, IoT y laboratorios virtuales.")

    elif "proyectos" in p:
        st.write("Los proyectos incluyen robótica, automatización y sistemas digitales aplicados.")

    elif "futuro" in p:
        st.write("El futuro incluye inteligencia artificial, chips más pequeños y mayor integración tecnológica.")

    else:
        respuesta = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "Eres experto en semiconductores en 2026"},
                {"role": "user", "content": pregunta}
            ]
        )

        st.write(respuesta.choices[0].message.content)
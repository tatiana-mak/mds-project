import streamlit as st
import requests

st.title("Контроль качества металла")

temp = st.number_input("Температура (°C)", 800, 1300, 1000)
speed = st.number_input("Скорость (м/с)", 0, 30, 10)

if st.button("Проверить"):
    r = requests.post(
        "http://localhost:8080/check",
        json = {"temperature": temp, "speed": speed}
    )
    res = r.json()

    if res["quality"] == "Годен":
        st.success("Годен")
    else:
        st.error("Брак")
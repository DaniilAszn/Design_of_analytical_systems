import streamlit as st
import joblib
import pandas as pd


st.set_page_config(page_title="Classification cars", page_icon=":🚘:")


model = joblib.load('RandomForestAutomobiles.pkl')


st.title("Классификация автомобиля")


st.subheader("Ввод данных:")
param1 = st.number_input("Введите значение массы (в кг)", min_value=750.0, max_value=3500.0)
param1 = (param1 - 1970) / 390
param2 = st.number_input("Введите значение максимальной скорости (в км/ч)", min_value=90.0, max_value=290.0)
param2 = (param2 - 209) / 45


st.subheader("Результат классификации:")
if st.button("Получить ответ"):
    input_features = pd.DataFrame({
        'Полная масса [кг]': [param1],
        'Максимальная скорость [км/ч]': [param2]
    })

    prediction = model.predict(input_features)[0]

    st.write(f"Тип кузова: {prediction}")

import streamlit as st
import time
import joblib
import pandas as pd

# Setting
st.set_page_config(page_title="Classification cars", page_icon=":🚘:")


model = joblib.load('Baseline_SVM.pkl')


st.title("Классификация автомобиля")


st.subheader("Ввод данных:")
param1 = st.number_input("Введите значение массы (в кг)", min_value=750.0, max_value=3500.0)
param1 = (param1 - 2000) / 990
param2 = st.number_input("Введите значение максимальной скорости (в км/ч)", min_value=80.0, max_value=300.0)
param2 = (param2 - 176) / 39


st.subheader("Результат классификации:")
if st.button("Получить ответ"):
    input_features = pd.DataFrame({
        'Полная масса [кг]': [param1],
        'Максимальная скорость [км/ч]': [param2]
    })


    prediction = model.predict(input_features)[0]
    probability = round(max(model.predict_proba(input_features)[0]), 5)


    col1, _ = st.columns([1, 1])

    progress_bar = col1.progress(0)
    for perc_completed in range(100):
        time.sleep(0.03)
        progress_bar.progress(perc_completed + 1)
    col1.success("Данные успешно загружены!")


    with st.spinner("Модель готовит ответ, нужно немного подождать"):
        time.sleep(10)


    st.write(f"Тип кузова: {prediction}")
    st.write(f"Уверенность модели в классификации: {probability * 100}%")

    col2, _ = st.columns([1, 1])
    col2.success('Модель успешно выдала ответ!')

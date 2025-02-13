import streamlit as st
import time
import joblib
import pandas as pd

# Функция для проверки корректности ввода
def validate_input_params(p_1, p_2):
    MIN_VALUE_1 = 750
    MAX_VALUE_1 = 3500
    MIN_VALUE_2 = 80
    MAX_VALUE_2 = 300
    if not(p_1) or not(p_2):
        return "имеются незаполненные поля!"
    if not p_1.isdigit() or not p_2.isdigit():
        return "введённые значения должны быть числами!"
    p_1, p_2 = float(p_1), float(p_2)
    if not(MIN_VALUE_1 <= p_1 <= MAX_VALUE_1):
        return f"масса должна быть в пределах от {MIN_VALUE_1} до {MAX_VALUE_1} кг!"
    if not(MIN_VALUE_2 <= p_2 <= MAX_VALUE_2):
        return f"максимальная скорость должна быть в пределах от {MIN_VALUE_2} до {MAX_VALUE_2} км/ч!"
    return None

# Состояние для хранения результата
if "message" not in st.session_state:
    st.session_state.message = ""

# Setting
st.set_page_config(page_title="Classification cars", page_icon=":🚘:")

# Интеграция модели
model = joblib.load("Baseline_SVM.pkl")


st.title("Классификация автомобиля")


st.subheader("Ввод данных:")
input_param_1 = st.text_input("Введите значение: масса (в кг)")
input_param_2 = st.text_input("Введите значение: максимальная скорость (в км/ч)")



st.subheader("Результат классификации:")
if st.button("Получить ответ"):
    error_message = validate_input_params(input_param_1, input_param_2)

    if error_message:
        st.session_state.message = f"Ошибка ввода: {error_message}"
        st.error(st.session_state.message)
    else:
        st.session_state.message = "Данные введены корректно! Система загружает данные в модель!"
        st.success(st.session_state.message)

        param_1_scaled = (float(input_param_1) - 2000) / 990
        param_2_scaled = (float(input_param_2) - 176) / 39
        input_features = pd.DataFrame({
            'Полная масса [кг]': [param_1_scaled],
            'Максимальная скорость [км/ч]': [param_2_scaled]
        })

        prediction = model.predict(input_features)[0]
        probability = max(model.predict_proba(input_features)[0])

        col_1_success_load, col_1_progress = st.columns([0.8, 1.5])

        progress_bar = col_1_progress.progress(0)
        for perc_completed in range(100):
            time.sleep(0.03)
            progress_bar.progress(perc_completed + 1)
        col_1_success_load.success("Данные успешно загружены!")

        with st.spinner("Модель готовит ответ, нужно немного подождать"):
            time.sleep(10)

        st.markdown(f"Тип кузова: **{prediction.lower()}**, уверенность модели в классификации - **{round(probability * 100, 2)}%**")

        col_2_success_classify, _ = st.columns([0.6, 1])
        col_2_success_classify.success('Модель успешно выдала ответ!')

import streamlit as st


st.set_page_config(page_title="Info about Model", page_icon=":🤖:")


st.title("Информация о модели")


st.subheader("RandomForest:")
st.write("Модель, интегрированная в АС, является моделью случайного леса. В ходе анализа данных было установлено, что "
         "данная модель демонстрирует наилучшие метрики (по сравнению с логистической регрессией, которая была взята в"
         "качестве baseline решения).")
st.write("Ниже приведены результаты оценки качества классификации модели.")


st.subheader("Classification report:")
st.image("classification_report.PNG", use_column_width=True)


st.subheader("Confusion matrix:")
st.image("confusion_matrix.PNG", use_column_width=True)
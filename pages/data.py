import streamlit as st
import pandas as pd
import plotly.graph_objects as go


st.set_page_config(page_title="Info about Data", page_icon=":📄:")


st.title("Информация о данных")


st.subheader("Исходная выборка:")
df = pd.read_excel('Automobiles.xlsx')
st.write(df)


st.subheader("Сводная информация:")
st.write("Ниже представлена общая статистика по набору данных.")
st.write(df.describe())


st.subheader("Распространённость различных типов кузова:")
st.write("Ниже приведена круговая диаграмма, демонстрирующая распространённость типов кузова.")
fig = go.Figure(
    go.Pie(
    labels = df['Тип кузова'].unique(),
    values = df['Тип кузова'].value_counts(),
    hoverinfo = "label+percent",
    textinfo = "value"
))

st.plotly_chart(fig, use_container_width=True)


st.subheader("Графики распределения:")
st.write("Ниже приведены распределения для физических характеристик.")
df_pdf = df.drop(columns=['id_modification'])
numeric_cols = df_pdf.select_dtypes(include='number').columns.tolist()
selected_col = st.selectbox("Выберите столбец:", numeric_cols)

fig = go.Figure()
fig.add_trace(go.Histogram(x=df_pdf[selected_col], nbinsx=30))
fig.update_layout(
    xaxis_title=selected_col,
    yaxis_title="Частота",
    bargap=0.1
)

st.plotly_chart(fig, use_container_width=True)

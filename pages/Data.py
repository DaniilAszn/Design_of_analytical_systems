import streamlit as st
import math as m
import pandas as pd
import plotly.graph_objects as go

# Setting
st.set_page_config(page_title="Info about Data", page_icon=":📄:")


st.title("Информация о данных")
df_X = pd.read_csv('DataInModel_X.csv')
df_y = pd.read_csv('DataInModel_y.csv')
df_X.drop(df_X.columns[0], axis=1, inplace=True)


st.subheader("Сводная статистика по исходной выборке:")
st.write(df_X.describe())


st.subheader("Распространённость различных типов кузова:")
fig = go.Figure(
    go.Pie(
    labels=df_y['Тип кузова'].unique(),
    values=df_y['Тип кузова'].value_counts(),
    hoverinfo="label+percent",
    textinfo="value"
))

st.plotly_chart(fig, use_container_width=True)


st.subheader("Графики распределения физических характеристик:")
numeric_cols = df_X.select_dtypes(include='number').columns.tolist()
selected_col = st.selectbox("Выберите столбец:", numeric_cols)

BINS = 1 + m.ceil(m.log(len(df_X), 2))

fig = go.Figure()
fig.add_trace(go.Histogram(x=df_X[selected_col], nbinsx=BINS))
fig.update_layout(
    xaxis_title=selected_col,
    yaxis_title="Частота",
    bargap=0.1
)

st.plotly_chart(fig, use_container_width=True)

import streamlit as st

# Setting
st.set_page_config(page_title="Info about Model", page_icon=":🤖:")


st.title("Информация о модели")


st.subheader("Support Vector Machine:")
st.write("Модель, интегрированная в систему, является моделью машины опорных векторов:")
st.latex(r'''    
            \frac{1}{2} ||w||^2 + С \sum_{i=1}^l max(0, 1 - \underbrace{y_i (<w, x_i> + \ w_0)}_{отступ}) \rightarrow min
            ''')

st.link_button("Подробнее о модели SVM", "https://habr.com/ru/companies/ods/articles/484148/")


st.subheader("Показатели качества классификации:")
st.write("Матрица ошибок")
st.image("ConfMat.PNG", width=480)


col_acc, _ = st.columns([2, 1])
col_acc.metric(label="Accuracy", value="0.88")


Pr_mean = 0.66
Rc_mean = 0.93
F1_mean = 0.70


st.write("**Класс: внедорожник**")
Pr_1 = 0.85
Rc_1 = 0.93
F1_1 = 0.89

col1_pr, col1_rc, col1_f1 = st.columns([1, 1, 1])
col1_pr.metric(label="Precision", value=f"{Pr_1}", delta=f"{round(Pr_1 - Pr_mean, 2)}")
col1_rc.metric(label="Recall", value=f"{Rc_1}", delta=f"{round(Rc_1 - Rc_mean, 2)}")
col1_f1.metric(label="F1-score", value=f"{F1_1}", delta=f"{round(F1_1 - F1_mean, 2)}")


st.markdown("**Класс: лифтбэк**")
Pr_2 = 0.16
Rc_2 = 1.00
F1_2 = 0.28

col2_pr, col2_rc, col2_f1 = st.columns([1, 1, 1])
col2_pr.metric(label="Precision", value=f"{Pr_2}", delta=f"{round(Pr_2 - Pr_mean, 2)}")
col2_rc.metric(label="Recall", value=f"{Rc_2}", delta=f"{round(Rc_2 - Rc_mean, 2)}")
col2_f1.metric(label="F1-score", value=f"{F1_2}", delta=f"{round(F1_2 - F1_mean, 2)}")


st.markdown("**Класс: седан**")
Pr_3 = 0.99
Rc_3 = 0.87
F1_3 = 0.92

col3_pr, col3_rc, col3_f1 = st.columns([1, 1, 1])
col3_pr.metric(label="Precision", value=f"{Pr_3}", delta=f"{round(Pr_3 - Pr_mean, 2)}")
col3_rc.metric(label="Recall", value=f"{Rc_3}", delta=f"{round(Rc_3 - Rc_mean, 2)}")
col3_f1.metric(label="F1-score", value=f"{F1_3}", delta=f"{round(F1_3 - F1_mean, 2)}")

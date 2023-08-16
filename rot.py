import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('file:///C:/rtp/medical_students_dataset.csv')

st.title("Мой первый проект Streamlit!")
st.text("Датасет, который я использовал при работе: ")
st.text("https://www.kaggle.com/datasets/slmsshk/medical-students-dataset?select=medical_students_dataset.csv")
st.info("Для удобства было принято решение сократить датасет до 10000 записей")

ds = df[['Age', 'Gender', 'Heart Rate', 'Blood Pressure', 'Cholesterol', 'Diabetes', 'Smoking']].head(10000)
st.dataframe(ds)

st.sidebar.title("Пожалуйста, выберите колонки для сравнения: ")

num1 = st.sidebar.selectbox("Колонка номер 1 :", ['Age', 'Gender', 'Heart Rate', 'Blood Pressure', 'Cholesterol', 'Diabetes', 'Smoking'])
num2 = st.sidebar.selectbox("Колонка номер 2 :", ['Age', 'Gender', 'Heart Rate', 'Blood Pressure', 'Cholesterol', 'Diabetes', 'Smoking'])

st.header("Проверка колонок")

st.text(num1)
st.bar_chart(ds[num1].value_counts())

st.text(num2)
st.bar_chart(ds[num2].value_counts())

st.sidebar.title("Зависимость параметров")
dep1 = st.sidebar.selectbox("Параметр 1 :", ['Age', 'Heart Rate', 'Blood Pressure', 'Cholesterol'])
dep2 = st.sidebar.selectbox("Параметр 2 :", ['Age', 'Heart Rate', 'Blood Pressure', 'Cholesterol'])

corr = ds[dep1].corr(ds[dep2]).round(3)
st.write("Значение корреляции между", dep1, "и", dep2, "равна",corr)

st.info("Корреляция до 0.2 - очень слабая; до 0.5 - слабая: до 0.7 - средняя; до 0.9 - высокая; свыше 0.9 - очень высокая корреляция")



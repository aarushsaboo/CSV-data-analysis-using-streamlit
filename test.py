import streamlit as st
import plotly.express as px
import pandas as pd


dataframe =pd.read_csv('student-performance.csv')
x_axis_column = 'AbsenteeismDays'
y_axis_column = 'MathGrade'
st.bar_chart(dataframe, x= x_axis_column, y=y_axis_column)

fig = px.pie(dataframe, names=x_axis_column, values= y_axis_column)
st.plotly_chart(fig)

correlation = dataframe[x_axis_column].corr(dataframe[y_axis_column])

st.write(f"The correlation between the columns {x_axis_column} and {y_axis_column} is {correlation}")

# 1: Perfect positive correlation. As one variable increases, the other variable increases.
# -1: Perfect negative correlation. As one variable increases, the other variable decreases.
# 0: No correlation. There is no relationship between the variables
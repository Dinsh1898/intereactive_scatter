from ast import Interactive
from matplotlib.pyplot import title
import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
import matplotlib as plt

df = pd.read_csv("winequality-red.csv")
st.write(df)
st.sidebar.header("Pick two variables for your scatterplot")

x_val = st.sidebar.selectbox("Pick your x axis",df.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y axis",df.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(df,title = f"correlation between {x_val} and {y_val}").mark_circle().encode(
    x=x_val, 
    y=y_val ,
    tooltip = [x_val,y_val]
).interactive()

st.altair_chart(scatter, use_container_width=True)

corr = round(df[x_val].corr(df[y_val]),1)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Histogram Görselleştirici")

file = st.file_uploader("bir csv doysasi yükleyin lutfen ", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.write("yüklenen veri")
    st.write(df)

    numeric_cols = df.select_dtypes(include=["int64","float64"]).columns
    column = st.selectbox("histogram için bir sütun seçiniz:",numeric_cols)

    if column:
        fig , ax = plt.subplots()
        ax.hist(df[column],bins=20,alpha=0.7)
        ax.set_title("columnların histogrami")
        ax.set_xlabel(column)
        ax.set_ylabel("frekans")
        st.pyplot(fig)

        ort_deger = df[column].mean()
        st.write(f"ortalama deger {ort_deger}")
        
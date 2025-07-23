import streamlit as st
import pandas as pd
st.title("Bismillah Mulai Progress Mini FPDC")
st.subheader("iyh ini kerjaan gua")

st.header("gimana cara buat tabel")
st.write(
    "Let's start building! For healp and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("my_data.csv")
st.line_chart(df)

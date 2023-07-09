import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

st.set_page_config(page_title="GRADE CALCULATOR ",page_icon="✅",layout="wide")
st.title(":green[GRADE] :blue[CALCULATOR]")
col1,col3=st.columns(2)
df=pd.read_excel("data/GRADE.xlsx",index_col=0,engine='openpyxl')
   
with col1:
    internal=0
    d=0
    internal=st.number_input("ENTER YOUR INTERNAL MARK:",step=None,min_value=0,max_value=50)
    inte=int(float(internal))
    if st.button("Submit"):
        if(inte>50):
            st.subheader("ENTER MARK :red[ < 50]")
        d=inte
        df1=df.loc[d]
        st.table(df1)
        
    st.subheader("TO SEE IN :blue[BAR GRAPH]")
    st.markdown("Press the :red[Display] Button")
    if st.button("DISPLAY"):
        st.markdown(":white[Note:]:red[Bars Are arranged in Ascending Order]")
        d=inte
        df1=df.loc[d]
        col_name=list(df.columns)
        st.bar_chart(df1,x=col_name)

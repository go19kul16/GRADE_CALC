import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
import time
st.set_page_config(page_title="GRADE CALCULATOR ",page_icon="✅",layout="wide")

st.title(":green[GRADE] :blue[CALCULATOR]")
col1,col3=st.tabs(["TABLE","BAR GRAPH"])
df=pd.read_excel("GRADE.xlsx",engine='openpyxl')
   
with col1:
    internal=0
    d=0
    internal=st.number_input("ENTER YOUR INTERNAL MARK:",step=None,min_value=0,max_value=50)
    inte=int(float(internal))
    if st.button("Submit"):
        d=inte
        df1=df.loc[d]
        st.table(df1)
with col3:   
    internals=st.number_input("ENTER YOUR INTERNAL MARK:",step=1,max_value=50)
    intes=int(float(internals))
    #st.subheader("TO SEE IN :blue[BAR GRAPH]")
    #st.markdown("Press the :red[Display] Button")
    if st.button("DISPLAY"):
        with st.spinner(text='Fetching Data'):
            time.sleep(1)
            
        st.markdown(":white[Note:]:red[Bars Are arranged in Ascending Order]")
        d=intes
        df2=df.loc[d]
        col_name=list(df.columns)
        st.bar_chart(df2,x=col_name)
   


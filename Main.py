import streamlit as st
import plotly.express as pe
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from streamlit import title

st.title("Covid App Visulatisation")

st.sidebar.header("Options")

def process_data(data):
    data_change = data.melt(id_vars=["Province/State", "Country/Region", "Lat", "Long"], var_name="Date",
                          value_name="Confirmed")

    data_change["Date"] = pd.to_datetime(data_change["Date"])
    return data_change

def load_data():
    df=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
    return df

def select_country(data):
    choice=st.sidebar.selectbox("Select a Country", data["Country/Region"].unique())
    return choice

def filter_data(data,country):
    f_data=data[data["Country/Region"]==country]
    return f_data

def plot_2d(data,country):
    fig=pe.line(data,x="Date",y="Confirmed",title=f"Covid cases in {country}")
    st.plotly_chart(fig)

def plot_3D(data,country):
    fig=pe.scatter_3d(data,x="Date",y="Lat",z="Long",color="Confirmed",title=f"3D plot of {country}")
    st.plotly_chart(fig)

def main():
    var=st.sidebar.checkbox("Show Raw Data")
    df=load_data()
    p_data = process_data(df)
    if var==True:
        st.write(df)
    else:
        st.write("Processed Data:")
        p_data = process_data(df)
        st.write(p_data)
    country=select_country(df)
    final_data=filter_data(p_data,country)
    if st.button("show")==True:
        st.write(final_data)
        plot_2d(final_data,country)
        plot_3D(final_data,country)


main()

import matplotlib.pyplot as plt 
import streamlit as st 
import pandas as pd
import numpy as np

df=pd.read_csv('D:\\Drive into Analysis\\Covid Data Analysis\\covid.csv')
df.head()
print(df['Continent'].unique())

st.header('Covid Data Analysis')
st.sidebar.title('Analysis Data Using Given Attributes')

def continent(df):
    include_data=st.sidebar.radio('Continent:',df['Continent'].dropna().unique())
    return include_data

def plots(continent,df):
    labels=df.select_dtypes(include=['int64','float64']).columns.to_list()
    data=df[df['Continent']==continent][labels].sum()
    fig,ax=plt.subplots(figsize=(10,5))
    ax.bar(labels,data)
    ax.set_xlabel('Information')
    ax.set_ylabel('Record')
    ax.set_title(f'Information about covid data in {continent}')
    return fig


col1,col2=st.columns([4,1])
with col1 :
    st.write('Graph to get data of each Continent')
    data=continent(df)
    ps=plots(data,df)
    st.pyplot(ps)

with col2 :
    data_=df.groupby('Continent')['TotalDeaths'].sum().reset_index()
    max_death=data_.max()
    st.write(f'Max Number death takes place in continent {max_death[0]} with total deaths {max_death[1]}')




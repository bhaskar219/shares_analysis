import streamlit as st
import pandas as pd
from datetime import datetime
dtype=[datetime,int,int,str,float,float,float]
df=pd.read_csv('s1.csv',parse_dates=['Date'])
df['summary']=df['Credit']-df['Debit']
#df['cum_sum'] = df["summary"].cumsum()
df1=df.sort_values('Date')
st.write(df)
#s1t.write(df['Date1'].unique())


df1=df[['Date','summary']].sort_values('Date').reset_index(drop=True)
df1['cum_sum'] = df1["summary"].cumsum()
#st.line_chart(df1)
#st.write(df1)
df2 = df1.rename(columns={'Date':'index'}).set_index('index')
st.line_chart(df2[['cum_sum']])

sf1=df.sort_values('Date').reset_index(drop=True)
sf1['investment']=sf1[sf1['Type']=='REC']['summary']
sf1['trans_JV']=sf1[sf1['Type'].isin(['JV'])]['summary']
sf1['trans_NSE']=sf1[sf1['Type'].isin(['NSE'])]['summary']
sf1['trans_total']=sf1[sf1['Type'].isin(['NSE','JV'])]['summary']
sf1=sf1.fillna(0)
st.write(sf1.fillna(0))
sf1['cumsum_inv']=sf1[['investment']].cumsum()
sf1['cumsum_JV']=sf1[['trans_JV']].cumsum()
sf1['cumsum_NSE']=sf1[['trans_NSE']].cumsum()
sf1['cumsum_total']=sf1[['trans_total']].cumsum()
sf2=sf1[['Date','cumsum_inv','cumsum_JV','cumsum_NSE','cumsum_total']]
sf2 = sf2.rename(columns={'Date':'index'}).set_index('index')
st.write(sf2)
st.line_chart(sf2)


#df2= df[['Date','Type','summary']].pivot(index='Date',columns='Type').reset_index(drop=True)
#st.write(df2)


a="""
df_final=df[['Type','Debit','Credit']].groupby(df['Type']).sum()
st.write(df_final)
st.write(df_final['Credit']-df_final['Debit'])
st.write(df.plot(x ='Date', y='Balance', kind = 'scatter'))
df.plot(x ='Date', y='Balance', kind = 'scatter')
st.bar_chart(df[['Debit','Credit','Balance']])
import matplotlib.pyplot as plt
#plt.scatter(df['Date'],df['Balance'])
#st.pyplot()
import altair as alt
chart =alt.Chart(df).mark_circle().encode(
x='Date', y ='Balance',tooltip=['Date','Balance']
)
st.graphviz_chart('''
digraph[
watch -> like
like ->share
share->subsribe
]''')
st.altair_chart(chart,use_container_width=True)


chart1 = alt.Chart(df).transform_fold(
    ['Credit', 'Debit']
).mark_bar().encode(
    x='Date',
    y='value:Q',
    color='key:N'
    ,tooltip=['Date','Credit', 'Debit']
)
st.altair_chart(chart1,use_container_width=True)


chart2=alt.Chart(df).transform_fold(
    ['Credit', 'Debit']
).mark_line().encode(
    x='Date',
    y='value:Q',
    color='key:N',

    tooltip=['Date','Credit', 'Debit']
)
st.altair_chart(chart2,use_container_width=True)


st.line_chart(df)


df1 = df.rename(columns={'Date':'index'}).set_index('index')
st.line_chart(df1[['Type','Credit','Debit']])

st.bar_chart(df1[['Type','Balance']])
"""

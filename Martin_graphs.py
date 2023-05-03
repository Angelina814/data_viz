import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Does being rich :moneybag:, reflect a better society? ")

st.subheader(" The Rich Get Richer, but Do They Get Less Corrupt? :thinking_face:")

st.text(" (Feel free to click on the regions for a more detailed view!)")

df = pd.read_csv("world-happiness-report-2021.csv")

gdp_per_capita = df['Logged GDP per capita'] 
gdp_per_capita = np.exp(gdp_per_capita)
gdp_series = pd.Series(data=gdp_per_capita, name='GDP per capita(€)')

df['gdp'] = gdp_series

happiness = df['Ladder score']
happiness_series = pd.Series(data=happiness, name='Happiness Score')

df['Happiness'] = happiness_series


corruption = 'Perceptions of corruption'
regions = 'Regional indicator'


gdp_vs_happiness = px.treemap(df, 
                 path=['Regional indicator', 'Country name'],
                 values='gdp', 
                 color= corruption,
                 color_continuous_scale='balance',
                 hover_name='Country name',
                 hover_data={corruption: True, 'gdp': ':.2f'},
                 )



st.plotly_chart(gdp_vs_happiness)

st.subheader("The Happiness Trifecta: How GDP :money_with_wings: and Social Support :manual_wheelchair: Impact Happiness :smiley: " )

trifecta = px.scatter(df, size="gdp", x="Social support", color='Regional indicator', y='Happiness')
st.plotly_chart(trifecta)

st.subheader(" How evil are greedy rich people? Plotting GDP vs Generosity ")

contour = px.bar_polar(df, r="Generosity", x="Generosity", z='Happiness', color='Regional indicator')
st.plotly_chart(contour)

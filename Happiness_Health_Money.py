import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np


#Loading Data
df = pd.read_csv("world-happiness-report-2021.csv")

#Converting GDP into actual value (Dataset gives log gdp)
gdp_per_capita = df['Logged GDP per capita']
gdp_per_capita = np.exp(gdp_per_capita)
gdp_series = pd.Series(data=gdp_per_capita, name='GDP per capita(€)')
df['gdp'] = gdp_series



#================================================================================
# MAIN STREAMLIT APP
st.markdown("#### Made by: Angelina Andreeva and Martin Sejas")
st.title(":violet[Money Can't Buy Me Love, But Can It Buy Happiness and Health?]")
st.write('---')
st.header("Exploring the Intersection of Happiness, Health, and Wealth: A Global Perspective")
st.markdown("*In this project, we investigate the relationship between three key indicators of societal success: **happiness**, **health**, and **wealth**. By analyzing data from countries around the world, we aim to gain a better understanding of how these factors intersect and influence one another. Through our exploration of this complex topic, we hope to shed light on what it truly means for a society to be 'successful' and what factors contribute to this success.*")
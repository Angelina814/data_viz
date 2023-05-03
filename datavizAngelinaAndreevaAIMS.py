import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
df = pd.read_csv("world-happiness-report-2021.csv")
print(df)
gdp_per_capita = df['Logged GDP per capita']

gdp_per_capita = np.exp(gdp_per_capita)

gdp_series = pd.Series(data=gdp_per_capita, name='GDP per capita(€)')

df['gdp'] = gdp_series

st.title("Does being healthy requires being happier?")

st.write('This is a table used in the project')
st.write(df)

#################################################################################
# add from here
st.write('Area showing the average ladder score depending on the region')
st.write("We can see that the ladder score is the lowest in Sub-Saharan Africa and the highest in North America and ANZ")
#fig1 = px.bar(df, x="Regional indicator", y="Healthy life expectancy")
#fig1 = px.area(df, x="Regional indicator", y="Ladder score")
fig1 = px.bar_polar(df, r='Ladder score', theta='Regional indicator', color='Ladder score', template='plotly_dark', color_discrete_sequence=px.colors.sequential.Plasma_r)
#fig1 = px.ecdf(df, x="Healthy life expectancy")
st.plotly_chart(fig1)

st.write('Treemap showing the comparison between the healthy life expectancy and generosity depending on the region')
tree1 = px.treemap(df, path=[px.Constant("world"), "Regional indicator", "Country name"], values="Healthy life expectancy", color = "Generosity", color_continuous_scale="RdYlGn")
st.plotly_chart(tree1)

st.write('Scatter plot showing the comparison between the healthy life expectancy and social support depending on the region')
st.write("We can see that the higher is the ratio of social support the higher is the healthy life expectancy")
fig2 = px.scatter(df, x="Healthy life expectancy", y="Social support", color="Regional indicator")
st.plotly_chart(fig2)

st.write('Scatter plot showing the correlation between the healthy life expectancy and the ladder score')
st.write("We can see that the high correlation beween the two parametrs and the increase in counts with the increase of the both parameters")
fig4 = px.density_heatmap(df, x="Healthy life expectancy", y ="Ladder score")
st.plotly_chart(fig4)


st.write('Scatter plot showing the comparison between the healthy life expectancy and GDP on the region')
st.write("We can see that s the GDP get higher than 20k the healthy life expectancy starts to increase")
fig3 = px.scatter(df, x="Healthy life expectancy", y="gdp", color="Regional indicator")
st.plotly_chart(fig3)

st.write('Scatter plot showing the comparison between the healthy life expectancy, perceptions of corruption and the ladder score depending on the region')
st.write("We can see that for the low level of corruption healthy life expectancy is high, however, for the high level of corruption healthy life expectancy varies")
st.write("We can see that the lower is the perception of corruption the higher is the ladder score")
fig5 = px.scatter_3d(df, x="Healthy life expectancy", y ="Perceptions of corruption", z = "Ladder score", color="Regional indicator")
st.plotly_chart(fig5)

st.write('Scatter plot showing the correlation between the freedom to make life choices and the ladder score')
st.write("We can see that the high correlation beween the two parametrs and the increase in counts with the increase of the both parameters")
fig6 = px.density_heatmap(df, x="Freedom to make life choices", y ="Ladder score", color_continuous_scale="RdYlGn")
st.plotly_chart(fig6)

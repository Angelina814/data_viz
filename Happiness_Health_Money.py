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


#Adding happiness to the dataframe 

happiness = df['Ladder score']
happiness_series = pd.Series(data=happiness, name='Happiness Score')

df['Happiness'] = happiness_series



#================================================================================
# MAIN STREAMLIT APP
#INTRODUCTION
st.markdown("#### Made by: Angelina Andreeva and Martin Sejas")
st.title(":violet[Money Can't Buy Me Love, But Can It Buy Happiness and Health?]")
st.write('---')
st.header("Exploring the Intersection of Happiness, Health, and Wealth: A Global Perspective")
st.markdown("*In this project, we investigate the relationship between three key indicators of societal success: **happiness**, **health**, and **wealth**. By analyzing data from countries around the world, we aim to gain a better understanding of how these factors intersect and influence one another. Through our exploration of this complex topic, we hope to shed light on what it truly means for a society to be 'successful' and what factors contribute to this success.*")


#IMPACT OF HEALTH - PART 1
st.write('---')
st.title("Does being healthy requires being happier?")

st.write('This is a sample of the data used in the project')
st.write(df)


happiness = 'Happiness'
regions = 'Regional indicator'

#Sum happiness by region
#divide by number of instances 


EUW = df[df['Regional indicator'] == 'Western Europe']
NA = df[df['Regional indicator'] == 'North America and ANZ']
MiddleEast = df[df['Regional indicator'] == 'Middle East and North Africa']
LatinAmerica = df[df['Regional indicator'] == 'Latin America and Caribbean']
EEEurope = df[df['Regional indicator'] == 'Central and Eastern Europe']
EastAsia = df[df['Regional indicator'] == 'East Asia']
SoutheastAsia = df[df['Regional indicator'] == 'Southeast Asia']
Independent = df[df['Regional indicator'] == 'Commonwealth of Independent States']
SubSaharaAfrica = df[df['Regional indicator'] == 'Sub-Saharan Africa']
SouthAsia = df[df['Regional indicator'] == 'South Asia']


avg_happiness =  [np.average(EUW[happiness].to_numpy()),np.average(NA[happiness].to_numpy()),np.average(MiddleEast[happiness].to_numpy()),np.average(LatinAmerica[happiness].to_numpy()),
                  np.average(EEEurope[happiness].to_numpy()), np.average(EastAsia[happiness].to_numpy()), np.average(SoutheastAsia[happiness].to_numpy()), np.average(Independent[happiness].to_numpy()),
                  np.average(SubSaharaAfrica[happiness].to_numpy()), np.average(SouthAsia[happiness].to_numpy())]

region_names = ['Western Europe','North America and ANZ', 'Middle East and North Africa','Latin America and Caribbean','Central and Eastern Europe',
                'East Asia', 'Southeast Asia', 'Commonwealth of Independent States','Sub-Saharan Africa','South Asia' ]

avg_happiness_series = pd.Series(data=avg_happiness, name='Happiness')


 
#CHART 1
st.subheader("Mapping Happiness: A Global Perspective by Region")
st.caption("We can see that the happiness is the lowest in Sub-Saharan Africa and the highest in North America and ANZ")
average_happiness_chart = px.bar_polar(df, r=avg_happiness, theta=region_names,color=avg_happiness_series, template='plotly_dark', color_continuous_scale='Spectral')
st.plotly_chart(average_happiness_chart)

#CHART 2
st.subheader('Treemap showing the comparison between the healthy life expectancy and generosity depending on the region')
tree1 = px.treemap(df, path=[px.Constant("world"), "Regional indicator", "Country name"], values="Healthy life expectancy", color = "Generosity", color_continuous_scale="RdYlGn")
st.plotly_chart(tree1)


#CHART 3

st.subheader('Scatter plot showing the comparison between the healthy life expectancy and social support depending on the region')
st.caption("We can see that the higher is the ratio of social support the higher is the healthy life expectancy")
fig2 = px.scatter(df, x="Healthy life expectancy", y="Social support", color="Regional indicator")
st.plotly_chart(fig2)

#CHART 4
st.subheader('Scatter plot showing the correlation between the healthy life expectancy and the happiness')
st.caption("We can see that the high correlation beween the two parameters and the increase in counts with the increase of the both parameters")
fig4 = px.density_heatmap(df, x="Healthy life expectancy", y =happiness)
st.plotly_chart(fig4)


#CHART 5
st.subheader('Scatter plot showing the comparison between the healthy life expectancy and GDP on the region')
st.caption("We can see that s the GDP get higher than 20k the healthy life expectancy starts to increase")
fig3 = px.scatter(df, x="Healthy life expectancy", y="gdp", color="Regional indicator")
st.plotly_chart(fig3)

#CHART 6
st.subheader('Scatter plot showing the comparison between the healthy life expectancy, perceptions of corruption and the happiness depending on the region')
st.caption("We can see that for the low level of corruption healthy life expectancy is high, however, for the high level of corruption healthy life expectancy varies")
st.caption("We can see that the lower is the perception of corruption the higher is the happiness")
fig5 = px.scatter_3d(df, x="Healthy life expectancy", y ="Perceptions of corruption", z = happiness, color="Regional indicator")
st.plotly_chart(fig5)


#CHART 7 
st.subheader('Scatter plot showing the correlation between the freedom to make life choices and the happiness')
st.caption("We can see that the high correlation beween the two parametrs and the increase in counts with the increase of the both parameters")
fig6 = px.density_heatmap(df, x="Freedom to make life choices", y =happiness, color_continuous_scale="RdYlGn")
st.plotly_chart(fig6)

st.write('---')

corruption = 'Perceptions of corruption'
regions = 'Regional indicator'

#CHART 8
st.title("Does being rich :moneybag:, reflect a better society? ")

st.subheader("The Happiness Trifecta: How GDP :money_with_wings: and Social Support :manual_wheelchair: Impact Happiness :smiley: " )

trifecta = px.scatter(df, size="gdp", x="Social support", color='Regional indicator', y='Happiness')
st.plotly_chart(trifecta)



#CHART 9
st.subheader(" The Rich Get Richer, but Do They Get Less Corrupt? :thinking_face:")

st.text(" (Feel free to click on the regions for a more detailed view!)")


gdp_vs_happiness = px.treemap(df, 
                 path=['Regional indicator', 'Country name'],
                 values='gdp', 
                 color= corruption,
                 color_continuous_scale='balance',
                 hover_name='Country name',
                 hover_data={corruption: True, 'gdp': ':.2f'},
                 )


st.plotly_chart(gdp_vs_happiness)





#CHART 10
st.subheader(" How evil are greedy rich people? Plotting GDP vs Generosity ")

contour = px.scatter(df, size='gdp',  x="Generosity", y='Happiness', color='Regional indicator')
st.plotly_chart(contour)

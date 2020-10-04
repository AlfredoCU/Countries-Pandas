#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 23:00:54 2020

@author: alfredocu
"""

import pandas as pd


df = pd.read_csv('countries.csv')

#1 ¿A qué continente pertenece Tunisia?
dfTunisia = df[df.country == 'Tunisia'].continent.iat[0]
print(dfTunisia)


#2 ¿En qué países la esperanza de vida fue mayor a 80 en el 2007?
dfLifeE = list(df[(df.lifeExp > 80)&(df.year == 2007)].country)
print(dfLifeE)


#3 ¿Qué país de América tiene el mayor PIB?
dfAmerica = df[df.continent == 'Americas']
dfPIBA = dfAmerica[dfAmerica.gdpPercap == max(dfAmerica.gdpPercap)].country.iat[0]
print(dfPIBA)


#4 ¿Qué país tenia más habitantes en 1967 entre Venezuela y Paraguay?
dfVP = df[(df['country'] == 'Venezuela')&(df['year'] == 1967)|(df['country'] == 'Paraguay')&(df['year'] == 1967)]
dfPopVP = dfVP[dfVP['pop'] == max(dfVP['pop'])].country.iat[0]
print(dfPopVP)


#5 ¿En que año Panamá alcanzó una esperanza de vida mayor a 60 años?
dfPan = df[(df.country == 'Panama')&(df.lifeExp > 60)].sort_values('year').year.iat[0]
# df[df.country == 'Panama'][df.lifeExp > 60].sort_values('lifeExp').year.iat[0] -> Marca advertencia.
print(dfPan)


#6 ¿Cuál es el promedio de la esperanza de vida en África en 2007?
dfAfrica = df[(df.continent == 'Africa')&(df.year == 2007)]
dfLiExAf = dfAfrica['lifeExp'].mean()
print(dfLiExAf)


#7 ¿Enlista los países en que el PIB de 2007 fue menor que su PIB en 2002?
dfPIB07 = df[['country', 'year', 'gdpPercap']][df.year == 2007]
dfPIB02 = df[['country', 'year', 'gdpPercap']][df.year == 2002]
dfData = pd.merge(dfPIB07, dfPIB02, on='country', suffixes=('_1', '_2'))
dfPIBL = list(dfData[dfData.gdpPercap_1 < dfData.gdpPercap_2].country)
print(dfPIBL)


#8  ¿Qué país tiene más habitantes en 2007?
dfMaxPop = df[(df.year == 2007)&(df['pop'] == max(df['pop']))].country.iat[0]
print(dfMaxPop)


#9 ¿Cuántos habitantes tiene América en 2007?
dfAme = df[(df.continent == 'Americas')&(df.year == 2007)].sort_values('pop')
dfTotalPopA = dfAme['pop'].sum()
print(dfTotalPopA)


#10 ¿Qué continente tiene menos habitantes en 2007?
df1 = df[df.year == 2007]
df2 = df1[df1.continent == 'Asia']['pop'].sum()
df3 = df1[df1.continent == 'Africa']['pop'].sum()
df4 = df1[df1.continent == 'Europe']['pop'].sum()
df5 = df1[df1.continent == 'Americas']['pop'].sum()
df6 = df1[df1.continent == 'Oceania']['pop'].sum()
data = {
        'continent': ['Asia', 'Africa', 'Europe', 'Americas', 'Oceania'],
        'pop': [df2, df3, df4, df5, df6]
        }
df7 = pd.DataFrame(data)
dfPopContinent = df7[df7['pop'] == min(df7['pop'])].continent.iat[0]
print(dfPopContinent)


#11 ¿Cuál es el promedio de PIB en Europa?
dfEurope = df[df.continent == 'Europe'] # df2.describe()
dfPIBE = dfEurope['gdpPercap'].mean()
print(dfPIBE)


#12 ¿Cuál fue el primer país de Europa en superar los 70 millones de habitantes?
dfPopE = df[(df.continent == 'Europe')&(df['pop'] > 70000000)].sort_values('year').country.iat[0]
print(dfPopE)


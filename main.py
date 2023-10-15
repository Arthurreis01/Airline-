import pandas as pd
import streamlit as st
import plotly.express as px

#O que eu quero?
# Lista de companhias aereas no filtro;
#   Numero de acidentes fatal por companhia de 85 a99 Número de acidentes fatal por companhia de  00 a 14 comparativo
st.set_page_config(layout="wide")
#Projeto de análise de dados de trafego aereo (acidentes, fatalidades..)

st.title ("Projeto de análise de dados de trafego aereo (acidentes, fatalidades..)")
# Trazer a base de dados

df_data = pd.read_csv("airline-safety.csv")


# Trazer as companhias em filtro

selected_airline = st.sidebar.selectbox("Companhias Aéreas", df_data["airline"].unique())

# Filtrar o DataFrame com base na companhia aérea selecionada
df_filtered = df_data[df_data["airline"] == selected_airline]

# Agora você pode usar df_filtered para visualizar os dados
st.dataframe(df_filtered)

# Gráfico comparativo por empresa entre as duas décadas

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

fig = px.bar(df_filtered, x="fatalities_85_99",y="fatalities_00_14",orientation="h", title= "Comparativo de Fatalidades entre a decada de 90 e a decada de 2000")

fig.update_traces(marker_color="red")
fig.update_xaxes(title="Fatalities 1985-1999")
fig.update_yaxes(title="Fatalities 2000-2014")


# segundo gráfico
fig_prod = px.line(df_filtered, x="incidents_85_99", y= "incidents_00_14", title="Incidentes que aconteceram sem morte")

# Exibir o gráfico
st.write(fig)
st.write(fig_prod)

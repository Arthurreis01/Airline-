import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Análise de volume em transação do DOLFUT 2023 a 2021")

#Puxar a base de dados
df=pd.read_excel("C:\\Users\\arthu\\OneDrive\\Documentos\\Base de dados DOLFUT 2023 a 2021.xlsx")



#iniciar a parametrização para os dados
# Calculamos as diferenças
df['Dif_Abertura_Máxima'] = df['Abertura'] - df['Máxima']
df['Dif_Abertura_Mínima'] = df['Abertura'] - df['Mínima']
df['Dif_Abertura_Fechamento'] = df['Abertura'] - df['Fechamento']

# Fazemos o filtro
filtro = ((df['Dif_Abertura_Máxima'].abs() >= 20) |
          (df['Dif_Abertura_Mínima'].abs() >= 20) |
          (df['Dif_Abertura_Fechamento'].abs() >= 20))

# Aplicamos o filtro e obtemos as datas que atendem à condição
horas_filtradas = df[filtro]['Hora']

# Exibimos as datas


#somar no filtro, a quantidade de vezes que se repete a informação por horário
# Aplicamos o filtro e obtemos as horas que atendem à condição
horas_filtradas = df[filtro]['Hora']

# Contagem de ocorrências de cada hora
contagem_horas = horas_filtradas.value_counts()

# Criamos uma nova coluna com a contagem
df['Contagem_Horas'] = df['Hora'].map(contagem_horas)


# Fazemos um filtro na coluna 'VWAP D' usando a lista de horas filtradas
filtro_vwap = df['Hora'].isin(horas_filtradas)

# Aplicamos o filtro na coluna 'VWAP D' para obter os volumes correspondentes
volumes_filtrados = df[filtro_vwap]['VWAP D']

# Exibimos os volumes


#Colocar em modo visual
#Pegar os horários e colocar em modo visual gráfico de barras

col1, col2 = st.columns(2)
col3 = st.columns(1)

fig_date = px.bar(df, x=("Contagem_Horas"), y=("Hora"), title= "Horários com maiores volatidades para estrategia de mais de 20 pontos")
col1.plotly_chart(fig_date, use_container_width=True)

fig_vwap = px.bar(df, x="VWAP D", y=("Hora"), title= "Análise de volume por tempo")
col2.plotly_chart(fig_vwap, use_container_width=True)



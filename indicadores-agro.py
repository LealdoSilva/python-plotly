#importando as bibliotecas
from cProfile import label
from telnetlib import LINEMODE
from tkinter import X
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import dash_bootstrap_components as dbc
import app
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import json
import dash
from globals import *
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


#Criando a template da Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

#Lendo os dados das tabelas 
df = pd.read_excel("cotacao.xlsx")


#Criando as variaveis para armazenar os dados dos indicadores e o tipo de gráfico
fig = px.line(df, x="Data", y="Valor", color="Indicador", text="Cidade")

#Listando e unificando todas as informações dos indicadores
opcoes = list(df['Cidade'].unique())

#Adicionando elementos ou itens na lista 
opcoes.append("Todas as Cidades")

#Criando a aplicação
server = app.server
app.scripts.config.serve_locally = True

#Criando o layout
app.layout = html.Div(children=[
     
    #cabeçalho do layout com a logo
    html.Img(id="logo", src=app.get_asset_url("logo.png"), height=250, width=1520, style={"margin-bottom": "1px"}),
                                                                     
            # Aviso
        html.H4("Selecione uma Cidade:",
              style = {'fontFamily': 'Roboto', 'width': '40%', 'paddingLeft': '5%' 
              }),           
                  
    dcc.Dropdown(opcoes, value='Todos os indicadores', id='lista_indicadores' , style = {'width': '57%',                          
                                                          'display': 'inline-block', 
                                                                           'paddingTop': 0
                                                                                               }),
        
    


       #dcc.Graph(id='grafico_indicadores', figure=fig, style={"height": "390v"}),
       dcc.Graph(id='grafico_indicadores',
                    figure=fig, style = {'paddingLeft': '0%', 
                  
                     'paddingRight': '0%',
                    'width': '100%',
                     'height': '0%',
                     'figuregAlign': 'center',
                     'display': 'inline-block'}
       ),
     
  
#Referencia
    html.Div([
        html.Label(["Fonte:",
                html.A('imea.com.br',
                       href='https://www.imea.com.br/imea-site/dashboards'),
                        #". Acesso em 01/08/2022"
                   ]),
       
            html.P("""Dashboard de Indicadores de Performance Desenvolvido Por:  Lealdo Silva Analista de Tecnologia da Informação""")
        
            ], style={'textAlign': 'center',
                       'fontFamily' : "Roboto",
                       'paddingTop': 1
                      }
    )    
      

])

#Passando o parâmetro para a executar o código no gráfico de linhas
@app.callback(

     Output('grafico_indicadores', 'figure'),
     
           Input('lista_indicadores', 'value')

  
 
)

#Utilizando o parâmetro para gerar saidas
def update_output(value):
  
    
    
    if value == "cidade":

        fig = px.line(df, x="Data", y="Valor", color="Indicador", text="Cidade")
        

    else:

        tabela_filtrada = df.loc[df['Cidade']==value, :]

        fig = px.line(tabela_filtrada, x="Data", y="Valor", color="Indicador")

        

    return fig


#Rodando aplicação atraves de um servidor
if __name__ == '__main__':
    
    app.run_server(debug=True)


# pip install dash
# pip install pandas
# pip install openpyxl

# Estrutura
# Layout -> Tudo que vai ser visualizado
# Callbacks -> Funcionalidades que você terá do dash

from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_excel('corona.xlsx')
# Esta linha lê o arquivo Excel e armazena os dados em uma variável chamada df

fig = px.pie(df, values="Total de infectados", names="Faixa Etária", title="Covid-19")

opcoes = ["Total de infectados", "Mulheres Infectadas", "Homens Infectados"]
# Esta linha cria uma lista contendo todos os valores unicos da coluna "ID Loja"

# Esta linha adiciona a string "Todas as Lojas" ao final da lista de opcoes

app.layout = html.Div(children=[
    html.H1(children='Impacto da Infecção por Coronavírus por Faixa Etária'),
    html.H2(children='Análise do Número de Casos em Crianças, Adultos e Idosos'),
    dcc.Dropdown(opcoes, value='Total de infectados', id='opcoes_grafico'),
    
    dcc.Graph(
        id='grafico_covid-19',
        figure=fig
    )
])

@app.callback(
    Output('grafico_covid-19', 'figure'),
    Input('opcoes_grafico', 'value')
)

def update_output(value):
    fig = px.pie(df, values=value, names="Faixa Etária", title="Covid-19")
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
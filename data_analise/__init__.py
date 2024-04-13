import pandas as pd
import plotly.express as px
def importar_dados():
    dados = pd.read_csv('D:\\pythonProjects\\turmacompila\\dados\\dadostrends.csv')
    dados.drop(columns=['data'], inplace=True)

    return dados

def processar_dados(dados):
    fig = px.line(dados, x=dados.index, y='interesse')
    return fig.to_html()


importar_dados()
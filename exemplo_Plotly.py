import pandas as pd
import plotly.express as px



listX = ['2019', '2020', '2021']
listY = [100, 50, 360]

#CONTROLE DE VISUALIZAÇÃO DOS GRÁFICOS
show = 3

if show == 0:
    
    #GRÁFICO DE LINHAS
    fig = px.line(x=listX, 
                  y=listY, 
                  title="Vendas por ano", 
                  width=800, height=400
                  )
    fig.update_yaxes(title="Eixo Y")        
    fig.update_xaxes(title="Eixo X")            
    fig.show()

elif show == 1:

    #GRÁFICO DE PIZZA
    fig = px.pie(names=listX,
                values=listY,
                title="Vendas por ano", 
                width=800, height=400
                )
    fig.show()    

elif show == 2:

    vCaminhoTabela = r"dados.xlsx"
    dados = pd.read_excel(vCaminhoTabela)

    fig = px.pie(data_frame=dados,
                 title="Vendas por ano", 
                 width=800, height=400
                )
    fig.show()   

elif show == 3:             
    
    #GRÁFICO DE BARRAS
    fig = px.bar(x=listX, 
                 y=listY, 
                 title="Vendas por ano", 
                 width=800, height=400)
    fig.show()  
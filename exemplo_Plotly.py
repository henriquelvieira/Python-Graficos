#https://plotly.com/graphing-libraries/

import pandas as pd
import plotly.express as px


listX = ['2019', '2020', '2021']
listY = [100, 50, 360]


#CONTROLE DE VISUALIZAÇÃO DOS GRÁFICOS
show = 5

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
    #GRÁFICO DE PIZZA C/ DATA FRAME
    vCaminhoTabela = r"dados.xlsx"
    dados = pd.read_excel(vCaminhoTabela)

    fig = px.pie(data_frame=dados,
                 names='DATE',
                 values='QTDE',
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

elif show == 4:   

    #GRÁFICO DE DISPERSÃO
    listX2 = ['2019', '2020', '2021']
    listY2 = [20, 95, 401]
    newListY = listY + listY2
    newListX = listX + listX2
    fig = px.scatter(x=newListX, 
                     y=newListY, 
                     title="Vendas por ano", 
                     width=800, height=400)
    fig.show()  

elif show == 5 :   

    #GRÁFICO DE DISPERSÃO C/ DATA FRAME 
    vCaminhoTabela = r"dados2.xlsx"
    dados = pd.read_excel(vCaminhoTabela)
    
    fig = px.timeline(data_frame=dados,
                      x_start='INICIO',
                      x_end='FIM',
                      y='TAREFA',
                      title="Vendas por ano", 
                      width=800, height=400)
    fig.update_yaxes(autorange='reversed')                      
    fig.show()  
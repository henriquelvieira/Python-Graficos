from funcoesGraficos import geraGraficoLinhas, geraGraficoPizza
import pandas as pd

vCaminhoTabela = r"dados.xlsx"
dados = pd.read_excel(vCaminhoTabela)

listX = dados['DATE'].tolist() #CONVERÇÃO DA COLUNA EM LISTA
listY = dados['QTDE'].tolist() #CONVERÇÃO DA COLUNA EM LISTA
vTotal = dados['QTDE'].sum()

geraGraficoLinhas(listX=listX, 
                  listY=listY, 
                  labelY='Qtde',
                  title=f'Acompanhamento - Total {vTotal}'
                 )   

geraGraficoPizza(listY, listX)    

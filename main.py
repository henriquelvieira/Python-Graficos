from funcoesGraficos import geraGraficoLinhas
import pandas as pd

vCaminhoTabela = r"dados.xlsx"
vDados = pd.read_excel(vCaminhoTabela)

vListX = vDados['DATE'].tolist() #CONVERÇÃO DA COLUNA EM LISTA
vListY = vDados['QTDE'].tolist() #CONVERÇÃO DA COLUNA EM LISTA
vTotal = vDados['QTDE'].sum()

geraGraficoLinhas(listX=vListX, 
                  listY=vListY, 
                  labelY='Qtde',
                  title=f'Acompanhamento - Total {vTotal}'
                 )    

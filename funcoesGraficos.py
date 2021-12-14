from matplotlib import pyplot as plt

def geraGraficoLinhas(listX=[], 
                      listY=[], 
                      labelX=None, 
                      labelY=None, 
                      title=None,
                      style='ggplot'):
    '''
    Função para Geração de Gráfico de Linhas

    Args:
        listX []: Lista com os dados do eixo X
        listY []: Lista com os dados do eixo Y 
        labelX []: Label do eixo X
        labelY []: Label do eixo Y
        title (str): Título
        style (str): Stylo do Gráfico

    Return:
        Gráfico gerado através do matplotlib
    '''                      
    
    plt.style.use(style) #DEFINIÇÃO DO STYLO DO GRÁFICO
    if title:
        plt.title(title) #DEFINIÇÃO DO TÍTULO
    
    if labelY:
        plt.ylabel(labelY) #LABEL DO EIXO XY

    if labelX:
        plt.xlabel(labelX) #LABEL DO EIXO Y

    plt.xticks(rotation=25) #ROTAÇÃO DO LABEL DO EIXO X
    plt.plot(listX, listY) #LISTAS COM OS DADOS P/ OS EIXOS X E Y DO GRÁFICO
    plt.show() #PLOT DO GRÁFICO

def geraGraficoPizza(listValues, listLabels, title=None):
    '''
    Função para Geração de Gráfico de Linhas

    Args:
        listValues []: Lista com os valores
        listLabels []: Lista com as labels
        title (str): Título

    Return:
        Gráfico gerado através do matplotlib
    '''    
    fig1, ax1 = plt.subplots()
    ax1.pie(listValues, 
            labels=listLabels, 
            autopct='%1.1f%%',
            shadow=True, 
            startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    if title:
        plt.title(title)
        
    plt.show() #PLOT DO GRÁFICO

if __name__ == '__main__':
    listX = ['2019', '2020', '2021']
    listY = [100, 250, 360]
    
    geraGraficoLinhas(listX=listX, 
                      listY=listY, 
                      labelY='Label Eixo Y',
                      labelX='Label Eixo X',
                      title='Título do Gráfico'
                      )    

    geraGraficoPizza(listY, listX)      
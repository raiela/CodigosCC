try:
    
    #importando pacotes necessarios
    import plotly.offline as py
    import plotly.express as px
    import plotly.graph_objs as go

except:

    print("A biblioteca usada para essa questao eh a plotly. \nCaso esteja aparecendo isso significa que ela nao ta instalada no seu computador. \nRode a instrucao - pip install plotly - no seu vscode para baixar os pacotes dessa biblioteca\nApos isso, rode de novo a questao")

# valores de x
def data_x_values():
    
    x = [79049, 50770, 32029, 26248, 13840, 5195, 1638, 1602, 1431, 491, 474, 341]
    return x

# valores de y
def data_y_values():
    
    y = ['Messenger RNA', 'Coding Sequences', 'Genes', 'Transfer RNAs', 'CpG islands', 'Pseudogenes', 'Micro-RNAs', 'Small nucleolar RNAs', 'Small nuclear RNAs', 'Miscellaneous RNA', 'Immunoglobulin Segments', 'Ribosomal RNAs']
    return y

# função principal para plotar o grafico
def q2_graphing():
    
    # variável que guardara a figura gerada
    fig = go.Figure()
    
    # edição das partes visuais
    fig.add_trace(go.Bar(
        y = data_y_values(),
        x = data_x_values(),
        name='Valor',
        orientation='h',
        marker=dict(
            color='rgba(128, 128, 128, 0.6)',
            line=dict(color='rgba(128, 128, 128, 1)', width=1.2)
        )
    ))
    
    # Ainda editando aspectos visuais
    fig.update_layout(barmode='stack', template = 'plotly_white', margin_l=0, margin_r=900, margin_pad=10)
    fig.update_traces(width=0.7, selector=dict(type='bar'), )
    fig.update_xaxes(title_text='Feature Count', color=('gray'),title_font_size=20)
    
    fig.show()

q2_graphing()


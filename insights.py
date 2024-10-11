import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def receitas_por_orgao(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        receitas_json = json.load(f)
    receitas_data = receitas_json['data']
    receitas_df = pd.DataFrame(receitas_data)
    receitas_df['R$ Valor'] = pd.to_numeric(receitas_df['R$ Valor'], errors='coerce')
    receitas_agrupadas = receitas_df.groupby('Orgão')['R$ Valor'].sum().reset_index()
    
    return receitas_agrupadas


def despesas_por_orgao(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        despesas_json = json.load(f)
    despesas_data = despesas_json['data']
    despesas_df = pd.DataFrame(despesas_data)
    despesas_df['Valor'] = pd.to_numeric(despesas_df['Valor'], errors='coerce')
    despesas_agrupadas = despesas_df.groupby('Orgão')['Valor'].sum().reset_index()
    
    return despesas_agrupadas


def analise_superavit_deficit(receitas_df, despesas_df):
   
    receitas_df = receitas_df[receitas_df['Orgão'] != 'Total Geral']
    despesas_df = despesas_df[despesas_df['Orgão'] != 'Total Geral']
    receitas_df['R$ Valor'] = pd.to_numeric(receitas_df['R$ Valor'], errors='coerce')
    despesas_df['Valor'] = pd.to_numeric(despesas_df['Valor'], errors='coerce')
    comparacao_df = pd.merge(receitas_df, despesas_df, on='Orgão', how='outer', suffixes=('_Receitas', '_Despesas'))
    comparacao_df.fillna(0, inplace=True)
    comparacao_df['Superávit/Deficit'] = comparacao_df['R$ Valor'] - comparacao_df['Valor']
    
    return comparacao_df


def identificar_orgaos_maior_peso(receitas_df, despesas_df):
    total_receitas = receitas_df['R$ Valor'].replace({',': ''}, regex=True).astype(float).sum()
    total_despesas = despesas_df['Valor'].replace({',': ''}, regex=True).astype(float).sum()

    receitas_df['Participação Receitas (%)'] = (receitas_df['R$ Valor'].replace({',': ''}, regex=True).astype(float) / total_receitas) * 100
    receitas_df['Participação Receitas (%)'] = receitas_df['Participação Receitas (%)'].map('{:.2f}%'.format)

    despesas_df['Participação Despesas (%)'] = (despesas_df['Valor'].replace({',': ''}, regex=True).astype(float) / total_despesas) * 100
    despesas_df['Participação Despesas (%)'] = despesas_df['Participação Despesas (%)'].map('{:.2f}%'.format)

    comparacao_peso_df = pd.merge(receitas_df, despesas_df, on='Orgão', how='outer', suffixes=('_Receitas', '_Despesas'))
    comparacao_peso_df.fillna(0, inplace=True)

    return comparacao_peso_df[['Orgão', 'Participação Receitas (%)', 'Participação Despesas (%)']]


# Arquivos JSON com dados de receitas e despesas
receitas_file = 'C:/Users/caduc/Documents/analisededados/receitas.json'
despesas_file = 'C:/Users/caduc/Documents/analisededados/despesas.json'

receitas_por_orgao_df = receitas_por_orgao(receitas_file)
despesas_por_orgao_df = despesas_por_orgao(despesas_file)

resultado_df = analise_superavit_deficit(receitas_por_orgao_df, despesas_por_orgao_df)
orgaos_maior_peso_df = identificar_orgaos_maior_peso(receitas_por_orgao_df, despesas_por_orgao_df)

# Gráfico de Barras - Comparação de Receitas e Despesas
fig_barras = go.Figure()
fig_barras.add_trace(go.Bar(x=resultado_df['Orgão'], y=resultado_df['R$ Valor'], name='Receitas'))
fig_barras.add_trace(go.Bar(x=resultado_df['Orgão'], y=resultado_df['Valor'], name='Despesas'))
fig_barras.update_layout(barmode='group', title="Comparação de Receitas e Despesas por Órgão")
fig_barras.show()

# Gráfico de Pizza - Participação das Receitas por Órgão
fig_pizza_receitas = px.pie(receitas_por_orgao_df, values='R$ Valor', names='Orgão', title='Participação de Receitas por Órgão')
fig_pizza_receitas.show()

# Gráfico de Pizza - Participação das Despesas por Órgão
fig_pizza_despesas = px.pie(despesas_por_orgao_df, values='Valor', names='Orgão', title='Participação de Despesas por Órgão')
fig_pizza_despesas.show()

# Gráfico de Linhas - Superávit ou Déficit por Órgão
fig_superavit_deficit = px.line(resultado_df, x='Orgão', y='Superávit/Deficit', title='Superávit/Deficit por Órgão')
fig_superavit_deficit.show()

# Gráfico de Barras - Órgãos com maior peso no orçamento
fig_peso = go.Figure()
fig_peso.add_trace(go.Bar(x=orgaos_maior_peso_df['Orgão'], y=orgaos_maior_peso_df['Participação Receitas (%)'], name='Receitas (%)'))
fig_peso.add_trace(go.Bar(x=orgaos_maior_peso_df['Orgão'], y=orgaos_maior_peso_df['Participação Despesas (%)'], name='Despesas (%)'))
fig_peso.update_layout(barmode='group', title="Órgãos com Maior Peso no Orçamento")
fig_peso.show()

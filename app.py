import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, dash_table

df_mortalidad = pd.read_excel('Anexo1.NoFetal2019_CE_15-03-23.xlsx', sheet_name='No_Fetales_2019')
df_divipola = pd.read_excel('Divipola_CE_.xlsx', sheet_name='Hoja1')
df_codigos = pd.read_excel('Anexo2.CodigosDeMuerte_CE_15-03-23.xlsx', sheet_name='Final', header=8)

df_merged = pd.merge(df_mortalidad, df_divipola[['COD_DANE', 'DEPARTAMENTO', 'MUNICIPIO']], on='COD_DANE', how='left')

df_codigos.columns = [str(c).strip() for c in df_codigos.columns]
col_codigo_3 = [c for c in df_codigos.columns if 'tres caracteres' in c][0]
col_desc_3 = [c for c in df_codigos.columns if 'mortalidad a tres' in c][0]

df_codigos_clean = df_codigos[[col_codigo_3, col_desc_3]].drop_duplicates().rename(
    columns={col_codigo_3: 'COD_CIE10', col_desc_3: 'DESCRIPCION_MUERTE'}
)

df_merged['COD_CIE10'] = df_merged['COD_MUERTE'].astype(str).str[:3]
df_final = pd.merge(df_merged, df_codigos_clean, on='COD_CIE10', how='left')

df_final['DEPARTAMENTO'] = df_final['DEPARTAMENTO'].fillna('DESCONOCIDO')
df_final['MUNICIPIO'] = df_final['MUNICIPIO'].fillna('DESCONOCIDO')
df_final['DESCRIPCION_MUERTE'] = df_final['DESCRIPCION_MUERTE'].fillna('OTRAS CAUSAS')

df_depto = df_final.groupby('DEPARTAMENTO').size().reset_index(name='TOTAL')
fig_mapa = px.bar(df_depto, x='DEPARTAMENTO', y='TOTAL', title='Muertes por Departamento')

df_mes = df_final.groupby('MES').size().reset_index(name='TOTAL')
fig_lineas = px.line(df_mes, x='MES', y='TOTAL', title='Muertes por Mes')

df_homicidios = df_final[df_final['MANERA_MUERTE'].str.lower().str.contains('homicidio', na=False)]
df_violentas = df_homicidios.groupby(['MUNICIPIO']).size().reset_index(name='TOTAL').sort_values(by='TOTAL', ascending=False).head(5)
fig_barras = px.bar(df_violentas, x='MUNICIPIO', y='TOTAL', title='Top 5 Ciudades Violentas')

df_menor = df_final.groupby(['MUNICIPIO']).size().reset_index(name='TOTAL').sort_values(by='TOTAL', ascending=True).head(10)
fig_pie = px.pie(df_menor, names='MUNICIPIO', values='TOTAL', title='Ciudades con Menor Mortalidad')

df_causas = df_final.groupby(['COD_CIE10', 'DESCRIPCION_MUERTE']).size().reset_index(name='TOTAL').sort_values(by='TOTAL', ascending=False).head(10)

df_final['SEXO_STR'] = df_final['SEXO'].map({1: 'Masculino', 2: 'Femenino'}).fillna('Otro')
df_sexo_depto = df_final.groupby(['DEPARTAMENTO', 'SEXO_STR']).size().unstack(fill_value=0).reset_index()
fig_apilada = px.bar(df_sexo_depto, x='DEPARTAMENTO', y=['Masculino', 'Femenino'], title='Muertes por Sexo y Departamento')

fig_hist = px.histogram(df_final, x='GRUPO_EDAD1', title='Distribucion por Grupo de Edad')

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1('Dashboard de Mortalidad en Colombia 2019'),
    dcc.Graph(figure=fig_mapa),
    dcc.Graph(figure=fig_lineas),
    dcc.Graph(figure=fig_barras),
    dcc.Graph(figure=fig_pie),
    dash_table.DataTable(
        data=df_causas.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df_causas.columns],
        page_size=10
    ),
    dcc.Graph(figure=fig_apilada),
    dcc.Graph(figure=fig_hist)
])

if __name__ == '__main__':
    app.run_server(debug=True)
from dash.dependencies import Input, Output
# from layouts import layout_page_1, layout_page_2,layout_index
from data import(df,df_econ, df_adil_econ, df_sandy_econ, df_warne_econ, df_kumble_econ, 
                df_rashid_econ, df_chahal_econ,df_mishra_econ,df_zampa_econ, df_tahir_econ)

from main import app

import plotly.graph_objs as go
####
### Callback for Average
names = df['Name'].unique()


@app.callback(
    Output('econ-graphic', 'figure'),
    [Input('player_picker', 'value')]
)
def econ_graph(player_name):
    data = []
    if 'All' in player_name:
        data = df_econ
        color = ['lightgrey']*9
        color[1] = 'red'
    else:
        data = df[df['Name'].isin(player_name)]
        color = 'lightgrey'
        # print(data)
        # print(type(data))
    figure = {
        'data': [go.Bar(x=data['Name'],y=data['Econ'], marker={'color': color})]
    }
    return figure
@app.callback(
    Output('avg-graphic', 'figure'),
    [Input('player_picker', 'value')]
)
def avg_graph(player_name):
    data = []
    if 'All' in player_name:
        data = df
        color = ['lightgrey']*9
        color[1] = 'red'
    else:
        data = df[df['Name'].isin(player_name)]
        color = 'lightgrey'
        # print(data)
        # print(type(data))
    figure = {
        'data': [go.Bar(x=data['Name'],y=data['Ave'], marker_color= color)]
    }
    return figure
    







########


@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('app-2-display-value', 'children'),
    [Input('app-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
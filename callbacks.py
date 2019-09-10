from dash.dependencies import Input, Output
# from layouts import layout_page_1, layout_page_2,layout_index
from data import(df_econ, df_adil_econ, df_sandy_econ, df_warne_econ, df_kumble_econ, 
                df_rashid_econ, df_chahal_econ,df_mishra_econ,df_zampa_econ, df_tahir_econ)

from app import app

import plotly.graph_objs as go
####
### Callback for Average
@app.callback(
    Output('average-graphic', 'figure'),
    [Input('player_picker', 'value')]
)
def economy_graph(player_name):
    data = []
    if '' in player_name:
        data = df_econ
    if 'Sandeep Lamichhane' in player_name:
        data = df_sandy_econ
        # print(data)
    elif 'Adil Rashid' in player_name:
        data = df_adil_econ
        # print(data)
    else:
        data = df_econ
        # print(type(data))
    figure = {
        'data': [go.Bar(x=data['Name'],y=data['Econ'])]
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
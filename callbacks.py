from dash.dependencies import Input, Output
# from layouts import layout_page_1, layout_page_2,layout_index
from data import(labels, df,df_1, df_econ)

from main import app

import plotly.graph_objs as go
####
### Callback for Average
names = df['Name'].unique()

@app.callback(
    Output('match-played','figure'),
    [Input('player_picker','value')]
)
def match_played(player_name):
    data = []
    if 'All' in player_name:
        data = df
        color = ['lightgrey']*9
        color_wkts = ['darkgrey']*9
        color[1] = 'red'
        color_wkts[1]  = 'orange'
    else:
        data = df[df['Name'].isin(player_name)]
        color = 'lightgrey'
        # print(data)
        # print(type(data))
    figure = {
        'data': [go.Bar(x=data['Name'],y=data['Mat'], marker={'color': 'skyblue'}, name = 'Matches Played'),
                go.Bar(x=data['Name'],y=data['Wkts'], marker={'color': 'lightblue'}, name = 'Wickets Taken')
        ]
    
    }
   
    return figure



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


@app.callback(
    Output('cbr-vs-eco','figure'),
    [Input('player_picker','value')]
)
def cbrvsecon(player_name):
    data = []
    if 'All' in player_name:
        data = df
        color = ['lightgrey']*9
        color_wkts = ['darkgrey']*9
        color[1] = 'red'
        color_wkts[1]  = 'orange'
    else:
        data = df[df['Name'].isin(player_name)]
        color = 'lightgrey'
        # print(data)
        # print(type(data))
    figure = {
        'data': [go.Bar(x=data['Name'],y=data['Econ'], marker={'color': '#C8553D'}, name = 'Econ'),
                go.Bar(x=data['Name'],y=data['CBR'], marker={'color': '#588B8B'}, name = 'CBR')
        ]
    
    }
   
    return figure

@app.callback(
    Output('indi-stats','figure'),
    [Input('indi_player_picker','value')]
)
def indistats(player_name):
    data = []
    if 'Sandeep Lamichhane' in player_name:
        data = df_1.iloc[1].tolist()
    # Work on a better solution when the tummy is full, for now 
    elif 'Adil Rashid' in player_name:
        data = df_1.iloc[0].tolist()
    elif 'Shane Warne' in player_name:
        data = df_1.iloc[2].tolist()
    elif 'Anil Kumble' in player_name:
        data = df_1.iloc[3].tolist()
    elif 'Rashid Khan' in player_name:
        data = df_1.iloc[4].tolist()
    elif 'Yuzvendra Chahal' in player_name:
        data = df_1.iloc[5].tolist()
    elif 'Amit Mishra' in player_name:
        data = df_1.iloc[6].tolist()
    elif 'Adam Zampa' in player_name:
        data = df_1.iloc[7].tolist()
    elif 'Imran Tahir' in player_name:
        data = df_1.iloc[8].tolist()
    figure = {
        'data': [go.Pie(values= data, labels = labels, hole = .6, textinfo= 'value')],
        "layout": go.Layout(title="{}".format(player_name), margin={"l": 50},
                            legend={"x": 1, "y": 0.1},
                            width=450, height= 450)
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
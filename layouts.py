import dash_core_components as dcc
import dash_html_components as html

#importing the data files
from data import (df, player_names)

player_label = [{'label': i, 'value': i} for i in player_names]

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_index = html.Div([
# Header div
    html.Div([
        html.H1("Comparing prominent leg spinners", style = {'color': 'black', 'margin-top': '20px'})
    ],className= 'row'),
# Main body   
    html.Div([
        html.Div([
            html.P("Average graph goes here"),
            dcc.Dropdown(
    id = 'player_picker',
    options= player_label,
    multi=True,
    style = {'width': '85%'},
    value=[""]
    ),
    
    dcc.Graph(id='average-graphic')

        ],className='six columns'),
        html.Div([
             html.P("Average graph goes here")
        ],className='six columns')
    ],className='row')
    # dcc.Link('Navigate to "/page-1"', href='/page-1'),
    # html.Br(),
    # dcc.Link('Navigate to "/page-2"', href='/page-2'),
], className= 'offset-by-one columns')


# For other pages (not required right now)
layout_page_1 = html.Div([
    html.H3('App 1'),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-1-display-value'),
    dcc.Link('Go to App 2', href='/apps/app2')
])

layout_page_2 = html.Div([
    html.H3('App 2'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/apps/app1')
])
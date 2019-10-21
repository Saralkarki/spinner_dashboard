import dash_core_components as dcc
import dash_html_components as html

#importing the data files
from data import (df, player_names)

player_label = [{'label': i, 'value': i} for i in player_names]

all_players = {'label': 'All', 'value': 'All'}
player_label.append(dict(all_players))
# print(player_label)

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_index = html.Div([
# Header div
    html.Div([
        html.H1("Comparing T20 International stats for leg spinners", style = {'color': 'black', 'margin-top': '20px'
        ,'margin-left': '50px'})
    ],className= 'row'),
# Player Picker
html.Div([
    html.H5('Select Players by clicking here:'),
    html.Div([
        dcc.Dropdown(
    id = 'player_picker',
    options= player_label,
    multi=True,
    style = {'width': '85%'},
    value=['Rashid Khan','Imran Tahir','Sandeep Lamichhane','Shane Warne'],
    placeholder = 'Pick one or more players',
    ),
    html.P("To deselect click the (x) before the players name", style = {'color': 'black','font-style':'italic'}),
    html.P('The Matches Played & wicket taken bar change accordingly. Scroll down to see Career bowling economy and average change'),
    html.Br(),
    html.P('''All of the data were collected from Cricinfo.com(as of July 8th,2019) and after meticulous cleaning of the data, 
    here are the findings. The bowlers in the list are : Shane Warne, Anil Kumble, 
    Rashid Khan, Yuzvendra Chahal, Amit Mishra, Imran Tahir, Adam Zampa, Adil Rashid, Rashid Khan 
    and Sandeep Lamichhane.'''),
    html.Br(),
    html.P('Individual Stats', style={'font-size': '18px','font-weight':'bold'}),
    html.P('For viewing individual stats of the bowlers change bowlers here'),
    html.P('Hover on the graph to see more info. Click on the legengs to acitvate and deactivate the information', style = {'font-weight':'bold'}),
     dcc.Dropdown(
    id = 'indi_player_picker',
    options= player_label,
    multi=False,
    style = {'width': '85%'},
    value='Sandeep Lamichhane',
    placeholder = 'Pick a player',
    clearable = False
    ),
    # html.Img(src='sandy.jpeg'),
    dcc.Graph(id='indi-stats')
    ],className = 'four columns'),
    html.Div([
        # dcc.Link('Click here', href = "http://www.google.com"),
        html.A('For full article on how the data was extracted and analysed: click here', href = 'http://bit.ly/2kvM6dv',target='_blank',style={'text-decoration': 'none','font-size':24,'color':'black','font-weight': 'bold'} ),
        html.P('Matches Played and Wickets taken', style = {'font-weight':'bold', 'margin-top':'90px', 'font-size': '32px'}),
        html.Br(),
        html.Strong('''Hover on the graph for more information. To see individual bars for wickets and matches played click on 
        the label to disable and enable them''', style={'font-style':'italic', 'opacity': '1', 'color':'black'}),
        dcc.Graph(
            id = 'match-played'
        ),
        
    ], className = 'six columns')
], className = 'row'),
# Main body   
    html.Div([
        html.Div([
            html.Br(),
            html.P("Career Bowling Economy", style = {'font-weight': 'bold', 'font-size': '28px'}),
            html.Br(),
            html.P('''A player's economy rate is the number of runs they have conceded per over bowled. 
            The lower the economy rate is, the better the bowler is performing. It is one of a number of statistics used to compare bowlers, commonly used alongside bowling 
            average and strike rate to judge the overall performance of a bowler.'''),
            html.Strong('''Hover on the graph for more information. To see individual bars for wickets and matches played click on 
        the label to disable and enable them''', style={'font-style':'italic', 'opacity': '1', 'color':'black'}),
            
    dcc.Graph(id='econ-graphic')

        ],className='five columns'),
        html.Div([
             html.Br(),
             html.P("Career Bowling Averages", style = {'font-weight': 'bold', 'font-size': '28px'}),
             html.Br(),
             html.P('''The bowling average is one of a number of statistics used to compare bowlers in the sport of cricket. 
            It is the ratio of runs conceded per wickets taken, 
            meaning that the lower the bowling average is, the better the bowler is performing.'''),
            html.Strong('''Hover on the graph for more information. To see individual bars for wickets and matches played click on 
        the label to disable and enable them''', style={'font-style':'italic', 'opacity': '1', 'color':'black'}),
      html.Br(),       
        dcc.Graph(id='avg-graphic')
        ],className='five columns')
    ],className='row'),
    html.Div([
        html.Div([
            html.P('Combined Bowling rate(CBR) vs Economy rate(Econ)', style= {'font-weight': 'bold', 'font-size': '28px'}),
            html.Br(),
            html.P('''However, it is widely recognized that average and economy rates have severe limitations in assessing the true 
            abilities of a player’s performance. Therefore, we will be looking at the measure called Combined Bowling Rate(CBR) as 
            developed by Lemmer. '''),
            html.A('For full article on CBR', href = 'http://bit.ly/2kvM6dv', target='_blank'),
        ], className = 'six columns'),
        html.Div([
            dcc.Graph(id = 'cbr-vs-eco')
        ], className = 'nine columns')
        
    ], className='row', style={'margin-top': '20px'}),

    # dcc.Link('Navigate to "/page-1"', href='/page-1'),
    # html.Br(),
    # dcc.Link('Navigate to "/page-2"', href='/page-2'),
], className= 'offset-by-one columns twelve columns')


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
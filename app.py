# import dash
# import dash_html_components as html

# import flask

# from layouts import url_bar_and_content_div,layout_index,layout_page_1,layout_page_2


# app = dash.Dash(
#     __name__,
#     external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
# )

# server = app.server
# # app.config.suppress_callback_exceptions = True

# # def serve_layout():
# #     if flask.has_request_context():
# #         return url_bar_and_content_div
# #     return html.Div([
# #         url_bar_and_content_div,
# #         layout_index,
# #         layout_page_1,
# #         layout_page_2,
# #     ])


# app.layout = serve_layout

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# from app import app
from layouts import layout_page_1, layout_page_2, layout_index
import callbacks

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
         return layout_page_1
    elif pathname == '/apps/app2':
         return layout_page_2
    else:
        return layout_index

if __name__ == '__main__':
    app.run_server(debug=True)
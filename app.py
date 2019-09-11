import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from main import app
from layouts import layout_page_1, layout_page_2, layout_index
import callbacks

server = app.server
app.config.suppress_callback_exceptions = True

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
    app.run_server(debug=False)
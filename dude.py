# import dash
# import dash_html_components as html

# import flask

# from layouts import url_bar_and_content_div,layout_index,layout_page_1,layout_page_2


# app = dash.Dash(
#     __name__,
#     external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
# )

# server = app.server
# app.config.suppress_callback_exceptions = True

# def serve_layout():
#     if flask.has_request_context():
#         return url_bar_and_content_div
#     return html.Div([
#         url_bar_and_content_div,
#         layout_index,
#         layout_page_1,
#         layout_page_2,
#     ])


# app.layout = serve_layout
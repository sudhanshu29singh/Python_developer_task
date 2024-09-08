import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import sqlite3

# Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(
    style={'backgroundColor': 'lightgreen', 'padding': '20px', 'fontFamily': 'Arial'},
    children=[
        html.H2(
            "SQLite Database Analysis",
            style={'textAlign': 'center', 'marginBottom': '20px', 'padding': 1}
        ),
        html.Div(
            children=[
                html.Button('Amount Spent by Each User', id='btn_total_spent', n_clicks=0),
                html.Button('Top 3 Spent Users', id='btn_top_3_spent', n_clicks=0),
                html.Button('Users_ No Transactions', id='btn_no_transactions', n_clicks=0),
            ],
            style={'textAlign': 'center', 'marginBottom': '20px'}
        ),
        html.Div(
            children=[
                dcc.Graph(id='report_graph', style={'marginBottom': '20px'}),
                dash_table.DataTable(
                    id='report_table',
                    style_cell={'textAlign': 'left', 'padding': '10px'},
                )
            ],
            style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}
        )
    ]
)

@app.callback(
    [Output('report_graph', 'figure'), Output('report_table', 'data')],
    [Input('btn_total_spent', 'n_clicks'),
     Input('btn_top_3_spent', 'n_clicks'),
     Input('btn_no_transactions', 'n_clicks')]
)
def update_graph(btn_total_spent, btn_top_3_spent, btn_no_transactions):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'btn_total_spent'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    conn = sqlite3.connect('example.db')
    try:
        if button_id == 'btn_total_spent':
            df = pd.read_sql_query('''
                SELECT users.name, users.email, SUM(transactions.amount) AS total_spent
                FROM users
                JOIN transactions ON users.user_id = transactions.user_id
                GROUP BY users.user_id
            ''', conn)
            fig = px.bar(df, x='name', y='total_spent', title='Total Amount Spent by Each User')
            table_data = df.to_dict('records')

        elif button_id == 'btn_top_3_spent':
            df = pd.read_sql_query('''
                SELECT users.name, users.email, SUM(transactions.amount) AS total_spent
                FROM users
                JOIN transactions ON users.user_id = transactions.user_id
                GROUP BY users.user_id
                ORDER BY total_spent DESC
                LIMIT 3
            ''', conn)
            fig = px.bar(df, x='name', y='total_spent', title='Top 3 Users Who Spent the Most')
            table_data = df.to_dict('records')

        elif button_id == 'btn_no_transactions':
            df = pd.read_sql_query('''
                SELECT name, email FROM users
                WHERE user_id NOT IN (SELECT DISTINCT user_id FROM transactions)
            ''', conn)
            fig = px.bar(df, x='name', title='Users with No Transactions')
            table_data = df.to_dict('records')

    finally:
        conn.close()

    return fig, table_data

if __name__ == '__main__':
    app.run_server(debug=True)
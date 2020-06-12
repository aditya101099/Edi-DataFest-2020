import pandas as pd
import glob
import matplotlib.pyplot as plt
import plotly.graph_objs as go 
import webbrowser
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from collections import deque

plt.style.use('dark_background')



# Plots for all tech keywords
path = r'TechCSVs'
all_files = glob.glob(path + "/*.csv")
li = [pd.read_csv(filename, index_col='Day') for filename in all_files]
frame = pd.concat(li, axis=1, ignore_index=False)
frame.rename(columns=lambda x: x.rstrip('(United Kingdom)')[:-1], inplace=True)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Search Trend Analysis',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Tech Trends', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [{'x':frame.index, 'y':frame[frame.columns[i]], 'type':'line', 'name':frame.columns[i]} for i in range(16)],
            'layout': {
                'plot_bgcolor':colors['background'],
                'paper_bgcolor':colors['background'],
                'font': {
                    'color':colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
	webbrowser.open('http://127.0.0.1:8050')
	app.run_server(debug=True)





# frame.plot(subplots=True, layout=(4,4), figsize=(15,10))
# plt.show()


# plt.plot(figsize=(150,50), kind='line')
# for col in frame.columns:
# 	plt.plot(frame[col], label = col)
# plt.title("Trends Over Time")
# plt.legend(loc="best", fontsize=8)
# plt.show()

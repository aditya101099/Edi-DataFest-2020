import pandas as pd
import glob
import matplotlib.pyplot as plt
import plotly.graph_objs as go 
import webbrowser
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
from collections import deque

plt.style.use('dark_background')



# Plots for all tech keywords
paths = [r'TechCSVs'] # list of paths of all folders
all_files = [glob.glob(path + "/*.csv") for path in paths] # get all CSVs, organize it by folder title

lis = [[pd.read_csv(filename, index_col='Day') for filename in these_files] for these_files in all_files] # Each list contains a list of all the dataframes

dfs = [pd.concat(li, axis=1, ignore_index=False) for li in lis] # Concatenate all dataframes into 1

for df in dfs:
	df.rename(columns=lambda x: x.rstrip('(United Kingdom)')[:-1], inplace=True)
	# df = df.reindex(sorted(df.columns), axis=1, copy=False)
dfs = {None: None, "Tech":dfs[0], "Business":dfs[0], "Companies":dfs[0]}

analysis = {None:"Enter term for analysis", "5G":"Blah blah blah", "Automation":"This is automated", "Computer Vision":"This is visioned using a computer."}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#000000',
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

	# Dropdown and analysis input field logic 
	
	html.Div(children = [
		dcc.Dropdown(id='input-graph', options=[ 
			{'label': 'Tech', 'value':'Tech'},
			{'label': 'Business/Marketing', 'value':'Business'},
			{'label': 'Companies', 'value':'Companies'}
		], placeholder="Search keyword category", style={
			'borderColor':'#FFFFFF',
			'backgroundColor':'#000000',
			'width':'250px',
			'color':'#000000'
		}, searchable=False),
		
		# Analysis input field logic
		dcc.Input(id='input-analysis', placeholder="Enter term for analysis", type='text', style={
			'borderColor':'#FFFFFF',
			'backgroundColor':'#000000',
			'color':'#FFFFFF'
	})]
	),
	
	# Title logic
	
	html.H3(id='section-header'),
	
	
	# Instructions logic
	
	html.Div(children='Double click on any line in the legend to isolate it', style={
		'textAlign': 'center',
		'color': colors['text']
	}),
	
	# Output graph logic 
	
	html.Div(id='output-graph'),
   
	# Output Analysis logic
	html.Div(id='output-analysis')
])

@app.callback(
	[Output(component_id="section-header", component_property='children'),
	Output(component_id="output-graph", component_property='children'), Output(component_id="output-analysis", component_property='children')],
	[Input(component_id="input-graph", component_property='value'), Input(component_id="input-analysis", component_property='value')]
)


	
def update_graph_and_title(input_data, input_analysis):
	relevant_df = dfs[input_data]
	title = input_data
	output = f"{input_analysis} Analysis: {analysis[input_analysis]}/n"
	return html.H3(id='section-header', children=f"{title} Trends", style={
		'textAlign': 'center',
		'color': colors['text'],
	}), dcc.Graph(
		id='output-graph',
		figure={
			'data': [{'x':relevant_df.index, 'y':relevant_df[relevant_df.columns[i]], 'type':'line', 'name':relevant_df.columns[i]} for i in range(16)],
			'layout': {
				'plot_bgcolor':colors['background'],
				'paper_bgcolor':colors['background'],
				'font': {
					'color':colors['text']
				}
			}
		}
	), html.Div(id='output-analysis', children=output, style={
		'textAlign':'center',
		'color': "#FFFFFF",
		'paddingTop':"20px"
	})
	
# def update_section_header(input_data):
# 	return html.Div(id='section-header', children="{} Trends".format(input_data), style={
# 		'paddingTop':'50px',
# 		'textAlign': 'center',
# 		'color': colors['text'],
# 		'fontSize':'2em'
# 	})	
# def update_value(input_data):
# 	return "Analysis: {}".format(input_data)

if __name__ == '__main__':
	webbrowser.open('http://127.0.0.1:8050')
	app.run_server(debug=False)


# -------- TASKS TO DO ---------

# Add all other trends
# Add all other analyses
# Make it all look pretty


# # frame.plot(subplots=True, layout=(4,4), figsize=(15,10))
# # plt.show()
# 
# 
# # plt.plot(figsize=(150,50), kind='line')
# # for col in frame.columns:
# # 	plt.plot(frame[col], label = col)
# # plt.title("Trends Over Time")
# # plt.legend(loc="best", fontsize=8)
# # plt.show()

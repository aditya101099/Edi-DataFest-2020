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
paths = [r'BusMarkCSVs', r'CompaniesCSVs',r'EntertainmentCSVs', r'SkillsCSVs', r'TechCSVs'] # list of paths of all folders
all_files = [sorted(glob.glob(path + "/*.csv")) for path in paths] # get all CSVs, organize it by folder title

lis = [[pd.read_csv(filename, index_col='Day') for filename in these_files] for these_files in all_files] # Each list contains a list of all the dataframes

dfs = [pd.concat(li, axis=1, ignore_index=False) for li in lis] # Concatenate all dataframes into 1

for df in dfs:
	df.rename(columns=lambda x: x.rstrip('(United Kingdom)')[:-1], inplace=True)
	# df = df.reindex(sorted(df.columns), axis=1, copy=False)

dfs = {None: None, "Business/Marketing":dfs[0], "Companies":dfs[1], "Entertainment":dfs[2], "Skills":dfs[3], "Tech":dfs[4]}
# for col in dfs['Business/Marketing'].columns:
# 	print(col)
# -- All analyses follow below -- #

analysis = {

	None: {"Enter term for analysis": "Enter term for analysis"}, 
	"Tech": {
		"5G":"The graph shows a normal-like curve with a peak in early April, when concerns about 5G causing coronavirus were high after a now labelled “fake” video surfaced of people in Wuhan tearing down cell phone towers. The concerns were shot down quickly which is why we see a fall as fast as the rise.", 
		"Automation":"This is automated", 
		"Computer Vision":"This is visioned using a computer.",
		"Drones":"Searches for drones have increased since the start of March, with the highest number of searches on 24 April and 27 March, when it was reported drones will be delivering coronavirus supplies and the police were using drones to send messages to people breaking lockdown respectively.",
		"Cloud Computing":"Cloud computing searches saw a gradual increase until the start of May, with a peak at the start of May reflecting conference activity. General volatility of searches nonetheless shows an increasing trend over time, suggesting greater focus on cloud computing during lockdowns.",
		"Disruptive Technology":"Interest in disruptive technologies has been sporadic across March to May. Peaks have been consistent around the same level of searches.",
		"Web 2.0":"Searches for Web 2.0 have seen a progressive decline since the early and mid March peaks, brought about by conference activity and the subsequent release of a seminal paper by HBR on Web 2.0 respectively,  to less than 1/3rd of peak levels.",
		"Augmented Reality":"Searches for AR and Artificial reality peaked across March 25-29 following a set of promising press releases and Facebook's F8 livestream announcement of a new roll-out of AR features, before falling to pre-lockdown levels.",
		"Virtual Reality":"Searches for VR have remained sporadic across the March-May period, with a slight decrease in searches from regular 60-65/100 peaks in March to peaks of 52-54/100 in May. With a peak on April 4th reflecting the publication of the AR & VR market reports by PRNewswire and the announcement of Apple's planned acquisition of NextVR.",
		"Robotics":"Interest in robotics searches has been sporadic, with a decrease between index scores of 94-100 in early March to around 50 by mid april. Despite this, search volatility remains high, peaking around new announcements in the industry and during Robotics Conference times."},
	"Skills": {
		"how to make a mask":"The search trends have increased with the first small peaks being in April and the biggest increase being on May 12, the day after the UK government advised the public to buy masks but most stores were still low on supply, leading to people enquiring how to make their own.",
		"emotional intelligence":"The search trends for emotional intelligence have remained fairly consistent and coronavirus seems to have had no effect on this.",
		"sewing":"The search trends for sewing increased over the sample time period with the first big jump on April 22, the day series 6 of the Great British Sewing Bee premiered and the following next peaks being the days of new episodes.",
		"learn a language":"Searches for learn a language experienced an increase in early April and have remained relatively constant since.",
		"painting":"Searches for the painting have increased during the sample time, with a steady increase in searches up until 26 April with an index score of 100l. This high engagement with the search term has had multiple peaks, remaining consistently high on an index score (70-100/100).",
		"drawing":"Searches for drawing saw a major increase from low index scores of about 40/100 in early March to an average of 80/100 index score in late March, this continued on.",
		"baking":"The searches increased over the lockdown period with most of the peaks occurring on weekends. This can be attributed to the food shortage the UK was experiencing where most could not get ahold of basics like bread so people switched to making these items themselves.",
		"ks2 maths":"This search term saw its biggest increase after UK schools shut and many parents were forced to be in charge of their child’s learning. There was a significant decrease over the first two weeks of April, this would have been the Easter holiday for most children, hence there were less searches as parents wanted to stick with the normal school schedule.",
		"home workout":"The searches follow a normal-like curve with a peak on 24 March and has been slowly decreasing since. This can be attributed to people having to adjust to not using gyms. The fall in searches can be attributed to people finding a home workout they’re comfortable with and so stop searching or routines.",
		"online courses":"Searches began to increase around 16 March and had a small peak on March 24, searches had a slight drop over two days but picked back up quickly to reach its peak on March 31. Many businesses were closing at this time and workers were being furloughed, uncertain whether their job will be available when they were able to come back. This is why we see an increase in the search term as workers are looking to gain new skills / learn something new.",
		"working from home":"Searches steadily increased from the start of March, peaking on March 17. This was around the period most companies were shifting their operations to function remotely in anticipation of a nationwide lockdown. This search term had a second peak on March 23, the day the UK lockdown was announced, and began falling from then. The dips in the graphs occur on Sundays, slowly rising until Wednesday and slowly dipping again. This trend has continued on since March 23. ",
		"supermarket jobs":"The trend of the graph shows a Normal-like curve with a peak on March 21, which, again, was when most businesses were closing but supermarkets were in need of more employees due to the demand.",
		"how to buy stocks":"The graph is pretty consistent, a series of spikes and falls with the spikes being the start of the week. However, there is a jump on April 20, which is the day oil went negative and many were flooding to the Internet to try and take advantage of this opportunity.",
		"how to code":"The search trends so slow growth, with the biggest increase over the week the UK lockdown begun.",
		"volunteering":"The graph shows a normal-like curve with a peak on March 25, which was the day after the government launched their “Your NHS needs You” campaign, looking for 250,000 volunteers to help vulnerable groups.",
		"internships":"Searches for internships significantly decreased from the start of March, this can be attributed to most companies not looking for new hires due to the economic state of the country."},
	"Companies": {
		"Microsoft":"Interest in Microsoft searches spiked on the 23rd of March and has shown continued high activity on weekdays since then. There has been a gradual slight decrease in demand from its highest point, however demand is still high averaging 78-82 on weekdays on a /100 index (as compared with 48-50 on weekdays pre-COVID).This reflects how many firms have shifted to using Microsoft Teams to communicate in light of the pandemic, more than doubling the user base over this time period.",
		"Amazon":"Interest in Amazon in the UK has remained very high across all UK regions, with Wales and Scottish demand outpacing English or Northern Irish demand proportionally to population over this time period. Amazon interest has seen a steady increase from approximately 61/100 to 100 on March 29th, with multiple further peaks in April and May. Consistently high demand has slightly subsided from maximum levels, but interest in Amazon still far exceeds pre-Covid levels, with an almost 50% increase in daily searches. Interestingly, the biggest increase in searches has touched on amazon's delivery status (3,200%+ growth), amazon hair clippers and amazon paddling pools and (2650%+ growth), reflecting how the UK population is preparing for summer and buying more stay-at-home products.",
		"Facebook":"Interest in facebook searches peaked on March 22nd and April 5th and has since seen a slow stabilisation at 75-85% of maximum recorded interest. A decrease in interest may reflect how the economy is starting to open up and less people are now surfing social media than durign the pandemic time. An interesting trend is that proportional to population there is considerably higher interest in facebook in NI (100/100) Wales (90/100) and Scotland (80/100) compared to England (64/100) which may reflect the continuation of work in industrial hubs in England and the subsequently lower-than-proportional use of social media.",
		"Tesla":"Tesla searches saw a major drop  from early march to mid april, and despite the peak across apr 30-may 3, has since been on a downwards trajectory.",
		"BMW":"BMW searches dropped off with an almost 50% decrease between 6th of March and early march. While there has been a gradual uptake in increase this has been relatively slow, with end of may interest in BMW searches still at 3/4 of early march levels.",
		"Apple":"Apple has seen an increase in searches over this time period with a steady positive trajectory taking them from a 61/100 index score at the start of March to 82/100 by end of May. This likely reflects increased consumer activity as some covid restrictions are reduced, and Apple is beginning to reopen certain stores around the world.",
		"Nike":"Nike saw a significant decrease in demand in the run-up to lockdown announcements, however has since seen a significant rise in searches, with searches for Nike growing from the Mar 23rd low of 27/100 to an index peak on may 25th, reflecting stronger consumer purchasing behaviour.",
		"Uber":"Interest in Uber has shown considerable volatility over this time. Despite this, there has been a clear decreasing trend of searches with searches falling from a high index score of 100 on march 21st to 36/100 by mid march and only reaching the high 50s by end of May.",
		"IBM":"Searches for IBM reflect business work days. While there has been a slight decrease in peak searches, generally week-to-week, across weekdays IBM searches remain at 70-80. On weekends across the time studied, demand falls significantly to ~25/100 index scores.",
		"Walt Disney":"Searches for walt disney peaked on March 13th when Disney's theme parks were closed and have since been erratic, falling to 19/100 and rising to 78/100 before stabilising on an a decreasing average search path of approx 40/100 index searched per day by end of May.",
		"Zoom":"Searches for zoom saw a significant increase from index 8/100 to 82/100 across the 3rd week of March. Strong popularity of this search remained until 3rd of may, since which there has been a decline in search interests, reaching 34/100 index searches by end of May.",
		"Slack":"Search interest in slack largely reflects working weeks over this period with drop-offs over the weekends Interest picked up in mid march with peaks at Mar 17-18. Since then, interest has dropped steadily, falling from 68/100 to 52/100 over the next 2 months.",
		"McDonalds":"Search interest in Mcdonalds peaked on march 22nd following McDonald’s rolling closure of stores up to march 21th/21th but has otherwise remained far below index max, with only a very slow growth in interest from 13/100 on march 14 to 29/100 on May 25th.",
		"Tesco":"Searches for tesco peaked after the announcement of lockdowns, likely reflecting panic buying. Besides an anomalous further spike in April 12th, where Tesco releases below expected annual revenues, wa. Besides an anomalous further spike in April 12th.",
		"Ocado":"Ocado saw a significant increase in the rup up to lockdown announcements with max usage at across the immediate pre-lockdown team, Despite it's two pre-lockdown spikes, this has not remained as popular a search with searches now at 25% or lower of the index maximum at around May 24rd.",
		"EasyJet":"'EasyJet' saw a significant in searches with a peak in mid march and a subsequent significant decrease in searches post lock-down and flight grounding. Despite occasional peaks near conference times and post announcements from EasyJet."},
	"Business/Marketing": {
		"Big Data":"Searches for Big data have been sporadic reflecting ongoing innovation and interest in the sector. Peaks on the 6th of March and 7th of April reflect hi reflected ongoing global big data conferences, and otherwise search activity has varied between index values of 79 and 53.",
		"Gamification":"Gamification hasn't seen a lot of search engagement with a marked exception of May 1st. This likely reflects the release of the industry leading Cole of Duty gamification reports on May 1st and the post ‘EUvsVirus’ hackathon interest across April 30th/May 1st. Otherwise searches for gamification remain relatively consistent with a small decrease post May 12.",
		"Growth Hacking":"Searches for growth hacking have been sporadic across this period without a notable increase in searches over time. Nevertheless, noticeable peaks around April 21st and May 13th saw a 50% and 23% increase above average. Reflecting a rise in interest after several leading newspapers like 'Business because' and 'Entrepreneur' published articles detailing strategies for growth hacking.",
		"Value Investing":"There has been a trend towards increasing searches for themes around Value investing in the UK over this period with new peaks set over the course of April and then May. This is suggesting increased interest in this investment strategy over time as businesses and retail investors adapt to COVID-related volatility.",
		"Ideation":"Searches for ideation saw a significant decrease from the beginning of march with a trend of spikes towards the middle of the month and a subsequent decline in interest. This may reflect multiple ongoing conference events and the risk averse attitude to new ideas in some companies, hence the volatility.",
		"Millenials":"Since March 20th there has been a consistent clear trend of decreasing searches for Millennials. This reflects a changing focus onto Generation Z-targeted businesses as more firms target the most digitally-friendly generation.",
		"Cusomter Journey":"While interest in a customer journey saw several a general downwards trend between March 7th and May 8th, since then, there has been a significant increase in searches, suggesting a rejuvenation of business activity in this space.",
		"Generation Y":"During the covid pandemic there has been continuous interest in Generation Y related searches. This likely reflects how Generation Y comprises a large segment of the 30s-40s year old audience, who are an important business segment for many consumer facing companies.",
		"Generation Z":"Searches for generation Z have been largely constant with a slight decrease from early highs of index 80/100 around March 24th down to 43/100 by May 25th. This pattern of a gradual decrease likely reflects how many businesses have faced increased difficulty since the imposition of lockdowns and the furlough schemes, leading to a drop in active searches around this topic. Nonetheless, searches increased around April 21. Reflecting posts by the Cosmopolitan, Forbes, the New York Post, Vogue and elemental on the topic of how Covid was affecting Gen Z during this time.",
		"ROI":"Interest in ROI (return on investment) searches fell significantly from March 12th and has been at around 75/100 index scores during weekdays and 50/100 during weekends reflects how businesses have been focusing on dealing with COVID-related problems and have not been investing in expansion.",
		"Offshoring":"There has been an increase in interest in offshoring up until the end of March, however, after the imposition of lockdowns this has largely decreased, with searches around 'offshoring' falling to an index score of <40/100, with the marked exceptions of May 3rd and 6th following conferences addressing issues with Chinese supply chain dependency.",
		"Sustainability":"Since an initial high interest in sustainability with peaks around the 3rd and 10th of March (95+/100), there has been a decrease in interest in sustainability to a index score of approximately 62/100 with only minor increases in popularity across some days in April and May suggesting that sustainability has not seen a significant increase in searches. Interestingly this contrasts with queries about what sustainability means which has seen 250% growth over this time period, suggesting limited knowledge on this topic rather than a lack of interest.",
		"Content Marketing":"Interest in content marketing saw a marked decline after the lockdown announcement on 23rd of March from 100/100 index score to ~60/100. This has slowly risen to approximately 70/100 suggesting a trend towards renewed business marketing activity.",
		"Business Cards":"Since the March 3rd peak there has been a very significant drop in searches for business cards, suggesting how business owners and employees were pessimistic about meeting other employees in the short term. This trend persisted till Approximately april 18th, after which there has been a small trend towards an increased interest in searches, reflecting how businesses are preparing for lockdown restrictions to be lifted.",
		"Real Estate":"Interest in real estate has remained high across the period, with only one fall below 49/100 index score and an otherwise consistent level of searching. The uptake in searches towards the end of August correlates with increasing numbers of retail investors looking to invest at a heavily impacted market and explains the subsequent increase in real estate to nearly equal early March highs. One of the reasons for the lack of marked decrease could be the classification of builders as essential workers and the subsequent strong performance of construction companies during the March/April/May period.",
		"Digital Marketing":"Searches for digital marketing have seen a market decrease from early March, suggesting a decreased focus on marketing widely across the UK amid business closures and the implementation of Lockdowns. So far there isn't a clear trend to suggest there has been an increase in searches across the March to late May period."},
	"Entertainment": {
		"Youtube":"Searches for YouTube have remained very high with a minor increase after the imposition of lockdowns and a consistently 75/100 - 100/100 index score across the march and early april period. In the second half of april and throughout May, searches for Youtube have not been as high as the earlier COVID-time level, however have remained considerably higher than winter-time searches",
		"TikTok":"Searches for TikTok saw a major increase from low index scores of 30-40/100 in early March to a period across early April where TikTok saw a significant increase in searches to a peak 100/100 index score. Since then, there has been a mild decrease in TikTok searches, however this remains >50% higher than pre-March and more than 25% higher than early March levels.",
		"Live Streaming":"Searches for live streaming have decreased across the march to end of may period, even as searches for teams and zoom have risen, suggesting that 'live streaming' as a search has been replaced by brand names that occupy this space. The search term itself grew in popularity until April 2nd and has since seen a fall from an index score of 100/100 to 34/100 by May 24",
		"Twitch":"Twitch has grown significantly as a search term, reflecting the growth of the platform as more conferences and leading influencers move to Twitch instead of other platforms for easy scaling and digital delivery of content. This trend is very clear, with a rise in interest from the March 9th low of a 33/100 index score to high 80-98/100 levels seen at the end of May",
		"Vimeo":"Vimeo searches saw a significant increase from index score 50/100 to 100/100 (doubling) between the start of March and the 8th of April. Since then, searches for Vimeo significantly decreased, falling to early March levels by the end of May.",
		"Disney":"Disney+ searches saw a peak around the March 24th date, when Disney+ launched in the UK. While searches in index terms have since fallen to pre-Covid times with index popularity of 17-21/100. At the same time, related queries have seen a marked increase, with 3900% growth in questions regarding disney plus devices over the same time period",
		"Netflix":"The popularity of searches for Netflix increased significantly in the run up and the immediate aftermath of the COVID lockdowns in the UK and has remained very high up until the end of May, seeing a small decrease, likely reflecting increased competition in the video entertainment space from Amazon Prime and Disney Plus. At the same time, more than 20 searches for specific shows combined with netflix like 'kaos netflix' have seen more than 3,500% growth across this period, reflecting how users largely search for a given programme or film, rather than just the platform.",
		"NowTV":"Searches for NOW TV peaked around the imposition of lockdowns but have seen a decrease since then with a proportional fall in searches of 25-40% since the Mar 21 and Mar 28th peaks. This reflects the popularity of specific shows. The progressive decrease in the popularity of searches likewise reflects increased competition from other platforms like Netflix, Disney+ and Amazon Prime.",
		"HBO":"Searches for HBO have largely remained constant across March, though there was a spike around 2nd-3rd april, when HBO announced they would be offering popular TV shows, movies and documentaries for free through their HBO Go and HBO Now apps. Since then, searches have decreased proportionally falling to indicator scores of ~50 and remaining at this level from the start of May.",
		"FT":"Searches for the FT have increased during the sample Covid time, with a steady increase in searches up until Apr 7th leading to a 3 month high level. This high engagement with the FT has had multiple peaks, remaining consistently high on an index score (86-100/100) reflecting repeat readership and active interest in the FT newspaper.",
		"Economist":"Searches for the economist have remained largely constant, experiencing a small decrease in the second half of May. Peak engagement occurred on April the 14th and 17th when the Economist published key findings from the IMFand subsequently analysed the extent of downturns for the developed economies.",
		"BBC News":"Searches for the BBC show a very interesting trend with peaks around the pre-lockdown times and a subsequent major decrease in searches for the BBC reflecting a decreased engagement with the news. This reflects both the transition of many research-based employees and financial services workers to furlough schemes and the decrease in engagement with the news, which has come out of increased opportunities for leisure at home. Despite small peaks on April 6th and 7th, with index scores of 69 and 71 respectively, search numbers for \'BBC news\' have fallen more than 50% since the May 23rd peak.",
		"The Guardian":"Searches for the Guardian increased in the pre-lockdown deliberation stage but have since declined with a 40% fall in searches between March 16th and early April and a secondary 33% decrease in searches between April 6th and May 22. ",
		"Daily Mail":"The Daily Mail saw an increase in searches up until March 16th, whereafter as the lockdown anouncement became imminent searches largely fell, falling by 37% between the March peak and May 22nd. Since then there have been some signs to suggest an increase in searches, but it isn't yet clear if this will be just a temporary occurrence.",
		"Telegraph":"Searches for the Telegraph rose to peak around March 16-18th but have since slightly decreased, falling to an index score of 75-85/100 across the later march and april period and dropping to 63-70/100 in May and continuing like that till 24th of May.",
		"Independent":"Searches for Independent peaked between March 16th-18th at 97-100/100 index scores before falling to an average of 75 across most of April and an average of 65-70/100 across May, reflecting decreased interest in the Independent relative to \'before COVID times\'."}
}


# -- END OF ANALYSIS ---- #

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
			{'label': 'Business/Marketing', 'value':'Business/Marketing'},
			{'label': 'Companies', 'value':'Companies'},
			{'label': 'Entertainment', 'value':'Entertainment'},
			{'label': 'Skills', 'value':'Skills'},
			{'label': 'Tech', 'value':'Tech'}
		], placeholder="Search keyword category", style={
			'borderColor':'#FFFFFF',
			'backgroundColor':'#000000',
			'width':'250px',
			'color':'#000000'
		}, searchable=False),
		
		# Analysis input field logic
		dcc.Input(id='input-analysis', value="Enter term for analysis", type='text', style={
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
	analysis_to_out = analysis[input_data][input_analysis]
	output = f"{input_analysis} Analysis: {analysis_to_out}"
	data = 	[{'x':relevant_df.index, 'y':relevant_df[relevant_df.columns[i]], 'type':'line', 'name':relevant_df.columns[i]} for i in range(16)]
	
	return html.H3(id='section-header', children=f"{title} Trends", style={
		'textAlign': 'center',
		'color': colors['text'],
	}), dcc.Graph(
		id='output-graph',
		figure={
			'data': data,
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
	app.run_server(debug=True)

# 
# # -------- TASKS TO DO ---------
# 
# 
# # Add all other analyses
# # Make it all look pretty
# 
# 

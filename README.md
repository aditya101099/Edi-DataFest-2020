# Edi-DataFest-2020
Team Phoenix's submission for the COVID Edinburgh DataFest

**Team Name:** Phoenix 
**Names of team members:** [Aditya Rudrapatna](https://www.linkedin.com/in/aditya-r-0ab3b277/), [Lauryn Mwale](https://www.linkedin.com/in/lauryn-mwale-959889182/), [Mark Kleyner](https://www.linkedin.com/in/markkleyner/), [Nia Indigo Allen-Cooper](https://www.linkedin.com/in/nia-allen-cooper/)

We've built a beautiful web app where you can experience our submission. Check it out [here](https://phoenix-datafest.herokuapp.com)

# Table of Contents
* [Introduction](https://github.com/aditya101099/Edi-DataFest-2020#introduction)
* [Technologies](https://github.com/aditya101099/Edi-DataFest-2020#technologies)
* [Usage](https://github.com/aditya101099/Edi-DataFest-2020#usage)
* [Requirements](https://github.com/aditya101099/Edi-DataFest-2020#requirements)
* [Status](https://github.com/aditya101099/Edi-DataFest-2020#status)


## Introduction
Team Phoenix was tasked with exploring the societal impacts of COVID-19 beyond health outcomes. We decided to investigate whether there were surges in certain searches during the UK lockdown. While UK lockdowns began on March 23rd, we chose to study the March 1st - May 25th period, hypothesising that many people would have begun to change their search preferences 2-3 weeks before in anticipation. We limited the search period to May 25th, the day George Floyd died, so that results wouldn’t be skewed by the BLM movement & protest news. Google Trends provides data on the relative search volumes (RSV) of topics and queries over time and across geographical areas. We thus used this to analyse changing public interests during the pandemic. 

We identified 16 buzzwords to look into for across the categories of entertainment, skills, companies, business/marketing and technology to provide a sufficient representation of large UK sectors and general concepts. Each of the categories was chosen for a set of key reasons, to give us an overall analysis of the UK economy today and the relevant socio-economic impacts:

**Business/Marketing search terms:** Big Data, Gamification, Growth Hacking, Value Investing, Ideation, Millennials, Customer Journey, Generation Y, Generation Z, Return on Investment, Offshoring, Sustainability, Content Marketing, Business Cards, Real Estate, Digital Marketing

**Companies serach terms:** Microsoft, Amazon, Facebook, Tesla, BMW, Apple, Nike, Uber, IBM, Walt Disney, Zoom, Slack, McDonalds, Tesco, Ocado, EasyJet

**Entertainment search terms:** Youtube, TikTok, Live Streaming, Twitch, Vimeo, Disney +, Netflix, NowTV, HBO, FT, Economist, BBC News, The Guardian, Daily Mail, Telegraph, The Independent

**Skills search terms:** Baking, Home Workout, Online Courses, Working from Home, Supermarket jobs, How to buy stocks, Learn a language, How to code, Painting, Drawing, Sewing, KS2 Maths, How to make a mask, Volunteering, Emotional Intelligence, Internships

**Tech search terms:** Natural Language Processing, Computer Vision, Internet of Things, Quantum Computing, Blockchain, Artificial Intelligence, Machine Learning, Automation, 5G, Drones, Cloud Computing, Disruptive Technologies, Web 2.0, AR, Virtual Reality, Robotics

You can also get access to our [report](https://drive.google.com/file/d/1naFgk1-DI_3NmTkHEmq1-RDZ1NkmiMqV/view), as well as our [methodology](https://drive.google.com/file/d/1PS2Z9xrk1Bns6eTOfWXdvwUWZsUv6Ndy/view)

## Technologies

This visualization runs on Python, with a backend powered by Dash by Plotly. The web app is deployed using Flask and Heroku. The data organization and analysis is done using Pandas. 

## Usage

You can access the web app with the link at the top of this page, or you can run it on your own system. 

To use this on your own system, you need to download Dash, by Plotly. Instructions on how to do so are [here](https://dash.plotly.com/installation). Then, run ___app.py___ as you would run any other Python script. To view the visualization, simply then navigate to http://127.0.0.1:8050 in the browser of your choice. The server will remain active insofar as the Terminal window is not deactivated.

## Requirements

In addition to Dash, you might also need the latest version of Python, which you can get [here](https://www.python.org/downloads/)

If you don't have [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html) or [numpy](https://scipy.org/install.html), you need to get that too.

A full list of requirements can be found in the [requirements.txt](https://github.com/aditya101099/Edi-DataFest-2020/blob/master/requirements.txt) file.

## Status

As of June 14 2020, both the web app and local app are perfeclty functuonal. You can assume this is true subject to further ntoice. 
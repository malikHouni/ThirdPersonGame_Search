import streamlit as st
# Library for opening url and creating
# requests
import urllib.request

# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present
# on the website
from html_table_parser.parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd


# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):

	# Opens a website and read its
	# binary contents (HTTP Response Body)

	#making request to the website
	req = urllib.request.Request(url=url)
	f = urllib.request.urlopen(req)

	#reading contents of the website
	return f.read()

# defining the html contents of a URL.
xhtml = url_get_contents('https://en.wikipedia.org/wiki/List_of_third-person_shooters').decode('utf-8')

# Defining the HTMLTableParser object
p = HTMLTableParser()

# feeding the html contents in the
# HTMLTableParser object
p.feed(xhtml)

# Now finally obtaining the data of
# the table required
#pprint(p.tables[1])

# converting the parsed data to
# dataframe
print("\n\nPANDAS DATAFRAME\n")
df=pd.DataFrame(p.tables[1])

#the first row is actually the columns, let's arrange that with following lines
df.columns = df.iloc[0] 
df = df[1:]
df['Platform(s)']=df['Platform(s)'].str.split(',')

st.header("Find the Third-Person-Shooter by platform:")

listPlatforms=[]
for elem in df['Platform(s)']:
    for item in elem:
        listPlatforms.append(item)
len(listPlatforms)
stripList=[]
for item in listPlatforms:
    stripList.append(item.strip())
len(stripList)
finalPlatformList = set(stripList)

choosenPlatform = st.selectbox("Platform: ",finalPlatformList)
#choosenPlatform = st.text_input("give a platform name(ex:Wii,Win,...")
choosenPlatform2= " "+choosenPlatform
st.table(df[df['Platform(s)'].apply(lambda x: any(item for item in [choosenPlatform,choosenPlatform2] if item in x))])
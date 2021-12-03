import streamlit as st


# for converting the parsed data in a
# pandas dataframe
import pandas as pd


df = pd.read_csv("./tpsList.csv")
df= df.drop(['Unnamed: 0'],axis=1)

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

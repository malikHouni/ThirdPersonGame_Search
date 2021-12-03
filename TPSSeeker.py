import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("./tpsList.csv")
df= df.drop(['Unnamed: 0'],axis=1)
df['Platform(s)']=df['Platform(s)'].str.split(',')

listPlatforms=[]
for elem in df['Platform(s)']:
    for item in range(len(elem)):
        listPlatforms.append(np.array(elem)[item])
stripList=[]
for item in listPlatforms:
    stripList.append(item.strip())
len(stripList)
finalPlatformList = set(stripList)
st.header("Find the Third-Person-Shooter by platform:")
choosenPlatform = st.selectbox("Platform: ",finalPlatformList)
#choosenPlatform = st.text_input("give a platform name(ex:Wii,Win,...")
choosenPlatform2= " "+choosenPlatform
st.table(df[df['Platform(s)'].apply(lambda x: any(item for item in [choosenPlatform,choosenPlatform2] if item in x))])

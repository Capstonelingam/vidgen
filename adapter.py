import streamlit as st
import pandas as pd


def preprocess_script(script):
    charDf,sceneList=None,None

    #add function to call to model api

    #placeholder
    if charDf==None or sceneList==None:
        st.warning("Model not connected using placeholder values")
        charDict={
            "object-id":["James","Mary"],
            "image-path":['assets/james.jpeg','assets/mary.jpeg']
        }
        charDf=pd.DataFrame(charDict)
        sceneList=['<James> and <Mary> are in a room','<James> and <Mary> are eating an icecream']
    return charDf,sceneList

def textual_invertor(charDf):
    #add function to call to model api

    #placeholder
    st.warning("Model not connected using placeholder values")
    charDict={
        "object-id":["James","Mary"],
        "image-path":['assets/james.jpeg','assets/mary.jpeg']
    }
    #model with trained images
    model_path='temp/model.h5'
    for index,row in charDf.iterrows():
        #call textual inversion here
        continue

    return model_path

def video_generator(model_path,sceneList):
    #add function to call to model api

    #placeholder
    st.warning("Model not connected using placeholder values")
    video_path='temp/video.gif'
    return video_path
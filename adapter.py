import streamlit as st
import pandas as pd
import script_preprocessor as sp
import torch
import gc

def check_memory():
    file=open('temp/memory.txt','w')
    for obj in gc.get_objects():
        
        try:
            if torch.is_tensor(obj) or (hasattr(obj, 'data') and torch.is_tensor(obj.data)):
                print(type(obj), obj.size(),file=file)
        except: pass

    # for obj in gc.get_objects():
    #     try:
    #         if torch.is_tensor(obj) or (hasattr(obj, 'data') and torch.is_tensor(obj.data)):
    #             print(type(obj), obj.size())
    #     except:
    #         pass

def preprocess_script(script,script_given):
    if script_given==False:
        st.warning("Input Script not given using placeholder values")
        charDict={
            "object-id":["James","Mary"],
            "image-path":['assets/james.jpeg','assets/mary.jpeg']
        }
        charDf=pd.DataFrame(charDict)
        sceneList=['<James> and <Mary> are in a room','<James> and <Mary> are eating an icecream']

        

    else:
    #add function to call to model api
        charList=sp.get_char_list(script)
        sceneDf=sp.createJSON(script)
     
        torch.cuda.empty_cache()
        gc.collect()

        ##still a list of characters
        print(charList)
        print(sceneDf)

        print()
        print()
        print()

        check_memory()



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
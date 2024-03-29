import streamlit as st
import pandas as pd
import script_preprocessor as sp
import scriptrunner as sr
import torch
import gc,os
from utils.get_character_images import get_character_images
from PIL import Image,ImageEnhance

from script_to_video_pipeline import ScriptToVideoPipeline
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
            "image-path":['assets/james.jpg','assets/mary.jpg']
        }
        charDf=pd.DataFrame(charDict)
        promptList=['<James> and <Mary> are in a room','<James> and <Mary> are eating an icecream']

        

    else:
    #add function to call to model api
       # charList=sp.get_char_list(script)
        #sceneDf=sp.createJSON(script)
        charList,sceneJSON=sr.script_preprocess(script)
        torch.cuda.empty_cache()
        gc.collect()
        promptList = []
        for scene in sceneJSON.keys():
            for action in sceneJSON[scene]['Actions']:
                promptList.append(action + " in " + sceneJSON[scene]['Env'])


        
        ##still a list of characters
        output_folder='temp'
        charDf=sr.make_images_for_characters(charList,output_folder)
        print()
        print()
        print()

        #check_memory()

    return charDf,promptList

def make_image_dataset(charDf):
    print("populating image dataset")
    st.success("Populating Image Dataset")
    for index,row in charDf.iterrows():
        #call textual inversion here
        temp_folder='/'.join(row['image-path'].split('/')[:-1])+'/'
        print(row['image-path'])
        original=Image.open(row['image-path'])
        sharpener = ImageEnhance.Sharpness(original)
        brightness=ImageEnhance.Brightness(original)


        vertical=original.transpose(Image.FLIP_LEFT_RIGHT)
        horizontal=original.transpose(Image.FLIP_TOP_BOTTOM)
        rotated=original.transpose(Image.ROTATE_90)
        sharper=sharpener.enhance(2.0)
        blurred=sharpener.enhance(-2.0)
        brighter=brightness.enhance(2.0)
        darker=brightness.enhance(0.5)


        
        row['object-id']=str(row['object-id'])

        vertical.save(temp_folder+'vertical_'+row['object-id']+'.png')
        horizontal.save(temp_folder+'horizontal_'+row['object-id']+'.png')
        rotated.save(temp_folder+'rotated_'+row['object-id']+'.png')
        sharper.save(temp_folder+'sharper_'+row['object-id']+'.png')
        blurred.save(temp_folder+'blurred_'+row['object-id']+'.png')
        brighter.save(temp_folder+'brighter_'+row['object-id']+'.png')
        darker.save(temp_folder+'darker_'+row['object-id']+'.png')

        
        row['image-path']=temp_folder

    st.success("Populated Image Dataset")
    return charDf

def preprocess_prompt(charDf,promptList):
    #add function to call to model api
    #placeholder

    #replace James with <James>
    for index,row in charDf.iterrows():
        for i in range(len(promptList)):
            if str(row['object-id']) in promptList[i]:
                promptList[i]=promptList[i].replace(row['object-id'],'<'+row['object-id']+'>')

  
    return promptList  

def train_textual_inversion():
    placeholder_csv=pd.read_csv('temp/placeholder.csv')
    charDf=pd.read_csv('temp/charFinal.csv')
    output_folder='temp/model'
    if placeholder_csv.equals(charDf)==False:
        os.mkdir(output_folder)
        print(charDf)
        pretrained=False    
        for index,row in charDf.iterrows():
            if pretrained==False:
                output_folder=sr.addCharacter(row['object-id'],row['image-path'],output_folder=output_folder)
                pretrained=True
            else:
                output_folder=sr.addCharacter(row['object-id'],row['image-path'],output_folder,pretrained=True)
    return output_folder+"/learned_embeds.bin"

def video_generator(model_path,sceneList):
    promptList=['<<James>> and <<Mary>> are in a room', '<<James>> and <<Mary>> are eating an icecream']

    if sceneList!=promptList:
        
        pipe=ScriptToVideoPipeline()
        video_path=pipe.generate_video(sceneList,custom_pipeline=True,custom_pipeline_path=model_path,demo = False)
        #add function to call to model api

        #placeholder
    else:
        st.warning("Model not connected using placeholder values")
        video_path='temp/video.gif'
    return video_path

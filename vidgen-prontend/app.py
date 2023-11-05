import streamlit as st
import pandas as pd
import adapter
from PIL import Image
import os
import base64


#states of the application
TEXT_GIVEN = False
TEXT_ANALYSED = False

IMAGES_CONFIRM = False
IMAGES_LEARNED = False

VIDEO_GENERATED = False
VIDEO_UPSCALED = False
VIDEO_INTERPOLATED = False



#setup
st.set_page_config(page_title="Script In Video Out",page_icon='assets/icon.jpeg')

header_container=st.container()
with header_container:
    title_body="""
    <h1 style='text-align: center; font-size:10vh'>
    Script-To-Video Generator
    </h1>
    """
    st.markdown(title_body, unsafe_allow_html=True)
    caption_body="""
    <h3 style='text-align: center; font-size:3vh'>
    An end-to-end pipeline to generate videos from text
    </h3>
    """
    st.caption(caption_body,unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)




#input container
input_script_container=st.container()
script=None
with input_script_container:
    st.header("Input Script")
    col1, col2 = st.columns((1,1))
    with col1:
        script=st.text_area("Enter Script Here")
    with col2:
        uploaded_file=st.file_uploader("Upload Script Here",type=['txt'],help="Upload a text file containing the script")
        if uploaded_file:
            script=str(uploaded_file.read()).lstrip("b'").rstrip("'")
    if st.button("Submit Script"):
        if script:
            TEXT_GIVEN=True
            st.text(script)
            st.success("Script Uploaded Successfully")


        else:
            st.warning("Please enter a script or upload a text file")  
        
    st.markdown("---", unsafe_allow_html=True)


#process script
process_script_container=st.container()
#change line to pipeline api

charDf,sceneList=adapter.preprocess_script(script)




def save_uploadedfile(uploadedfile):
     with open(os.path.join("temp",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))


#character container
character_container=st.container()
with character_container:
    st.title("Characters")
    dimensions=[1]*len(charDf)
    display_list=st.columns(dimensions)
    for index,row in charDf.iterrows():
        image_file=Image.open(row['image-path'])
        display_list[index].image(image_file,caption=row['object-id'])
        uploaded_file=display_list[index].file_uploader(f"Upload Custom Image for {row['object-id']}",type=['png','jpg','jpeg'],help="Upload an image of the character")

        if uploaded_file:
            save_uploadedfile(uploaded_file)
            row['image-path']=os.path.join("temp",uploaded_file.name)
            image_file=Image.open(row['image-path'])
            display_list[index].image(image_file,caption=row['object-id'])
        IMAGES_CONFIRM=True
    st.title("SceneList")
    for i in range(len(sceneList)):
        st.code(sceneList[i])
    st.markdown("---", unsafe_allow_html=True)


if st.button("Generate Video"):
    #textual inversion
    model=adapter.textual_invertor(charDf)

    #call model
    video_path=adapter.video_generator(model,sceneList)





    #video_player
    video_player_container=st.container()
    with video_player_container:
        st.header("Video Player")
        
        file_ = open(video_path, "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="Video File">',
            unsafe_allow_html=True,
    )
        
#footer
footer_container=st.container()
with footer_container:
    st.markdown("---", unsafe_allow_html=True)    
    col1, col2, col3 = st.columns((2,1,1))
    with col1:
        st.header("Paper Information")
        paper_info="""
        <p>
        Animated Videos with sequential storylines and consistent characters. <br/>
        The paper for the above project can be found <a href="https://arxiv.org/abs/2104.00680"> here </a>
        </p>
        """
        st.markdown(paper_info, unsafe_allow_html=True)
    
    with col2:
        st.header("Contact Information")
        contact_info="""
            <p>
                <table>
                    <tr>
                        <th> Name </th>
                        <th> Github </th>                
                    </tr>
                    <tr>
                        <td> Ayush Singh </td>
                        <td> <a href='https://github.com/CoderCatA5'>CoderCatA5</a> </td>                
                    </tr>
                    <tr>
                        <td> Ram Selvaraj</td>
                        <td> <a href='https://github.com/ramselvaraj'>ramselvaraj</a> </td>                
                    </tr>
                    <tr>
                        <td> Shafiudeen Kameel </td>
                        <td> <a href='https://github.com/ShafiudeenKameel'>ShafiudeenKameel</a> </td>                
                    </tr>
                    <tr>
                        <td> Rahul Samal </td>
                        <td> <a href='https://github.com/Omicron02'>Omricon02</a> </td>                
                    </tr>
                </table>
            </p>
        """
        st.markdown(contact_info, unsafe_allow_html=True)

    st.markdown("---", unsafe_allow_html=True) 
        


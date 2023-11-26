#from Optional import str,int,bool
from torch.cuda import empty_cache
import gc
import os
import subprocess
import json
import pandas as pd


def run_inference(model,prompt,num_frames,width,height,window_size,num_steps,custom_pipeline_path="temp/model/learned_embeds.bin",custom_pipeline=None,fps=17,seed=6969,guidance=25,output_folder="/output", sop = "/output",prompt_num = 0):
    custom_pipeline_path ="temp/model/learned_embeds.bin"
    
    print(sop)
#     os.system(f'python inference.py \
#         --model {model} \
#         --prompt "{prompt}" \
#         --num-frames 60 \
#         --width 256 \
#         --height 256 \
#         --window-size 60 \
#         --num-steps 500 \
#         --custom_pipeline_path {custom_pipeline_path} \
#         --custom_pipeline False \
#         --fps 18 \
#         --seed 420\
#         -g 25 \
#         --sdp\
#     ')
#     os.system(f'python inference.py \
#         --model {model} \
#         --prompt "{prompt}" \
#         --num-frames 60 \
#         --width 256 \
#         --height 256 \
#         --window-size 60 \
#         --num-steps 500 \
#         --fps 18 \
#         --seed 420\
#         -g 25 \
#         --sdp\
#     ')
    command_list=["python", "inference.py", 
                  "--model", "cerspense/zeroscope_v2_576w", 
                  "--prompt", prompt, "--num-frames", str(24), 
                  "--width", str(256), "--height", str(256), 
                  "--window-size", str(60), 
                  "--num-steps", str(400), "--custom_pipeline_path", custom_pipeline_path, 
                  "--custom_pipeline", str(custom_pipeline), 
                  "--fps", str(18), "--seed", str(420), "-g", str(guidance), 
                  "--sdp", 
                  "--scene_out_path", sop, "--scene_number", str(prompt_num)
                  ]
    subprocess.run(command_list)
    print(command_list)
    #os.system(f"""python inference.py --model "cerspense/zeroscope_v2_576w" --prompt "{prompt}" --num-frames 24 --width 256 --height 256 --window-size 60 --num-steps 150 --fps 18 --seed 420 -g 25 --sdp --scene_out_path "{sop}" --scene_number {prompt_num}

#     print(f"""python inference.py --model "cerspense/zeroscope_v2_576w" --prompt "{prompt}" --num-frames 8 --width 256 --height 256 --window-size 60 --num-steps 100 --fps 2 --seed 420 -g 25 --sdp --scene_out_path "{sop} --scene_number {prompt_num}"
#

    empty_cache()
    gc.collect()

def script_preprocess(script: str):
    subprocess.run(['python','script_preprocessor.py'])
    empty_cache()
    gc.collect()
    charList = []
    prepped_JSON_dict = {}
    with open('./temp/charList.txt', 'r') as file:
        file_content = file.read()
        charList = file_content.split(',')
        file.close()
    with open('./temp/preppedJSON.json','r') as file:
        file_content = file.read()
        prepped_JSON_dict = json.loads(file_content)
        file.close()
    print(charList)
    return charList, prepped_JSON_dict


def addCharacter(character,path_to_input_images,output_folder,pretrained=False,num_steps=100):
    
    if pretrained==False:
    
        #!leap_textual_inversion 
        # --pretrained_model_name_or_path=stabilityai/stable-diffusion-2-1-base 
        # --placeholder_token="<kunal>" 
        # --train_data_dir=train_images/kunal 
        # --learning_rate=0.001 
        # --leap_model_path=weights/leap_ti_2.0_sd2.1_beta.ckpt 
        # --max_train_steps 100 
        subprocess.run(['leap_textual_inversion',
                        '--pretrained_model_name_or_path=stabilityai/stable-diffusion-2-1-base',
                        f'--placeholder_token="<{character}>"',
                        f'--train_data_dir={path_to_input_images}' ,
                        '--learning_rate=0.001',
                        '--leap_model_path=sd-leap-booster/weights/leap_ti_2.0_sd2.1_beta.ckpt',
                        f'--output_dir={output_folder}',
                        '--max_train_steps',str(num_steps)
                        ])
    else:
        subprocess.run(['leap_textual_inversion',
                    f'--pretrained_model_name_or_path={output_folder}',
                    f'--placeholder_token="<{character}>"',
                    f'--train_data_dir={path_to_input_images}' ,
                    '--learning_rate=0.001',
                    '--leap_model_path=sd-leap-booster/weights/leap_ti_2.0_sd2.1_beta.ckpt',
                    '--output_dir='+output_folder,
                    '--max_train_steps',num_steps
                    ])

    print(f'{output_folder}/learned_embeds.bin')
    return output_folder


def make_images_for_characters(characterList, output_folder):
    characterListStr = ','.join(characterList)
    print(characterListStr)    
    characterListStr = characterListStr.replace(' ','')
    subprocess.run(['python','utils/get_character_images.py','--characterList',characterListStr,'--output_folder',output_folder])
    charDf=pd.read_csv(output_folder+"/charList.csv")
    return charDf


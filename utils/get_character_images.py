from diffusers import StableDiffusionPipeline
import torch
import os
import argparse
import pandas as pd

def get_character_images(characterList,output_folder):
    model_id ="stabilityai/stable-diffusion-2-1-base" 
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")
    print(characterList)

    image_path_list=[]
    for character in characterList:
        print(character)
        os.mkdir(output_folder + '/'+character)
    
        prompt = "A waist up potrait of james, realistic , high quality" +character

        image = pipe(prompt, num_inference_steps=50).images[0]
        image_path=output_folder+ '/'+ character+'/' +character+ ".png"
        image.save(image_path)
        image_path_list.append(image_path)
    data={
        "object-id":characterList,
        "image-path":image_path_list
    }
    df=pd.DataFrame(data)
    df.to_csv(output_folder+"/charList.csv",index=False)
    print(df)



def list_of_strings(arg):
    return arg.split(',')

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--characterList', nargs='+', help='List of characters to be added',type=list_of_strings)
    parser.add_argument('--output_folder', help='output folder')
    args = parser.parse_args()
    get_character_images(args.characterList[0],args.output_folder)

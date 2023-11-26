import inference  # inference.py
from typing import List, Optional
import script_preprocessor 
import os
from einops import rearrange
from utils.lama import inpaint_watermark
from train import export_to_video
from utils.video_sticher import stitch_video 
import torch
import json
from scriptrunner import run_inference,addCharacter
import os
from moviepy.editor import VideoFileClip, VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import clips_array
class ScriptToVideoPipeline:
    def __init__(self, script="EmptyScript", model_path="cerspense/zeroscope_v2_576w"):
        self.script = script
        self.model_path = model_path
    
    def prepare_inputs_for_vidgen(self,original_script):
        # ramsel
        # function calls llm to get characters
        # function calls llm to get actions
        # function calls llm to get environment
        charList = script_preprocessor.get_char_list(original_script)
        prepped_json_dict = script_preprocessor.createJSON(original_script)
#         prepped_json_dict = json.loads("""{
    
#         "Scene 1": {"Actions":["Emily wanders through the French Quarter", "Marcus plays his guitar on a corner", "Emily sketches Marcus" ], "Env": "New Orleans" } ,
    
#         "Scene 2": {"Actions":["Alex dives into the digital realm", "Elena grapples with the moral implications of artificial intelligence" ], "Env": "Neonova" } ,
    
#         "Scene 3": {"Actions":["Emily and Marcus collaborate on an art exhibit", "Alex and Elena's online exchanges deepen"  ], "Env": "New Orleans" }
# }""")
#         charList = ["Emily","Marcus"]
        # calls leap for each new token in embeddings
        # placeholder variable
#         prepped_script = ['<james> standing', '<james sitting>',
#                           '<james> walking', '<james> running']
        
        return charList,prepped_json_dict

    def video_upscaler(path_to_videos):
        # kameel
        # calls vid2vid
        # returns path to upscaled videos
        return path_to_videos

    def save_video(self, videos,fps=30, filename="outputs/test_video",remove_watermark=False):
        # saves video to path
    

        for video in videos:
            if remove_watermark:
                print("Inpainting watermarks...")
                video = rearrange(video, "c f h w -> f c h w").add(1).div(2)
                video = inpaint_watermark(video)
                video = rearrange(video, "f c h w -> f h w c").clamp(0, 1).mul(255)

            else:
                video = rearrange(video, "c f h w -> f h w c").clamp(-1, 1).add(1).mul(127.5)

            video = video.byte().cpu().numpy()

            export_to_video(video, f"{filename}.mp4", fps)

    def generate_video(self,sceneList, model="cerspense/zeroscope_v2_576w", init_video=None, seed=6969, custom_pipeline=False,window_size=50,num_frames=50,custom_pipeline_path="", demo = False):
        
         #to make a file handling solution for this
        #give an option to the user to either use the previous video or not
        #save all intermediate videos in a folder with scene number 
        #stitch them together at the end

        output_folder = f"./output/{sceneList[0]}"
        os.makedirs(output_folder, exist_ok=True)
        os.makedirs(output_folder+"/temp", exist_ok=True)

        #init_video = "takes the path to the previous video that has already been generated"
        init_video = None

        if demo == True:
            sceneList = sceneList[0:2]

        for scene_num,scene in enumerate(sceneList):
            torch.cuda.empty_cache()
            torch.cuda.reset_peak_memory_stats()
            print(f"Generating video for scene {scene_num+1}...")

            #output_path=f"{scene_num}_{scene}.mp4"
            
            print(scene)
            run_inference(model=model,
                          prompt=scene,
                          num_frames=50,
                          width=300,
                          height=300,
                          window_size=50,
                        num_steps=100,
                        custom_pipeline_path=custom_pipeline_path,
                        custom_pipeline=False,
                        seed=6969,
                        guidance=25,
                        output_folder=output_folder,
                        fps=17,
                         sop = f"output/{sceneList[0]}",
                          prompt_num = scene_num+1
                          )
            
            

        #save the video
        #self.save_video(videos, f"{output_folder}/{output_path}", remove_watermark=True)
        #CHANGE TO DUMP FRAMES ON CPU AND COMBINE from there
        # Define the directory containing the MP4 files
        input_directory = f"./output/{sceneList[0]}/temp"

        # Get a list of MP4 files in the directory
        mp4_files = [f for f in os.listdir(input_directory) if f.endswith(".mp4")]

        # Sort the files by their numeric names
        mp4_files.sort(key=lambda x: int(os.path.splitext(x)[0]))

        # Create VideoFileClip objects for each MP4 file
        video_clips = [VideoFileClip(os.path.join(input_directory, mp4_file)) for mp4_file in mp4_files]

        # Concatenate the video clips into a single video
        final_video = concatenate_videoclips(video_clips, method="compose")

        # Define the output directory and file name
        output_directory = f"./output/{sceneList[0]}"
        output_file = os.path.join(output_directory, f"{sceneList[0]}.mp4")

        # Write the final video to the output file
        final_video.write_videofile(output_file, codec="libx264")

        # Close the video clips
        for video_clip in video_clips:
            video_clip.reader.close()

        # Clean up (optional) - delete the original files from the input directory
        for mp4_file in mp4_files:
            os.remove(os.path.join(input_directory, mp4_file))
        
        return output_file
           
    def run(self):
        import decord
        import gc

        decord.bridge.set_bridge("torch")
        torch.cuda.empty_cache() 
        gc.collect()
        
        #model = "cerspense/zeroscope_v2_576w" default
        #model = "strangeman3107/animov-512x"  anime-style
        #model = "damo-vilab/text-to-video-ms-1.7b"  all purpose use with a remove watermark
        

       
        charList,sceneJSON = self.prepare_inputs_for_vidgen(script)
        torch.cuda.empty_cache() 
        gc.collect()
        #sceneList=['a girl is running on the treadmill','a girl is running on the snow']
        sceneList = []
        for scene in sceneJSON.keys():
            for action in sceneJSON[scene]['Actions']:
                sceneList.append(action + "in " + sceneJSON[scene]['Env'])
        print(sceneList)                        
        self.generate_video(sceneList[0:2], model=self.model_path, init_video=None, seed=6969, custom_pipeline=False)

    def addCharacters(charList,init_model):
        custom_pipeline_path = "sd-leap-booster/text-inversion-model/learned_embeds.bin"
        return custom_pipeline_path


if __name__=="__main__":
    script = """In the enchanting city of New Orleans, the lively streets come alive with music and color. Emily, a passionate artist, wanders through the French Quarter, her sketchbook capturing the essence of the vibrant scenes around her. One day, her path crosses with Marcus, a reclusive writer, who plays his guitar on a corner. Intrigued by his melodies, Emily starts sketching him, and they strike up an unlikely friendship.

Meanwhile, across the country in the high-tech hub of Neonova, Alex, a skilled hacker, dives into the digital realm, seeking the thrill of challenges that push the boundaries. In this city of neon lights and innovation, Elena, a brilliant scientist, grapples with the moral implications of artificial intelligence. Through an online forum, Alex and Elena engage in intense debates, their virtual connection deepening.

As Emily and Marcus collaborate on an art exhibit inspired by the spirit of New Orleans, Alex and Elena's online exchanges evolve into a shared vision for a more responsible AI-driven future. Their paths unexpectedly cross when Elena is invited to speak at a conference in New Orleans, and Alex seizes the opportunity to meet in person. The chemistry between them is palpable, and their ideas flourish when brought together.

The art exhibit becomes a stunning reflection of Emily and Marcus' friendship and the soul of the city, while Alex and Elena's joint presentation at the conference sparks a fresh dialogue about ethics in technology. These four individuals, each driven by their unique passions, soon realize that their talents are complementary, sparking a collaborative project that marries art and technology to create social change.

Through twists and turns, challenges and triumphs, the four find themselves united by their shared purpose. The exhibit attracts attention not only for its beauty but also for the message it carries."""
    #charList,prepped_json_dict = ScriptToVideoPipeline.prepare_inputs_for_vidgen(script)
    custom_pipeline_path = ScriptToVideoPipeline.addCharacters([],init_model = "")
    pipeline = ScriptToVideoPipeline(script,custom_pipeline_path)
    pipeline.run()
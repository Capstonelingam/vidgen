from inference import inference  # inference.py
from typing import List, Optional
from script_preprocessor import createJSON
import os
from einops import rearrange
from utils.lama import inpaint_watermark
from train import export_to_video
from utils.video_sticher import stitch_video 
class ScriptToVideoPipeline:
    def __init__(self, script, model_path):
        self.script = script
        self.model_path = model_path
    
    def prepare_inputs_for_vidgen(original_script):
        # ramsel
        # function calls llm to get characters
        # function calls llm to get actions
        # function calls llm to get environment
        json_output = createJSON(original_script)
        # calls leap for each new token in embeddings
        # placeholder variable
        prepped_script = ['<james> standing', '<james sitting>',
                          '<james> walking', '<james> running']
        return prepped_script

    def video_upscaler(path_to_videos):
        # kameel
        # calls vid2vid
        # returns path to upscaled videos
        return path_to_videos


    
    def save_video(self, videos,fps, filename="outputs/test_video",remove_watermark=False):
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



    def generate_video(self,
                       sceneList,
                       model: str ="cerspense/zeroscope_v2_576w",     #model path to huggingface
                       negative_prompt: Optional[str] = None,
                       width: int = 256,
                       height: int = 256,
                       num_frames: int = 45,
                       window_size: Optional[int] = None, #full sequence
                       vae_batch_size: int = 8,
                       num_steps: int = 50,
                       guidance_scale: float = 15,
                       init_video: Optional[str] = None,
                       init_weight: float = 0.5,
                       device: str = "cuda",
                       xformers: bool = False,
                       sdp: bool = False,
                       lora_path: str = "",
                       lora_rank: int = 64,
                       loop: bool = False,
                       seed: Optional[int] = 6969,
                       custom_pipeline: bool = False,
                       custom_pipeline_path: str = "",#path to bin file with textual inversion
                       use_previous_video: bool = False,
                       fps:int=20
                       ):


        #to make a file handling solution for this
        #give an option to the user to either use the previous video or not
        #save all intermediate videos in a folder with scene number 
        #stitch them together at the end

        output_folder = f"output/{sceneList[0]}"
        os.makedirs(output_folder, exist_ok=True)



        #init_video = "takes the path to the previous video that has already been generated"
        init_video = None

        for scene_num,scene in enumerate(sceneList):
            output_path=f"{scene_num}_{scene}.mp4"
            
            video = inference(
                model=model,
                prompt=scene,
                negative_prompt=negative_prompt,
                width=width,
                height=height,
                num_frames=num_frames,
                window_size=window_size,
                vae_batch_size=vae_batch_size,
                num_steps=num_steps,
                guidance_scale=guidance_scale,
                init_video=init_video,
                init_weight=init_weight,
                device=device,
                xformers=xformers,
                sdp=sdp,
                lora_path=lora_path,
                lora_rank=lora_rank,
                loop=loop,
                custom_pipeline =custom_pipeline,
                custom_pipeline_path=custom_pipeline_path
            )
            

            #save the video
            self.save_video(video,fps, f"{output_folder}/{output_path}", remove_watermark=True)
            
            if use_previous_video:
                if init_video==None:
                    init_video = output_path
                else:
                    init_video = output_path
            else:
                init_video=None


    def run(self):
        
        #model = "cerspense/zeroscope_v2_576w" default
        #model = "strangeman3107/animov-512x"  anime-style
        #model = "damo-vilab/text-to-video-ms-1.7b"  all purpose use with a remove watermark


        #sceneList = self.prepare_inputs_for_vidgen(self.script)
        prepped_script = ['<james> standing', '<james sitting>',
                          '<james> walking', '<james> running']
        self.generate_video(prepped_script, model=self.model_path, init_video=None, seed=6969, custom_pipeline=False)
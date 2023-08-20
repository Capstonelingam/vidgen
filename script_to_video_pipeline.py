from inference import inference  # inference.py
from typing import List, Optional
from script_preprocessor import createJSON

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


    
    def save_video(self, video, path="outputs",name):
        # saves video to path
        pass

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
                       ):

        init_video = "output/A chicken crossing the road .Anime style 110156a9.mp4"

        for scene in sceneList:
            video=inference(model,
                      scene,
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
                      seed=seed,
                      custom_pipeline=custom_pipeline,
                      custom_pipeline_path=custom_pipeline_path,
                      )
        


    def run(self):
        
        #model = "cerspense/zeroscope_v2_576w" default
        #model = "strangeman3107/animov-512x"  anime-style
        #model = "damo-vilab/text-to-video-ms-1.7b"  all purpose use with a remove watermark


        sceneList = self.prepare_inputs_for_vidgen(self.script)
        self.generate_video(sceneList, model=self.model_path, init_video=None, seed=6969, custom_pipeline=False)
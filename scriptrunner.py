#from Optional import str,int,bool
from torch.cuda import empty_cache
import gc
import os
def run_inference(model,prompt,num_frames,width,height,window_size,num_steps,custom_pipeline_path="sd-leap-booster/text-inversion-model/learned_embeds.bin",custom_pipeline=None,fps=17,seed=6969,guidance=25,output_folder="/output", sop = "/output",prompt_num = 0):
    custom_pipeline_path = "sd-leap-booster/text-inversion-model/learned_embeds.bin"
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
    os.system(f"""python inference.py --model "cerspense/zeroscope_v2_576w" --prompt "{prompt}" --num-frames 24 --width 256 --height 256 --window-size 60 --num-steps 150 --fps 18 --seed 420 -g 25 --sdp --scene_out_path "{sop}" --scene_number {prompt_num}
""")
#     print(f"""python inference.py --model "cerspense/zeroscope_v2_576w" --prompt "{prompt}" --num-frames 8 --width 256 --height 256 --window-size 60 --num-steps 100 --fps 2 --seed 420 -g 25 --sdp --scene_out_path "{sop} --scene_number {prompt_num}"
# """)

    empty_cache()
    gc.collect()

def addCharacter(character,path_to_input_images):
    path_to_custom_pipeline = "sd-leap-booster/text-inversion-model/learned_embeds.bin"
    
    
    return path_to_custom_pipeline


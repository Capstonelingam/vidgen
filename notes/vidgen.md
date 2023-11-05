## NOTES FOR VIDGEN


### Inference.py


#### IMPORTS
-   argparse - FOR MAKING INTERACTIVE COMMAND LINE ARGUMENTS
-   platform - To identify which machine config we have.(cuda)
-   re       - Regular expressions in python strings
-   uuid     - Generate random strings(used for unique filenames)
- compel    - A text prompt WEIGHTING AND BLENDING library (rework different parts of the embedding that produces the string)
- einops - For tensor operations like rearraging vectors
-torch.nn.functional - interpolate is used when prev video frames smaller than new video
-tqdm - Progress bar


#### Functions
- initialize_pipeline
    - Used to load pipeline onto memory
    - pipeline includes scheduler, tokenizer, text_encoder, vae, _unet
    - **DPMSolveMultiStepScheduler**- Fast dedicated high-order soler with convergence gaurnteed
    - pipeline uses handle_memory_attention, load_primary_models from train.py

- prepare_input_latents
    - If init_video exists then we load the vae with the init_video tensors
    - Else we load it with the pretrained sd model weights

- encode
    - If init_video is true then based on batch size make latents for the init_video
    -retur latents of the given video

- decode
    - decodes latents to pixel space
    - iterates batch by batch decoding latents back to pixel space
    - `pixels = rearrange(pixels, "(b f) c h w -> b c f h w", f=nf)` b and f represent batch and no_of_frame
    - calls autoencoders decode function to decode the latents

- primes_upto_n
    - function for finding primes upto n

- **diffuse** 
    - **main logic of the inference lies here**
    - encodes prompt to embeddings 
    - rotate adds shifts to the video (changes order of break points so that we get an illusion of looping)

    - use a unet to predict `noise_residual`
    - `noise_pred = noise_pred_uncond + guidance_scale * (noise_pred_text - noise_pred_uncond)`
    
`





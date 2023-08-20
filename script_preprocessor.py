#!/usr/bin/env python3

import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline, TextStreamer, TextIteratorStreamer
from threading import Thread
import json

def load_llm():
    model_id = "Trelis/Llama-2-7b-chat-hf-sharded-bf16-5GB" # sharded model by RonanKMcGovern. Change the model here to load something else.
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )

    config = transformers.AutoConfig.from_pretrained(model_id, trust_remote_code=True)
    config.init_device = 'cuda:0' # Unclear whether this really helps a lot or interacts with device_map.

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(model_id, config=config, quantization_config=bnb_config, device_map='auto', trust_remote_code=True) # for inference use 'auto', for training us device_map={"":0}
    
    #load LoRA
    model.load_adapter()
    
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.eos_token
    return model,tokenizer

def generate(script):
    model, tokenizer = load_llm()
    encoding = tokenizer(purpose, return_tensors="pt").to("cuda:0")
    output = model.generate(input_ids=encoding.input_ids, attention_mask=encoding.attention_mask, max_new_tokens=4096, do_sample=True, temperature=0.000001, eos_token_id=tokenizer.eos_token_id, top_k = 0)
    return tokenizer.decode(output[0], skip_prompt = True,skip_special_tokens=True)
    
   
def sanityCheck(JSONDict: dict):
    #function to check if JSON is correct, written at end after format is finalized
    return True

def createJSON(script : str):
    JSONDict = json.loads(generate(script))
    
    #Function to Perform Sanity check on JSON
    try:
        sanityCheck(JSONDict)
    except ValueError:
        print("Unfortunately, JSON Formatted Data isn't accurate")
    except Exception as e:
        #generic error print
        print(str(e))
    
    return JSONDict
    
        
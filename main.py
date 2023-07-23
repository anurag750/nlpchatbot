import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from transformers import GPT2LMHeadModel, GPT2Tokenizer

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
import torch


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
    
max_length = 50  
temperature = 0.7  

def chat_with_bot(input_text):
    # Tokenize the input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate a response
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            temperature=temperature,
            pad_token_id=tokenizer.eos_token_id,
            num_return_sequences=1,
        )

    # Decode the output and remove the input text from the response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    response = response.replace(input_text, "").strip()

    return response


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    
    for text in request.text:        
        output.append(chat_with_bot(text))
        

    return SimpleText(dict(text=output))


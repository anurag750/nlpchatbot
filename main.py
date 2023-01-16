import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from transformers import pipeline

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass
    



############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    model_name = "distilbert-base-cased-distilled-squad"
    nlpchatbot = pipeline('question-answering',model=model_name)
    for text,context in request.text:
        # TODO Add code here
        res = nlpchatbot(question=text,context = context)
        output.append(res[0]['answer'])

    return SimpleText(dict(text=output))


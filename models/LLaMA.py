'''
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
import torch

#Defining model name
#model_name = 'meta-llama/Llama-2-7b-chat-hf'
model_name = 'google/flan-t5-base'

#Creating Model object of type name
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
#model = AutoModelForCausalLM.from_pretrained(model_name, device_map='auto', load_in_4bit=True)

#Initializing Tokenizer of the model name type
tokenizer = AutoTokenizer.from_pretrained(model_name)

#Storing Prompt
prompt = "Write a short summary on Northeastern University"

#Creating tokens using our tokenizer and inputting them to the LLM, returned tokens are in python format
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)

#Storing output received as tokens with a set limit
out = model.generate(**inputs, max_new_tokens=200)

#Detokenizing tokens to readable words and printing them
print(tokenizer.decode(out[0], skip_special_tokens=True))
'''
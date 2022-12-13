#pip install galai

from transformers import AutoTokenizer, OPTForCausalLM
import torch
# tokenizer = AutoTokenizer.from_pretrained("facebook/galactica-1.3b")
tokenizer = AutoTokenizer.from_pretrained("facebook/galactica-30b")
tokenizer.pad_token_id = 1
tokenizer.padding_side = 'left'
tokenizer.model_max_length = 4020

# NOTE: the argument 'torch_dtype = torch.float32' is necessary to get the model run on a CPU (model was trained on float16)
model = OPTForCausalLM.from_pretrained("facebook/galactica-125m", device_map = "auto", torch_dtype = torch.float32)

input_text = "Title: Prediction of total genetic value using genome-wide dense marker maps \nAbstract:"
input_ids = tokenizer(input_text, return_tensors = "pt", padding='max_length').input_ids.to()

outputs = model.generate(input_ids,
                        max_new_tokens=200,
                        do_sample=True,
                        temperature=0.7,
                        top_k=25,
                        top_p=0.9,
                        no_repeat_ngram_size=10,
                        early_stopping=True)

print(tokenizer.decode(outputs[0]).lstrip('<pad>'))

#import galai as gal
#model = gal.load_model("mini")
#out = model.generate("Maize ear corn-kernel density [START_REF]", new_doc = True, top_p = 0.7, max_length = 100)
#
#print(tokenizer.decode(out[0]))
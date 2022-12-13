# requirements:
#! pip install huggingface_hub
#! git config --global credential.helper store

from huggingface_hub import HfFolder

import json

token = "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"

#enter your API key, you can make one for free on HF
#notebook_login()

from huggingface_hub import InferenceApi
import torch

inference = InferenceApi("bigscience/bloom",token=HfFolder.get_token())

import time

def infer(prompt,
          max_length=32,
          top_k=0,
          num_beams=0,
          no_repeat_ngram_size=2,
          top_p=0.9,
          seed=42,
          temperature=0.7,
          greedy_decoding=False,
          return_full_text=False):

    top_k = None if top_k == 0 else top_k
    do_sample = False if num_beams > 0 else not greedy_decoding
    num_beams = None if (greedy_decoding or num_beams == 0) else num_beams
    no_repeat_ngram_size = None if num_beams is None else no_repeat_ngram_size
    top_p = None if num_beams else top_p
    early_stopping = None if num_beams is None else num_beams > 0

    params = {
        "max_new_tokens": max_length,
        "top_k": top_k,
        "top_p": top_p,
        "temperature": temperature,
        "do_sample": do_sample,
        "seed": seed,
        "early_stopping": early_stopping,
        "no_repeat_ngram_size": no_repeat_ngram_size,
        "num_beams": num_beams,
        "return_full_text": return_full_text
    }

    s = time.time()
    response = inference(prompt, params=params)
    # print(response)
    proc_time = time.time() - s
    print(f"Processing time was {proc_time} seconds")
    return response


prompt = """"
We can convert the following R function (block within square brackets):

[
    parseString <- function(str) {
  # split the string into individual characters
  str <- strsplit(str, "")[[1]]
  # create an array of the same length as the string
  arr <- array(NA, length(str))
  # loop over the string and store each character in the array
  for (i in 1:length(str)) {
	arr[i] <- str[i]
  }
  # return the array
  return(arr)
}
]

to the following C++ function (block within square brackets):

[

"""

#resp = infer(
    #prompt, 
    #max_length = 250
    #)

#print(resp)

prompt = """
Abstract
Recent advances in molecular genetic techniques will make dense marker 
maps available and genotyping many individuals for these markers feasible. 
Here we attempted to estimate the effects of approximately 50,000 marker 
haplotypes simultaneously from a limited number of phenotypic records. 
A genome of 1000 cM was simulated with a marker spacing of 1 cM. 
The markers surrounding every 1-cM region were combined into marker haplotypes. 
Due to finite population size N(e) = 100, the marker haplotypes were in linkage 
disequilibrium with the QTL located between the markers. Using least squares, 
all haplotype effects could not be estimated simultaneously. 
When only the biggest effects were included, they were overestimated and the 
accuracy of predicting genetic values of the offspring of the recorded animals 
was only 0.32. Best linear unbiased prediction of haplotype effects assumed 
equal variances associated to each 1-cM chromosomal segment, which yielded an 
accuracy of 0.73, although this assumption was far from true. 
Bayesian methods that assumed a prior distribution of the variance associated 
with each chromosome segment increased this accuracy to 0.85, even when 
the prior was not correct. It was concluded that selection on genetic values 
predicted from markers could substantially increase the rate of genetic gain in 
animals and plants, especially if combined with reproductive techniques to shorten the generation interval.

The 3 take home messages (one sentence each) are:

1)
"""


resp = infer(
    prompt, 
    max_length = 250
)
print(resp)
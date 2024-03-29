
# PyAutoCode: GPT-2 based Python auto-code.

PyAutoCode is a cut-down python autosuggestion built on **GPT-2** *(motivation: GPyT)* model. This baby model *(trained only up to 3 epochs)* is not **"fine-tuned"** yet therefore, I highly recommend not to use it in a production environment or incorporate PyAutoCode in any of your projects. It has been trained on **112GB** of Python data sourced from the best crowdsource platform ever -- **GitHub**.

*NOTE: Increased training and fine tuning would be highly appreciated and I firmly believe that it would improve the ability of PyAutoCode significantly.*

> The model is published on [huggingface](https://huggingface.co/P0intMaN/PyAutoCode). You may go ahead and check it out!

## Some Model Features

- Built on *GPT-2*
- Tokenized with *ByteLevelBPETokenizer*
- Data Sourced from *GitHub (almost 5 consecutive days of latest Python repositories)*
- Makes use of *GPTLMHeadModel* and *DataCollatorForLanguageModelling* for training

## Navigating this Code Repository

If you want to directly run the model, then you can go ahead and execute `app.py`. But, be warned that the requirements of this program is not attached with the repo since requirements may vary based on the system GPUs and architecture.

If you want to understand how this code is functioning, you can take a look at the **PyAutoCode > templates** folder for a descriptive explanation of each module / concept used.

## Get a Glimpse of the Model

You can make use of the **Inference API** of huggingface *(present on the right sidebar)* to load the model and check the result. 

## Usage

You can use this model too! Here's a quick tour of how you can achieve this:

Install transformers
```sh
$ pip install transformers
```

Call the API and get it to work!
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("P0intMaN/PyAutoCode")

model = AutoModelForCausalLM.from_pretrained("P0intMaN/PyAutoCode")

# input: single line or multi-line. Highly recommended to use doc-strings.
inp = """import pandas"""

format_inp = inp.replace('\n', "<N>")
tokenize_inp = tokenizer.encode(format_inp, return_tensors='pt')
result = model.generate(tokenize_inp)

decode_result = tokenizer.decode(result[0])
format_result = decode_result.replace('<N>', "\n")

# printing the result
print(format_result)
```

Upon successful execution, the above should probably produce *(your results may vary when this model is fine-tuned)*
```sh
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

```

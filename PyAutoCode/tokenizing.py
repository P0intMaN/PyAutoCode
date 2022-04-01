from sty import fg, rs, bg
from tokenizers import ByteLevelBPETokenizer
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer

path = "PyAutoCode\\python_code_dataset.txt"
exception_hits = 0

# initializing the tokenizer
tokenizer = ByteLevelBPETokenizer()

print(f"{fg.yellow}started tokenizing...{fg.rs}")

try:
    tokenizer.train(files=path, vocab_size=52_000, min_frequency=2, special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>"
    ])

except (UnicodeDecodeError, UnicodeError):
    exception_hits+=1

# save the model to disk
tokenizer.save_model("PyAutoCode\\tokenizer")

# loading our own pre-trained tokenized model to train GPT2
tokenizer = GPT2Tokenizer.from_pretrained('tokenizer')

# let GPT know about the specialized tokens used during tokenizing
tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})


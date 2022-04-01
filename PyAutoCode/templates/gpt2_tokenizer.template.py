from transformers import GPT2Tokenizer

# I will use GPT2Tokenizer over the pre-trokenized ByteLevelBPETokenizer (BBPET)
# This is to overcome the inefficiency of BBPET to optimize the encoding and decoding
# process.

# loading our own pre-trained tokenized model to train GPT2
tokenizer = GPT2Tokenizer.from_pretrained('PyAutoCode\\tokenizer')

# let GPT know about the specialized tokens used during tokenizing
tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})

# print out the encoded and decoded values
t = tokenizer.encode("print('hello world!')")
print(t)
print(tokenizer.decode(t))

from sty import fg, rs, bg
from tokenizers import ByteLevelBPETokenizer

# recommended to use the relative path (small optimizations)
path = "PyAutoCode\\python_code_dataset.txt"
exception_hits = 0

# initializing the tokenizer
tokenizer = ByteLevelBPETokenizer()

print(f"{fg.yellow}started tokenizing...{fg.rs}")

# handling exceptions during tokenization (Unicode errors)
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

# save the model to disk (relative path recommended)
tokenizer.save_model("PyAutoCode\\tokenizer")

print(f"{fg.green}tokenizing completed...{fg.rs}")
print(f"{fg.red}exception hits {exception_hits}{fg.rs}")

# testing the tokenizer against a simple input
inp = "print('hello world!')"
t = tokenizer.encode(inp)

print(f"\n{fg.cyan}hello world{fg.rs} is tokenized as: ")
print(f'token ids: {fg.cyan}{t.ids}{fg.rs}')
print(f'token values: {fg.cyan}{t.tokens}{fg.rs}')

from sty import fg, rs, bg
from tokenizers import ByteLevelBPETokenizer

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

print(f"{fg.green}tokenizing completed...{fg.rs}")
print(f"{fg.red}exception hits {exception_hits}{fg.rs}")


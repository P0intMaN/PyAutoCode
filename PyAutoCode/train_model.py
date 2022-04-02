from tokenizing import tokenizer, path
from transformers import GPT2Config, GPT2LMHeadModel, DataCollatorForLanguageModeling, Trainer, TrainingArguments
from datasets import load_dataset

# tokenize per line
def line_encoder(lines):
    return tokenizer(lines['text'], add_special_tokens=True, truncation=True, max_length=512) # 1024 (default GPT2 recn)

# GPT2 configs
config = GPT2Config(
    vocab_size=tokenizer.vocab_size,
    bos_token=tokenizer.bos_token_id,
    eos_token=tokenizer.eos_token_id
)

model = GPT2LMHeadModel(config)

dataset = load_dataset("text", data_files=path)
dataset.set_transform(line_encoder)
dataset = dataset['train']

# fill mask tokens
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

# training
training_args = TrainingArguments(
    output_dir='PyAC',
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=10,
    save_steps=100,
    save_total_limit=2,
    prediction_loss_only=True,
    remove_unused_columns=False
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset
)

trainer.train()
trainer.save_model('PyAC')

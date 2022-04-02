from transformers import GPT2Config, GPT2LMHeadModel, DataCollatorForLanguageModeling, Trainer, TrainingArguments
from datasets import load_dataset

# need a tokenizer instance and path to the pre-trained tokenizer
tokenizer = "Tokenizer()"
path = ["Your relative path to a saved tokenizer folder (containing vocab and merges.txt)"]

# a function to tokenize the input line by line. Also passing max length as 512.
def line_encoder(lines):
    return tokenizer(lines['text'], add_special_tokens=True, truncation=True, max_length=512) # 1024 (default GPT2 recn)

# configuring the GPT2 to let it know about the vocab size of each tokenized line and 
# special tokens used for starting and ending a sentence (string)
config = GPT2Config(
    vocab_size=tokenizer.vocab_size,
    bos_token=tokenizer.bos_token_id,
    eos_token=tokenizer.eos_token_id
)

# passing the config settings to GPT2LanguageModelHeadModel
model = GPT2LMHeadModel(config)

# loading the dataset is a tricky part. The default training of GPT2 loads all the data at
# once, which is very inefficient and memory heavy. Huggingface provides an awesome datasets
# library where in I can load the data "batch-wise" keeping in mind the memory usage.
dataset = load_dataset("text", data_files=path)

# I figured that the data needs to be encoded again (GPT2 uses seperate environment while 
# training?) just before training.
dataset.set_transform(line_encoder)
dataset = dataset['train']

# DCFLM fills the random positions (as defined by the mlm_probability) in the neural networks
# with <masks>. These areas are needed to be filled with the correct language syntax. GPT is 
# a bi-directional neural network based model. Hence, it will try to fill the syntax referring
# both backward as well as forward decisions.
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

# training: requires to agents(TA and Trainer). TA specifies certain requirements for Trainer
# to implement. Something I personally liked the most since it allows you to 'fine-tune'
# certain parameters and experiment with them. Trainer takes in the model and returns a 
# trainer object. Use it to train the model.
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

# training and saving the model to PyAC folder. I won't be pushing the trained configs of 
# PyAC folder along with the merges since it won't be much beneficial. Its something that you 
# recieve after training the model.
trainer.train()
trainer.save_model('PyAC')

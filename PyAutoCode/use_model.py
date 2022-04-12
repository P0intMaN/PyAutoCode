# deploy this file in training computer. Configure later in huggingface.co
# 
#                                   OR
# 
# pip install transformers
# 
# from transformers import AutoTokenizer, AutoModelForCausalLM
#
# tokenizer = AutoTokenizer.from_pretrained("P0intMaN/PyAutoCode")
#
# model = AutoModelForCausalLM.from_pretrained("P0intMaN/PyAutoCode")
#
# NOTE: input: single line or multi-line. Highly recommended to use doc-strings.
# inp = """import pandas"""
#
# format_inp = inp.replace('\n', "<N>")
# tokenize_inp = tokenizer.encode(format_inp, return_tensors='pt')
# result = model.generate(tokenize_inp)


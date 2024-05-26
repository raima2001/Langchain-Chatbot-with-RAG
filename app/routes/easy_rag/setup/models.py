from transformers import AutoModel, AutoTokenizer

model_name = "intfloat/multilingual-e5-base"
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("models/multilingual-e5-base", safe_serialization=False)
tokenizer.save_pretrained("models/multilingual-e5-base")
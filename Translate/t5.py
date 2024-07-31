# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")

sentence = "やさしい日本語で“今週の日本”"
# [1022, 3448, 245, 23174, 5, 1]
tokens = tokenizer.encode(sentence)

tokenss = tokenizer.decode(tokens[:-1])

print(tokens)
print(tokenss)
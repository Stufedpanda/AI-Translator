# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")

sentence = "やさしい日本語で“今週の日本”"
# [1022, 3448, 245, 23174, 5, 1]
tokens = tokenizer.encode(sentence)

tokenss = tokenizer.decode(tokens[:-1])

print(tokens)
print(tokenss)
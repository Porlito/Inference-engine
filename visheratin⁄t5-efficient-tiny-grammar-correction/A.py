import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Point to the local virtual folder we defined in TOML
model_path = "./model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

def fix_it(input_text):
    prompt = f"gec: {input_text}"
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.no_grad():
        generated = model.generate(**inputs, max_new_tokens=50, num_beams=5)
    
    return tokenizer.decode(generated[0], skip_special_tokens=True)

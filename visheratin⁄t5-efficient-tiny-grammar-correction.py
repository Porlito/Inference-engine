import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "visheratin/t5-efficient-tiny-grammar-correction"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.eval()

# The specific prompt format this model expects
# Note: No brackets, just the sentence
text = "undocimented code is bad"
prompt = f"gec: {text}" 

inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    generated = model.generate(
        **inputs,
        max_new_tokens=50,
        num_beams=5,    # Beams help tiny models find the best path
        do_sample=False # Keeps it focused on correcting, not "chatting"
    )

output_text = tokenizer.decode(generated[0], skip_special_tokens=True)
print(f"Original: {text}")
print(f"Fixed:    {output_text}")
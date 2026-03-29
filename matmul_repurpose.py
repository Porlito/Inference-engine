import torch
import torch.nn as nn
from transformers import AutoModelForCausalLM, AutoTokenizer

# Counter for total matmuls
matmul_count = 0


# Debug Linear Layer
class DebugLinear(nn.Module):
    def __init__(self, linear_layer, name=""):
        super().__init__()
        self.weight = linear_layer.weight
        self.bias = linear_layer.bias
        self.name = name

    def forward(self, x):
        global matmul_count
        matmul_count += 1

        print(f"\n[MATMUL {matmul_count}] Layer: {self.name}")
        print(f"Input shape: {tuple(x.shape)}")
        print(f"Weight shape: {tuple(self.weight.shape)}")

        # Perform actual computation
        out = x @ self.weight.T

        if self.bias is not None:
            out += self.bias

        return out


# Replace all Linear layers recursively
def replace_linear_layers(model, prefix=""):
    for name, module in model.named_children():
        full_name = f"{prefix}.{name}" if prefix else name

        if isinstance(module, nn.Linear):
            setattr(model, name, DebugLinear(module, full_name))
        else:
            replace_linear_layers(module, full_name)


# Load model (start with GPT-2)
model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.eval()

# Replace Linear layers
replace_linear_layers(model)

# Input prompt
prompt = "Explain gravity simply"
inputs = tokenizer(prompt, return_tensors="pt")

# Run inference
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=5)

# Output result
print("\nGenerated text:\n")
print(tokenizer.decode(outputs[0]))

# Final stats
print(f"\nTotal matrix multiplications: {matmul_count}")

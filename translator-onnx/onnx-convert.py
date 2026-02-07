from optimum.onnxruntime import ORTModelForSeq2SeqLM
from transformers import AutoTokenizer
from pathlib import Path

model_id = "Helsinki-NLP/opus-mt-en-it"
output_dir = "./onnx-marian-en-it"

print(f"Start model : {model_id}")

# 'from_transformers=True' set Optimum to convert PyTorch weights in ONNX
model = ORTModelForSeq2SeqLM.from_pretrained(
    model_id, 
    from_transformers=True
)

# Loading tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Save ONNX locally
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)

print(f" Completed! Files in: {output_dir}")
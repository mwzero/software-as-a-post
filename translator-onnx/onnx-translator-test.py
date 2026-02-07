from optimum.onnxruntime import ORTModelForSeq2SeqLM
from transformers import AutoTokenizer, pipeline

model_path = "./onnx-marian-en-it"
print(f"Loading ONNX model: {model_path}...")

# 1. Loading local model and tokenizer
model = ORTModelForSeq2SeqLM.from_pretrained(model_path, provider="CPUExecutionProvider")
tokenizer = AutoTokenizer.from_pretrained(model_path)

# 2. Initialize pipeline
translator = pipeline("translation", model=model, tokenizer=tokenizer)

# 3. Test
test_text = "The artificial intelligence is running locally in my browser."

print(f"\n📝 Originale Text: {test_text}")
result = translator(test_text)
print(f"\nTranslation: {result[0]['translation_text']}")
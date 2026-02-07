#Neural Transpose: The Private WebGPU Translator

**Neural Transpose** is a "Software as a Post" (SaaP) experiment. It’s a high-performance, private, and serverless translation engine that runs state-of-the-art neural networks directly in your browser using **WebGPU** and **Transformers.js**.

No APIs, no monthly subscriptions, and no data leaving your machine. Just pure local inference.

## 🚀 Features

* **WebGPU Accelerated**: Leverages your local GPU for near-instant translation.
* **Privacy-First**: Switch to **Local Mode** to process data entirely offline.
* **Hybrid Source**: Load models from Hugging Face (Xenova) or your local server.
* **Persistent History**: Your translation history is saved locally via `localStorage`.
* **Lightweight**: Uses optimized MarianMT (OPUS) models (~150MB) for specific language pairs.

---

## 🛠️ Quick Start (Cloud Mode)

1. Clone this repository.
2. Open `index.html` in a WebGPU-compatible browser (Chrome 113+ or Edge).
3. Ensure "CLOUD (Xenova)" is selected.
4. Type your text and hit **Run Translation**.

---

## 🏗️ Local Execution (The "Software as a Post" Way)

To run this application 100% offline and bypass browser CORS restrictions, you need to serve the model files via a local server.

### 1. Convert/Download Models

You need to have the model files in a specific folder structure: `./onnx-marian-[src]-[tgt]/`.

**The most reliable way is using Python and the `optimum` library:**

```bash
pip install "optimum[onnxruntime]" transformers sentencepiece protobuf

```

Run the following script to export your desired pair (e.g., English to Italian):

```python
from optimum.onnxruntime import ORTModelForSeq2SeqLM
from transformers import AutoTokenizer

model_id = "Helsinki-NLP/opus-mt-en-it"
save_dir = "./onnx-marian-en-it"

# Export to ONNX
model = ORTModelForSeq2SeqLM.from_pretrained(model_id, export=True)
tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)

# Save locally
model.save_pretrained(save_dir)
tokenizer.save_pretrained(save_dir)

```

> **⚠️ Critical Note:** If `tokenizer.json` is not generated, download it manually from the [Xenova/opus-mt-en-it](https://www.google.com/search?q=https://huggingface.co/Xenova/opus-mt-en-it/tree/main) repository. This file is mandatory for browser execution.

### 2. Run Local Server

Open your terminal in the project root and start a server:

```bash
# Using Python
python -m http.server 8000

```

Now access the app at `http://localhost:8000`. Switch the source toggle to **LOCAL (Server)**.

---

## 📊 Technical Architecture

The app follows a modern edge-computing flow:

1. **User Input**: Text is captured in the UI.
2. **Tokenizer**: Words are converted to numerical IDs locally.
3. **Inference**: WebGPU executes the ONNX graph using the local GPU.
4. **De-tokenizer**: Numerical IDs are converted back to the target language text.

---

## 💡 Why "Software as a Post"?

Modern web tech has reached a point where the browser is a powerful operating system. By packaging AI models and logic into a single-file-like experience, we move away from centralized SaaS and back to **user-owned computing**. This project demonstrates that we no longer need massive cloud infrastructures for everyday tasks like translation.

---

## ⚠️ Requirements

* **Browser**: Chrome v113+, Edge v113+, or any browser with `WebGPU` enabled.
* **GPU**: A dedicated or integrated GPU with at least 1GB of VRAM for smooth performance.
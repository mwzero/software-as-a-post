#Vibe Coding Prompt: "The Private Neural Transposer"

**Objective:**
Build a high-end, single-page "Software as a Post" translation app that runs neural networks entirely in the browser using **WebGPU** and **Transformers.js v3**. The app should be private, serverless, and professional.

**Core Tech Stack:**

* **Engine:** `@huggingface/transformers` (v3).
* **Models:** `Xenova/opus-mt` series (MarianMT architecture).
* **Frontend:** HTML5, Tailwind CSS, Lucide Icons (for iconography).
* **Storage:** LocalStorage for persistent session history.

**Functional Requirements:**

1. **Hybrid Model Loading:** Create a toggle to switch between "Cloud (Hugging Face CDN)" and "Local (Localhost Server)". If local, the app must look for model folders named `onnx-marian-[src]-[tgt]`.
2. **Dynamic Pipeline:** Based on two independent dropdowns (Source/Target language), dynamically construct the model string (e.g., `en` + `it` -> `Xenova/opus-mt-en-it`).
3. **WebGPU First:** Initialize the pipeline targeting `device: 'webgpu'` with a graceful fallback to `wasm` if WebGPU is unavailable or fails.
4. **Persistent History:** Save every translation (Original text, Translated text, Lang pair, Timestamp) to `localStorage`. Display these in a "Recent History" list with a "Copy to Clipboard" and "Clear All" function.
5. **Model Specs Card:** Show a technical info card detailing the architecture (MarianMT), estimated parameters (~77M), and execution provider (WebGPU/WASM).
6. **Performance Benchmarking:** Measure and display the inference time in seconds for every translation.

**UI/UX Aesthetic:**

* **Theme:** Professional Light Mode. Use a soft background (`#f8fafc`) with indigo and cyan decorative blurred blobs.
* **Components:** Glassmorphism cards with subtle borders (`rgba(255, 255, 255, 0.7)`).
* **Interactions:** A prominent "Run Translation" button with a loading overlay and a real-time progress bar for model downloads.
* **Typography:** Clean, sans-serif (Inter/System stack).

**Specific Logic Instructions:**

* Use `env.allowLocalModels` and `env.localModelPath` to manage local vs remote fetching.
* Ensure the `tokenizer.json` is correctly handled for MarianMT models.
* Implement a 10-item limit for the history list.


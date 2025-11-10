# 🚀 AI Multimodal Studio

### 🧠 Powered by **FastAPI**, **Gemini**, and **Stability AI**

A sleek and intelligent multimodal AI application that allows you to:
- 📝 Generate text from prompts (Gemini API)
- 🎨 Generate realistic images from text (Stability AI API)
- 💾 Save and download your outputs instantly
- 🌗 Toggle between **Light & Dark mode** in a stunning responsive UI

---

## ⚙️ Tech Stack

| Category | Tools / Frameworks |
|-----------|--------------------|
| Backend | 🐍 Python (FastAPI) |
| Frontend | 🧩 HTML, Tailwind CSS, Alpine.js |
| AI Models | 🤖 Google Gemini API, Stability AI API |
| File Handling | DOCX, PDF, TXT exports |
| Environment | dotenv, Jinja2 templates |

---

## 💡 Features

✅ Text to Text Generation using **Gemini API**  
✅ Text to Image Generation using **Stability AI API**  
✅ Responsive, modern UI built with **Tailwind CSS**  
✅ Auto-saves outputs to `/output` folder  
✅ Download text and images directly from the interface  
✅ Secure API key management with `.env`  
✅ Light / Dark theme toggle  

---

## 🧠 Project Structure

AI-Multimodal-Studio/
│
├── main.py # FastAPI backend
├── templates/
│ └── index.html # Beautiful frontend (Tailwind + Alpine.js)
├── output/ # Stores generated text and images
├── .env # API keys (ignored in git)
├── .gitignore
└── requirements.txt

yaml
Copy code

---

## 🧰 Setup & Installation

### 1️⃣ Clone this Repository
```bash
git clone https://github.com/ranjithjunnu09/AI-Multimodal-Studio.git
cd AI-Multimodal-Studio
2️⃣ Create and Activate Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Create .env File in Root Directory
bash
Copy code
GEMINI_API_KEY=your_gemini_api_key
STABILITY_API_KEY=your_stability_api_key
⚠️ Do not share or commit this .env file.

5️⃣ Run the App
bash
Copy code
uvicorn main:app --reload --port 8001
Then open your browser and visit:
👉 http://127.0.0.1:8001

🖼️ Screenshots
🧠 Text-to-Text Generation
<img src="https://user-images.githubusercontent.com/00000000/placeholder1.png" width="600"/>
🎨 Text-to-Image Generation
<img src="https://user-images.githubusercontent.com/00000000/placeholder2.png" width="600"/>
🧾 Example .env
ini
Copy code
GEMINI_API_KEY=sk-your_gemini_key_here
STABILITY_API_KEY=sk-your_stability_key_here
🤝 Contributing
Contributions, feedback, and improvements are always welcome!
Fork this repo, make your changes, and submit a PR 🚀

🌟 Acknowledgments
Google Gemini API

Stability AI API

FastAPI

TailwindCSS

Alpine.js

👨‍💻 Developed by Junnu — AI Engineer
✨ “From text to imagination — one prompt at a time.”

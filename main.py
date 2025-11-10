import os
import requests
from datetime import datetime
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai

# ===========================
# CONFIGURATION
# ===========================
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

if not GEMINI_API_KEY or not STABILITY_API_KEY:
    raise ValueError("❌ Missing API Keys in .env file")

client = genai.Client(api_key=GEMINI_API_KEY)

app = FastAPI(title="AI Multimodal Studio")

# Static + Templates
app.mount("/output", StaticFiles(directory=BASE_DIR / "output"), name="output")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# ===========================
# MODELS
# ===========================
class TextRequest(BaseModel):
    prompt: str

class ImageRequest(BaseModel):
    prompt: str


# ===========================
# ROUTES
# ===========================
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/text/generate")
async def generate_text(req: TextRequest):
    """
    Generate text via Gemini and save to output folder
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=req.prompt
        )
        text_output = response.text.strip()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        output_dir = BASE_DIR / "output"
        output_dir.mkdir(exist_ok=True)
        file_path = output_dir / f"text_output_{timestamp}.txt"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_output)

        return JSONResponse({
            "response": text_output,
            "file_path": f"/download/text/{file_path.name}"
        })

    except Exception as e:
        print("❌ Error generating text:", e)
        return JSONResponse({"error": str(e)}, status_code=500)


@app.get("/download/text/{filename}")
async def download_text(filename: str):
    file_path = BASE_DIR / "output" / filename
    if file_path.exists():
        return FileResponse(file_path, media_type="text/plain", filename=filename)
    return JSONResponse({"error": "File not found"}, status_code=404)


@app.post("/image/generate")
async def generate_image(req: ImageRequest):
    """
    Generate image via Stability AI and save as .jpg
    """
    try:
        url = "https://api.stability.ai/v2beta/stable-image/generate/core"

        headers = {
            "Authorization": f"Bearer {STABILITY_API_KEY}",
            "Accept": "image/jpeg"
        }

        files = {
            "none": ("", ""),
        }

        data = {
            "prompt": req.prompt,
            "aspect_ratio": "1:1",
            "style_preset": "photographic"
        }

        response = requests.post(url, headers=headers, data=data, files=files)

        if response.status_code != 200:
            print("❌ Stability API Error:", response.text)
            return JSONResponse({"error": "Image generation failed"}, status_code=500)

        output_dir = BASE_DIR / "output"
        output_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_path = output_dir / f"generated_image_{timestamp}.jpg"

        with open(image_path, "wb") as f:
            f.write(response.content)

        return JSONResponse({
            "file_path": f"/download/image/{image_path.name}"
        })

    except Exception as e:
        print("❌ Error generating image:", e)
        return JSONResponse({"error": str(e)}, status_code=500)


@app.get("/download/image/{filename}")
async def download_image(filename: str):
    file_path = BASE_DIR / "output" / filename
    if file_path.exists():
        return FileResponse(file_path, media_type="image/jpeg", filename=filename)
    return JSONResponse({"error": "File not found"}, status_code=404)

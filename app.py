import os
import torch
from flask import Flask, request, jsonify
from diffusers import StableDiffusionPipeline

app = Flask(__name__)

# Auto-install dependencies (only runs once)
def install_dependencies():
    os.system("pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118")
    os.system("pip install diffusers transformers accelerate flask")

install_dependencies()

# Load model (downloads automatically if not found)
MODEL_NAME = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(MODEL_NAME, torch_dtype=torch.float16).to("cuda")

@app.route("/generate", methods=["POST"])
def generate_image():
    try:
        prompt = request.json.get("prompt", "A beautiful landscape")
        image = pipe(prompt).images[0]
        image_path = "output.png"
        image.save(image_path)
        return jsonify({"status": "success", "image": image_path})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

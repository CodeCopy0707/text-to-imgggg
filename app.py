import os
import torch
from diffusers import DiffusionPipeline

# 🔹 Step 1: Dependencies Install Karo
print("📥 Installing dependencies...")
os.system("pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118")
os.system("pip install diffusers transformers accelerate safetensors invisible_watermark")

# 🔹 Step 2: Model Load Karo
print("📥 Downloading Stable Diffusion XL Model...")
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", 
    torch_dtype=torch.float16, 
    use_safetensors=True,
    variant="fp16"
)

# 🔹 Step 3: GPU Pe Move Karo (Agar Available Hai)
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe.to(device)

# 🔹 Step 4: Image Generate Karo
prompt = "A futuristic city with flying cars at sunset"
print(f"✨ Generating Image for prompt: {prompt}")

image = pipe(prompt=prompt).images[0]

# 🔹 Step 5: Image Save Karo
image_path = "generated_image.png"
image.save(image_path)
print(f"✅ Image saved as {image_path}")

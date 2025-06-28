import easyocr
from PIL import Image
import numpy as np
import json
import yaml
import os

# Load OCR zones
with open("zones.json", "r") as f:
    zones = json.load(f)

# Load events and prompts
with open("events.yaml", "r") as f:
    events = yaml.safe_load(f)
with open("prompts.yaml", "r") as f:
    prompts = yaml.safe_load(f)

# Load screenshot
import glob

# Find the latest PNG or JPG in the screenshots folder
screenshot_dir = "screenshots"
img_files = sorted(
    glob.glob(os.path.join(screenshot_dir, "*.png")) + glob.glob(os.path.join(screenshot_dir, "*.jpg")),
    key=os.path.getmtime,
    reverse=True
)

if not img_files:
    raise FileNotFoundError(f"No PNG or JPG files found in {screenshot_dir}!")

img_path = img_files[0]  # Latest screenshot
print(f"Analyzing: {img_path}")

img = Image.open(img_path)
reader = easyocr.Reader(['en'])

ocr_results = {}
for key, coords in zones.items():
    x1, y1, x2, y2 = coords["x1"], coords["y1"], coords["x2"], coords["y2"]
    cropped = img.crop((x1, y1, x2, y2))
    text = reader.readtext(np.array(cropped), detail=0)
    ocr_results[key] = " ".join(text)

print("OCR Results:", ocr_results)

# Match events (simple version: look for event_text triggers)
matched_event = None
for event in events:
    if "trigger_text" in event and any(t in ocr_results.get("event_text", "") for t in event["trigger_text"]):
        matched_event = event
        break

if matched_event:
    prompt_type = matched_event["prompt_type"]
    prompt_template = prompts[prompt_type]
else:
    prompt_type = "lore_drop"
    prompt_template = prompts.get(prompt_type, "")

# Fill in the prompt template
prompt_filled = prompt_template.format(
    event_text=ocr_results.get("event_text", ""),
    location_name=ocr_results.get("location_name", ""),
    quest_log=ocr_results.get("quest_log", "")
)

# Output to file
output = {
    "event": matched_event["name"] if matched_event else "unknown",
    "ocr_results": ocr_results,
    "prompt": prompt_filled
}

# Ensure outputs folder exists relative to script location
if not os.path.exists("outputs"):
    os.makedirs("outputs")

with open(os.path.join("outputs", "ocr_output.json"), "w") as f:
    json.dump(output, f, indent=2)

print(f"\nEvent Detected: {output['event']}\nPrompt for GPT:\n{prompt_filled}")

"""Utility functions for AI-Navi Vanilla"""

import json
import mss
import numpy as np
from PIL import Image
import pytesseract

def load_config(config_path):
    """
    Load JSON configuration from the given path.
    Returns a dictionary of configuration data.
    """
    with open(config_path, 'r') as f:
        return json.load(f)

def capture_screen_region(region):
    """
    Capture a specific region of the screen.
    `region` should be a dict with keys: top, left, width, height.
    Returns a PIL Image.
    """
    with mss.mss() as sct:
        monitor = {
            'top': region['top'],
            'left': region['left'],
            'width': region['width'],
            'height': region['height']
        }
        sct_img = sct.grab(monitor)
        img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
        return img

def perform_ocr(image, lang='eng'):
    """
    Run OCR on a PIL Image and return the extracted text.
    """
    text = pytesseract.image_to_string(image, lang=lang)
    return text.strip()

def log_event(event_data, output_path='game_template/outputs/events.log'):
    """
    Append event_data (dict or str) to the log file at output_path.
    """
    with open(output_path, 'a') as f:
        f.write(f"{event_data}\n")

def draw_overlay(image, box, text):
    """
    Draw a simple overlay box and text onto a PIL Image.
    Returns the modified image.
    """
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(image)
    # Semi-transparent box
    draw.rectangle([(box['left'], box['top']), (box['left']+box['width'], box['top']+box['height'])],
                   fill=(0,0,0,180), outline=(255,255,255,200), width=2)
    # Text
    try:
        font = ImageFont.truetype('arial.ttf', 16)
    except IOError:
        font = ImageFont.load_default()
    draw.text((box['left'] + 5, box['top'] + 5), text, font=font, fill=(255,255,255))
    return image

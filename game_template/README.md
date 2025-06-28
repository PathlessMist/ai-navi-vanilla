# AI-Navi Vanilla

> 🧠 *Screen-aware AI companions for games and beyond.*

**AI-Navi Vanilla** is a lightweight framework for integrating AI assistant logic into visual environments using screen-based OCR and LLM prompts. Designed for modders, developers, and futurists, it enables an immersive, prompt-driven experience that overlays game state with intelligent feedback, prophecy-style prompts, or guidance narration.

---

## ✨ Features

- 🔲 **Zone-Based Prompt Triggering**  
  Define screen areas that map to different in-game events or HUD elements (via `prompt_zones.json`)

- 🧠 **LLM-Powered Interactions**  
  Use captured screen text + predefined context to trigger LLM prompts (ChatGPT, Claude, etc.)

- 👁 **OCR-First Design**  
  Uses Tesseract or EasyOCR to extract in-game or screen text dynamically

- 🧩 **Mod-Friendly Architecture**  
  Plug AI-Navi into other mods or tools using lightweight JSON templates

- 🛠️ **Completely Offline-Compatible (Optional)**  
  Swap in local models and OCR engines for no-internet use

---

## 🧰 How It Works

1. **Screen Capture**  
   Continuously (or on hotkey) captures a defined region of the screen

2. **Text Recognition (OCR)**  
   Extracts readable text from screen zones via OCR

3. **Prompt Resolution**  
   Matches extracted text to zone definitions (`prompt_zones.json`)

4. **LLM Prompt Execution**  
   Sends text + prompt logic to a connected language model

5. **Response Handling**  
   Displays or routes response to voice, overlay, log, or file

---

## 🚀 Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/yourname/ai-navi-vanilla
   cd ai-navi-vanilla
   ```

2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the assistant  
   ```bash
   python src/main.py
   ```

4. Customize your zones  
   Edit `templates/prompt_zones.json` to define capture areas and associated prompts.

---

## 🧪 Example Use Case

> You’re playing a game with an intricate UI. When you open your inventory, a prompt zone is triggered that sends screen text to GPT, asking:  
> “Analyze this loadout. What’s missing for a balanced mid-game build?”  
>  
> The LLM replies with specific suggestions—right as you’re thinking about your next move.

---

## 🔭 Roadmap & Vision

- 🎮 Game-specific mod integrations (Skyrim, Factorio, etc.)
- 🗣️ Voice integration (speech-to-text + TTS response)
- 📱 Mobile or AR client support
- 🌐 Prophetic/visionary theme overlays for storytelling
- 🎥 TikTok/Shorts demos to showcase "AI as oracle" gameplay

---

## 🧾 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---

## 🤝 Contributing

Open to PRs, forks, and discussions. This project is meant to be remixed. Let’s build the future of narrative intelligence—together.

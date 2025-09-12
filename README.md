# Jolly A.I Desktop Assistant

Jolly A.I is a simple voice-activated desktop assistant built with Python. It can recognize your speech, respond with voice, open popular websites, play music, launch apps, and answer questions using AI.

## Features
- Listens to your voice commands using your microphone
- Responds with speech using text-to-speech
- Opens websites (YouTube, Google, Wikipedia) when you say "Open <site>"
- Opens music, games folder, and popular apps (Camera, WhatsApp, Calculator, Chrome)
- Ask questions to AI using Hugging Face/DeepSeek integration
- Easy to extend with more commands

## Requirements
- Python 3.7+
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [pyaudio](https://pypi.org/project/PyAudio/) (for microphone input)
- [openai](https://pypi.org/project/openai/) (for AI integration)

## Installation
1. Clone this repository or download the code.
2. Install the required Python packages:
	```powershell
	pip install speechrecognition pyttsx3 pyaudio openai
	```
	> If you have trouble installing `pyaudio` on Windows, download the appropriate wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it with pip.
3. Add your Hugging Face token to `apikey.py` (replace the placeholder string).

## Usage
1. Make sure your microphone is connected and working.
2. Run the assistant:
	```powershell
	python main.py
	```
3. Speak commands like:
	- "Open YouTube"
	- "Open Google"
	- "Open Wikipedia"
	- "Open music"
	- "Open games"
	- "Open camera"
	- "Ask AI" or "Question"

The assistant will respond and open the requested website, app, or answer your question using AI.

## Extending
You can add more sites, apps, or commands by editing the `sites` and `apps` lists in `main.py` or adding more logic to the command loop.

## Troubleshooting
- If you get errors related to the microphone, check your audio device settings.
- If speech is not recognized, ensure you have a stable internet connection (Google Speech Recognition API is used).
- For `pyaudio` installation issues, see the note above.
- For AI features, ensure your Hugging Face token is valid and you have internet access.

## License
This project is for educational purposes only.

---


**WORK IN PROGRESS**

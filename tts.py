from elevenlabs import generate, save, set_api_key
import os

set_api_key(os.getenv("ELEVEN_API_KEY"))

def speak(text, voice="Rachel", filename="output.mp3"):
    audio = generate(text=text, voice=voice, model="eleven_monolingual_v1")
    save(audio, filename)
    return filename

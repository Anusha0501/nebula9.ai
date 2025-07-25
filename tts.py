from TTS.api import TTS
from pydub import AudioSegment
from pydub.playback import play
import os

# ✅ Use English model with a clear voice
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

def speak_text(text):
    os.makedirs("audio", exist_ok=True)
    output_path = "audio/response.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    audio = AudioSegment.from_wav(output_path)
    play(audio)

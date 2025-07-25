# tts.py

from TTS.api import TTS
import os
from pydub import AudioSegment
from pydub.playback import play

# 🔊 Load default English TTS model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

def speak_text(text):
    output_path = "audio/response.wav"
    tts.tts_to_file(text=text, file_path=output_path)

    # Play audio
    audio = AudioSegment.from_wav(output_path)
    play(audio)

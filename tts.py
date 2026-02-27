from pathlib import Path
from typing import Optional

from TTS.api import TTS

AUDIO_DIR = Path("audio")
AUDIO_DIR.mkdir(exist_ok=True)

# Keep model initialization global so it's loaded once per process.
tts_model = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)


def synthesize_speech(text: str, output_path: Optional[Path] = None) -> Path:
    """Generate speech audio and return a filesystem path to the WAV file."""
    output = output_path or AUDIO_DIR / "response.wav"
    tts_model.tts_to_file(text=text, file_path=str(output))
    return output

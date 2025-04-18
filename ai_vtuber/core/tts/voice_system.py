from elevenlabs import generate, set_api_key, Voice, VoiceSettings
from loguru import logger
import os
from ai_vtuber.config.config import settings

class VoiceSystem:
    def __init__(self):
        set_api_key(settings.ELEVENLABS_API_KEY)
        self.voice = Voice(
            voice_id=settings.ELEVENLABS_VOICE_ID,
            settings=VoiceSettings(
                stability=0.5,
                similarity_boost=0.75,
                style=0.0,
                use_speaker_boost=True
            )
        )
        self.output_dir = "audio_output"
        os.makedirs(self.output_dir, exist_ok=True)

    async def generate_speech(self, text: str) -> str:
        try:
            # Generate audio from text
            audio = generate(
                text=text,
                voice=self.voice,
                model="eleven_monolingual_v1"
            )

            # Save the audio file
            filename = f"{self.output_dir}/response_{len(os.listdir(self.output_dir))}.mp3"
            with open(filename, "wb") as f:
                f.write(audio)

            logger.info(f"Generated speech and saved to {filename}")
            return filename

        except Exception as e:
            logger.error(f"Error generating speech: {str(e)}")
            return None
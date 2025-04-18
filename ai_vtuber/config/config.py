import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    # Twitch Configuration
    TWITCH_OAUTH_TOKEN: str = os.getenv("TWITCH_OAUTH_TOKEN", "")
    TWITCH_CHANNEL: str = os.getenv("TWITCH_CHANNEL", "")
    TWITCH_CLIENT_ID: str = os.getenv("TWITCH_CLIENT_ID", "")
    TWITCH_CLIENT_SECRET: str = os.getenv("TWITCH_CLIENT_SECRET", "")

    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

    # ElevenLabs Configuration
    ELEVENLABS_API_KEY: str = os.getenv("ELEVENLABS_API_KEY", "")
    ELEVENLABS_VOICE_ID: str = os.getenv("ELEVENLABS_VOICE_ID", "")

    # Personality Settings
    VTUBER_NAME: str = os.getenv("VTUBER_NAME", "AI Companion")
    PERSONALITY_PROMPT: str = os.getenv("PERSONALITY_PROMPT", """
    You are a friendly, witty, and slightly mysterious AI companion. 
    You have a playful sense of humor and enjoy engaging in natural conversation.
    You're knowledgeable but not overly formal, and you maintain a chill, approachable demeanor.
    """)

    class Config:
        env_file = ".env"

settings = Settings() 
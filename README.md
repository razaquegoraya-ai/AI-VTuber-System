# AI VTuber System

A real-time AI-powered VTuber system that interacts with Twitch chat using natural language processing and text-to-speech capabilities.

## Features

- Real-time Twitch chat interaction
- AI-powered responses using GPT-3.5
- Natural-sounding voice synthesis using ElevenLabs
- Customizable personality and voice settings
- Automatic audio file generation and management

## Prerequisites

- Python 3.8 or higher
- Git
- Twitch account and OAuth token
- OpenAI API key
- ElevenLabs API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-vtuber.git
cd ai-vtuber
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your API keys:
```env
# Twitch Configuration
TWITCH_OAUTH_TOKEN=your_oauth_token
TWITCH_CHANNEL=your_channel_name
TWITCH_CLIENT_ID=your_client_id
TWITCH_CLIENT_SECRET=your_client_secret

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-3.5-turbo

# ElevenLabs Configuration
ELEVENLABS_API_KEY=your_elevenlabs_api_key
ELEVENLABS_VOICE_ID=your_voice_id

# Personality Settings
VTUBER_NAME=AI Companion
PERSONALITY_PROMPT=Your personality prompt here
```

## Usage

1. Start the AI VTuber:
```bash
python -m ai_vtuber.main
```

2. The system will:
   - Connect to your Twitch channel
   - Listen for chat messages
   - Generate AI responses
   - Convert responses to speech
   - Save audio files in the `audio_output` directory

## Project Structure

```
ai_vtuber/
├── main.py              # Main application entry point
├── core/
│   ├── twitch/         # Twitch chat handling
│   ├── ai/             # AI personality and response generation
│   └── tts/            # Text-to-speech functionality
├── config/             # Configuration management
└── audio_output/       # Generated audio files
```

## Troubleshooting

### Common Issues

1. **File Encoding Issues (Windows)**
   - If you encounter encoding issues in VS Code:
     1. Click the encoding indicator in the bottom right
     2. Select "Reopen with Encoding"
     3. Choose "UTF-8"
     4. Save with UTF-8 encoding

2. **API Key Issues**
   - Ensure all API keys in `.env` are correct
   - Check API rate limits and quotas
   - Verify network connectivity

3. **Twitch Connection Issues**
   - Verify OAuth token is valid
   - Check channel name is correct
   - Ensure bot has proper permissions

### VS Code Settings

Add these settings to your VS Code `settings.json`:
```json
{
    "files.encoding": "utf8",
    "files.autoGuessEncoding": true,
    "files.eol": "\n"
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers. # AI-VTuber-System

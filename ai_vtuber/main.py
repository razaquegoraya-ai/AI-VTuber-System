import asyncio
from loguru import logger
from ai_vtuber.core.twitch.chat_handler import TwitchChatBot
from ai_vtuber.core.ai.personality import AIPersonality
from ai_vtuber.core.tts.voice_system import VoiceSystem
from ai_vtuber.config.config import settings

class AIVTuber:
    def __init__(self, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self.bot = TwitchChatBot(loop=self.loop)
        self.personality = AIPersonality()
        self.voice_system = VoiceSystem()

    async def process_message(self, message_data):
        if not message_data:
            return

        user = message_data['user']
        content = message_data['content']

        # Generate AI response
        response = await self.personality.generate_response(content, user)
        
        # Send response to Twitch chat
        await self.bot.send_message(response)
        
        # Generate speech
        audio_file = await self.voice_system.generate_speech(response)
        if audio_file:
            logger.info(f"Audio response saved to: {audio_file}")

    async def run(self):
        try:
            # Start the Twitch bot
            await self.bot.start()

            while True:
                try:
                    # Check for new messages
                    message = self.bot.get_next_message()
                    if message:
                        await self.process_message(message)
                    
                    # Small delay to prevent CPU overuse
                    await asyncio.sleep(0.1)

                except Exception as e:
                    logger.error(f"Error in main loop: {str(e)}")
                    await asyncio.sleep(1)
        except KeyboardInterrupt:
            logger.info("Shutting down...")
        except Exception as e:
            logger.error(f"Fatal error: {str(e)}")
        finally:
            # Cleanup
            await self.bot.close()

def main():
    # Configure logger
    logger.add("ai_vtuber.log", rotation="1 day", retention="7 days")
    
    # Create event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        # Create and run the AI VTuber
        vtuber = AIVTuber(loop=loop)
        loop.run_until_complete(vtuber.run())
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    finally:
        loop.close()

if __name__ == "__main__":
    main()
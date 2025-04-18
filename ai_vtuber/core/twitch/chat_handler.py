from twitchio.ext import commands
from loguru import logger
from ai_vtuber.config.config import settings
import asyncio

class TwitchChatBot(commands.Bot):
    def __init__(self, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        super().__init__(
            token=settings.TWITCH_OAUTH_TOKEN,
            prefix='!',
            initial_channels=[settings.TWITCH_CHANNEL],
            loop=self.loop
        )
        self.message_queue = []

    async def event_ready(self):
        logger.info(f'Logged in as {self.nick}')
        logger.info(f'Connected to channel: {settings.TWITCH_CHANNEL}')

    async def event_message(self, message):
        if message.echo:
            return

        # Ignore messages from the bot itself
        if message.author.name.lower() == self.nick.lower():
            return

        # Add message to queue for processing
        self.message_queue.append({
            'user': message.author.name,
            'content': message.content,
            'timestamp': message.timestamp
        })

        logger.info(f'Message from {message.author.name}: {message.content}')

    def get_next_message(self):
        if self.message_queue:
            return self.message_queue.pop(0)
        return None

    async def send_message(self, message: str):
        channel = self.get_channel(settings.TWITCH_CHANNEL)
        if channel:
            await channel.send(message)
            logger.info(f'Sent message: {message}') 
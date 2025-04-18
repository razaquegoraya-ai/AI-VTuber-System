from openai import OpenAI
from loguru import logger
from ai_vtuber.config.config import settings

class AIPersonality:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.conversation_history = []
        self.max_history = 10  # Keep last 10 messages for context

    def _format_conversation(self, message: str, user: str) -> str:
        return f"{user}: {message}"

    def _update_history(self, message: str, user: str, response: str):
        self.conversation_history.append({
            'user': user,
            'message': message,
            'response': response
        })
        if len(self.conversation_history) > self.max_history:
            self.conversation_history.pop(0)

    async def generate_response(self, message: str, user: str) -> str:
        try:
            # Format conversation history
            history = "\n".join([
                f"{msg['user']}: {msg['message']}\n{settings.VTUBER_NAME}: {msg['response']}"
                for msg in self.conversation_history
            ])

            # Create the prompt with personality and context
            system_prompt = settings.PERSONALITY_PROMPT.strip()
            user_prompt = f"""Previous conversation:
{history}

Current message from {user}:
{message}

{settings.VTUBER_NAME}'s response:"""

            # Generate response using OpenAI
            response = self.client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=150,
                temperature=0.7
            )

            ai_response = response.choices[0].message.content.strip()

            # Update conversation history
            self._update_history(message, user, ai_response)

            logger.info(f"Generated response: {ai_response}")
            return ai_response

        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return "I'm having trouble thinking of a response right now. Could you try again?"
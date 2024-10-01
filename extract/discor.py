from typing import Final
import os 
from dotenv import load_dotenv
from discord import Intents , Client , Message
from responses import HTTPResponse
 

#  import token
load_dotenv()
Token: Final[str]=os.getenv('DiscordT')
print(Token)

# Bot setup : make the bot work
# intents(bot permission)


bot_intent :Intents = intents.default()
bot_intent.message_content=1

cli: Client = Client(intents=bot_intent)


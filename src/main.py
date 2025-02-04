import asyncio
import logging

import pydirectinput
from twitchio.ext import commands

import config
import utils

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
CONFIG = config.Config()
LOGGER.setLevel(logging.getLevelName(CONFIG.log_level))
KEY_INPUTS = CONFIG.key_inputs
# Create a Twitch bot instance
BOT = commands.Bot(
    token=CONFIG.token,
    client_id=CONFIG.client_id,
    nick=CONFIG.nick,
    prefix='!',
    initial_channels=[CONFIG.channel]
)


# Event handler for when the bot connects to the Twitch channel
@BOT.event()
async def event_ready():
    LOGGER.info(f"Connected to {CONFIG.channel}")


# Event handler for processing chat messages
@BOT.event()
async def event_message(ctx):
    message_content = ctx.content.lower()

    inputs = message_content.split(" ")

    if inputs[0] in KEY_INPUTS and len(inputs) <= 2:
        key = KEY_INPUTS[inputs[0]]
        # Check if we have a second value that's an int, for how long to
        # hold the key down.
        duration = CONFIG.key_press_duration
        if len(inputs) == 2:
            try:
                duration = utils.clamp(int(inputs[1]),
                                       CONFIG.key_press_duration_min,
                                       CONFIG.key_press_duration_max)
            except:
                LOGGER.warning(f"Invalid duration parameter: {inputs[1]}")
                return

        LOGGER.info(f"User {ctx.author.name} pressing key {key} for duration {duration}")

        pydirectinput.keyDown(key)
        await asyncio.sleep(duration*CONFIG.key_press_scale_factor)
        pydirectinput.keyUp(key)

def main():
    LOGGER.info('Starting chat bot')
    LOGGER.debug(config.Config())
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(BOT.start())
    except KeyboardInterrupt:
        loop.run_until_complete(BOT.close())
    finally:
        loop.close()


if __name__ == "__main__":
    main()

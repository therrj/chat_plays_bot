import asyncio
import logging

import pydirectinput
from twitchio.ext import commands

import utils

LOGGER = logging.getLogger("ChatPlaysBot")

class TwitchBot(commands.Bot):

    def __init__(
        self,
        token,
        client_id,
        nick,
        channel,
        key_press_duration,
        key_press_scale_factor,
        key_press_duration_min,
        key_press_duration_max,
        key_inputs
    ):
        self.token = token
        self.client_id = client_id
        # We can't use nick, so we just use username.
        self.username = nick
        self.channel = channel
        self.key_press_duration = key_press_duration
        self.key_press_scale_factor = key_press_scale_factor
        self.key_press_duration_min = key_press_duration_min
        self.key_press_duration_max = key_press_duration_max
        self.key_inputs = key_inputs
        super().__init__(
            token=self.token,
            client_id=self.client_id,
            nick=self.username,
            prefix='!',
            initial_channels=[self.channel]
        )

    async def event_ready(self):
        LOGGER.info(f"Connected to {self.channel}")

    async def event_message(self, ctx):
        """Event handler for processing chat messages."""
        message_content = ctx.content.lower()

        inputs = message_content.split(" ")

        if inputs[0] in self.key_inputs and len(inputs) <= 2:
            key = self.key_inputs[inputs[0]]
            # Check if we have a second value that's an int, for how long to
            # hold the key down.
            duration = self.key_press_duration
            if len(inputs) == 2:
                try:
                    duration = utils.clamp(int(inputs[1]),
                                           self.key_press_duration_min,
                                           self.key_press_duration_max)
                except:
                    LOGGER.warning(f"Invalid duration parameter: {inputs[1]}")
                    return

            LOGGER.info(f"User {ctx.author.name} pressing key {key} for duration {duration}")

            pydirectinput.keyDown(key)
            await asyncio.sleep(duration * self.key_press_scale_factor)
            pydirectinput.keyUp(key)

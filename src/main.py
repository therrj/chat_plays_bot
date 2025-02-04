import asyncio
import logging

import config
import twitch

LOGGER = logging.getLogger("ChatPlaysBot")


def main():
    logging.basicConfig()

    conf = config.Config()
    print(conf.log_level)

    LOGGER.setLevel(logging.getLevelName(conf.log_level))
    LOGGER.info('Starting chat bot')
    LOGGER.debug(conf)

    bot = twitch.TwitchBot(
        conf.token,
        conf.client_id,
        conf.nick,
        conf.channel,
        conf.key_press_duration,
        conf.key_press_scale_factor,
        conf.key_press_duration_min,
        conf.key_press_duration_max,
        conf.key_inputs
    )

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(bot.start())
    except KeyboardInterrupt:
        loop.run_until_complete(bot.close())
    finally:
        loop.close()


if __name__ == "__main__":
    main()

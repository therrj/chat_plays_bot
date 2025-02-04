# Configuration settings:

## Logging
- `LOG_LEVEL` - controls the logging level. You can choose one of
`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`

If you want more info use `DEBUG` if you want no info, use `CRITICAL`

## Twitch Connection Settings
- `TWITCH_USERNAME` - Twitch user tokens were generated for
- `TWITCH_ACCESS_TOKEN` - Twitch Auth Token
- `TWITCH_CLIENT_ID` - Twitch Client ID
- `TWITCH_CHANNEL` - Channel you want to monitor messages in

You'll need to generate auth tokens for whatever account you plan to run
the bot from. You can generate these from https://twitchtokengenerator.com/
and copy the output to the `TWITCH_ACCES_TOKEN` and `TWITCH_CLIENT_ID` 
settings

## Key Press Settings
The following are settings related to how long key presses will be activated.

The length the key will be pressed is `KEY_PRESS_DURATION` * `KEY_PRESS_SCALE_FACTOR`
- `KEY_PRESS_DURATION` - Set the default key press duration. Default is 1
- `KEY_PRESS_SCALE_FACTOR` - Set the keypress duration scale factor. Default is 0.05
- `KEY_PRESS_DURATION_MIN` - Set the minimum duration value. Default is 1
- `KEY_PRESS_DURATION_MAX` - Set the maximum duration value. Default is 10

The `KEY_PRESS_DURATION_MIN` and `KEY_PRESS_DURATION_MAX` settings are preventative
measures to stop someone from running something like `a 10000` which could potentially
hold the A button for a long time.

If you want to effectively disable the duration functionality, you can set
`KEY_PRESS_DURATION`, `KEY_PRESS_DURATION_MIN`, and `KEY_PRESS_DURATION_MAX` to the same value.

## Key Input Mappings
`chat_plays_bots` allows you to customize, add, or remove any key combinations you see fit

The format is:
```yaml
key_action:
  - text
  - to
  - trigger
  - key
```
For example
```yaml
KEY_INPUTS:
  left:
    - l
    - left
  right:
    - r
    - right
  a:
    - a
    - jump
```

Using the above example, a user can enter `a` or `jump` and the `a` key will be pressed.
You can add as many triggers as you like, and they don't need to make sense:
```yaml
up:
  - b
  - foobar 
```
In this example, a user can type `b` or `foobar` and the `up` key will be pressed.

**_NOTE:_**: If you add multiple inputs for the same key, the last
occurrence will take precedence. 

A full list of supported keys can be found here:
https://github.com/learncodebygaming/pydirectinput/blob/master/pydirectinput/__init__.py#L48
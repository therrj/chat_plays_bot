# Chat Plays Bot
The goal of Chat Plays Bot is to try and create a chat bot integration for less technical users, 
to allow their chat to control games.

This supports potential overlapping key presses from multiple users.

All configuration is handled via a `config.yaml` file and at minimum, you'll need
to add a few settings to a `config.yaml` file before you can get started.

See [Configuration File](#configuration-file) for initial setup.

If you don't want to deal with building this manually, you can just download the `chat_plays_bot.exe` file [here](./executable).

## Configuration file
At minimum, you'll need to set up authentication tokens and specify the following
in a `config.yaml` file
- `TWITCH_USERNAME`
- `TWITCH_ACCESS_TOKEN`
- `TWITCH_CLIENT_ID` 
- `TWITCH_CHANNEL`

and you should also setup your `KEY_INPUT` mapping.

For more information on all settings and an example `config.yaml` file check
out the config [README](./config/README.md).

## Running Chat Plays Bot
Once you have your configuration file setup, place it in the same location as the `chat_plays_bot`
executable you can simply run the `chat_plays_bot.exe` file.

## Using Chat Plays Bot as Chat Member
This example is based on the `KEY_INPUTS` in the 
[example config.yaml file](./config/config.yaml).

For a more detailed description of input handling check out the 
[Key Press Settings](./config/README.md#key-press-settings).

Chat inputs can take one of two formats:
- `key`: A key press using the default duration
- `key duration`: A key press for `duration` amount of time

For example, a user can trigger the `a` key in one of two ways:
- `a`
- `a 6`

In the first example, the `a` key will be pressed for the default duration.

In the second example, the `a` key will be pressed for 6 times longer than the default duration.

These settings can be configured via the [Key Press Settings](./config/README.md#key-press-settings).


# For Developers:
You'll need to make sure you have the following packages available:
- `twitchio`
- `pyyaml`
- `pydirectinput`

## Building A New Executable
If you make updates or would like to build a new executable you can run the following 
for Windows from the `src` directory:
```shell
python -m PyInstaller main.py -F -n chat_plays_bot.exe --distpath "../build/build" --workpath "../build/dist" --specpath "../build"
```
The executable will end up in `build/build`

## Future Plans
Ideally these would get done, but this is a bit of a hobby project so I might
not be able to dedicate a lot of time to it.

If you would like any of these to get done feel free to post a comment or open
a feature request!

### Short Term Support
- Add more protection against bad configs
- Create a cleaner release mechanism so users can just download the exe

### Potential Future Functionality Additions
- Possibly add support for custom durations per key
- Support multi-key combinations (ie, right + jump)
- Add support for mouse control
- Youtube support

### Best Practice TODOs
- Add testing/checks
- Better setup for logging per module
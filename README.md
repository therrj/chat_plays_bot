

## Building A New Executable
python -m PyInstaller main.py -F -n twitch_plays.exe --distpath "../build/build" --workpath "../build/dist" --specpath "../build"

## Possible Future Support
- Add support for custom durations per key
- Support multi-key combinations (ie, right + jump)
- Youtube support
- Maybe setup logging per module, instead of just using a global logger
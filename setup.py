from cx_Freeze import setup, Executable

base = None

executables = [Executable("alien_invasion.py", base=base)]

packages = ["idna","sys","pygame","time","settings","game_stats","scoreboard","button","bullet","alien"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Alien_Invasion",
    options = options,
    version = "0.11",
    description = 'Game',
    executables = executables
)
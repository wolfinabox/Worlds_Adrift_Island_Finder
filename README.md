# Worlds_Adrift_Island_Finder
Simple Python tool to see if a Worlds Adrift island is in-game

To use this, download an executable from the [Releases](https://github.com/wolfinabox/Worlds_Adrift_Island_Finder/releases), run it, and paste/type in the island number. This can either be the entire Steam Workshop link (eg: https://steamcommunity.com/sharedfiles/filedetails/?id=673943027), or just the number at the end (673943027).

![in_game.png](https://i.imgur.com/NVwTuVc.png)
![not_in_game.png](https://i.imgur.com/5jVuO3I.png)

To compile this for Windows, clone the repository, create a virtualenv (recommended) of Python 3.6.7 or compatible, and have Pip install from the requirements.txt. You can make your own executable using the pyinstaleller command shown in .vscode/tasks.json (the correct pyinstaller version is included in the requirements.txt)

For other platforms, pyinstaller *may* work but I've not tested it. You should still be able to execute this script with the Python interprerter, however.

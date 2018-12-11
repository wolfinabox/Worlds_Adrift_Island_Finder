# Worlds_Adrift_Island_Finder
Simple Python tool to see if a Worlds Adrift island is in-game

To use this, download an executable from the [Releases](https://github.com/wolfinabox/Worlds_Adrift_Island_Finder/releases), run it, and paste/type in the island number. This can either be the entire Steam Workshop link (eg: https://steamcommunity.com/sharedfiles/filedetails/?id=673943027), or just the number at the end (673943027).

![in_game.png](https://i.imgur.com/IZiE6jP.png)

![link_in_game.png](https://i.imgur.com/ufxBl9k.png)

![not_in_game.png](https://i.imgur.com/hLqPqWJ.png)

To compile this for Windows, clone the repository, create a virtualenv (recommended) of Python 3.6.7 or compatible, and have Pip install from the requirements.txt. You can make your own executable using the Pyinstaller command shown in .vscode/tasks.json (the correct Pyinstaller version is included in the requirements.txt)


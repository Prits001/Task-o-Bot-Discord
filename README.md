# Task-o-Bot-Discord
Simple discord bot that is able to save, store, and manipulate user notes
- /create-task
- /read-tasks
- /erase-task
- /delall-tasks

Notes(tasks) are saved into a messages.json file with userid.
Be aware that `/read-tasks` can show your list to others! Better to use the bot in direct messages.

Reads environment variable `TOKEN` from `.env` file.
Example of `.env` file
```
TOKEN = VALUE
```

# Installation
```bash
git clone https://github.com/Prits001/Task-o-Bot-Discord.git
cd Task-o-Bot-Discord
echo "{}" >> messages.json
python -m pip install py-cord dotenv
python main.py
```

# Contributing
Feel free to open pull requests if you wish to contribute


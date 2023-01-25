# Telegram Bot - Get IP bot

Basically the idea is to have a way to getting the bot's server's current IP. Useful for getting a dynamic IP, just use the command `/locate`.

## Standalone usage

```
git clone https://github.com/anthares101/get-ip-bot.git
cd get-ip-bot
pip install -r requirements.txt
```

Create a telegram bot and fill the variables in the `config.py` file. Start the bot script with `python main.py`.

## Docker usage

To build the image, simply run:

`docker build -t get-ip-bot .`

After that is done, you can start your container:

`docker run -v <<PATH/TO/YOUR/config.py>>:/app/config.py get-ip-bot`

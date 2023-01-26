# Telegram Bot - Get IP bot

Basically the idea is to have a way to get the bot's server's current IP. Useful for getting a dynamic IP, just use the command `/locate`.

## Before you start

Create a telegram bot and fill the variables in the `config.py` file.

## Standalone usage

```
git clone https://github.com/anthares101/get-ip-bot.git
cd get-ip-bot
pip install -r requirements.txt
```

Start the bot script with `python main.py`.

## Docker usage

### Recommended way

This repository takes care of building a docker image when necessary and uploads it to [DockerHub](https://hub.docker.com/r/anthares101/get-ip-bot). You don't need to build anything!

```
docker run -v </PATH/TO/YOUR/config.py>:/app/config.py anthares101/get-ip-bot:latest
```

### Build it yourself

To build the image, simply run:

```
docker build -t get-ip-bot .
```

After that is done, you can start your container:

```
docker run -v </PATH/TO/YOUR/config.py>:/app/config.py get-ip-bot
```

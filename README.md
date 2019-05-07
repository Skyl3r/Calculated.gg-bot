# Calculated.gg-bot


## Dependencies
- Python 3.7
- Discord.py 1.0
- requests
- [Pydle](https://github.com/Shizmob/pydle)
- [profanity-check](https://github.com/vzhou842/profanity-check)

## Description

A couple changes are made in the logic of the bot to reduce code redundancy over the existing bot. The core functionality of the bot revolves around two core classes. `Command` and `Connector`.

#### Command

Command is a template class that has the following attributes you can set:
- `requiredArgs`: the number of arguments required for the command. -1 will allow any number of arguments (so that your function can determine what to do)
- `helpMessage`: the message to be displayed when a user runs <prefix>help command-name
- `action`: the method that will be run if the command was used with the correct number of args.
  
#### Connector

`Connector` is a template for how connections should be established. It requires several functions defined to work.
- `message_received(sender, channel, message)`: this is used to parse messages and execute commands
- `connector_run()`: this should start the connector.
- `send_message(sender, channel, message)`: this should send a message to the target platform


#### Message

The `Message` class is essentially a wrapper for Discord.Embed. It is used as a compatibility layer to provide nicer formatting for platforms that support it.


## Setup

#### Debian

1. Make sure you have Python 3.7 and pip for Python 3.7. At the present time these are available in buster (current unstable).
```bash
apt update
apt install python3 python3-pip
```
2. Install necessary Python dependencies.
```bash
apt install python3-requests
pip3 install discord pydle profanity-check
```
3. Clone Calculated.gg-bot
```bash
git clone https://github.com/Skyl3r/Calculated.gg-bot
```
4. Review `irc_example.py` or `discord_example.py` to create your run script. Then launch by running:
```bash
python3 irc_example.py # Or discord_example.py
```

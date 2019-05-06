###########################################
#
#  Discord Connector
#
#  Will implement connectors and override
#  methods to create an abstraction layer
#  discord.Client methods will call Connector methods
#  in order to build compatibility layer.
#
#  -Skyl3r
#
###########################################

from discord import Client

from classes.connector import Connector


class DiscordConnector(Connector, Client):

    # Discord requires bot token
    token = ""

    def __init__(self):
        Client.__init__(self)

    def connector_run(self):
        self.run(self.token)

    async def send_message(self, user, channel, message, icon=""):
        channel = self.get_channel(channel)
        await channel.send(message)

    # Discord Methods
    async def on_ready(self):
        pass

    async def on_message(self, message):
        async with message.channel.typing():
            await self.received_message(message.author, message.channel.id, message.content)

##########################################
# Command class is a standard
# interface for commands.
# Each connector can decide how to handle
#
# -Skyl3r
##########################################


class Command:

    helpMessage = ""
    icon = ""
    requiredArgs = 0
    connector = object

    def __init__(self, connector):
        self.connector = connector

    async def action(self, sender, channel, args):
        pass

    async def send_message(self, sender, channel, message):
        await self.connector.send_message(sender, channel, message)
    pass
###########################################
#
#  IRC Connector
#
#  Will implement connectors and override
#  methods to create an abstraction layer
#  uses twisted
#
#  -Skyl3r
#
###########################################

from classes.connector import Connector
from twisted.words.protocols import irc


class IrcConnector(Connector, irc.IRCClient):
    nick = ""
    channel = ""
    password = ""
    server = ""
    port = 6667

    def __init__(self):
        irc.IRCClient.__init__()

    def privmsg(self, user, channel, message):
        self.received_message(user, channel, message)
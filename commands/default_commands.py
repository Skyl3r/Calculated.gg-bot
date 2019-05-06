##################################################
#
#  This is where default commands will be defined
#  It will be a dictionary that is supplied to
#  connector when initialized
#
# -Skyl3r
#
###################################################

import requests
from classes.command import Command

##########################
# Helper Functions
##########################


def get_player_id(player_name):
    response_id = requests.get("https://calculated.gg/api/player/{}".format(player_name)).json()
    if str(type(response_id)) == "<class 'dict'>":
            response_id = "User not found"
    return response_id


def get_player_profile(player_id):
    response_profile = requests.get("https://calculated.gg/api/player/{}/profile".format(player_id)).json()

    avatar_link = response_profile["avatarLink"]
    avatar_name = response_profile["name"]
    platform = response_profile["platform"]
    past_names = response_profile["pastNames"]

    return avatar_link, avatar_name, platform, past_names


#########################
# Commands
#########################

# Help command, gets help message for given command
class HelpCommand(Command):
    # Requires one arg. The name of the command
    requiredArgs = -1

    # Simple message there...
    helpMessage = """do <prefix>help [command name] for more information on a command.
    To see all commands, try <prefix>listcommands"""

    async def action(self, sender, channel, args):
        if args[0] not in self.connector.commands:
            await self.send_message(sender, channel, "command " + args[0] + " does not exist.")
        await self.send_message(sender, channel, self.connector.commands[args[0]].helpMessage,
                                    "https://i.imgur.com/LqUmKRh.png")


class QueueCommand(Command):
    requiredArgs = 0
    helpMessage = "Shows current amount of replays in the queue."

    async def action(self, sender, channel, args):
        response = requests.get("https://calculated.gg/api/global/queue/count").json()
        print(response[2]["count"])
        await self.send_message(sender, channel, str(response[2]["count"]) + ' replays in the queue.')


class FullQueueCommand(Command):
    requiredArgs = 0
    helpMessage = ""

    async def action(self, sender, channel, args):
        response = requests.get("https://calculated.gg/api/global/queue/count").json()
        say = "Number of replays in each queue."

        for priority in response:
            msg = str(priority["count"])
            say += " " + str(priority["name"]) + " " + msg

        await self.send_message(sender, channel, say)


class ProfileCommand(Command):
    requiredArgs = 1
    helpMessage = ""

    async def action(self, sender, channel, args):
        player_id = get_player_id(args[0])
        response_stats = requests.get("https://calculated.gg/api/player/{}/profile_stats".format(player_id)).json()

        car_name = response_stats["car"]["carName"]
        car_percentage = str(round(response_stats["car"]["carPercentage"] * 100, 1)) + "%"

        try:
            avatar_link, avatar_name, platform, past_names = get_player_profile(player_id)
        except KeyError:
            await self.connector.send_message(sender, channel, "User could not be found, please try again")

        list_past_names = ""
        for name in past_names:
            list_past_names += name + "\n"

        say = "Favourite car: " + car_name + " (" + car_percentage + "). Past names: " + list_past_names

        await self.send_message(sender, channel, say)


class RanksCommand(Command):
    requiredArgs = 1
    helpMessage = ""

    async def action(self, sender, channel, args):
        player_id = get_player_id(args[0])
        ranks = requests.get("https://calculated.gg/api/player/{}/ranks".format(player_id)).json()

        say = ""

        order = ['duel', 'doubles', 'solo', 'standard', 'hoops', 'rumble', 'dropshot', 'snowday']
        for playlist in order:
            say += playlist.title() + ": " + ranks[playlist]['name'] + " - " + str(ranks[playlist]['rating']) + "\n"

        await self.send_message(sender, channel, say)

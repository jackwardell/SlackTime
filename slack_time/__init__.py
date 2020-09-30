# -*- coding: utf-8 -*-
import os

from .api import SlackAPI
from .methods import Admin
from .methods import Api
from .methods import Apps
from .methods import Auth
from .methods import Bots
from .methods import Calls
from .methods import Chat
from .methods import Conversations
from .methods import Dialog
from .methods import Dnd
from .methods import Emoji
from .methods import Files
from .methods import Migration
from .methods import OAuth
from .methods import Pins
from .methods import Reactions
from .methods import Reminders
from .methods import Rtm
from .methods import Search
from .methods import Stars
from .methods import Team
from .methods import Usergroups
from .methods import Users
from .methods import Views
from .methods import Workflows
from .utils import cached_property
from .utils import SlackError

__all__ = ["get_slack_time", "SlackTime", "SlackError"]


class SlackTime(SlackAPI):
    """
    SlackTime client

    use:
      >>> from slack_time import SlackTime
      >>> client = SlackTime("xoxo-token-goes-here")
      >>> client.chat.post_message("#general", "hey team!")
      <Response [200]>
    """

    @cached_property
    def admin(self) -> Admin:
        return Admin(**self.params)

    @cached_property
    def api(self) -> Api:
        return Api(**self.params)

    @cached_property
    def apps(self) -> Apps:
        return Apps(**self.params)

    @cached_property
    def auth(self) -> Auth:
        return Auth(**self.params)

    @cached_property
    def bots(self) -> Bots:
        return Bots(**self.params)

    @cached_property
    def calls(self) -> Calls:
        return Calls(**self.params)

    @cached_property
    def chat(self) -> Chat:
        return Chat(**self.params)

    @cached_property
    def conversations(self) -> Conversations:
        return Conversations(**self.params)

    @cached_property
    def dialog(self) -> Dialog:
        return Dialog(**self.params)

    @cached_property
    def dnd(self) -> Dnd:
        return Dnd(**self.params)

    @cached_property
    def emoji(self) -> Emoji:
        return Emoji(**self.params)

    @cached_property
    def files(self) -> Files:
        return Files(**self.params)

    @cached_property
    def migration(self) -> Migration:
        return Migration(**self.params)

    @cached_property
    def oauth(self) -> OAuth:
        return OAuth(**self.params)

    @cached_property
    def pins(self) -> Pins:
        return Pins(**self.params)

    @cached_property
    def reactions(self) -> Reactions:
        return Reactions(**self.params)

    @cached_property
    def reminders(self) -> Reminders:
        return Reminders(**self.params)

    @cached_property
    def rtm(self) -> Rtm:
        return Rtm(**self.params)

    @cached_property
    def search(self) -> Search:
        return Search(**self.params)

    @cached_property
    def stars(self) -> Stars:
        return Stars(**self.params)

    @cached_property
    def team(self) -> Team:
        return Team(**self.params)

    @cached_property
    def usergroups(self) -> Usergroups:
        return Usergroups(**self.params)

    @cached_property
    def users(self) -> Users:
        return Users(**self.params)

    @cached_property
    def views(self) -> Views:
        return Views(**self.params)

    @cached_property
    def workflows(self) -> Workflows:
        return Workflows(**self.params)


def get_slack_time(env_var: str = "SLACK_API_TOKEN", **kwargs) -> SlackTime:
    """get a SlackTime client"""
    token = os.getenv(env_var)
    assert token, f"You must save a '{env_var}' environment variable"
    return SlackTime(token, **kwargs)

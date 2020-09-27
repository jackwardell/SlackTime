# -*- coding: utf-8 -*-
import os

from slack_time.api import SlackAPI
from slack_time.methods import Admin
from slack_time.methods import Api
from slack_time.methods import Apps
from slack_time.methods import Auth
from slack_time.methods import Bots
from slack_time.methods import Calls
from slack_time.methods import Chat
from slack_time.methods import Conversations
from slack_time.methods import Dialog
from slack_time.methods import Dnd
from slack_time.methods import Emoji
from slack_time.methods import Files
from slack_time.methods import Migration
from slack_time.methods import OAuth
from slack_time.methods import Pins
from slack_time.methods import Reactions
from slack_time.methods import Reminders
from slack_time.methods import Rtm
from slack_time.methods import Search
from slack_time.methods import Stars
from slack_time.methods import Team
from slack_time.methods import Usergroups
from slack_time.methods import Users
from slack_time.methods import Views
from slack_time.methods import Workflows
from slack_time.utils import cached_property
from slack_time.utils import SlackError

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

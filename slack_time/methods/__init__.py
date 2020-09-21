# -*- coding: utf-8 -*-
from .admin import Admin
from .api import Api
from .apps import Apps
from .auth import Auth
from .bots import Bots
from .calls import Calls
from .chat import Chat
from .conversations import Conversations
from .dialog import Dialog
from .dnd import Dnd
from .emoji import Emoji
from .files import Files
from .migration import Migration
from .oauth import OAuth
from .pins import Pins
from .reactions import Reactions
from .reminders import Reminders
from .rtm import Rtm
from .search import Search
from .stars import Stars
from .team import Team
from .usergroups import Usergroups
from .users import Users
from .views import Views
from .workflows import Workflows

from slack_time.utils import cached_property
from slack_time.api import SlackAPI

__all__ = [
    "Admin",
    "Api",
    "Apps",
    "Auth",
    "Bots",
    "Calls",
    "Chat",
    "Conversations",
    "Dialog",
    "Dnd",
    "Emoji",
    "Files",
    "Migration",
    "OAuth",
    "Pins",
    "Reactions",
    "Reminders",
    "Rtm",
    "Search",
    "Stars",
    "Team",
    "Usergroups",
    "Users",
    "Views",
    "Workflows",
    "SlackTime",
]


class SlackTime(SlackAPI):
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

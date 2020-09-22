# SlackTime

## Background
* This library is a wrapper around the Slack WebAPI (https://api.slack.com/methods)
* This library is a homage to the great (and now archived) Slacker (https://github.com/os/slacker)
* This library is a response to the official Slack client (https://github.com/slackapi/python-slackclient). I'm so petty I couldn't stand the the camel/snake-case hybrid: `client.chat_postMessage`
* This library was made mostly by a script that scraped the Slack API method page and automagically generated the code
* This library was touched up by a human and some tests and docs generated, but I am fully aware there could be bugs


## Aim
This library aims to be:
* Simple
* Intuitive
* Fast

## Install
* This library uses type hints so is Python 3.5+
* Simply install using pip
```
pip install slack_time
```

## Learn by example
#### Getting a client:
```
from slack_time import get_slack_time

slack_time = get_slack_time()
```
* `get_slack_time` will grab the `SLACK_API_TOKEN` environment variable
* Environment variable grabbed can be changed:
```
slack_time = get_slack_time('SLACK_TOKEN')
```

#### Making a client:
```
from slack_time import SlackTime

slack_time = SlackTime('xoxo-hello-world')
```
* Or with other config:
```
from slack_time import SlackTime
import requests

token = "xoxo-gossip-girl"
session = requests.Session()
proxies = {"http": "10.10.10.10:80", "https": "10.11.12.13:8080"}
timeout = 60

slack_time = SlackTime(token, session=session, proxies=proxies, timeout=timeout)
```

#### Using the client:
```
from slack_time import get_slack_time

slack_time = get_slack_time()

slack.chat.post_message("general", "Hey team, I love this knock off Slacker library!"
```


#### How it works
* In the web API docs (https://api.slack.com/methods) the methods are listed as endpoints e.g. admin.apps.requests.list
* The url for admin.apps.requests.list would be https://slack.com/api/admin.apps.requests.list
* The client method would be `slack_time.admin.apps.requests.list(*args, **kwargs)`
* The method translation would be from camelCase to snake_case

Some examples:
* admin.conversations.convertToPrivate -> slack_time.admin.conversations.convert_to_private
* admin.conversations.ekm.listOriginalConnectedChannelInfo -> admin.conversations.ekm.list_original_connected_channel_info
* files.revokePublicURL -> files.revoke_public_url
* etc

#### Examples
```
from slack_time import get_slack_time

slack = get_slack_time()

slack.files.upload('hello_world.txt')

with open('hello_world.txt') as f:
    slack.files.upload(f)
```


#### Docs
Please use the slack docs https://api.slack.com/methods


#### Contributing
* I imagine there are bugs
* Please feel free to submit a PR, you will need to install pre-commit (https://pre-commit.com/)

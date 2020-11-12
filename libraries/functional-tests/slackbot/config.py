#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978

    SLACK_VERIFICATION_TOKEN = os.environ.get("SlackVerificationToken", "16q9F4wbB9o2sMie2CREoQbg")
    SLACK_BOT_TOKEN = os.environ.get("SlackBotToken", "xoxb-1493382945509-1502666884372-S6emLrmxCQrbLZYrz1pP7uPp")
    SLACK_CLIENT_SIGNING_SECRET = os.environ.get("SlackClientSigningSecret", "a52331e1bdf3b90667e9b7b3ffe8308e")

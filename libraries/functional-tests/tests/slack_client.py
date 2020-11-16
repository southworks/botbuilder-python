# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import hashlib
import hmac
import json
import os
import uuid
import aiounittest
import datetime
import time
import http.client

import requests


class SlackClient(aiounittest.AsyncTestCase):
    async def test_send_and_receive_slack_message(self):
        # Arrange
        self._slack_url_base: str = "https://slack.com/api"
        self._client: http.client
        self._slack_channel: str
        self._slack_bot_token: str
        self._slack_client_signing_secret: str
        self._slack_verification_token: str
        self._bot_name: str
        self._get_environment_vars()

        echo_guid = str(uuid.uuid4())

        # Act
        await self._send_message_async(echo_guid)
        response = await self._receive_message_async()

        # Assert
        self.assertEqual(f"Echo: {echo_guid}", response)

    async def _receive_message_async(self, response):
        last_message = ""
        i = 0

        while not ("Echo" in last_message) and i < 60:
            self._client = http.client.HTTPSConnection(
                f"{self._slack_url_base}/conversations.history?token={self._slack_bot_token}&channel={self._slack_channel}"
            )
            self._client.request("GET", "/")
            response = json.loads(self._client.getresponse().read().decode())

            last_message = response["Messages"][0]

            time.sleep(1)
            i += 1

        return last_message

    async def _send_message_async(self, echo_guid: str):
        timestamp = str(int(datetime.datetime.utcnow().timestamp()))
        message = self._create_message(echo_guid)
        hub_signature = self._create_hub_signature(message, timestamp)
        client = http.client.HTTPSConnection(
           f"{self._bot_name}.azurewebsites.net"
        )
        headers = {
            "X-Slack-Request-Timestamp": timestamp,
            "X-Slack-Signature": hub_signature,
            "Content-type": "application/json",
        }
        json_data = json.dumps(message)

        client.request("POST", "/api/messages", body=json_data, headers=headers)

        response = client.getresponse().read()
        # bot_response = requests.post(
        #     f"https://{self._bot_name}.azurewebsites.net/api/messages",
        #     headers=headers,
        #     json=json_data)

    def _create_message(self, echo_guid: str):
        slack_event = {
            "client_msg_id": "client_msg_id",
            "type": "message",
            "text": echo_guid,
            "user": "userId",
            "channel": self._slack_channel,
            "channel_type": "im",
        }

        message = {
            "token": self._slack_verification_token,
            "team_id": "team_id",
            "api_app_id": "apiAppId",
            "event": slack_event,
            "type": "event_callback",
        }

        return json.dumps(message)

    def _create_hub_signature(self, message: str, timestamp: str):
        signature = {"v0", timestamp, message}
        base_string = ":".join(signature)

        hash_computed = hmac.new(
            bytes(self._slack_client_signing_secret, encoding='utf8'),
            base_string.encode("utf-8"),
            digestmod=hashlib.sha256,
        ).hexdigest()

        hash_result = "v0=%s" % (hash_computed,)

        return hash_result

    def _get_environment_vars(self):
        self._slack_channel = os.getenv("SlackChannel")
        if not self._slack_channel:
            raise Exception('Environment variable "SlackChannel" not found.')

        self._slack_bot_token = os.getenv("SlackBotToken")
        if not self._slack_bot_token:
            raise Exception('Environment variable "SlackBotToken" not found.')

        self._slack_client_signing_secret = os.getenv("SlackClientSigningSecret")
        if not self._slack_client_signing_secret:
            raise Exception(
                'Environment variable "SlackClientSigningSecret" not found.'
            )

        self._slack_verification_token = os.getenv("SlackVerificationToken")
        if not self._slack_verification_token:
            raise Exception('Environment variable "SlackVerificationToken" not found.')

        self._bot_name = os.getenv("BotName")
        if not self._bot_name:
            raise Exception('Environment variable "BotName" not found.')

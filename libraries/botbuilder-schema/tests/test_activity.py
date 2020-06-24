# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import aiounittest
from botbuilder.schema import (
    Activity,
    ConversationReference, ConversationAccount
)


class TestActivity(aiounittest.AsyncTestCase):
    def test_constructor(self):
        # Arrange
        activity = Activity()

        # Assert
        self.assertIsNotNone(activity)

    def test_apply_conversation_reference(self):
        # Arrange
        conversation = ConversationAccount()
        channel_id = "test_channel_id"
        service_url = "test_service_url"
        reference = ConversationReference(
            conversation=conversation,
            channel_id=channel_id,
            service_url=service_url
        )

        # Act
        result = Activity.apply_conversation_reference(reference)

        # Assert
        self.assertIsNotNone(result)
        self.assertEqual(result.conversation, conversation)
        self.assertEqual(result.channel_id, channel_id)
        self.assertEqual(result.service_url, service_url)

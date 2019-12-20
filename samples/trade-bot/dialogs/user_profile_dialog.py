# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.dialogs import (
    ComponentDialog,
    WaterfallDialog,
    WaterfallStepContext,
    DialogTurnResult,
)
from botbuilder.dialogs.prompts import (
    TextPrompt,
    NumberPrompt,
    ChoicePrompt,
    ConfirmPrompt,
    PromptOptions,
    PromptValidatorContext,
)
from botbuilder.dialogs.choices import Choice
from botbuilder.core import MessageFactory, UserState

from data_models import UserProfile


class UserProfileDialog(ComponentDialog):
    def __init__(self, user_state: UserState):
        super(UserProfileDialog, self).__init__(UserProfileDialog.__name__)

        self.user_profile_accessor = user_state.create_property("UserProfile")

        self.add_dialog(
            WaterfallDialog(
                WaterfallDialog.__name__,
                [
                    self.options_step,
                    self.portfolio_show_step,
                    self.next_step,
                    self.check_is_info_ok
                ],
            )
        )
        self.add_dialog(TextPrompt(TextPrompt.__name__))
        self.add_dialog(TextPrompt("text_prompt_input"))

        self.add_dialog(
            NumberPrompt(NumberPrompt.__name__, UserProfileDialog.age_prompt_validator)
        )
        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))
        self.add_dialog(ConfirmPrompt(ConfirmPrompt.__name__))

        self.add_dialog(ChoicePrompt("options_step"))

        self.initial_dialog_id = WaterfallDialog.__name__

    async def options_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        """ working so far, this is a Choice select """
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Welcome! What can I help you with?"),
                choices=[Choice("Portfolio"), Choice("Trade"), Choice("Help")],
            ),
        )

    @staticmethod
    async def age_prompt_validator(prompt_context: PromptValidatorContext) -> bool:
        """ This condition is our validation rule. You can also change the value at this point. """
        return (
            prompt_context.recognized.succeeded
            and 0 < prompt_context.recognized.value < 150
        )

    async def portfolio_show_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        """ Step description:  """
        step_context.values["option_selected"] = step_context.result.value

        step_context.values["input"] = step_context.result

        if step_context.result:
            #  Get the current profile object from user state.  Changes to it
            # will saved during Bot.on_turn.
            user_profile = await self.user_profile_accessor.get(
                step_context.context, UserProfile
            )

            user_profile.transport = step_context.values["option_selected"]

        if step_context.result.value == 'Portfolio':
            await step_context.context.send_activity(
                MessageFactory.text(f"Very well, this is your portfolio.")
            )
            await step_context.context.send_activity(
                MessageFactory.text(f"[PORTFOLIO_CARD]")
            )
            # Here, the conversation could continue, or be terminated and reset
            return await step_context.end_dialog()

        elif step_context.result.value == 'Trade':
            await step_context.context.send_activity(
                MessageFactory.text(f"Ok, you want to trade.")
            )
            # esto deberia ir dentro de Trade. Para portfolio, deberia reusar algun paso o cerrar.
            return await step_context.prompt(
                "text_prompt_input",
                PromptOptions(prompt=MessageFactory.text("What do you want to buy or sell?")),
            )
            # Here we wait for a TextPrompt input, that should contain the user intent,
            # like:
            # Buy 25 MSFT for $ 120

            # here, we can also have a Choice Prompt based on our current holdings.
            # that way, the user intent, is getting narrowed in a interactive fashion.

        elif step_context.result.value == 'Help':
            await step_context.context.send_activity(
                MessageFactory.text(f"Some day, when the sun is bright in the sky and all the backlog tasks are completed, I will be able to give you help. Sorry.")
            )
            return await step_context.end_dialog()

    async def next_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        """ finally worked """
        step_context.values["input"] = step_context.result

        # We can send messages to the user at any point in the WaterfallStep.
        await step_context.context.send_activity(
            MessageFactory.text(f"ECHO INPUT: {step_context.result}")
        )
        await step_context.context.send_activity(
            MessageFactory.text(f"[In this step, we can use Recognizers-Text to know the user intention.]")
        )

        return await step_context.prompt(
            ConfirmPrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Is this correct?")
            ),
        )

        # if we don't ask for confirmation, we terminate it:
        # return await step_context.end_dialog()

    async def check_is_info_ok(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        query = step_context.values["input"]

        if step_context.result:
            # User said "yes" so we can execute the operation.
            await step_context.context.send_activity(
                MessageFactory.text(f"Executing Operation.")
            )

            await step_context.context.send_activity(
                MessageFactory.text(f"[Lie] Operation Executed. This is the details of the operation:")
            )
            await step_context.context.send_activity(
                MessageFactory.text(f"[CARD WITH TRANSACTION DETAILS]")
            )

            return await step_context.end_dialog()

        # User said "no"
        # so we will have to terminate for now
        # also we could reuse some of the previous steps.
        await step_context.context.send_activity(
            MessageFactory.text(f"I'm sorry I did not understand your order: '{query}'")
        )
        await step_context.context.send_activity(
            MessageFactory.text(f"I am still learning, you know?")
        )

        return await step_context.end_dialog()

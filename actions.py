from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_core_sdk.events import (
    Restarted,
)

class ActionOutOfScope(Action):

    def name(self):
        return "action_out_of_scope"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message("Didn't understand that.")

        return [Restarted()]

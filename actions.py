from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_core_sdk.events import (
    Restarted,
)

import json
import socket

from server_request import Request

my_request = Request("http://127.0.0.1:5000/")

class ActionGetTime(Action):
	def name(self):
		return "action_get_time"

	def run(self, dispatcher, tracker, domain):
		data = my_request.send_intent("get_time")
		if "error" in data:
			dispatcher.utter_message("Looks like an error has occured with the action.")
			return[Restarted()]

		dispatcher.utter_message("The time is %d:%d." % (data['hour'], data['minute']))
		return []


class ActionOutOfScope(Action):

    def name(self):
        return "action_out_of_scope"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message("Didn't understand that.")

        return [Restarted()]

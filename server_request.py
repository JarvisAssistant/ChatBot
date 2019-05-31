import requests
import json

class Request:
	def __init__(self, server):
		self.server = server

	def send_intent(self, intent, parameters=[]):
		intent_payload = {'intent' : intent, 'parameters' : parameters}

		try:
			r = requests.put(self.server + "intent", json=intent_payload)
		except requests.exceptions.ConnectionError:
			return { "error" : "connection_error" }

		data = None
		try:
			data = r.json()
		except ValueError:
			return { "error" : "no_json" , "status_code" : data.status_code }

		return data

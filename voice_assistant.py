from wit import Wit
import json


# Class object to convert intents and entities to actions
class VoiceAssistant:
    """
    Voice Assistant object.
    Responds to text inputs and checks datetime for
    calendar appointments.
    """

    def __init__(self, wit_access_token, actions, emo_train_filename=None):
        self.client = Wit(access_token=wit_access_token)
        self.actions = actions
        self.emotion_list = [

        ]

    # Respond to text input
    def respond(self, input_text, context=None, voice_output=False):
        resp = self.client.message(input_text)
        entities = resp['entities']
        intents = entities['intent']
        for intent in intents:
            text_resp = self.actions[intent['value']](entities)
        return text_resp

    def calendar(self, datetime):
        pass

    def emotion_update(self):
        pass





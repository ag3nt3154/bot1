from voice_assistant import VoiceAssistant
import interactions_1
import numpy as np
from misc_fn import dump, load

# Access wit.ai app with access token
access_token = 'U5B35XDDKAAG7MBTFNF6JZDXT73HN6WD'

# Collate available actions
actions = {
    'greeting': interactions_1.default_greeting,
    'send_nudes': interactions_1.send_nudes,
    'introduction': interactions_1.introduction
}



# Set up voice assistant iona
iona = VoiceAssistant(wit_access_token=access_token,
                      actions=actions)

test_texts = [
    'hello',
    'who are you?',
    'tell you about yourself'
]

# for text in test_texts:
#     print(iona.respond(input_text=text))













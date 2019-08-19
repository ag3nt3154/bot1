import json
from misc_fn import rand_choice, find_entity, compare
import os
from icrawler.builtin import GoogleImageCrawler
from PIL import Image



def default_greeting(entities):
    """
    Returns a greeting from a list.
    E.g. 'hello', 'hi'
    """
    print('--- Running interactions_1.default_greeting')

    greetings_list = [
        'Hello!',
        'Hey there!',
        'Yo!'
    ]

    # Gets names from entities
    try:
        contact_val = str(entities['contact'][0]['value'])
    except KeyError:
        contact_val = None

    # Gets greeting string depending on contact detected.
    if contact_val is None:
        text_resp = rand_choice(greetings_list)
    elif compare(contact_val, 'iona'):
        text_resp = 'Hello Kami-sama!'
    elif compare(contact_val, 'siri'):
        text_resp = 'Do I look like a dumb blonde living in an overpriced phone?'
    elif compare(contact_val, 'alexa'):
        text_resp = 'I am neither mythical, nor savage, nor missing my right boob.'
    elif compare(contact_val, 'cortana'):
        text_resp = 'You need treatment John, that PTSD cannot go on forever.'
    else:
        text_resp = 'I am not ' + contact_val + '!'
    return text_resp


def send_nudes(entities):
    """
    Sends nudes
    """
    print('--- Running send_nudes')
    # Get path of current file
    path = os.getcwd()
    path = path + '\img'

    # Choose random keyword
    keywrd = [
        'jesus',
        'jesus staring',
        'jesus wallpaper'
    ]

    # Google image search for 5 images
    google_crawler = GoogleImageCrawler(storage={'root_dir': path})
    google_crawler.crawl(keyword=rand_choice(keywrd), max_num=3)
    file_list = os.listdir(path=path)
    path_list = []

    # Choose random image to display
    for file in file_list:
        file = path + '\\' + str(file)
        path_list.append(file)
    image = rand_choice(path_list)

    # Display image
    img = Image.open(image)
    img.show()

    # Delete downloaded images
    for file in path_list:
        os.remove(file)

    text_resp = 'SENDING NUDES'
    return text_resp


def introduction(entities):
    """
    :param entities:
    :return text_resp:
    E.g. 'Who are you?'
    """
    intro_list = [
        'I am iona-90, a voice assistant.'
    ]
    text_resp = rand_choice(intro_list)
    return text_resp
import string
import time
import sys

skip_words = ['a', 'abouta', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
                'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 
                'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
                'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
                'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
                'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
                'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
                'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
                'wish', 'with', 'would']

def set_terminal_size(width, height):
    sys.stdout.write("\x1b[8;{row};{col}t". format(row=height, col=width))
      # import os os.get_terminal_size()

def chage_title(room):
    sys.stdout.write("\x1b[2;{title}\x07". format(title = room['name']))

def textout(tin):

    for element in tin:
        time.sleep(0.05)
        print(element, end='', flush=True)

    print()

def input_filter(text):
    user_input = ''

    for element in text:
        if not (element in string.punctuation):
            user_input = user_input + element

    user_input = (user_input.lower().split())

    user_input = [element for element in user_input if element not in skip_words]

    return user_input


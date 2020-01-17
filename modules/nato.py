# nato.py: Encode/decode a message in the NATO phonetic alphabet
# by James Davidson

import re

nato_alph = {
    "a": "Alfa", "b": "Bravo", "c": "Charlie", "d": "Delta",
    "e": "Echo", "f": "Foxtrot", "g": "Golf", "h": "Hotel",
    "i": "India", "j": "Juliet", "k": "Kilo", "l": "Lima",
    "m": "Mike", "n": "November", "o": "Oscar", "p": "Papa",
    "q": "Quebec", "r": "Romeo", "s": "Sierra", "t": "Tango",
    "u": "Uniform", "v": "Victor", "w": "Whiskey", "x": "Xray",
    "y": "Yankee", "z": "Zulu", "0": "Zero", "1": "One",
    "2": "Two", "3": "Three", "4": "Four", "5": "Five",
    "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", " ": "(space)"
}


"""
Return a value's key in the above alphabet, if it exists.
"""
def fetch_key(val: str) -> str:
    if val not in nato_alph.values():
        return val
    return list(nato_alph.keys())[list(nato_alph.values()).index(val)]


"""
Return as a string the NATO alphabet encoding of the given message.
Any message characters not in the above alphabet are stripped.
"""
def encode(msg: str) -> str:
    encoded_msg = []
    for ch in msg:
        if not ch.isspace() and not ch.isalnum():
            encoded_msg.append(ch)
        else:
            encoded_msg.append(nato_alph[ch.lower()])
    return ' '.join(encoded_msg)


"""
Return as a string the translation of a given NATO message.
Any message characters not in the above alphabet are stripped.
"""
def decode(msg: str) -> str:
    decoded_msg = []
    for word in msg.split():
        decoded_msg.append(fetch_key(word))
    return ''.join(decoded_msg) 
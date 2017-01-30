import string

upper_offset = 65
lower_offset = 97

def alphabet_position(letter):
    if letter in string.ascii_uppercase:
        return ord(letter) - upper_offset
    elif letter in string.ascii_lowercase:
        return ord(letter) - lower_offset
    else:
        return -1

def rotate_character(char, rot):
    if char in string.ascii_uppercase:
        return chr((alphabet_position(char) + rot) % 26 + upper_offset)
    elif char in string.ascii_lowercase:
        return chr((alphabet_position(char) + rot) % 26 + lower_offset)
    else:
        return char

def encrypt(text, rot):
    new_text = ""
    for char in text:
        new_text += rotate_character(char, rot)
    return new_text

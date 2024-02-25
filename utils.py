# common utils
import random

def code_generator(title):
    title_to_upper = str.upper(title)
    rand_int = random.randint(0, 999)
    formatted_three_digit = '{:03d}'.format(rand_int)
    return title_to_upper + formatted_three_digit
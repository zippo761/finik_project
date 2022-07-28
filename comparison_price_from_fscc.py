import re


def price_fscc():
    """Load price from FSCC"""
    with open('test_text.txt', 'r') as file:
        text = file.read()
        text = text.replace('\n', ' ')
        text = re.findall('(?<=\d\d\.\d\.\d\d\.\d\d-\d\d\d\d).+?(?=\d\d\.\d\.\d\d\.\d\d-\d\d\d\d)', text, re.M)

    return text




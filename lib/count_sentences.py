#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, initial_value=''):
        self._value = str(initial_value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        
        sentences = [s.strip() for s in re.split(r'[.!?]', self._value) if s.strip()]
        return len(sentences)

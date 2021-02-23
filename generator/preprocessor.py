import numpy as np


class Preprocessor:

    def __init__(self, text_path, token_size = 10):
        self.text_path = text_path
        self.token_size = token_size

    def run(self):

        raw_text = self._load_doc()
        sequences = self._make_sequence(raw_text = raw_text)
        return sequences





    def _make_sequence(self,  raw_text):

        tokens = raw_text.split()
        raw_text = " ".join(tokens)
        sequences = list()

        for i in range(self.token_size, len(raw_text)):
            seq = raw_text[i - self.token_size: i + 1]
            sequences.append(seq)

        return sequences




    def _load_doc(self):

        with open(self.text_path) as f:
            text = f.read()

        return text




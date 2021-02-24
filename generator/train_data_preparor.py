from generator.util import load_file
from keras.utils import to_categorical
import numpy as np

class TrainDataPreparor:

    def __init__(self, src_path):
        self.src_path = src_path

    def _make_sequence(self, raw_text):
        lines = raw_text.split("\n")
        chars = sorted(list(set(raw_text)))
        mapping = dict((c, i) for i, c in enumerate(chars))
        sequences = list()

        for line in lines:
            encoded_seq = [mapping[char] for char in line]
            sequences.append(encoded_seq)

        vocab_size = len(mapping)
        sequences = np.array(sequences)

        return sequences, vocab_size



    def prepare(self):
        raw_text =  load_file(self.src_path)
        sequences, vocab_size = self._make_sequence(raw_text = raw_text)
        X, y = sequences[:, :-1], sequences[:, -1]
        sequences = [to_categorical(x, num_classes = vocab_size) for x in X]
        X = np.array(sequences)
        y = to_categorical(y, num_classes = vocab_size)

        return X, y




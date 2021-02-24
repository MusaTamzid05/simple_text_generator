from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import os
import pickle

class Generator:

    def __init__(self, train_dir_path):
        self.model = load_model(os.path.join(train_dir_path, "model.h5"))
        self.mapping = pickle.load(open(os.path.join(train_dir_path, "mapping.pkl"), "rb"))


    def generate(self, src_text, n_chars, seq_length = 10):

        input_text= src_text

        for _ in range(n_chars):
            encoded = [self.mapping[char] for char in input_text]
            encoded = pad_sequences([encoded], maxlen = seq_length, truncating = "pre")
            encoded = to_categorical(encoded, num_classes = len(self.mapping))
            prediction = self.model.predict_classes(encoded, verbose = 0)

            out_char = ""

            # @TODO : index based mapping should be used
            for char, index in self.mapping.items():
                if index == prediction:
                    out_char = char
                    print(out_char)
                    break

            input_text += out_char

        return input_text




import os
from generator.preprocessor import Preprocessor
from generator.util import write_file

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

class Trainer:

    def __init__(self, text_path, save_dir):

        if os.path.exists(save_dir) == False:
            os.mkdir(save_dir)
        preprocessor = Preprocessor(text_path = text_path)
        training_sequnces = preprocessor.run()

        self.train_data_path = os.path.join(save_dir, "training_seq.txt")

        #if os.path.exists(self.train_data_path):
            #raise RuntimeError(f"{self.train_data_path} already exists")
        write_file(path = self.train_data_path, lines = training_sequnces)


    def _init_model(self, width, height):

        model = Sequential()
        model.add(LSTM(75, input_shape = (width, height)))

        return model

    def train(self):
        pass




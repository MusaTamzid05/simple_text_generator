from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

import os
from generator.data_formatter import DataFormatter
from generator.train_data_preparor import TrainDataPreparor
from generator.util import write_file

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

from generator.util import load_file

import pickle


class Trainer:

    def __init__(self, text_path, save_dir):

        if os.path.exists(save_dir) == False:
            os.mkdir(save_dir)
        formatter = DataFormatter(text_path = text_path)
        training_sequnces = formatter.run()

        self.train_data_path = os.path.join(save_dir, "training_seq.txt")
        self.save_dir = save_dir

        #if os.path.exists(self.train_data_path):
            #raise RuntimeError(f"{self.train_data_path} already exists")
        write_file(path = self.train_data_path, lines = training_sequnces)


    def _init_model(self, width, height, output_size):

        print(width, height)
        model = Sequential()
        model.add(LSTM(75, input_shape = (width, height)))
        model.add(Dense(output_size, activation = "softmax"))
        model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])

        return model

    def train(self, epochs = 100, verbose = 2):
        train_data_preparor = TrainDataPreparor(src_path = self.train_data_path)
        X, y, mapping = train_data_preparor.prepare()
        model = self._init_model(width = X.shape[1], height = X.shape[2], output_size = len(y[0]))
        model.fit(X, y, epochs = epochs, verbose = verbose)
        model.save(os.path.join(self.save_dir, "model.h5"))
        pickle.dump(mapping, open(os.path.join(self.save_dir, "mapping.pkl"), "wb"))









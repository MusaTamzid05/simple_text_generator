from keras.models import load_model
import os
import pickle

class Generator:

    def __init__(self, train_dir_path):
        self.model = load_model(os.path.join(train_dir_path, "model.h5"))
        self.mapping = pickle.load(open(os.path.join(train_dir_path, "mapping.pkl"), "rb"))



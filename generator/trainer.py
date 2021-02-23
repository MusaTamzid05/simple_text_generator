import os
from generator.preprocessor import Preprocessor
from generator.util import write_file

class Trainer:

    def __init__(self, text_path, save_dir):

        if os.path.exists(save_dir) == False:
            os.mkdir(save_dir)
        preprocessor = Preprocessor(text_path = text_path)
        training_sequnces = preprocessor.run()

        self.train_data_path = os.path.join(save_dir, "training_seq.txt")
        write_file(path = self.train_data_path, lines = training_sequnces)

    def train(self):
        pass




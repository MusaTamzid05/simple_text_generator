import os
from generator.preprocessor import Preprocessor

class Trainer:

    def __init__(self, text_path, save_dir):

        if os.path.exists(save_dir) == False:
            os.mkdir(save_dir)
        preprocessor = Preprocessor(text_path = text_path)
        preprocessor.run()

    def train(self):
        pass




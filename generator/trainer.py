import os

class Trainer:

    def __init__(self, text_path, save_dir):

        if os.path.exists(save_dir) == False:
            os.mkdir(save_dir)



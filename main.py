from generator.trainer import Trainer
from generator.generator import Generator

def train():
    trainer = Trainer(text_path = "song.txt", save_dir = "results")
    trainer.train(epochs = 5)

def generate_example():
    generator = Generator(train_dir_path = "results")


def main():
    generate_example()



if __name__:
    main()

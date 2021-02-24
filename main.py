from generator.trainer import Trainer


def main():

    trainer = Trainer(text_path = "song.txt", save_dir = "results")
    trainer.train(epochs = 5)


if __name__:
    main()

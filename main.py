from generator.trainer import Trainer


def main():

    trainer = Trainer(text_path = "song.txt", save_dir = "results")
    trainer.train()


if __name__:
    main()

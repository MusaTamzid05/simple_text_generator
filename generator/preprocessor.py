
class Preprocessor:

    def __init__(self, text_path):
        self.text_path = text_path

    def run(self):

        raw_text = self._load_doc()
        sequences, vocab_size = self._make_sequence(raw_text = raw_text)
        print(vocab_size)



    def _make_sequence(self,  raw_text):

        lines = raw_text.split("\n")
        chars = sorted(list(set(raw_text)))
        mapping = {}

        for i, char in enumerate(chars):
            if char not in mapping.keys() and char != "\n":
                mapping[char] = i

        sequences = list()

        for line in lines:
            encoded_seq = [mapping[char] for char in line]
            sequences.append(encoded_seq)

        return sequences, len(mapping)


    def _load_doc(self):

        with open(self.text_path) as f:
            text = f.read()

        return text




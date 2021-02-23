

def write_file(path, lines):

    with open(path, "w") as f:
        f.write("\n".join(lines))


def load_file(path):

    with open(path) as f:
        text = f.read()

    return text




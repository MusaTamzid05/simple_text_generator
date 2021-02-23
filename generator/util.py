

def write_file(path, lines):

    with open(path, "w") as f:
        f.write("\n".join(lines))

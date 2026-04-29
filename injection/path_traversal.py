def read_file(filename):
    with open(f"./files/{filename}", "r") as f:
        return f.read()
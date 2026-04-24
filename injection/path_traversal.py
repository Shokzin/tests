def read_file(filename):
    # ❌ Vulnerável
    with open(f"./files/{filename}", "r") as f:
        return f.read()
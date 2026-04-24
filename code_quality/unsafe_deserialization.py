import pickle

def load_data(data):
    # ❌ Vulnerável
    return pickle.loads(data)
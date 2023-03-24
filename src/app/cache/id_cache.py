import pickle


class IdCache:

    def __init__(self, filename):
        self.cache: set = set()
        self.filename: str = filename

    def exists(self, key: str):
        return self.cache.__contains__(key)

    def set(self, key):
        self.cache.add(key)
        with open(self.filename, "a") as file:
            file.write(key + "\n")
            file.close()

    def load_values(self):
        try:
            with open(self.filename, "r") as file:
                self.cache = set(line.strip() for line in file)
                file.close()
        except EOFError:
            print("Cache has never been initialized before. Ignoring content.")

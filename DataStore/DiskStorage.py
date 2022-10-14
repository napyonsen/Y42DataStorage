
class DiskStorageCls:
    def __init__(self):
        pass

    def Save (self, data):
        with open("y42.data", "w") as f:
            f.write(data)

    def Load (self):
        with open("y42.data", "r") as f:
            data = f.read()
            if not data:
                return "{}"
            return data
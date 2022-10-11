import json

class JsonFormatterCls:
    def __init__(self):
        pass

    def Decode(self, data):
        return json.loads(data)

    def Encode(self, data):
        return json.dumps(data)
        


if __name__ == "__main__":
    data = '{"name": "John", "age": 31, "city": "New York"}'
    formatter = JsonFormatterCls()
    print(formatter.Decode(data))

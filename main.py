import json
import pickle

class Airplane():
    def __init__(self, passangers, fuel):
        self.passangers = passangers
        self.fuel = fuel
    #picklepart
    def pickle_dump(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def pickle_load(self, filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
    #jsonpart

    def to_dict(self):
        return {
            "passangers": self.passangers,
            "fuel": self.fuel
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["passangers"], data["fuel"])

    def json_dump(self, filename):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def json_load(cls, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        return cls.from_dict(data)


    def __str__(self):
        return f"passangers: {self.passangers}, fuel: {self.fuel}"


airplane = Airplane(100, 200)

airplane.pickle_dump("airplane.pickle")
airplane.json_dump("airplane.json")

unpack_airplane_pickle = Airplane.pickle_load("airplane.pickle")
print(unpack_airplane_pickle)

unpack_airplane_json = Airplane.json_load("airplane.json")
print(unpack_airplane_json)







class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.data = "Data of the Singleton instance"

    def get_data(self):
        return self.data

    def __str__(self):
        return f"{self.data}"


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1)
print(singleton2)

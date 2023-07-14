

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list and \
                all(isinstance(ele, str) for ele in attrs):
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
            }
        else:
            return self.__dict__
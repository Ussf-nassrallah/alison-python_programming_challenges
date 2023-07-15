import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("youssef", 23)

def encode_user(obj):
    if isinstance(obj, User):
        return {
            "name": obj.name,
            "age": obj.age,
            obj.__class__.__name__: True
        }
    else:
        raise TypeError("Object of type User is not JSON serializable")

userJSON = json.dumps(user, default=encode_user)
print(userJSON)
print("----")


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


# user = json.loads(userJSON)
# print(user)

# can't access to Ex:user.name
# print(user.name)

user = json.loads(userJSON, object_hook=decode_user)
print(user)

# Now we can accesses to EX:user.name by decode_user function
print(user.name)
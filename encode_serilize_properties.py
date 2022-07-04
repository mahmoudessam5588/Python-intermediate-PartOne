import json
from json import JSONEncoder
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
user = User(name='max',age=27)           
# def encode_user(obj):
#         if isinstance(obj,serlizie_props):
#             return{'name':obj.name,'age':obj.age,obj.__class__.__name__:True}
#         else:
#             raise TypeError('object is not serilible')

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o,User):
            return{'name':o.name,'age':o.age,o.__class__.__name__:True}
        return JSONEncoder.default(self,o)
        
def decode_user(dct):
        if User.__name__ in dct:
            return User(name=dct['name'],age=dct['age'])
        return dct   
              
#userjson = json.dumps(seri,cls=serlizie_props)
#encode
userjson = UserEncoder().encode(user)
print(userjson)
#decode
user=json.loads(userjson,object_hook=decode_user)
print(user.name)
print(user.age)            
import json

class Person():
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def __str__(self):
        return 'name = ' + self.name + ' age = ' + str(self.age)
    def toJson(self):
         return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
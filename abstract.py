from abc import ABC, abstractmethod

# more like an interface which the object inheriting must comply with
class Obj1 (ABC):

    @abstractmethod
    def set_attr(self, *args) :
      pass

    @abstractmethod
    def get_attr(self) -> str :
      pass


class Obj_unknown :

  def __init__(self, *args):
    self.set_attr(*args)

  def set_attr(self, *args) :
    for i,x in enumerate(args) :
      setattr(self, f"param_{i}", x)

  def get_attr(self) -> str :
    i = 0
    output = []
    while True :
      param_i = f"param_{i}"
      if not hasattr(self, param_i):
        break
      output.append(str(getattr(self, param_i)))
      i += 1
    return ", ".join(output)



if __name__ == "__main__" :
  Obj1.register(Obj_unknown)
  obj = Obj_unknown(*[1,2,3])
  print(obj.get_attr())



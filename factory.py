

class Obj1 :

  def __init__(self, attr1, attr2):
    self.attr1 = attr1
    self.attr2 = attr2



class Obj1Factory(Obj1):

    @classmethod
    def get_obj(cls, id_: str) -> Obj1:
      assert(id_ in ["01337", "00000", "11111"])
      return cls(id_, "ok")




if __name__ == "__main__" :
  obj = Obj1Factory.get_obj("11111")
  print(f"{obj.attr1} {obj.attr2}")

  # raise error here
  obj2 = Obj1Factory.get_obj("11112")



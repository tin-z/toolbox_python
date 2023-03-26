

class Prop() :

  def __init__(self, value):
    self._value = value

  def __checker(self, new_value) :
    assert new_value >= 0, "Negative value"

  def get_value(self):
    return self._value

  def set_value(self, value):
    self.__checker(value)
    self._value = value

  def del_value(self) :
    self._value = 1337

  value = property(get_value, set_value, del_value, "Value properties")



if __name__ == "__main__":
  p = Prop(1)
  print(p.value)
  p.value = 10
  print(p.value)
  del p.value
  print(p.value)


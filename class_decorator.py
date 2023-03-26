

def simple_trace(cls):

  class wrapper :
    def __init__(self, *args, **kwargs):
      print("{}.__init__({}, {})".format(cls.__name__, args, kwargs))
      self.inner_class = cls(*args, **kwargs)

    # def __getattribute__(self, a): # no otherwise when we have recursion fail on self.__dict__ call
    #                                # we trick this by calling object.__getattribute__
    def __getattr__(self, a):
      print("{}.__getattribute__({})".format(cls.__name__, a))
      return object.__getattribute__(self.inner_class, a)

    def __setattr__(self, a, v):
      if a == "inner_class" :
        self.__dict__[a] = v
      else :
        print("{}.__setattr__({}, {})".format(cls.__name__, a, v))
        object.__setattr__(self.inner_class, a, v)

  return wrapper


@simple_trace
class simple_class :
  def __init__(self, a):
    self.a = a

  def func(self, a):
    return self.a * a



if __name__ == "__main__" :
  obj = simple_class(2)
  print(obj.a)
  obj.a = 10
  print(obj.func(3))






# notes "PA" unimi course:
#
# - metaclasses add code to be run at class creation time and not at instance creation time
# - Metaclasses are subclasses of `type` class (is not a object class)
#    * `type` is a class that generates user-defined classes.
#    * Metaclasses are subclasses of the `type` class.
#    * Class objects are instances of the `type` class, or a subclass thereof.
#    * Instance objects are generated from a class.
#
# - Coding Metaclasses
#    * must inherit from `type`
#    * must override __new__ (__init__ and __call__ operators also)
#    * class taking the metaclass should declare the argument 'metaclass`
#


# Example: add tracer to each method of a class without declaring for each line the decorator


from types import FunctionType


def simple_trace(F, print_counter=False):
  calls = 0
  def wrapper(*args, **kwargs):
    nonlocal calls
    calls += 1
    print(
      "Calling {}({}, {})".format(
      F.__name__, args, kwargs, calls) + 
      (" #{}".format(calls) if print_counter else "")
    )
    return F(*args, **kwargs)
  return wrapper


def decorate_metaclass(print_counter=False):
  class MetaTrace(type):
    def __new__(cls, classname, supers, classdict):
      for k, v in classdict.items():
        if type(v) is FunctionType :
          classdict[k] = simple_trace(v, print_counter=print_counter)
      return type.__new__(cls, classname, supers, classdict)

  return MetaTrace



class simple_class(metaclass=decorate_metaclass(True)):
  def __init__(self, a):
    self.a = a

  def func1(self, b) :
    return self.a + b

  def func2(self, b) :
    return self.a * b



if __name__ == "__main__" :
  obj = simple_class(10)
  rets = obj.func1(2)
  rets_2 = obj.func2(2)
  print(rets, rets_2)
  print()
  for x in range(3) :
    obj.func2(x)
  obj_2 = simple_class(10)
  obj_2.func2(1)




global_module_storage = {
  "default" : 1
}


class A(object):
  
  def __init__(self):
    pass

  def __getattribute__(self, a):
    return object.__getattribute__(self, a)

  def __getattr__(self, a):
    """
      object.__getattribute__ didn't find the attribute,
      then return global module storage memory
    """
    if a in global_module_storage :
      return global_module_storage[a]
    else :
      raise AttributeError(a)

  def __delattr__(self, attr):
    try :
      object.__delattr__(self, a)
    except AttributeError as ex:
      if a not in global_module_storage :
        raise ex
      del global_module_storage[a]
    return

  def __setattr__(self, a, v):
    if a in self.__dict__ :
      object.__setattr__(self, a, v)
    else :
      if a not in global_module_storage :
        global_module_storage.update({a:v})
      else :
        global_module_storage[a] = v


class B(A) :
  pass

class C(A) :
  pass



if __name__ == "__main__" :
  b = B()
  c = C()
  b.new_object = 1337
  print(c.new_object)





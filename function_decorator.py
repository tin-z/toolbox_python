

def simple_trace(F):
  def wrapper(*args, **kwargs):
    print("Calling {}({}, {})".format(
      F.__name__, args, kwargs
    ))
    return F(*args, **kwargs)
  return wrapper


@simple_trace
def simple_method(a, b, is_negative=False):
  if is_negative :
    return a - b
  return a + b



if __name__ == "__main__" :
  a = 10
  b = 2
  rets = simple_method(a, b)
  rets_negative = simple_method(a, b, is_negative=True)
  print(rets, rets_negative)


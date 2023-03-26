

def set_greater(x):
  assert x>1, "Value should be greater than 1"

  def test_1(a):
    return a > x

  def test_2(a):
    return a % x == 0

  def test_3(a):
    return (a ** x) % (x - 1) == 0

  tests = [test_1, test_2, test_3]

  def test(a):
    return \
      sum([1 if test_i(a) else 0 for test_i in tests]) == len(tests)

  return test


if __name__ == "__main__" :
  checker_10 = set_greater(10)
  checker_2 = set_greater(2)
  print(checker_10(42))
  print(checker_2(42))





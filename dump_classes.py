import sys
import inspect

inc = 8
space_inc = " " * inc


class Node :
  print_attributes = False

  def __init__(self, ID, name, module, isclass=True):
    self.ID = ID
    self._module = module
    self._name = name
    self.isclass = isclass
    self.visited = True
    self.print_attributes = Node.print_attributes

    self.to_str = self.__str1
    if not self.isclass :
      self.to_str = self.__str2
      self.nodes = []
      self.visited = False
    elif self.print_attributes :
      self.to_str = self.__str3


  def __str1(self):
    def to_print(spaces) :
      return spaces + "\"{}\" :[]".format(self._name)
    return to_print

  def __str2(self):
    def to_print(spaces) :
      return \
        spaces + "\"{}\"".format(self._name) + ": {\n" + \
        ",\n".join( [ x.to_str()(spaces + space_inc) for x in self.nodes ]) + \
        "\n" + spaces + "}"
    return to_print

  def __str3(self):
    def to_print(spaces) :
      return \
        spaces + "\"{}\"".format(self._name) + ": [\n" + \
        ",\n".join(["{}{}\"{}\"".format(spaces, space_inc, k) for k,v in self._module.__dict__.items()]) +\
        "\n" + spaces + "]"
    return to_print

  def add_edge(self, next_node):
    self.nodes.append(next_node)




def list_classes(print_attributes=False):
  Node.print_attributes = print_attributes
  output = {}
  to_visit = [ 
    Node(id(mod), mod.__name__, mod, False) for mod in list(sys.modules.values())
  ]

  root = to_visit[::]
  i = 0

  while True :
    if i >= len(to_visit):
      break

    mod_node = to_visit[i]
    i = i + 1

    if mod_node.visited :
      continue

    mod_id = mod_node.ID
    mod_name = mod_node._name
    module = mod_node._module
    
    if mod_id not in output :
      output.update({mod_id:mod_node})

    for name, obj in inspect.getmembers(module):
      tmp_mod_id = id(obj)

      if inspect.ismodule(obj):
        if tmp_mod_id not in output :
          output.update({tmp_mod_id: Node(tmp_mod_id, name, obj, False)})
        tmp_mod_node = output[tmp_mod_id]
        mod_node.add_edge(tmp_mod_node)
        to_visit.append(mod_node)

      elif inspect.isclass(obj):
        if tmp_mod_id not in output :
          output.update({tmp_mod_id: Node(tmp_mod_id, name, obj)})
        tmp_mod_node = output[tmp_mod_id]
        mod_node.add_edge(tmp_mod_node)

      else :
        # ignore
        pass

    mod_node.visited = True

  return (root, output)


def list_classes_str(print_attributes=False):
  root, output = list_classes(print_attributes=print_attributes)
  output_str = [x.to_str()("  ") for x in root]
  return \
    "{\n" +\
    ",\n".join(output_str) + \
    "\n}"

 
if __name__ == "__main__" :
  print(list_classes_str())


class Miranda:
  def __init__(self, name, age):
    self.name = 'USS Robert Scott'
    self.hull = 10000

  def myfunc(self):
    print("These are the voyages of the " + self.name)

p1 = Miranda("USS Robert Scott", 10000)
p1.myfunc()
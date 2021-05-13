'''
2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
  a.
      class Person:
          """
          Make the class with composition.
          """
      class Arm:
          """
          Make the class with composition.
          """
'''
class Person:
    def __init__(self):
        arm1 = Arm('System command 1')
        arm2 = Arm('System command 2')
        self.arms = [arm1, arm2]

class Arm:
    def __init__(self, command):
        self.command = command


'''
b.
      class CellPhone:
          """
          Make the class with aggregation
          """
      class Screen:
          """
          Make the class with aggregation
          """
'''
class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, size):
        self.size = size


if __name__ == '__main__':
    print('______Composition______')
    person = Person()
    for arm in person.arms:
        print(arm.command)

    print('_____Aggregation______')
    scr = Screen('6.3')
    ph = CellPhone(scr)
    print(ph.screen.size)

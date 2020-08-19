
class Card():
  
  def __init__(self, suite, face, value):
    self.suite = suite
    self.face = face  
    self.value = value
  #used to get my format of (queen of hearts) for example
  def display_card(self):
    return "{} of {}.".format(self.face , self.suite)

# Propery = Decorator used to define a method as a property (it can be accessed like an attribute)
#           Benefit: Add additional logic when read, write or delete attributes
#           Gives you getter, setter, and deleter methods

class Rectangle:
  def __init__(self, width, height):
    self._width = width  # The underscore tells us that these are protected
    self._height = height
  
  @property
  def width(self):
    return f"{self._width:.1f} cm"

  @property
  def height(self):
    return f"{self._height:.1f} cm"
  
  # The setter methods are used to set the values of protected attributes
  @width.setter
  def width(self, new_width):
    if new_width > 0:
      self._width = new_width
    else:
      print("Width must be greater than zero")

  @height.setter
  def height(self, new_height):
    if new_height > 0:
      self._height = new_height
    else:
      print("Height must be greater than zero")

  # Deleter methods can be used to delete
  @width.deleter
  def width(self):
    del self._width
    print("Width has been deleted")
  
  @height.deleter
  def height(self):
    del self._height
    print("Height has been deleted")



rectangle = Rectangle(3, 4)

rectangle.width = 5 # By assigning it a value, we are accessing the setter method
rectangle.height = 6

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height
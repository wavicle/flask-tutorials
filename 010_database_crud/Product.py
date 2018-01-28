class Product:
  id = None
  name = ''
  availableQty = 0

  def __init__ (self, id, name, qty):
    self.id = id
    self.name = name
    self.availableQty = qty

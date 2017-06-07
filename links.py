class Link:

  def __init__(self, col):
    self.left = self
    self.right = self
    self.up = self
    self.down = self
    self.col = col

  def setLeft(self, node):
    left = self.left
    node.left = left
    node.right = self
    left.right = node
    self.left = node

  def setRight(self, node):
    right = self.right
    node.left = self
    node.right = right

    right.left = node
    self.right = node

  def setDown(self, node):
    down = self.down
    down.up = node
    self.down = node

    node.up = self
    node.down = down

  def setUp(self, node):
    up = self.up
    up.down = node
    self.up = node

    node.up = up
    node.down = self
  
  def removeFromRow(self):
    # print "removing %s"%(self.label)
    self.left.right = self.right
    self.right.left = self.left

  def removeFromColumn(self):
    # print "Unlinking %s"%(self.col.label)
    self.up.down = self.down
    self.down.up = self.up
  
  def resetInColumn(self):
    # print "Linking %s"%(self.col.label)
    self.up.down = self
    self.down.up = self


  def resetInRow(self):
    # print "Resetting %s"%(self.label)
    self.left.right = self
    self.right.left = self

    # self.col.length += 1

class Column(Link):

  def __init__(self, label):
    Link.__init__(self, self)
    self.label = label
    self.length = 0

  def addRow(self):
    row = Link(self)
    self.setUp(row)
    self.length += 1
    return row
  
  def setLeft(self, node):
    Link.setLeft(self, node)
  
  def setRight(self, node):
    Link.setRight(self, node)
    return self.right
  
  def getFirstRow(self):
    return self.down

  def __nonzero__(self):
    return self.right != self

  def __str__(self):
    return "Column %s has length %d"%(self.label, self.length)
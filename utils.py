def findShortestColumn(root):
  c = root.right
  length = float('infinity')
  target = None
  while c != root:
    if c.length < length:
      length = c.length
      target = c
    c = c.right
  return target


def inspectCols(root):
  remainingCols = []

  i = root.right

  while i != root:
    remainingCols.append(i.label)
    remainingCols.append(i.length)
    i = i.right
  
  print 'Remaining cols'
  print remainingCols


def checkLinks(root, label):
  c = root.right

  while c != root and c.label != label:
    c = c.right

  print c

  r = c.getFirstRow()
  linkedCols = set()
  while r != c:
    col = r.right
    while col != r:
      linkedCols.add(col.col.label)
      col = col.right
    r = r.down
  print 'Cols linked to %s with length %d'%(c.label, c.length)
  print linkedCols

    


def lengths(root):
  c = root.right

  while c != root:
    print c
    c = c.right


def cover(column):
  # Remove column from header list.
  column.removeFromRow()
  rNode = column.down

  while rNode != column:
    cNode = rNode.right
    
    while cNode != rNode:
      cNode.removeFromColumn()
      cNode.col.length -= 1
      cNode = cNode.right
    rNode = rNode.down
  



def uncover(column):
  rNode = column.up
  
  while rNode != column:
    cNode = rNode.left 

    while cNode != rNode:
      cNode.resetInColumn()
      cNode.col.length += 1
      cNode = cNode.left
    rNode = rNode.up
  
  column.resetInRow()

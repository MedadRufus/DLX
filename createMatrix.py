from utils import inspectCols
from links import Link, Column

matrix = {
  'A': [1, 4, 7],
  'B': [1, 4],
  'C': [4, 5, 7],
  'D': [3, 5, 6],
  'E': [2, 3, 6, 7],
  'F': [2, 7]
}

matrix = {
  'A': [1, 2],
  'B': [5, 6],
  'C': [4, 5],
  'D': [1, 2, 3],
  'E': [3, 4],
  'F': [4, 5],
  'G': [1, 3, 5, 6]
}

def createMatrix(m):

  root = Column('root')

  maxNum = 0
  minNum = float('infinity')

  for c in m.values():
    if max(c) > maxNum:
      maxNum = max(c)
    if min(c) < minNum:
      minNum = min(c)
  
  leftNodes = {}

  node = root
  for c in m:

    node = node.setRight(Column(c))
    for i in m[c]:
      row = node.addRow()

      if i in leftNodes:
        # print 'Appending %s from column %s to column %s'%(i, leftNodes[i].col.label, node.col.label)
        leftNodes[i].setRight(row)

      leftNodes[i] = row

  return root
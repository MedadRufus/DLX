from links import Link, Column
from utils import checkLinks, cover, uncover, lengths, inspectCols, findShortestColumn
from createMatrix import createMatrix

matrix = {
  'A': [2, 4],
  'B': [3, 5],
  'C': [1, 3],
  'D': [2, 4, 6],
  'E': [1, 6],
  'F': [1, 3],
  'G': [2, 5, 6]
}


# matrix = {
#   'A': [1, 2],
#   'B': [1, 4],
#   'C': [4, 6],
#   'D': [2, 3, 4],
#   'E': [3, 5]
# }

# matrix = {
#   'A': [1, 4, 7],
#   'B': [1, 4],
#   'C': [4, 5, 7],
#   'D': [3, 5, 6],
#   'E': [2, 3, 6, 7],
#   'F': [2, 7]
# }


# matrix = {
#   'A': [1, 2],
#   'B': [5, 6],
#   'C': [4, 5],
#   'D': [1, 2, 3],
#   'E': [3, 4],
#   'F': [4, 5],
#   'G': [1, 3, 5, 6]
# }

# matrix = {
#   'A': [1, 2],
#   'B': [5, 6],
#   'C': [4, 5],
#   'D': [1, 2, 3],
#   'E': [6],
#   'F': [4, 5],
#   'G': [1, 3, 5, 6]
# }

# matrix = {
#   'A': [1],
#   'B': [3],
#   'C': [3, 4],
#   'D': [2, 4]
# }

def DLX(matrix):



  root = createMatrix(matrix)

  def search(k, solution):
    # inspectCols(root)
    
    if root.right == root:
      print 'Solution found!'
      for i in solution:
        print i.col.label
      return True
    # Find shortest column
    target = findShortestColumn(root)
    row = target.getFirstRow()
    cover(target)

    while row != target:
      newSolution = row
      col = row.right

      while col != row:
        cover(col.col)
        col = col.right

      search(k + 1, solution + [newSolution])
      target = row.col
      col = row.left

      while col != row:
        uncover(col.col)
        col = col.left

      row = row.down

    uncover(target)

    return solution


  return search(0, [])


  
solution = DLX(matrix)

print 'Result: '
for i in solution:
  print i.col.label
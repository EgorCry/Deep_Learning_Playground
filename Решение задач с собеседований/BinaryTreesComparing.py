"""
Given the node object:

Node:
  val: <int>,
  left: <Node> or null,
  right: <Node> or null
write a function compare(a, b) which compares the two trees defined by Nodes a and b and returns true if they are equal
in structure and in value and false otherwise.

Examples:

1       1
| \     | \
2  3    2  3
=> true

1       1
| \     | \
3  3    2  3
=> false (values not the same 2 != 3)

1       1
| \     |
2  3    2
        |
        3
=> false (structure not the same)
"""


# return True if the two binary trees rooted and a and b are equal in value and structure
# return False otherwise
def compare(a, b):
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return a.val == b.val and compare(a.left, b.left) and compare(a.right, b.right)

    return False


class Node:
  def __init__(self, val, left, right):
    self.val = val
    self.left = left
    self.right = right

a_node = Node(1, None, None)
b_node = Node(1, None, None)
c_node = Node(2, None, None)


results1 = compare(a_node, b_node)
print(results1)
results2 = compare(c_node, b_node)
print(results2)

from typing import Any, Callable, List
from treelib import Node, Tree


def visit(node: 'BinaryTree'):
    print(node.value, end= " ")



class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value

    def __str__(self):
        return str(self.value)


    def __repr__(self):
         return str(self.value)


    def is_leaf(self):
        if self.left_child is None or self.right_child is None:
            return True
        return False


    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)


    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)


    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)

        if self.right_child:
             self.right_child.traverse_in_order(visit)



    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_post_order(visit)

        if self.right_child:
            self.right_child.traverse_post_order(visit)

        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)

        if self.right_child:
             self.right_child.traverse_pre_order(visit)







class BinaryTree:
    root: BinaryNode

    def __init__(self, root):
        self.root = BinaryNode(root)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)


def top_line(tree: BinaryTree) -> List[BinaryNode]:
    l1 = []
    t = tree.root
    t2 = tree.root
    l1.append(t)

    while t.left_child != None:
        l1.append(t.left_child)
        t = t.left_child


    l1 = l1[::-1]

    while t2.right_child != None:
        l1.append(t2.right_child)
        t2 = t2.right_child
    return l1






tree = BinaryTree(10)
tree.root.add_left_child(9)
tree.root.add_right_child(2)
tree.root.left_child.add_right_child(3)
tree.root.left_child.add_left_child(1)
tree.root.right_child.add_right_child(6)
tree.root.right_child.add_left_child(4)

print(top_line(tree))
# tree.traverse_in_order(visit)

tree2 = BinaryTree(100)
tree2.root.add_left_child(10)
tree2.root.add_right_child(45)
tree2.root.right_child.add_right_child(70)
tree2.root.left_child.add_left_child(20)
tree2.root.left_child.add_right_child(8)
tree2.root.left_child.left_child.add_left_child(25)
tree2.root.left_child.left_child.left_child.add_left_child(40)
tree2.root.right_child.right_child.add_right_child(24)
tree2.root.right_child.right_child.add_left_child(81)
tree2.root.right_child.add_left_child(55)
tree2.root.left_child.left_child.left_child.add_right_child(31)
tree2.root.left_child.left_child.add_right_child(15)
tree2.root.left_child.left_child.right_child.add_left_child(17)
tree2.root.left_child.left_child.right_child.add_right_child(21)

print(top_line(tree2))


# new_tree = Tree()
# new_tree.create_node("10", "harry")  # root node
# new_tree.create_node("9", "jane", parent="harry")
# new_tree.create_node("2", "bill", parent="harry")
# new_tree.create_node("4",  parent="bill")
# new_tree.create_node("6",  parent="bill")
# new_tree.create_node("3",  parent="jane")
# new_tree.create_node("1",  parent="jane")
# new_tree.show()


# tree.root.traverse_in_order(visit)

# print(tree.root.value)

assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True




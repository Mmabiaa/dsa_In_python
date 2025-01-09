class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    """Insert a new value into the binary search tree."""
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    """Search for a value in the binary search tree."""
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)

def delete(root, value):
    """Delete a node with the given value."""
    if root is None:
        return root
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        min_larger_node = find_min(root.right)
        root.value = min_larger_node.value
        root.right = delete(root.right, min_larger_node.value)
    return root

def find_min(root):
    """Find the node with the smallest value."""
    while root.left:
        root = root.left
    return root

def find_max(root):
    """Find the node with the largest value."""
    while root.right:
        root = root.right
    return root

def inorder_traversal(root):
    """Perform inorder traversal of the BST."""
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right) if root else []

# Example usage
root = insert(None, 50)
insert(root, 30)
insert(root, 70)
insert(root, 20)
insert(root, 40)
insert(root, 60)
insert(root, 80)

print("Inorder Traversal:", inorder_traversal(root))
print("Search 40:", search(root, 40))
root = delete(root, 20)
print("After Deletion (Inorder Traversal):", inorder_traversal(root))
print("FindMin:", find_min(root).value)
print("FindMax:", find_max(root).value)
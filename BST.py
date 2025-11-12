class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

# ---------- MAIN ----------
tree = BST()
root = None

# Insert elements
for key in [50, 30, 70, 20, 40, 60, 80]:
    root = tree.insert(root, key)

print("Inorder traversal after insertion:")
tree.inorder(root)
print()

# Search for elements
print("\nSearching for 40:")
print("Found!" if tree.search(root, 40) else "Not found!")

print("Searching for 100:")
print("Found!" if tree.search(root, 100) else "Not found!")

# Delete elements
print("\nDeleting 20 (leaf node)...")
root = tree.delete(root, 20)

print("Deleting 30 (one child)...")
root = tree.delete(root, 30)

print("Deleting 50 (two children)...")
root = tree.delete(root, 50)

# Display final tree
print("\nInorder traversal after deletions:")
tree.inorder(root)
print()

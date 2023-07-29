class BinaryTreeNode:
    def __init__(node,data):
        node.left=None
        node.right=None
        node.data=data
        
def Insert(root,newval):
    if root is None:
        root=BinaryTreeNode(newval)
        return root
    if newval < root.data:
        root.left=Insert(root.left,newval)
    else:
        root.right=Insert(root.right,newval)
    return root

def PreOrder(root):
    if root is None:
        return
    print(root.data,end=" ")
    PreOrder(root.left)
    PreOrder(root.right)
def InOrder(root):
    if root is None:
        return
    InOrder(root.left)
    print(root.data,end=" ")
    InOrder(root.right)
def PostOrder(root):
    if root is None:
        return
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.data,end=" ")
    
n=int(input("Enter no.of nodes needed for binary tree:"))
print("Enter the root node of the tree:")
root=Insert(None,int(input()))
for i in range(n-1):
    l=int(input("Enter the values of remaining nodes:"))
    Insert(root,l)

print("The PreOrder traversal of Binary tree is :")
PreOrder(root)
print("\nThe Inorder traversal of the Binary tree is:")
InOrder(root)
print("\nThe PostOrder traversal of the tree is:")
PostOrder(root)

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,new_node):
        if self.root is None:#creating the root node
            self.root=new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node 
                        return
                    else:
                        temp=temp.right
    def inorder(self,node):
        if node is None:
            return
        else:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)
btree=BST()
btree.insert(Node(10))
btree.insert(Node(5))
btree.insert(Node(20))
btree.insert(Node(45))
btree.insert(Node(3))
btree.inorder(btree.root)



class TreeNode:

    def __init__(self,key,value,leftChild=None,rightChild=None,parent=None):
        self.key = key
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent
    
    def getValue(self):
        return self.value
    
    def getKey(self):
        return self.key
    
    def isLeaf(self):
        return True if self.leftChild == None and self.rightChild == None else False



class binarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0
    
    # put method to insert a new node based on key value pair
    def put(self,key,value):

        if self.root:
            return self._put(key,value,self.root)
        else:
            self.root = TreeNode(key,value,parent=self.root)
            self.size += 1
    
    """ 
        helper function for put() which does the heavy lifting of
        comparing the key to each node and inserting it as per BST.
    """
    def _put(self,key,value,currentNode):
        
        # create the node when a loc is found to assign parent
        # t = TreeNode(key,value)
        # if key is less than root then we go left
        if key < currentNode.key:

            if currentNode.leftChild:
                return self._put(key,value,currentNode.leftChild,)
            else:
                currentNode.leftChild = TreeNode(key,value,parent=currentNode)
                self.size += 1

        # need to handle duplicate key insertion
        # Here we willl update the value in case of duplicate key insertion

        elif key == currentNode.key:
            currentNode.value = value

        # else we go right
        else:

            if currentNode.rightChild:
                return self._put(key,value,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,value,parent=currentNode)
                self.size += 1
    

    # get: method to get the value assigned to a particular key
    def get(self,key):

        if self.root:
            # we use the helper method to search for the key
            res = self._get(key,self.root)   
            
            if res:
                return res.value
            else:
                return None

        else:
            return None
    
    """"
        Helper function to aid get() method in:
        - comparing the key of each node with the one searched for
        - returning the node once found
    """
    def _get(self,key,currentNode):
        
        if key == currentNode.key:
            return currentNode
        
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        
        else:
            return self._get(key,currentNode.rightChild)
    
    
    def delete(self,key):

        if self.size > 1:
            nodeToRemove = self._get(key,self.root)

            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -=1
            else:
                raise KeyError('Key Not found!')

        
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -=1
        
        else:
            raise KeyError('Key not found!')

        
    def remove(self,currentNode):
        
        # node to delete is a leaf
        if currentNode.isLeaf():
            # delete the reference to this child in the parent
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

    
    



# Global method to print the tree in inorder fashion
def inOrder(root):

    if root:

        if root.leftChild:
            inOrder(root.leftChild)
        
        print(root.value)

        if root.rightChild:
            inOrder(root.rightChild)




t = binarySearchTree()

t.put(70,70)

t.put(23,23)

t.put(93,93)

t.put(24,24)

t.put(14,27)

t.put(100,100)

print('Size of tree is ' , t.size)


inOrder(t.root)

#print(t.get(24))

t.delete(100)
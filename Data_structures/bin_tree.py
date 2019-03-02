
class TreeNode:

    def __init__(self,key,value,leftChild=None,rightChild=None):
        self.key = key
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
    
    def getValue(self):
        return self.value
    
    def getKey(self):
        return self.key



class binarySearchTree:

    def __init__(self):
        self.root = None
    
    # put method to insert a new node based on key value pair
    def put(self,key,value):

        if self.root:
            return self._put(key,value,self.root)
        else:
            self.root = TreeNode(key,value)
    
    """ 
        helper function for put() which does the heavy lifting of
        comparing the key to each node and inserting it as per BST.
    """
    def _put(self,key,value,currentNode):
        
        t = TreeNode(key,value)
        # if key is less than root then we go left
        if key < currentNode.key:

            if currentNode.leftChild:
                return self._put(key,value,currentNode.leftChild)
            else:
                currentNode.leftChild = t

        # need to handle duplicate key insertion
        # Here we willl update the value in case of duplicate key insertion

        elif key == currentNode.key:
            currentNode.value = value

        # else we go right
        else:

            if currentNode.rightChild:
                return self._put(key,value,currentNode.rightChild)
            else:
                currentNode.rightChild = t
    
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
    

    def _get(self,key,currentNode):
        
        if key == currentNode.key:
            return currentNode
        
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        
        else:
            return self._get(key,currentNode.rightChild)
    

        


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
    
inOrder(t.root)

print(t.get(24))
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:38:51 2019

@author: Christo Lagali
"""

class binaryTree(object):
    
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self,newNode):
        
        if self.leftChild == None:
            self.leftChild = binaryTree(newNode)
        else:
            t = binaryTree(newNode)
            while self.leftChild != None:
                self = self.leftChild

            t.leftChild = self.leftChild
            self.leftChild = t
    
    
    def insertRight(self,newNode):
        
        if self.rightChild == None:
            self.rightChild = binaryTree(newNode)
        else:
            t = binaryTree(newNode)

            while self.rightChild != None:
                self = self.rightChild

            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    

    def showPreOrder(self,root):
        
        if root:
            print(root.key)
            self.showPreOrder(root.leftChild)
            self.showPreOrder(root.rightChild)
    

    def showPreOrder2(self):
        
        print(self.key)

        if self.leftChild:
            self.leftChild.showPreOrder2()
        
        if self.rightChild:
            self.rightChild.showPreOrder2()


    def showInorder(self,root):

        if root:
            self.showInorder(root.leftChild)
            print(root.key)
            self.showInorder(root.rightChild)
    
    def showPostOrder(self,root):

        if root:
            self.showPostOrder(root.leftChild)
            self.showPostOrder(root.rightChild)
            print(root.key)

    

r = binaryTree('a')

r.insertLeft('b')

r.insertLeft('c')

r.insertRight('d')

r.insertRight('e')

print('Preorder')
r.showPreOrder(r)

print('Inorder')
r.showInorder(r)

print('Postorder')
r.showPostOrder(r)

print('Preorder2')
r.showPreOrder2()
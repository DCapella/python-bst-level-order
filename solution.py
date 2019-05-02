########################
# !!! SOLUTION CODE !!!#
########################

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
            #Write your code here
            nodes = [root]
            i = 0
            while True:
              try:
                node = nodes[i]

                if node.left: nodes.append(node.left)
                if node.right: nodes.append(node.right)

                i += 1
              except:
                break

            for n in nodes:
              print(n.data, end=" ")

T=int(input())

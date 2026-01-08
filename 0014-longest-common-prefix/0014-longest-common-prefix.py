class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Tree:
    def __init__(self,data=None):
        self.root = Node()
        if data:
            self.add_node(data)

    
    def add_node(self,data):
        current_node = self.root

        for idx, i in enumerate(data):
            if i not in current_node.children.keys():
                current_node.children[i] = Node()

            current_node = current_node.children[i]
        
        current_node.is_end = True
        


    def longest_Prefix(self):
        current_node = self.root
        lcp=""

        while len(current_node.children) == 1:
            if current_node.is_end:
                break
            # Get the only child's character and node
            char = list(current_node.children.keys())[0]
            current_node = current_node.children[char]
            lcp += char
    
        return lcp


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = Tree()
        for s in strs:
            t.add_node(s)

        return t.longest_Prefix()


        


                    

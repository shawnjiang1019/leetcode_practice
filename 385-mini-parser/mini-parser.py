# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:

    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[":
            return NestedInteger(int(s))
        
        stack = []
        stack.append(NestedInteger())

        cur_int = ""
        for i in range(1, len(s)):
            if s[i] == '[':
                stack.append(NestedInteger())
        
            elif s[i] == "]":
                if cur_int:
                    stack[-1].add(NestedInteger(int(cur_int)))
                    cur_int = ""
                
                if len(stack) > 1:
                    completed = stack.pop()
                    stack[-1].add(completed)
                    
            elif s[i] == ',':
                if cur_int:
                    stack[-1].add(NestedInteger(int(cur_int)))
                    cur_int = ""
            
            elif s[i] == '-' or s[i].isdigit():
                cur_int += s[i]
                
        return stack[0]


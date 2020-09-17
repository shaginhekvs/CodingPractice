'''
Leetcode Problem number 687. 
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

'''
class Solution:
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max_path = 0;
        if(root is None or (root.left is None and root.right is None )):
            pass
        else:
            self.find_max_path(root)
        
        return self.max_path
    
    def set_max_value(self,new_val)-> None:
        self.max_path = new_val

    def find_max_path(self, root: TreeNode) -> int:
        '''
        finds longest path of 1 value and updates the overall maximum value. 
        return : current node's maximum matching value
        '''
        if(root is None or (root.left is None and root.right is None )):
            return 0    
        
        cur_length=0
        left_is_same = False
        left_max_path = 0
        right_max_path = 0
        
        if(root.left):
            left_max_path = self.find_max_path(root.left)
            if(root.left.val == root.val ):
                cur_length += 1 + left_max_path;
                left_is_same = True
            else:
                cur_length = 0;
        
        if(root.right):
            right_max_path = self.find_max_path(root.right)
            if(root.right.val == root.val and left_is_same):
                self.set_max_value(max(self.max_path, cur_length + 1 + right_max_path))
            if(root.right.val == root.val):
                cur_length = max(1 +  right_max_path, cur_length);
        
        self.set_max_value(max(self.max_path,cur_length))
        
        return cur_length
            
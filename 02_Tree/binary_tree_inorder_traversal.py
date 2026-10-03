# Problem No.94
# https://leetcode.com/problems/binary-tree-inorder-traversal


# Solution 1:


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []
        self.inor(root, ans)
        return ans

    def inor(self, root, ans) -> list[int]:
        if root == None:
            return
        self.inor(root.left, ans)
        ans.append(root.val)
        self.inor(root.right, ans)


# Solution 2


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        res = []

        while root or st:
            while root:
                st.append(root)
                root = root.left

            root = st.pop()
            res.append(root.val)
            root = root.right

        return res

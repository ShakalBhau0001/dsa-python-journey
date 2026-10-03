# Problem No.144
# https://leetcode.com/problems/binary-tree-preorder-traversal


# Solution 1:


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []
        self.preor(root, ans)
        return ans

    def preor(self, root, ans) -> list[int]:
        if root == None:
            return
        ans.append(root.val)
        self.preor(root.left, ans)
        self.preor(root.right, ans)


# Solution 2:


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        res = []

        while root or st:
            while root:
                st.append(root)
                res.append(root.val)
                root = root.left

            root = st.pop()
            root = root.right

        return res

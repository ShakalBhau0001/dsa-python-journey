# Problem No.145
# https://leetcode.com/problems/binary-tree-postorder-traversal


# Solution 1:


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []
        self.postor(root, ans)
        return ans

    def postor(self, root, ans) -> list[int]:
        if root == None:
            return
        self.postor(root.left, ans)
        self.postor(root.right, ans)
        ans.append(root.val)


# Solution 2:


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        res = []

        if not root:
            return res

        st.append(root)

        while st:
            root = st.pop()
            res.append(root.val)

            if root.left:
                st.append(root.left)

            if root.right:
                st.append(root.right)

        return res[::-1]

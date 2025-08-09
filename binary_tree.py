class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if value == node.data:
            return node, parent, True
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
            return obj

    def show_tree(self, node):
        """DFS (Depth First Search) increasing order"""
        if node is None:
            return
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_tree_reverse(self, node):
        """DFS (Depth First Search) decreasing order"""
        if node is None:
            return
        self.show_tree_reverse(node.right)
        print(node.data)
        self.show_tree_reverse(node.left)

    def show_tree_bfs(self, node):
        """BFS (Breadth First Search)"""
        if node is None:
            return
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=' ')
                if x.left:
                    vn.append(x.left)
                if x.right:
                    vn.append(x.right)
            print()
            v = vn

    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)
        if not fl_find:
            return None

        if s.left is None and s.right is None:  # Leaf node
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:  # One descendant
            self.__del_one_child(s, p)
        else:  # Two descendants
            sr, pr = self.__find_min(s.right, s) # Find the minimum in the right subtrees
            s.data = sr.data
            self.__del_one_child(sr, pr)  # Delete the minimum node found


tree = Tree()
# ls = [5, 3, 7, 2, 4, 6, 8]
ls = [20, 5, 24, 2, 16, 11, 18]
for i in ls:
    tree.append(Node(i))

# tree.show_tree(tree.root)
# print("  ")
# tree.show_tree_reverse(tree.root)
# print("  ")
# tree.show_tree_bfs(tree.root)
tree.del_node(5)
tree.show_tree_bfs(tree.root)

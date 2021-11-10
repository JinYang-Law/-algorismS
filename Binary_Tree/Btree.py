
""" 先建立二叉树节点，有一个data数据域，left，right 两个指针域  """
""" 链式存储 构建 Btree """


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self):
        self.root = Node()

    # 递归实现
    ## 先序遍历
    def preorder_travel(self, node):
        if node is None:
            return
        print(node.data)
        self.preorder_travel(node.left)
        self.preorder_travel(node.right)


    def midorder_travel(self, node):
        if node is None:
            return
        self.midorder_travel(node.left)
        print(node.data)
        self.midorder_travel(node.right)


    def postorder_travel(self, node):
        if node is None:
            return
        self.postorder_travel(node.left)
        self.postorder_travel(node.right)
        print(node.data)


    # 迭代实现










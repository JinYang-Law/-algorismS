class Node(object):
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SingleLink(object):
    def __init__(self):
        self._head = Node()

    ## 判断链表是否为空
    def is_empty(self):
        return True if self._head is None

    """ 链表的长度， 遍历节点，统计指针指向None 时的个数"""

    def length(self):
        # 初始指针指向head
        cur = self._head
        count = 0
        # 指针指向None 表示到达尾部
        while cur.next is not None:
            count += 1
            cur = cur.next

        return count

    ## 构建链表
    # add在链表前端添加元素:O(1)
    def add(self, item):
        ## 实例化结点
        node = Node(item)

        ## 新结点指向原头部结点, 并将头部结点改为新结点
        node.next = self._head
        self._head = node

    # append在链表尾部添加元素: O(n)
    def append(self, item):
        ## 实例化结点
        node = Node(item)

        ## 两种情况
        # 如果链表为空，则直接将头部结点改为新结点 O（1）
        cur = self._head
        if self._head is None:
            self._head = node
        else:
            ## 迭代
            # 不是空链表，则找到尾部，将尾部next结点指向新结点
            while cur is not None:
                cur = cur.next
            cur.next = node

    # 指定位置插入元素 插入的复杂度 平均O(n)
    def insert(self, index, item):
        ## 实例化结点
        node = Node(item)

        ## 指定位置在第一个元素之前，在头部插入
        if index = 0:
            self.add(item)
        elif self.length() <= index:
            self.append(item)
        else:
            cur = self._head
            for i in range(1, index):
                cur = cur.next

            next_node = cur.next
            node.next = next_node
            cur.next = node

    # 删除结点
    def remove(self, target):
        cur = self._head
        pre = None
        while cur is not None:
            ### 找到指定元素
            if cur.item == target:
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next

    # 查找链表中的元素
    def search(self):
        return item in self.items()

    # 遍历结点 函数生成器
    def items(self):
        cur = self._head
        ## 循环遍历
        while cur is not None:
            ## 返回生成器
            yield cur.item
            ## 指针下移
            cur = cur.next


def main():
    link = SingleLink()
    link.add(23)
    link.add(35)
    link.add(25)
    link.insert(2, 2222)
    print(link._head.next.next.item)
    link.remove(35)

    print(list(link.items()))


if __name__ == '__main__':
    main()

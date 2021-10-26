## 定义类
class Search:
    def __init__(self, arr=None, item=None):
        self.arr = arr
        self.item = item

    def sort(self, arr=None):
        arr = self.arr if arr == None else arr
        return sorted(arr)

    def search_left(self, arr, target):
        if len(arr) == 0: return -1
        ### (left, right]
        left = 0
        right = len(arr)

        while left < right:
            mid = (right + left) // 2
            if arr[mid] == target:
                right = mid
            elif arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid

        return left


def main():
    test_arr = [2, 3, 12, 12, 45, 123, 453]

    ## 生成一个实例， 就是一个对象；
    ## 对象有公共属性和私有属性，以及可调用方法
    test_object = Search()
    # sorted_arr = test_object.sorted()
    print(test_object.search_left(test_arr, 12))


if __name__ == '__main__':
    main()

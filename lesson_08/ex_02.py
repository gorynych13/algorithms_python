import collections


class My_node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def show(self):
        print(f"Name - {self.value}, Left - {self.left}, Right - {self.right}")


def search(tree, number, path=''):
    if tree.value == number:
        return f'{path}'
    if number < tree.value and tree.left != None:
        return search(tree.left, number, path=f'{path}0')
    if number > tree.value and tree.right != None:
        return search(tree.right, number, path=f'{path}1')
    return f'Число {number} отсутствует'


def convert_to_tree(counter, i):
    l = (counter.most_common())
    l.reverse()
    print(l)
    c = My_node(f"node{i}")
    c.left = My_node(l[0][0])
    c.right = My_node(l[1][0])
    d = collections.OrderedDict(counter.most_common())
    d.pop(l[0][0])
    d.pop(l[1][0])
    d.update({c: l[0][1] + l[1][1]})
    counter = collections.Counter(d)
    print(c.show())
    print(c.left.show())
    print(c.right.show())
    return counter


s = 'beep boop beer'
count = collections.Counter(s)
n = len(list(count))

for i in range(n - 1):
    count = convert_to_tree(count, i)
    # print(count)

lst = list(count)
root = lst[0]
print(root)
print(root.show())
print(root.left.show())




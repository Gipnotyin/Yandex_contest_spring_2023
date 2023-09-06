from math import comb

class Node:
    def __init__(self):
        self.value = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()
        self.count = 0

    def insert(self, numbers):
        node = self.root
        for num in numbers:
            if num not in node.children:
                node.children[num] = Node()
            node = node.children[num]
            node.value += 1

    def non_recursive_traversal(self):
        stack = [child for child in self.root.children.values() if child.value > 1]
        while stack:
            node = stack.pop()
            self.count += comb(node.value, 2)
            stack.extend(child for child in node.children.values() if child.value > 1)

        return self.count


if __name__ == "__main__":
    trie = Trie()
    with open("input.txt", "r", encoding="utf-8") as file:
        n = int(file.readline())
        for _ in range(n):
            size = int(file.readline())
            trie.insert(list(map(int, file.readline().split())))

    # Нерекурсивный обход дерева и вывод префиксов и их значений
    print(trie.non_recursive_traversal())

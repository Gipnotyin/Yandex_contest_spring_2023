if __name__ == '__main__':
    with open("input.txt", "r", encoding='utf-8') as file:

        stack_a = [[0, 0]]
        stack_b = [[0, 0]]
        stack = [0]

        n = int(file.readline())
        results = [0] * n
        languages = ['0'] + file.readline().split()

        l_a = l_b = 0
        index = 0

        s = list(map(int, file.readline().split()))

        for i in range(1, 2 * (n + 1) - 1):
            if stack[index] == s[i]:
                if languages[s[i]] == 'A':
                    counter = index - stack_a[l_a - 1][1] - 1
                    l_a -= 1
                    stack_a.pop()
                else:
                    counter = index - stack_b[l_b - 1][1] - 1
                    l_b -= 1
                    stack_b.pop()
                results[s[i] - 1] = counter
                stack.pop()
                index -= 1
            else:
                stack.append(s[i])
                index += 1

                if languages[s[i]] == 'A':
                    l_a += 1
                    stack_a.append([s[i], index])
                else:
                    l_b += 1
                    stack_b.append([s[i], index])

        print(*results)

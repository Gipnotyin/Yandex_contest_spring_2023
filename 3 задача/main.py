if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as file:
        n, m, q = map(int, file.readline().split())

        names = dict()
        s = file.readline().split()

        for i in range(m):
            names[s[i]] = [i, -(10**9) - 1, 10**9 + 1]

        table = [list(map(int, file.readline().split())) for _ in range(n)]

        for _ in range(q):
            person, symb, val = file.readline().split()
            val = int(val)

            if symb == ">":
                if names[person][1] < val:
                    names[person][1] = val
            else:
                if names[person][2] > val:
                    names[person][2] = val

        res = 0

        for i in range(n):
            if all(names[s[j]][1] < table[i][j] < names[s[j]][2] for j in range(m)):
                res += sum(table[i])


        print(res)
from collections import defaultdict

N, M, Q = map(int, input().split())

A = defaultdict(int)
B = defaultdict(int)

uni = 0

for num in map(int, input().split()):
    A[num] += 1
for num in map(int, input().split()):
    B[num] += 1

for key, val in A.items():
    uni += abs(B.get(key, 0) - val)

for key, val in B.items():
    if A.get(key, 0) == 0:
        uni += val

result = []
for q in range(Q):
    t, player, card = input().split()
    t, card = int(t), int(card)
    razn = abs(A.get(card, 0) - B.get(card, 0))
    if t == 1:
        if player == 'A':
            A[card] += 1
        else:
            B[card] += 1
    else:
        if player == 'A':
            A[card] -= 1
            if A[card] == 0:
                del A[card]
        else:
            B[card] -= 1
            if B[card] == 0:
                del B[card]
    diff = abs(A.get(card, 0) - B.get(card, 0))
    uni += diff - razn
    result.append(uni)


print(' '.join(map(str, result)))

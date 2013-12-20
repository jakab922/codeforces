n = int(raw_input().strip())
zero = map(int, raw_input().strip().split(' '))
one = map(int, raw_input().strip().split(' '))
two = map(int, raw_input().strip().split(' '))

if n == 1:
    print max(zero[0], one[0])
    exit()

stack = [(zero[0], 0)]
index = 1

while index < n:
    nhas = [0, 0]
    while stack:
        value, has = stack.pop()
        if value + one[index] > nhas[1]:  # first
            nhas[1] = value + one[index]
        if has == 0 and value - zero[index - 1] + one[index - 1] + zero[index] > nhas[0]:
            nhas[0] = value - zero[index - 1] + one[index - 1] + zero[index]
        if has == 1 and value - one[index - 1] + two[index - 1] + zero[index] > nhas[0]:
            nhas[0] = value - one[index - 1] + two[index - 1] + zero[index]
    stack = [(nhas[0], 0), (nhas[1], 1)]
    index += 1


print max(stack[0][0], stack[1][0])

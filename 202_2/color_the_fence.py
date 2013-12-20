v = int(raw_input().strip())
costs = map(int, raw_input().strip().split(' '))

min_cost = min(costs)
if v < min_cost:
    print "-1"
    exit()

filler = -1

for i in xrange(8, -1, -1):
    if costs[i] == min_cost:
        filler = i + 1
        break

res = [filler for _ in xrange(v / min_cost)]
rl = len(res)
v -= rl * min_cost

for i in xrange(rl):
    for j in xrange(8, -1, -1):
        if v - costs[j] + costs[res[i] - 1] >= 0 and j + 1 > res[i]:
            v += costs[res[i] - 1] - costs[j]
            res[i] = j + 1
            break

print "".join(map(str, res))

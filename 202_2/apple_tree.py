n = int(raw_input().strip())
ais = map(int, raw_input().strip().split(' '))


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b
    return a

tree = [[] for _ in xrange(n)]
leaf_count = [-1 for _ in xrange(n)]

for _ in xrange(n - 1):
    fr, to = map(int, raw_input().strip().split(' '))
    fr -= 1
    to -= 1
    tree[fr].append(to)

total = 0

for i in xrange(n - 1, -1, -1):
    if tree[i] == []:
        leaf_count[i] == 1
    else:
        children = tree[i]
        child_weights = [ais[child] for child in children]
        min_weight = min(child_weights)
        child_leafs = [leaf_count[child] for child in children]
        child_gcd = reduce(gcd, child_leafs, child_leafs[0])
        new_weight = (min_weight / child_gcd) * child_gcd
        leaf_count[i] = child_gcd * len(children)
        for child_weight in child_weights:
            total += (child_weight - new_weight)
        ais[i] = new_weight * len(children)

print total

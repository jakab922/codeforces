from math import floor

n = int(raw_input().strip())
ais = map(float, raw_input().strip().split(' '))


small_parts = sorted(map(lambda x: x - floor(x), ais))

bottom = []
top = []
half_free = 0
zero_free = 0

for el in small_parts:
    if el == 0.0:
        zero_free += 1
    elif el == 0.5:
        half_free += 1
    elif el < 0.5:
        bottom.append(el)
    elif el > 0.5:
        top.append(el)

free = zero_free + half_free

lt = len(top)
lb = len(bottom)
mi = min(lb, lt)
ma = max(lb, lt) + free

total = 0.5 * half_free

if mi == lb:
    total += sum(bottom)
    for i in xrange(min(lt, lb + free)):
        total += 1.0 - top[lt - 1 - i]
    if i != lt - 1:
        for j in xrange(i + 1, lt):
            total += top[lt - 1 - j]
else:
    total += sum(map(lambda x: 1.0 - x, top))
    for i in xrange(min(lb, lt + free)):
        total += bottom[i]
    if i != lb - 1:
        for j in xrange(i + 1, lb):
            total += 1.0 - bottom[j]

print "%.3f" % total

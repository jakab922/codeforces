from math import floor

n = int(raw_input().strip())
ais = map(float, raw_input().strip().split(' '))


small_parts = sorted(map(lambda x: x - floor(x), ais))

bottom = []
top = []
free = 0

while free < 2 * n and small_parts[free] == 0.0:
    free += 1

bottom = small_parts[free:]
cl = len(bottom)
for i in xrange(1, cl):
    bottom[i] += bottom[i - 1]
top = small_parts[free:]
top = map(lambda x: 1.0 - x, top)
for i in xrange(1, cl):
    top[cl - 1 - i] += top[cl - i]

half = cl / 2
mi = float(cl)
for i in xrange(cl):
    if
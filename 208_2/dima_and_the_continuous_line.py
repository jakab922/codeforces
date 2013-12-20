n = int(raw_input().strip())
xis = map(int, raw_input().strip().split(' '))

if n < 3:
    print "no"
    exit()

low, high = xis[:2]
curr = xis[1]

for xi in xis[2:]:
    if not (curr == high and xi > high or
            curr == low and xi < low or
            xi > low and xi < high):
        print "yes"
        exit()
    low, high = min(curr, xi), max(curr, xi)
    curr = xi
print "no"

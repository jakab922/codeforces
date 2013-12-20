n = int(raw_input().strip())
ppl = map(int, raw_input().strip().split(' '))

cache = [0, 0]

for person in ppl:
    if person == 25:
        cache[0] += 1
    elif person == 50:
        if cache[0] == 0:
            print "NO"
            exit()
        else:
            cache[0] -= 1
        cache[1] += 1
    elif person == 100:
        if cache[1] != 0 and cache[0] != 0:
            cache[0] -= 1
            cache[1] -= 1
        elif cache[0] > 2:
            cache[0] -= 3
        else:
            print "NO"
            exit()

print "YES"

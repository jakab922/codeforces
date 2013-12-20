n = int(raw_input().strip())
ais = map(int, raw_input().strip().split(' '))

sais = sum(ais)
res = sais / (n - 1)
if sais % (n - 1) != 0:
    res += 1
print res

n = int(raw_input().strip())
ais = map(int, raw_input().strip().split(' '))

zero_count = len(filter(lambda x: x == 0, ais))
five_count = len(filter(lambda x: x == 5, ais))

if five_count / 9 == 0:
    if zero_count == 0:
        ret = "-1"
    else:
        ret = "0"
else:
    ret = "5" * (five_count - (five_count % 9))
    if zero_count != 0:
        ret += "0" * zero_count
    else:
        ret = "-1"

print ret

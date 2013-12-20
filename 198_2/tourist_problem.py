# 2 * (n - 1) -szer megyunk at tetszoleges tavolsagparon
# egy szakaszon annyiszor megyunk at elotte_pontok * utana_pontok


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(raw_input().strip())
ais = sorted(map(int, raw_input().strip().split(' ')))

zero_part = sum(ais)
numerator = 0
for i in xrange(len(ais) - 1):
    numerator += (i + 1) * (n - i - 1) * (ais[i + 1] - ais[i])

numerator *= 2
numerator += sum(ais)  # the first step

g = gcd(n, numerator)
numerator /= g
denumerator = n / g
print numerator, denumerator

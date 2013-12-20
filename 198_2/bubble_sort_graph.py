# Ez a graf egy vonalgraf, ami esetleg szet van torve egy par helyen.
# Jelolje az osszefuggo reszek pontszamat a1, ..., ak. Vagyis k
# osszefuggo reszunk van. Ekkor sum_{i = 1}^{k}{ceil(ai/2)} a valasz

n = int(raw_input().strip())
perm = map(int, raw_input().strip().split(' '))


#!/usr/bin/env python3
"""X6 S6 x signed primitive-step interface, exhaustive finite check (stdlib)."""
from itertools import permutations, combinations
P = list(permutations(range(6)))
S3 = list(combinations(range(6), 3))
counts = {"total":0,"commuting":0,"noncommuting":0,"hidden":0}
def obs(z, subset):
    a = [z[i] for i in subset]
    m = min(a)
    return tuple(v-m for v in a)
for sigma in P:
    for i in range(6):
        for eps in (-1,1):
            counts["total"] += 1
            z = [0]*6
            z[sigma[i]] += eps
            z[i] -= eps
            if sigma[i] == i:
                counts["commuting"] += 1
                assert not any(z)
            else:
                counts["noncommuting"] += 1
                assert sum(v!=0 for v in z)==2
                assert sum(abs(v) for v in z)==2
                assert sum(v*v for v in z)==2
                hidden = sum(obs(z,S)==(0,0,0) for S in S3)
                assert hidden==4
                counts["hidden"] += hidden
assert len(P)==720 and len(S3)==20
assert counts=={"total":8640,"commuting":1440,
                "noncommuting":7200,"hidden":28800}
print(counts)

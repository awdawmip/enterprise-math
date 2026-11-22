#!/usr/bin/env python3
"""T6 universal cancellation of 5^3 and 5^4 denominator layers; exact profiles."""
from collections import defaultdict

P, CAP = 5, 2331


def get_items(level):
    return tuple((j, P**level*j - 1)
                 for j in range(1, CAP//(P**level) + 1) if j % P)


def count_dp(items):
    dp = [0]*(CAP+1)
    dp[0] = 1
    for _, w in items:
        for mass in range(w, CAP+1):
            dp[mass] += dp[mass-w]
    return sum(dp)


def enumerate_profiles(items):
    a = [0]*len(items)
    def rec(i,rem):
        if i == len(items):
            yield tuple(a)
            return
        w = items[i][1]
        for n in range(rem//w+1):
            a[i] = n
            yield from rec(i+1,rem - n*w)
        a[i] = 0
    return list(rec(0,CAP))


def sig(a,items,K):
    return tuple(sum(n*pow(pow(j,k,P**k),-1,P**k)
                     for (j,w),n in zip(items,a)) % (P**k)
                 for k in range(1,K+1))


def run():
    for level,expected in [(4,((5,2),(7,0))), (3,((5,133439),(125,5050),(1109,48),(1157,0)))]:
        items = get_items(level)
        profiles = enumerate_profiles(items)
        n = len(profiles)
        assert n == count_dp(items) == (7 if level==4 else 1157)
        for K,(unique,pairs) in enumerate(expected,1):
            fibers = defaultdict(int)
            for a in profiles:
                fibers[sig(a,items,K)] += 1
            assert len(fibers) == unique
            assert sum(v*(v-1)//2 for v in fibers.values()) == pairs
            print(f"5^{level}: K={K}, profiles={n}, signatures={unique}, pairs={pairs}")
        assert len(set(sig(a,items,len(expected)) for a in profiles)) == n
    print("PASS exact 5^3 and 5^4 mass-bounded cancellation")


if __name__ == "__main__":
    run()

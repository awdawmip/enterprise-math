#!/usr/bin/env python3
"""Exact T6 p=3^4+ cancellation via six full-moment precision constraints."""
from collections import defaultdict
P, CAP = 3, 2331
EXPECTED = {
    7: ((2,0),),
    6: ((3,4),(6,0)),
    5: ((3,606),(27,59),(58,2),(60,0)),
    4: ((3,4493146),(27,499779),(243,58265),
        (3372,2537),(5071,77),(5148,0))
}
TOTAL = {7:2,6:6,5:60,4:5148}


def items(v):
    return [(j,P**v*j-1) for j in range(1,CAP//P**v+1) if j%P]


def enumerate_profiles(it):
    vec=[0]*len(it)
    def rec(i,remaining):
        if i==len(it):
            yield tuple(vec)
            return
        w=it[i][1]
        for n in range(remaining//w+1):
            vec[i]=n
            yield from rec(i+1,remaining-n*w)
        vec[i]=0
    return list(rec(0,CAP))


def independent_dp(it):
    dp=[0]*(CAP+1)
    dp[0]=1
    for j,w in it:
        for m in range(w,CAP+1):
            dp[m]+=dp[m-w]
    return sum(dp)


def signature(a,it,K):
    return tuple(sum(n*pow(pow(j,k,P**k),-1,P**k)
                     for n,(j,w) in zip(a,it)) % P**k
                 for k in range(1,K+1))


def run():
    for v in (7,6,5,4):
        it=items(v)
        ps=enumerate_profiles(it)
        assert len(ps)==independent_dp(it)==TOTAL[v]
        for K,(expected_unique,expected_pairs) in enumerate(EXPECTED[v],1):
            counts=defaultdict(int)
            for a in ps:counts[signature(a,it,K)]+=1
            assert len(counts)==expected_unique
            assert sum(n*(n-1)//2 for n in counts.values())==expected_pairs
            print(f"v={v},K={K}: {len(ps)} profiles, {len(counts)} signatures, {expected_pairs} pairs")
    print("PASS: all denominators divisible by 3^4 cancel for H0..H6")


if __name__ == "__main__":
    run()

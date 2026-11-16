"""Second, standalone certification of A389360(60) through (64).

No sharp period theorem or first-term wheel tables are imported.
For seed primes we construct a conservative periodic predicate from
binomial coefficients modulo adequate prime powers of the input.
At every survivor we test all remaining divisors by exact arithmetic.
"""
from math import comb


def highest_power(k, p):
    x=1
    while p*x<=k:
        x*=p
    return x


def valuation(n,p):
    a=0
    while not n%p:
        a+=1
        n//=p
    return a


def local_filters(k,p):
    # Above h=floor(log_p k) there are no baseline factors in k!.
    # Before this depth deleting one entry loses at most h counts.
    # A remaining multiple of p^(2h) already replenishes all of them.
    # An independent elementary upper limit to the exponent is v_p(k!).
    power=highest_power(k,p)**2
    alpha=sum(valuation(j,p) for j in range(1,k+1))
    q=min(power,p**alpha)
    start=((2*k+q-1)//q)*q
    allowed=[[] for _ in range(k)]
    for r in range(q):
        n=start+r
        s=valuation(comb(n,k),p)
        missing=[i for i in range(k) if valuation(n-i,p)>s]
        if not missing:
            for row in allowed:
                row.append(r)
        elif len(missing)==1:
            allowed[missing[0]].append(r)
    return q,allowed


def verify(k,best,offset,seeds,fast_primes):
    filters=[local_filters(k,p) for p in seeds]
    # Others are tested analytically via v_p(C(n,k)), or by straight division.
    extra=[local_filters(k,p) for p in fast_primes]
    valid=[{t:set(sets[t]) for t in range(k)} for q,sets in extra]
    direct=checked=0
    successes=[]
    for t in range(k):
        diffs=[(0,1)]
        for q,rows in filters:
            next_diffs=[]
            for a,m in diffs:
                inv=pow(m,-1,q)
                for b in rows[t]:
                    x=a+m*(((b-a)*inv)%q)
                    if x<=best:
                        next_diffs.append((x,m*q))
            diffs=next_diffs
        for a,m in diffs:
            lo=max(0,(2*k-a+m-1)//m)
            for n in range(a+m*lo,best+1,m):
                checked+=1
                if not all(n%q in valid[i][t] for i,(q,_) in enumerate(extra)):
                    continue
                direct+=1
                B=comb(n,k)
                if [i for i in range(k) if B%(n-i)]==[t]:
                    successes.append((n,t))
    print(k, checked, direct, successes,flush=True)
    assert successes==[(best,offset)]

if __name__=='__main__':
    verify(60,2117441088029,29,[2,3,5,59],[29,53,19,7,47,43,11])
    verify(61,569181900,50,[61,59,53,47],[29,3,5,7,19,2])
    verify(62,155275274056,8,[31,2,61,59],[29,53,3,5,7,19,47])
    verify(63,216949362182,35,[3,7,31,61],[59,29,53,19,47,5,43])
    verify(64,2600001558,22,[2,61,59,31],[7,3,29,53,19,47,5])

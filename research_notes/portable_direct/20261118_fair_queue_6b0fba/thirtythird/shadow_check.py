"""Exact floor, Farey-area, run, and cyclic endpoint checks for R005 §5."""
from fractions import Fraction as F
from collections import Counter
from itertools import product
from math import gcd, isqrt
import json


def ceil_sqrt(n):
    return isqrt(n-1)+1 if n else 0


def d(s, Q):
    return -((s*s % Q-2*s)//Q)


def farey(h):
    return sorted({F(a,b) for b in range(1,h+1) for a in range(b+1)})


def law(word, slopes):
    prefix = [0]
    for digit in word:
        prefix.append(prefix[-1]+digit)
    def width(v):
        z = [x-j*v for j,x in enumerate(prefix)]
        return max(F(0), 1+min(z)-max(z))
    heights = [width(v) for v in slopes]
    return sum((b-a)*(x+y)/2 for a,b,x,y in zip(slopes,slopes[1:],heights,heights[1:]))


def word_checks():
    results = []
    sample = {}
    for h in range(1,9):
        slopes = farey(h)
        values = {w:law(w, slopes) for w in product(range(2),repeat=h)}
        assert sum(values.values())==1
        totals = Counter()
        for word, prob in values.items():
            for A in (0,1):
                totals[h*A+sum(word)] += prob/2
        assert all(totals[j]==F(1 if j in (0,2*h) else 2,4*h) for j in range(2*h+1))
        assert values[(0,)*h]==values[(1,)*h]==F(1,2*h)
        tot = sum(p>0 for p in values.values())
        expected = 1+sum((h-j+1)*sum(gcd(a,j)==1 for a in range(1,j+1)) for j in range(1,h+1))
        assert tot==expected
        results.append(tot)
        if h==3:
            sample={''.join(map(str,k)):str(v) for k,v in values.items()}
        if h==4:
            assert values[(0,0,1,1)] == values[(1,1,0,0)] == 0
    return dict(support_counts_h1_to8=results, triples_conditional_A=sample)


def sorted_runs(q):
    Q=q*q
    last, length = None, 0
    out = [[], []]
    for s in range(1,Q):
        digit=d(s,Q)
        previous=(s-1)**2//Q
        assert digit==s*s//Q-previous+int((s-1)%q==0)
        if digit!=last:
            if last in (0,2):
                out[last//2].append(length)
            last, length = digit, 0
        length += 1
    if last in (0,2):
        out[last//2].append(length)
    return [sorted(r, reverse=True) for r in out]


def root_runs(q):
    Q=q*q
    # Zero digits are constant-floor plateaus, with a square plateau's first edge removed.
    zero=[]
    for n in range(Q):
        lo, hi = (ceil_sqrt(Q*j) for j in (n,n+1))
        length = min(Q,hi)-lo-1-int(isqrt(n)**2==n)
        if length>0:
            zero.append(length)
    # Two digits correspond in reverse to the function counting nonsquare thresholds.
    two=[]
    lo=0
    for n in range(2,Q+2):
        if isqrt(n)**2==n:
            continue
        hi=ceil_sqrt(Q*n)
        length=min(Q+1,hi)-max(1,lo)-1
        if length>0:
            two.append(length)
        lo=hi
    return [sorted(zero,reverse=True),sorted(two,reverse=True)]


def finite_runs():
    sample={}
    qs=[3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    for q in qs:
        observed, predicted=sorted_runs(q), root_runs(q)
        assert observed==predicted
        assert [r[0] for r in observed]==[q-2,ceil_sqrt(2*q*q)-2]
        count=sum(max(0,k-q+1) for k in observed[1])
        assert count==ceil_sqrt(2*q*q)-q-1
        if q in (7,31,97):
            sample[q]=dict(longest=[z[0] for z in observed], all_two_at_h_q=count)
    q=78553
    return dict(odd_primes_checked=qs, sample=sample, frozen_q_78553_arithmetic_only={
        'longest_zero':q-2,'longest_two':ceil_sqrt(2*q*q)-2,'all_two_at_h_q':ceil_sqrt(2*q*q)-q-1})


def frozen_input():
    q=78553
    Q=q*q
    assert all(q % d for d in range(2,isqrt(q)+1))
    P85=101412319996363309069
    smax=458*Q-ceil_sqrt(P85*q)
    half=Q//2
    def total(t):
        return t*t//Q + 1 + (t-1)//q if t else 0
    assert smax==3669621088 and 2*half<Q and 4*smax<3*Q
    zeros=half-total(half)
    twos=total(smax)-total(half)-(smax-half)
    starts=list(range((q//2+1)*q,smax,q))
    for s in starts:
        assert [d(t,Q) for t in range(s-1,s+3)]==[1,2,2,1]
    counts=[zeros,smax-zeros-twos,twos]
    assert counts==[1542604176,2071674840,55342072]
    assert len(starts)==7439
    return dict(q=q,Q=Q,smax=smax,deficits_0_1_2=counts,number_double_runs=len(starts),
                isolated_twos=twos-2*len(starts),first_pair=starts[0],last_pair=starts[-1],
                square_checks_on_every_pair=len(starts))


def cyc(q, window):
    Q=q*q
    prefix=[0]
    for j in range(1,Q+window+1):
        # multiply by Q, with mean correction (2j-1)/Q + 1/q.
        prefix.append(prefix[-1]+Q*d(j,Q)-(2*j-1)-q)
    values=Counter()
    cov_sum=0
    for x in range(Q):
        val=prefix[x+window]-prefix[x]
        b=(x+window-1)//q-(x-1)//q-window//q
        endpoint=(x*x%Q)-((x+window)**2%Q)+Q*b-q*(window%q)
        assert val==endpoint
        values[val]+=1
        cov_sum+=((x*x%Q)-((x+window)**2%Q))*b
    assert sum(v*n for v,n in values.items())==0
    if window%Q==0:
        assert values=={0:Q}
    elif window%q==0:
        assert values=={q*j:q-abs(j) for j in range(-q+1,q)}
    r=window%q
    covariance=F(cov_sum,Q*Q)
    expected_cov=-F(r*r%q,q**3)-F(q-1,2*q*q) if r else F(0)
    assert covariance==expected_cov
    var=F(sum(v*v*n for v,n in values.items()),Q**3)
    if window%q==0 and window%Q!=0:
        assert var==F(Q-1,6*Q)
    return var


def periodic_checks():
    total=0
    rows=[]
    for q in (3,5,7,11,13,17):
        Q=q*q
        classes={r:[] for r in range(q)}
        for h in range(1,2*Q+1):
            variance=cyc(q,h)
            total+=1
            if h<Q:
                classes[h%q].append(variance)
            if q in (7,17) and h in (1,q,Q):
                rows.append([q,h,str(variance)])
        for r in range(1,q):
            theta=F(r,q)
            local=sum((a*a%q-(a+r)**2%q)**2 for a in range(q))
            predicted=(theta*(1-theta)+(1-F(1,Q))*(1-F(4,q))/6
                       -F(2*(r*r%q),q**4)+F(local,q**5))
            assert sum(classes[r])/q==predicted
    return dict(all_windows_up_to_twice_period=total, sample_exact_variances=rows)


if __name__ == '__main__':
    print(json.dumps(dict(mechanical=word_checks(),runs=finite_runs(),cyclic=periodic_checks(), frozen=frozen_input()),
                     ensure_ascii=False,sort_keys=True,indent=2))

"""PREFIX-470 exact native X6 positive-BRC pattern-gate certificate.

Alphabet x, a,u, b,v, c,w, d,y, e,z: five signed axis pairs.
Only x is gated; x at time zero is permitted, all subsequent x need suffix PATTERN.
This code performs exact integer enumeration and independent bounded word enumeration.
No floating-point arithmetic or physical-time/phase model is used.
"""
from collections import defaultdict
from math import comb

LETTERS = ('x', 'a', 'u', 'b', 'v', 'c', 'w', 'd', 'y', 'e', 'z')
ZERO = (0,) * 11

def auto_next(pattern, q, ch):
    if ch == 'x':
        return 0
    word = pattern[:q] + ch
    return max(j for j in range(len(pattern) + 1) if word.endswith(pattern[:j]))

def base_key(counts):
    plus = [counts[1 + 2*i] for i in range(5)]
    minus = [counts[2 + 2*i] for i in range(5)]
    y = tuple(u-v for u, v in zip(plus, minus))
    p = [min(u, v) for u, v in zip(plus, minus)]
    return (counts[0],) + y + (p[1] + 2*p[3] + p[4], p[2] + p[4])

def iter_counts(n, d):
    if d == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for c in iter_counts(n-a, d-1):
                yield (a,) + c

def rational_coeff(n, pattern_length, observations=True):
    # Exact integer binomial convolution for the proposed rational series.
    k = pattern_length
    num = {0:1}
    if observations:
        for fact in [{0:1,2:2},{0:1,1:2,2:1}]:
            out = defaultdict(int)
            for j,a in num.items():
                for m,b in fact.items(): out[j+m]+=a*b
            num = out
    out = defaultdict(int)
    for j,a in num.items():
        for m,b in {0:1,1:1,k+1:-1}.items():out[j+m]+=a*b
    dim = 8 if observations else 10
    total = 0
    for power, coefficient in out.items():
        for period in range(max(0, (n-power)//(k+1))+1):
            remain = n-power-(k+1)*period
            if remain >= 0:
                total += coefficient * comb(remain+dim-1,dim-1)
    return total

def path_coeff(n,k,previous):
    if n==0:return 1
    if n==1:return 11
    return 10*previous[n-1] + (previous[n-k-1] if n>=k+1 else 0)

def native_run(pattern, max_length, check_full_parikh=False, check_literal=False, print_rows=False):
    assert pattern and 'x' not in pattern
    assert all(ch in LETTERS[1:] for ch in pattern)
    k = len(pattern)
    d = {(ZERO,0):1}
    path_totals=[]
    Bs=[]
    for n in range(max_length+1):
        byq = [{c for c,q in d if q==t} for t in range(k+1)]
        parikh = set().union(*byq)
        seen_base = [{base_key(c) for c in counts} for counts in byq]
        B = len(set().union(*seen_base))
        Bs.append(B)
        F = sum(map(len,seen_base))
        path_count=sum(d.values())
        assert B==rational_coeff(n,k), (pattern,n,B,rational_coeff(n,k))
        assert len(parikh)==rational_coeff(n,k,False)
        assert path_count==path_coeff(n,k,path_totals)
        # Tested words use at most one signed direction per axis.
        required={ch:pattern.count(ch) for ch in set(pattern)}
        if check_full_parikh:
            full = set(iter_counts(n,11))
            valid={c for c in full if all(c[LETTERS.index(ch)] >= count*max(c[0]-1,0)
                                          for ch,count in required.items())}
            assert parikh==valid and len(full)==comb(n+10,10)
        if check_literal:
            if n<=5:
                literal=defaultdict(int)
                def words(depth,c,q):
                    if depth==n:
                        literal[(c,q)]+=1
                        return
                    for i,ch in enumerate(LETTERS):
                        if ch=='x' and depth>0 and q!=k:continue
                        new=list(c);new[i]+=1
                        words(depth+1,tuple(new),auto_next(pattern,q,ch))
                words(0,ZERO,0)
                assert dict(literal)==d
        if pattern=='aba':
            Q = [len(v) for v in seen_base]
            def label(q,H):
                if H==0:return 0
                if H==1:return int(q==3)
                if H==2:return 0 if q in (0,1) else q-1
                return q
            N = [len({(base_key(c),label(q,H)) for c,q in d}) for H in range(4)]
            assert Q[0]==B-(0 if n==0 else 1 if n==1 else 4 if n==3 else 3)
            assert Q[1]==(Bs[n-1] if n>=1 else 0)
            assert Q[2]==(Bs[n-2] if n>=2 else 0)
            assert Q[3]==(Bs[n-3] if n>=3 else 0)
            assert N[0]==B
            assert N[1]==B+(Bs[n-3] if n>=3 else 0)
            assert N[2]==B+(Bs[n-2] if n>=2 else 0)+(Bs[n-3] if n>=3 else 0)
            assert N[3]==F
            if print_rows:
                print(f'n={n} paths={path_count} parikh={len(parikh)} B={B} Q={Q} F={F} N(H=0,1,2,>=3)={N}',flush=True)
        elif print_rows:
            print(f'pattern={pattern} n={n} paths={path_count} parikh={len(parikh)} B={B} F={F}',flush=True)
        if n<max_length:
            nxt=defaultdict(int)
            for (counts,q),weight in d.items():
                for j,ch in enumerate(LETTERS):
                    if ch=='x' and n>0 and q!=k:continue
                    c=list(counts);c[j]+=1
                    nxt[(tuple(c),auto_next(pattern,q,ch))]+=weight
            d=nxt
        path_totals.append(path_count)
    return Bs

if __name__=='__main__':
    print('CORE_PATTERN_aba',flush=True)
    native_run('aba',8,check_full_parikh=True,check_literal=True,print_rows=True)
    print('CROSS_PATTERN_monotone_sign_consistent',flush=True)
    for p in ('aaa','aab','abb','baa','ababa','auv'):
        # 'auv' mixes opposite signs of one axis and is out of scope.
        if p=='auv': continue
        native_run(p,6,check_full_parikh=True,check_literal=True)
        print(f'pattern={p} closed_base_series_coefficients=PASS n=0..6',flush=True)
    print('ALL_CHECKS_PASS')

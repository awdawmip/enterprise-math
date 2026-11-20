#!/usr/bin/env python3
"""PREFIX-971: exact parity-lifted quotient join for all seven gaps and resonance.

Scientific inputs match PREFIX-970's auxiliary named XOR observer. Only integer arithmetic;
full named histories and source slots retained, no native X6 or BRC transport assumed.
"""
from __future__ import annotations
import argparse
from bisect import bisect_left
from collections import Counter, defaultdict
from hashlib import sha256
from math import gcd
from statistics import median
from time import perf_counter
import json


def fibers(p):
    values = defaultdict(list)
    for i in range(p):
        for j in range(p):
            for s in (-1, 1):
                values[(1 << i) - s * (1 << j)].append((i, j, s))
    return {r: sorted((v, tuple(slots)) for v, slots in values.items() if v % 2 == r)
            for r in (0, 1)}


def ceildiv(a, b):
    assert b > 0
    return -((-a) // b)


def source_bits_ok(cslots, b, t):
    return [(i, j) for i, j, s in cslots
            if (((t * b + (1 << i)) >> j) & 1) == int(s == 1)]


def named_all(p, k, gaps=tuple(range(7))):
    assert p >= 4 and k >= 1 and k % 2 and k + 2 < (1 << (p - 1))
    assert all(0 <= m <= 6 for m in gaps)
    H = 1 << (p - 1); L = H + 1; U = 2 * H - 1
    f = fibers(p)
    numbers = {r: {v: slots for v, slots in f[r]} for r in (0, 1)}
    cache = {}
    out = {m: [] for m in gaps}
    counters = {m: Counter() for m in gaps}
    resonant_rs = {}
    for m in gaps:
        h = m // 2
        if m in (2, 4):
            rs = [c // k for c in numbers[0] | numbers[1]
                  if c % k == 0 and (k + 2) * (c // k) in numbers[0] | numbers[1]]
            resonant_rs[m] = sorted(set(rs))
        for t in range(1, 2 * k + 1):
            d = 2 * t - k * m
            st = counters[m]
            left = f[(1 - t) % 2]
            right = f[(1 - t - m) % 2]
            if d == 0:
                assert h in (1, 2) and t == k * h
                # For zero determinant: c=k*r, C=(k+2)*r and a=h*b+r.
                for r in resonant_rs[m]:
                    c = k * r; C = (k + 2) * r
                    cs = numbers[c % 2][c]; Cs = numbers[C % 2][C]
                    for b in range(L, U + 1, 2):
                        a = h * b + r
                        if not (L <= a <= U and a % 2 and a != b): continue
                        st['resonance_modulus_candidates'] += 1
                        ls = source_bits_ok(cs, b, t)
                        rsigned = source_bits_ok(Cs, b, t + m)
                        for i,j in ls:
                            for I,J in rsigned:
                                assert ((k*a) ^ (1<<j))-(1<<i) == t*b
                                assert (((k+2)*a) ^ (1<<J))-(1<<I) == (t+m)*b
                                out[m].append((a,b,t,t+m,i,j,I,J))
                continue
            g = gcd(k, t)
            assert g == gcd(k, d) and g % 2
            q = abs(d) // g
            modulus = 2 * q
            cache_key = (modulus, (1 - t - m) % 2)
            if cache_key not in cache:
                tab = defaultdict(list)
                for C, Cs in right: tab[C % modulus].append((C,Cs))
                cache[cache_key] = tab
            tab = cache[cache_key]
            inv = pow(k // g, -1, modulus)
            dl, dh = min(d*L, d*U), max(d*L, d*U)
            st['c_examined'] += len(left)
            for c,cs in left:
                if c % g: continue
                st['c_gcd_admissible'] += 1
                low = max(ceildiv((k+2)*c+dl,k), ceildiv((t+m)*c+dl,t))
                high = min(((k+2)*c+dh)//k, ((t+m)*c+dh)//t)
                if low > high: continue
                residue = ((((k+2)*c+d)//g)*inv) % modulus
                bucket = tab.get(residue, ())
                st['bucket_probes'] += len(bucket)
                start = bisect_left(bucket, (low,)); stop = bisect_left(bucket, (high+1,))
                for C,Cs in bucket[start:stop]:
                    st['interval_candidates'] += 1
                    N = k*C-(k+2)*c
                    assert (N-d) % (2*abs(d)) == 0
                    b = N//d
                    assert (m*b+C-c)%2 == 0
                    a = (m*b+C-c)//2
                    assert b%2 and a%2 and L<=b<=U and L<=a<=U
                    if a == b: continue
                    st['nondiagonal_candidates'] += 1
                    ls=source_bits_ok(cs,b,t)
                    rsigned=source_bits_ok(Cs,b,t+m)
                    for i,j in ls:
                        for I,J in rsigned:
                            assert ((k*a) ^ (1<<j))-(1<<i) == t*b
                            assert (((k+2)*a) ^ (1<<J))-(1<<I) == (t+m)*b
                            out[m].append((a,b,t,t+m,i,j,I,J))
        out[m].sort()
    return out, {m:dict(cnt) for m,cnt in counters.items()}, {
        'index_builds':len(cache),
        'index_entries':sum(len(v) for tab in cache.values() for v in tab.values()),
        'resonant_numeric_r': resonant_rs,
    }


def named_direct(p,k,m):
    H=1<<(p-1);L=H+1;U=2*H-1
    rows=Counter()
    for a in range(L,U+1,2):
        left=defaultdict(list);right=defaultdict(list)
        for i in range(p):
            for j in range(p):
                x=((k*a)^(1<<j))-(1<<i)
                y=(((k+2)*a)^(1<<j))-(1<<i)
                if x>0:left[x].append((i,j))
                if y>0:right[y].append((i,j))
        for x,ls in left.items():
            for y,rs in right.items():
                if m:
                    z=y-x
                    if z % m: continue
                    bs=(z//m,)
                else:
                    if y!=x:continue
                    bs=range(L,U+1,2)
                for b in bs:
                    if not(L<=b<=U and b%2 and b!=a and x%b==0):continue
                    t=x//b
                    if not(1<=t<=2*k):continue
                    for i,j in ls:
                        for I,J in rs:
                            rows[(a,b,t,t+m,i,j,I,J)]+=1
    return rows


def digest(rows):
    return sha256(''.join(','.join(map(str,row))+'\n' for row in rows).encode()).hexdigest()


def run(check=True, benchmark=False):
    small=[]
    if check:
        for p in range(4,8):
            H=1<<(p-1)
            for k in range(1,H-2,2):
                rows, _, _=named_all(p,k)
                for m in range(7):
                    direct=named_direct(p,k,m)
                    assert Counter(rows[m]) == direct, (p,k,m,len(rows[m]),sum(direct.values()))
                    small.append({'p':p,'k':k,'m':m,'named':len(rows[m]),'digest':digest(rows[m])})
        assert len(small)==392
    outs,counts,meta=named_all(19,21)
    res={'schema':'PREFIX971_R6_ALL_GAP_PARITY_LIFTED_JOIN_V1',
         'frozen_scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
         'model':'named-two-core-XOR-external-auxiliary',
         'small_cases':small,
         'Q19_k21':{'p':19,'k':21,'by_m':[
             {'m':m,'distinct_pairs':len({(a,b) for a,b,*_ in outs[m]}),
              'named_histories':len(outs[m]),'named_sha256':digest(outs[m]),**counts[m]}
             for m in range(7)], **meta},
         'scientific_status':'AUTHOR_PROOF_EXACT_INTEGER_CHECK_NOT_REVIEWED',
         'proof_scope':'nonzero determinant all seven gaps p>=4 and odd k with k+2<2^(p-1); resonance exact',}
    all_pairs={m:{(a,b) for a,b,*_ in outs[m]} for m in range(7)}
    union=set().union(*all_pairs.values())
    overlaps=[]
    for m in range(7):
        for n in range(m+1,7):
            for pair in sorted(all_pairs[m] & all_pairs[n]):
                overlaps.append({'gaps':[m,n], 'pair':list(pair)})
    res['Q19_k21']['total_named_histories']=sum(len(outs[m]) for m in range(7))
    res['Q19_k21']['union_distinct_pairs']=len(union)
    res['Q19_k21']['overlap_pairs']=overlaps
    assert res['Q19_k21']['total_named_histories']==8649
    assert len(union)==6203
    expected={0:(6,6),1:(442,614),2:(4724,6509),3:(839,1286),4:(190,231),5:(3,3),6:(0,0)}
    for row in res['Q19_k21']['by_m']:
        assert (row['distinct_pairs'],row['named_histories'])==expected[row['m']]
    assert overlaps==[{'gaps':[1,2], 'pair':[278529,290817]}]
    if benchmark:
        durations=[]
        for _ in range(6):
            t0=perf_counter();new,_,_=named_all(19,21)
            durations.append(perf_counter()-t0)
            assert new == outs
        res['benchmark']={'implementation':'CPython stdlib; full p19 all-seven-gap named recovery',
                          'runs':len(durations),'median_seconds':median(durations)}
    return res


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--benchmark',action='store_true')
    parser.add_argument('--output',default='PREFIX971_R6_EXACT_RESULTS.json')
    a=parser.parse_args()
    data=run(check=a.check,benchmark=a.benchmark)
    with open(a.output,'w',encoding='utf-8') as f:
        json.dump(data,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps({'small':len(data['small_cases']),'q19':data['Q19_k21'],'benchmark':data.get('benchmark')},indent=2))

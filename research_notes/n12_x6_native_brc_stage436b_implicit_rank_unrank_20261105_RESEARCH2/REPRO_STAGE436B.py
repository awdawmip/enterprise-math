#!/usr/bin/env python3
"""Stage436-B exact implicit future-class rank/unrank and integer BRC population checker.
All combinatorial quantities are Python arbitrary-precision integers.
"""
from functools import lru_cache
from itertools import combinations
from collections import Counter
import json

def choose(n, k):
    if k < 0 or n < 0 or k > n:
        return 0
    k = min(k, n-k)
    z = 1
    for i in range(1, k+1):
        z = z * (n-k+i) // i
    return z

def independent(bits):
    return all(not(bits[i] and bits[i-1]) for i in range(1, len(bits)))

class FutureClassCoder:
    """Window sites [a,b], binary defects, total exactly k in [2,m-1]."""
    def __init__(self, m, n, p, r, k):
        assert m >= n+r+2 and n >= p+1 and p >= 0 and r >= 1
        self.m, self.n, self.p, self.r, self.k = m,n,p,r,k
        self.a, self.b = n-p+1, n+r
        self.w = self.b-self.a+1
        self.left = self.a-2
        self.right = m-1-self.b
        self.L = m-2
        self.dp_calls = 0
        @lru_cache(None)
        def count(i, used, prev, first):
            self.dp_calls += 1
            if used > k: return 0
            if i == self.w:
                cap_left = (self.left + 1 - first)//2
                cap_right = (self.right + 1 - prev)//2
                return int(used <= k <= used + cap_left + cap_right)
            v = count(i+1,used,0, 0 if first == -1 else first)
            if not prev:
                v += count(i+1,used+1,1,1 if first == -1 else first)
            return v
        self.count = count
        self.q = count(0,0,0,-1)

    def class_of(self, defects):
        d = set(defects)
        assert len(d) == self.k
        assert all(2<=x<=self.m-1 for x in d)
        assert all((x+1 not in d) for x in d)
        return tuple(int(i in d) for i in range(self.a,self.b+1))

    def mass(self, bits):
        assert len(bits) == self.w and independent(bits)
        t = self.k - sum(bits)
        l = self.left - bits[0]
        h = self.right - bits[-1]
        return sum(choose(l-j+1,j)*choose(h-(t-j)+1,t-j)
                   for j in range(t+1)) if t>=0 else 0

    def rank(self, bits):
        assert len(bits)==self.w
        used=prev=0; first=-1; rank=0
        for i,bit in enumerate(bits):
            assert bit in (0,1) and (not prev or not bit)
            f0 = 0 if first == -1 else first
            if bit == 1: rank += self.count(i+1,used,0,f0)
            used += bit
            prev = bit
            first = bit if first == -1 else first
        assert self.mass(bits)>0 and 0<=rank<self.q
        return rank

    def unrank(self, rank):
        assert 0<=rank<self.q
        used=prev=0; first=-1; bits=[]
        for i in range(self.w):
            f0 = 0 if first==-1 else first
            z = self.count(i+1,used,0,f0)
            if rank < z: bit=0
            else:
                assert prev==0
                rank -= z
                bit=1
            bits.append(bit); used+=bit; prev=bit
            first=bit if first==-1 else first
        assert rank==0
        return tuple(bits)

def brute_defects(m,k):
    for d in combinations(range(2,m),k):
        if all(d[i]+1 < d[i+1] for i in range(len(d)-1)):
            yield d

def check(case):
    m,n,p,r,k=case
    c=FutureClassCoder(*case)
    pop=Counter(c.class_of(d) for d in brute_defects(m,k))
    assert sum(pop.values()) == choose(m-k-1,k)
    classes=sorted(pop)
    assert c.q==len(classes), (case,c.q,len(classes))
    assert sum(c.mass(bits) for bits in classes)==choose(m-k-1,k)
    for i,bits in enumerate(classes):
        assert c.rank(bits)==i
        assert c.unrank(i)==bits
        assert c.mass(bits)==pop[bits]
    assert c.unrank(0)==classes[0] if classes else c.q==0
    for mask in range(1<<c.w):
        bits=tuple((mask>>(c.w-1-i))&1 for i in range(c.w))
        if independent(bits):
            assert (c.mass(bits)>0)==(bits in pop)
    return {
        'params':list(case),'window':[c.a,c.b],'reservoir_lengths':[c.left,c.right],
        'fiber_total':sum(pop.values()),'classes':c.q,'mass_total':sum(pop.values()),
        'max_mass':max(pop.values(),default=0),'minimal_class_id_bits':(c.q-1).bit_length() if c.q else 0,
        'cached_dp_states':c.dp_calls,
        'class_masses_lex':[str(pop[x]) for x in classes] if c.q<=32 else 'omitted_large_output'
    }

def main():
    cases=[]
    for m in range(8,13):
        for n in range(2,m-2):
            for p in range(0,min(2,n-1)+1):
                for r in range(1,min(3,m-n-2)+1):
                    for k in (2,3):
                        cases.append((m,n,p,r,k))
    cases += [(13,6,2,2,2),(13,6,2,2,3),(17,8,2,3,3),
              (19,5,3,5,3),(20,8,4,5,3),(25,10,4,6,3),
              (17,5,2,3,2),(17,9,3,2,3)]
    cases=list(dict.fromkeys(cases))
    rows=[check(x) for x in cases]
    sample=next(x for x in rows if x['params']==[13,6,2,2,2])
    out={
        'marker':'STAGE436B_IMPLICIT_RANK_UNRANK_EXACT_PASS',
        'arithmetic':'Python arbitrary precision integers; exhaustive direct combinatorial enumeration',
        'checked_parameter_cases':len(rows),
        'checked_original_histories':sum(x['fiber_total'] for x in rows),
        'checked_future_classes':sum(x['classes'] for x in rows),
        'max_dp_cached_states':max(x['cached_dp_states'] for x in rows),
        'sample_13_6_2_2_2':sample,
        'boundary_sensitive_cases':sum(1 for x in rows if min(x['reservoir_lengths'])<x['params'][-1]),
        'all_cases_passed':True,
        'representative_cases': [x for x in rows if x['params'] in ([13,6,2,2,3],[17,8,2,3,3],[19,5,3,5,3],[20,8,4,5,3],[25,10,4,6,3])],
    }
    print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
if __name__ == '__main__':main()

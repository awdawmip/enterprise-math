#!/usr/bin/env python3
"""Projection oracle. Standard Python. Prints deterministic JSON; no filesystem input."""
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
import json


def bits(mask):
    while mask:
        i = mask & -mask
        yield i.bit_length() - 1
        mask ^= i


def census(d):
    """Ambient-cube DP: every nonempty subset, all nonempty strict coordinate demands."""
    n = 1 << d
    lim = 1 << n
    full = (1 << d) - 1
    pos = [sum(1 << x for x in range(n) if x & (1 << j)) for j in range(d)]
    count = Counter()
    gains = Counter()
    minimum = None
    for t in range(1,full):
        demand = tuple(bits(t))
        auxiliaries = tuple(bits(t ^ full))
        d0 = bytearray(lim)
        d1 = bytearray(lim)
        for u in range(1,lim):
            split0 = []
            for c in demand:
                v = u & pos[c]
                if v and v != u:
                    split0.append((v,u ^ v))
            if split0:
                d0[u] = 1 + min(max(d0[v],d0[w]) for v,w in split0)
                least = min(max(d1[v],d1[w]) for v,w in split0)
                if least > 0:
                    for c in auxiliaries:
                        v = u & pos[c]
                        if v and v != u:
                            least = min(least,max(d1[v],d1[u ^ v]))
                d1[u] = 1 + least
            size, width = u.bit_count(),len(demand)
            gain = d0[u]-d1[u]
            assert gain >= 0
            count[(width,gain)] += 1
            if gain:
                gains[size] += 1
                key = (size,width,u,t)
                if minimum is None or key < minimum:
                    minimum = key
    return dict(dimension=d, tasks=sum(count.values()),
                by_demand_and_gain={f'{k}:{g}':v for (k,g),v in sorted(count.items())},
                strict_by_histories={str(k):v for k,v in sorted(gains.items())},
                smallest_strict=None if minimum is None else
                dict(histories=list(bits(minimum[2])), demand=list(bits(minimum[3])),
                     dimension=d, binary_order='bit 0 first coordinate'))


class Solver:
    """History-indexed solver, projection labels may repeat, the permitted test list is explicit."""
    def __init__(self, words, T, allow):
        self.words = tuple(words)
        self.n = len(words)
        self.W = (1 << self.n)-1
        self.T = tuple(T)
        self.A = tuple(allow)
        self.pos = {j:sum(1 << i for i,w in enumerate(words) if w[j]) for j in self.A}
        self.labels = tuple(tuple(w[j] for j in T) for w in words)
        self.label_count = lru_cache(None)(lambda u:len({self.labels[i] for i in bits(u)}))

        @lru_cache(None)
        def depth(u):
            if self.label_count(u)<=1:
                return 0
            return min(v for v,j in self.scores(u))
        self.depth = depth

    def scores(self,u):
        return [(1+max(self.depth(v),self.depth(u ^ v)),j)
                for j in self.A if 0<(v:=u & self.pos[j])<u]

    def tree(self,u=None):
        u = self.W if u is None else u
        if self.depth(u)==0:
            return dict(output=list(self.labels[next(bits(u))]))
        _,j = min(self.scores(u))
        v = u & self.pos[j]
        return dict(query=j, zero=self.tree(u ^ v), one=self.tree(v))

    def advice(self,s):
        """Optimize over set partitions into at most 2**s cells (unlabelled cells)."""
        @lru_cache(None)
        def f(u,k):
            if u==0 or self.label_count(u)<=k:
                return 0
            if k==1:
                return self.depth(u)
            ans=self.depth(u)
            anch=u & -u
            sub=u ^ anch
            while True:
                cell=sub | anch
                ans=min(ans,max(self.depth(cell),f(u ^ cell,k-1)))
                if sub==0 or ans==0:
                    return ans
                sub=(sub-1) & (u ^ anch)
        return f(self.W,min(1 << s,self.n))

    def advice_cover(self,s):
        """Independent packing: min number of depth-d solvable sets covering remaining histories."""
        n=self.n
        for d in range(self.depth(self.W)+1):
            good=[u for u in range(1,self.W+1) if self.depth(u)<=d]
            maximal=[u for u in sorted(good, key=int.bit_count,reverse=True)
                     if not any(self.depth(u|v)<=d for v in (1<<j for j in range(n) if not u & (1<<j)))]
            @lru_cache(None)
            def cov(u):
                if not u:return 0
                anchor=u & -u
                return 1+min(cov(u & ~c) for c in maximal if c & anchor)
            if cov(self.W)<=1 << s:
                return d
        raise AssertionError

    def details(self, budgets=(0,1,2,3)):
        row=dict(depth=self.depth(self.W), min_tree=self.tree(),
                 root_depths={str(j):v for v,j in sorted(self.scores(self.W),key=lambda z:z[1])},
                 advice=[self.advice(s) for s in budgets])
        assert row['advice']==[self.advice_cover(s) for s in budgets]
        return row


def star(rows,k):
    return [tuple(int(i==label) for i in range(1,k+1))+tuple(tail) for label,tail in rows]


def both_needed():
    rows=[(0,(0,0)),(1,(0,0)),(2,(0,1)),(3,(0,1)),(2,(1,0)),(4,(1,0))]
    words=star(rows,4)
    names={'no_helpers':[0,1,2,3], 'a_only':[0,1,2,3,4], 'b_only':[0,1,2,3,5],
           'both':list(range(6))}
    tab={k:Solver(words,range(4),A).details() for k,A in names.items()}
    assert [v['depth'] for v in tab.values()]==[4,4,4,3]
    return dict(rows_label_ab=rows, tables=tab)


def fibre_sweep():
    # 5 labelled output symbols. Assign to each of the four possible helper pairs
    # one or more histories, with five labelled (not identified up to permutation) outputs.
    # Every fibre is a nonempty subset of {00,01,10,11}. The four demand
    # tests are singletons 1..4; there is no primitive for baseline label 0.
    # Sweep deterministic encodings plus encodings with exactly one doubled fibre:
    # 4**5 + 5*6*4**4 possibilities, no permutation quotient in the total.
    c=Counter()
    examples={}
    deterministic=tuple((i,) for i in range(4))
    pairs=tuple(combinations(range(4),2))
    for duplicated in (-1,0,1,2,3,4):
        for fib in product(*(pairs if l==duplicated else deterministic for l in range(5))):
            words=star([(l,(p>>1,p&1)) for l,ps in enumerate(fib) for p in ps],4)
            depth=tuple(Solver(words,range(4),a).depth((1<<len(words))-1)
                        for a in ((0,1,2,3,4),(0,1,2,3,5),range(6)))
            case=("5" if duplicated<0 else "6")+":"+','.join(map(str,depth))
            c[case]+=1
            if depth==(4,4,3) and case not in examples:
                examples[case]=fib
    return dict(total=sum(c.values()), conventions="label 0 has no demand marker, helpers ordered",
                depths_single_a_single_b_both=dict(sorted(c.items())), first_synergy=examples)


def greedy():
    # Four histories; tuple order (demand, other, other).
    w=[(0,0,0),(0,0,1),(0,1,0),(1,1,1)]
    s=Solver(w,[0],range(3))
    splits={str(j):[s.n-(s.W&s.pos[j]).bit_count(),(s.W&s.pos[j]).bit_count()]
            for j in s.A}
    return dict(words=w,demand=[0],world_split=splits,result=s.details())


def greedy_labels():
    # Nine different outputs. One helper isolates all four nuisance labels as
    # a group (the most balanced 4:5 split). Two helpers each isolate a triple.
    rows=[(label,(int(label>=5),int(label in (1,5,6)),int(label in (2,7,8)))) for label in range(9)]
    w=star(rows,8)
    s=Solver(w,range(8),range(11))
    tab={str(j):dict(labels_per_branch=[s.label_count(s.W & ~s.pos[j]),s.label_count(s.W & s.pos[j])],
                     depth_if_first=v) for v,j in s.scores(s.W)}
    assert s.depth(s.W)==4 and tab['8']['depth_if_first']==5
    return dict(rows=rows,results=tab,optimum=s.depth(s.W))


def masked_checks():
    out=[]
    pairs=[(2,4),(2,5),(2,6),(2,7),(2,8),(3,6),(3,7),(3,8),(3,9),(4,8),(4,10)]
    for L,N in pairs:
        rows=[(a,tuple((mask>>j)&1 for j in range(L)))
              for a in range(N) for mask in range(1<<L)
              if mask.bit_count()%2==int(a>=N//2)]
        w=star(rows,N-1)
        lens=[]
        # Helper index permutation preserves the entire feasible set, so all proper
        # subsets are covered (depth by cardinality). Fixed bijection of words.
        for used in range(L+1):
            s=Solver(w,range(N-1),range(N-1+used))
            ans=s.depth(s.W)
            expected=N-1 if used<L else min(N-1,L+(N+1)//2-1)
            assert ans==expected,(L,N,used,ans,expected)
            lens.append(ans)
        out.append(dict(helpers=L,labels=N,histories=len(w),worst_by_available_helper_count=lens))
    return out


if __name__=='__main__':
    result=dict(model="adaptive binary single-coordinate observations; output projection; no error; minimax",
                ambient=[census(d) for d in range(1,5)],
                synergistic_helpers=both_needed(),fibre_census=fibre_sweep(),greedy_histories=greedy(),
                greedy_labels=greedy_labels(),masked_synergy=masked_checks())
    print(json.dumps(result,indent=2,sort_keys=True))

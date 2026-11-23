#!/usr/bin/env python3
"""R284FT: exact finite 20/21-bit obstruction for (q,u)=(3,1).

Standard-library integers only. The prefix oracle is a NECESSARY test;
failing every count-lattice path excludes any write order. No Result/Review.
"""
from collections import deque
from functools import lru_cache
from itertools import combinations, product
from math import comb

Q, U = 3, 1
PAIRS = tuple(combinations(range(4), 2))
PHASE = {p: (0, p&1, (p>>1)&1, (p>>2)&1) for p in range(1, 8)}
LATEST = {}
for p, bits in PHASE.items():
    edges = {e for e in range(4) if bits[e] != bits[(e+1)%4]}
    LATEST[p] = tuple(next(e for e in ((i-1-t)%4 for t in range(4)) if e in edges)
                      for i in range(4))


def histograms(n, k=7):
    if k == 1:
        yield (n,)
    else:
        for a in range(n+1):
            for tail in histograms(n-a, k-1):
                yield (a,)+tail


def necessary_distance(x):
    for i,j in PAIRS:
        d = sum(x[p-1] for p in range(1,8) if PHASE[p][i]!=PHASE[p][j])
        adjacent = (j-i==1 or (i,j)==(0,3))
        if d < (2*Q+4*U+1 if adjacent else 2*(Q+U)+1):
            return False
    return True


def cut_patterns(i,j):
    pairs = [(p,LATEST[p][i],4+LATEST[p][j]) for p in range(1,8)
             if PHASE[p][i]!=PHASE[p][j]]
    out = set()
    for vertices in range(1,256):
        ps = tuple(p for p,a,b in pairs if vertices&(1<<a) and vertices&(1<<b))
        if ps:
            out.add((ps, Q*vertices.bit_count()+2*U+1))
    return tuple(out)

CUTS = {ij:cut_patterns(*ij) for ij in PAIRS}


def necessary_stable_cuts(x):
    return all(any(sum(x[p-1] for p in ps)>=threshold for ps,threshold in CUTS[ij])
               for ij in PAIRS)


class Flow:
    def __init__(self):
        self.g=[[] for _ in range(17)]
    def add(self,a,b,n):
        self.g[a].append([b,n,len(self.g[b])]);self.g[b].append([a,0,len(self.g[a])-1])
    def maximum(self):
        total=0
        while True:
            previous=[None]*17;previous[0]=(-1,-1)
            queue=deque([0])
            while queue and previous[16] is None:
                v=queue.popleft()
                for k,(w,capacity,_) in enumerate(self.g[v]):
                    if capacity and previous[w] is None:
                        previous[w]=(v,k);queue.append(w)
            if previous[16] is None: return total
            amount=10**9;v=16
            while v!=0:
                a,k=previous[v];amount=min(amount,self.g[a][k][1]);v=a
            v=16
            while v!=0:
                a,k=previous[v];b,_,back=self.g[a][k]
                self.g[a][k][1]-=amount;self.g[b][back][1]+=amount;v=a
            total+=amount


def minimum_prefix_distance(x,i,j,target,success):
    """Exact min Hamming distance from prefix-success image of S_i to S_j.

    Left groups 8..11 and right groups 12..15 each have omission capacity Q.
    Root is 0, ordinary type-demand nodes 1..7, sink 16. A successfully
    overwritten bit creates right-only demand if its target disagrees with j.
    """
    network=Flow();demand=0
    for p in range(1,8):
        free=x[p-1]-success.get(p,0)
        if free and PHASE[p][i]!=PHASE[p][j]:
            demand+=free;network.add(0,p,free)
            network.add(p,8+LATEST[p][i],free)
            network.add(p,12+LATEST[p][j],free)
        fixed=success.get(p,0)
        if fixed and PHASE[p][target]!=PHASE[p][j]:
            demand+=fixed;network.add(0,12+LATEST[p][j],fixed)
    for e in range(4):
        network.add(8+e,16,Q);network.add(12+e,16,Q)
    return demand-network.maximum()


def edge_has_safe_count_path(x,edge):
    target=(edge+1)%4
    types=tuple(p for p in range(1,8) if x[p-1] and PHASE[p][edge]!=PHASE[p][target])
    finish=tuple(x[p-1] for p in types)

    @lru_cache(None)
    def necessary_safe(prefix):
        # Every omission allocation and every earlier stable state are covered
        # through an exact min-distance flow, not sampled physical histories.
        for miss in product(*(range(min(Q,t)+1) for t in prefix)):
            if sum(miss)>Q:continue
            success={p:t-m for p,t,m in zip(types,prefix,miss)}
            for third in range(4):
                if third in (edge,target):continue
                if minimum_prefix_distance(x,edge,third,target,success)<=2*U:
                    return False
            if sum(success.values())<=2*U:
                if minimum_prefix_distance(x,edge,target,target,success)<=2*U:
                    return False
        return True

    start=(0,)*len(types)
    frontier=deque([start]);seen={start}
    while frontier:
        t=frontier.popleft()
        if t==finish:return True
        for k in range(len(types)):
            if t[k]==finish[k]:continue
            nxt=t[:k]+(t[k]+1,)+t[k+1:]
            if nxt not in seen:
                seen.add(nxt)
                if necessary_safe(nxt): frontier.append(nxt)
    return False


def check(n):
    count=distance=stable=0
    first_survivors=[];second_survivors=[]
    for x in histograms(n):
        count+=1
        if not necessary_distance(x):continue
        distance+=1
        if not necessary_stable_cuts(x):continue
        stable+=1
        if edge_has_safe_count_path(x,0):
            first_survivors.append(x)
            if edge_has_safe_count_path(x,1):second_survivors.append(x)
    assert count==comb(n+6,6)
    return (count,distance,stable,first_survivors,second_survivors)


def main():
    twenty=check(20);twentyone=check(21)
    assert twenty[:3]==(230230,4005,10),twenty
    assert twenty[3]==[(0,0,0,0,11,9,0)],twenty[3]
    assert twenty[4]==[],twenty[4]
    assert twentyone[:3]==(296010,10421,97),twentyone
    assert twentyone[3]==[
      (0,0,0,0,11,9,1),(0,0,0,0,11,10,0),(0,0,0,0,12,9,0),
      (0,0,0,1,10,9,1),(0,0,0,1,11,9,0),
      (0,0,1,0,10,9,1),(0,0,1,0,11,9,0),
      (0,1,0,0,10,9,1),(0,1,0,0,11,9,0),
      (1,0,0,0,11,9,0)],twentyone[3]
    assert twentyone[4]==[],twentyone[4]
    print('n=20: histograms=230230, distance=4005, six-cuts=10, edge0=1, edge1=0')
    print('n=21: histograms=296010, distance=10421, six-cuts=97, edge0=10, edge1=0')
    assert all(edge_has_safe_count_path((0,0,11,0,0,11,0),e) for e in range(4))
    print('22-bit Gray repeated-group construction passes the necessary prefix oracle')
    print('With R284FP n>=20 and R284FE n<=22, exact sharp n_min(3,1)=22')

if __name__=='__main__':main()

#!/usr/bin/env python3
"""PREFIX-798: exact weighted provenance histogram transfer.
Pure standard-library integer arithmetic; no network, no random inputs.
"""
from collections import defaultdict
from itertools import product
import json


def enumerate_tables(b, c, K):
    ranges = [range(z+1) for z in K]
    for tup in product(*ranges):
        rows = tuple(sum(tup[i*c+j] for j in range(c)) for i in range(b))
        cols = tuple(sum(tup[i*c+j] for i in range(b)) for j in range(c))
        yield tup,rows,cols


def histogram_dp(b,c,K,r,s,w):
    # Maps current column loads to exact polynomial histogram of query totals.
    state = {(0,)*c:{0:1}}
    for i in range(b):
        new = defaultdict(lambda:defaultdict(int))
        for t in product(*(range(K[i*c+j]+1) for j in range(c))):
            if sum(t)!=r[i]:continue
            wt=sum(w[i*c+j]*t[j] for j in range(c))
            for d,poly in state.items():
                nd=tuple(d[j]+t[j] for j in range(c))
                if any(nd[j]>s[j] for j in range(c)):continue
                for q,n in poly.items():new[nd][q+wt]+=n
        state={d:dict(poly) for d,poly in new.items()}
    return state.get(s,{})


def gcd(a,b):
    while b:a,b=b,a%b
    return abs(a)


def cycle_gcd(b,c,K,w):
    # A spanning forest yields an integer fundamental-cycle basis.
    n=b+c
    edges=[(i,b+j,w[i*c+j]) for i in range(b) for j in range(c) if K[i*c+j]>0]
    uf=list(range(n))
    def root(v):
        while uf[v]!=v:
            uf[v]=uf[uf[v]]
            v=uf[v]
        return v
    tree=[[] for _ in range(n)]
    chords=[]
    for u,v,weight in edges:
        ru,rv=root(u),root(v)
        if ru!=rv:
            uf[ru]=rv
            tree[u].append((v,weight))
            tree[v].append((u,weight))
        else:chords.append((u,v,weight))
    from collections import deque
    g=0
    for u,v,wuv in chords:
        parent={u:None}; q=deque([u])
        while q and v not in parent:
            a=q.popleft()
            for z,weight in tree[a]:
                if z not in parent:parent[z]=(a,weight);q.append(z)
        assert v in parent
        # Potential relation: edge row->col has weight = alpha_row+beta_col.
        # On trees set node potential with signed difference p(col)-p(row)=weight.
        z=v; delta=0
        while z!=u:
            a,weight=parent[z]
            delta+=(weight if a<b else -weight)
            z=a
        # path from row u to column v, delta = sum alternating signed path weights
        g=gcd(g,wuv-delta)
    return g


def check_family(b,c,kmax,stride=1):
    masks=0; states=0; fibers=0; checks=0; holes=0
    patterns=[tuple(1 if (i+j)%2==0 else 0 for i in range(b) for j in range(c)),
              tuple(((2*i+3*j)%4) for i in range(b) for j in range(c)),
              tuple(1 if i<max(1,b//2) and j<max(1,c//2) else 0 for i in range(b) for j in range(c)),
              tuple(2 if i==0 and j==0 else 3 if i==b-1 and j==c-1 else 0 for i in range(b) for j in range(c))]
    for idx,K in enumerate(product(range(kmax+1),repeat=b*c)):
        if idx%stride:continue
        K=tuple(K); masks+=1
        groups=defaultdict(list)
        for x,r,s in enumerate_tables(b,c,K):
            groups[(r,s)].append(x)
            states+=1
        for (r,s),fiber in groups.items():
            fibers+=1
            for w in patterns:
                expected=defaultdict(int)
                for x in fiber:expected[sum(a*b for a,b in zip(w,x))]+=1
                got=histogram_dp(b,c,K,r,s,w)
                assert dict(expected)==got,(b,c,K,r,s,w,expected,got)
                checks+=1
                g=cycle_gcd(b,c,K,w)
                keys=sorted(expected)
                if g==0:assert len(keys)==1
                else:assert all((v-keys[0])%g==0 for v in keys)
                checks+=1
                if len(keys)>1 and g==1 and keys!=list(range(keys[0],keys[-1]+1)):
                    holes+=1
                # modulus greater than range is an injective residue encoding.
                m=keys[-1]-keys[0]+1
                residue=defaultdict(int)
                for v,n in got.items():residue[v%m]+=n
                assert len(residue)==len(keys)
                checks+=1
    return dict(shape=f'{b}x{c}',kmax=kmax,stride=stride,capacity_masks=masks,enumerated_tables=states,distinct_fibers=fibers,assertions=checks,gcd_one_gap_fibers=holes)


def examples():
    # Two disconnected 2x2 cycles. Each block has row/column margins (1,1).
    b=c=4
    K=(1,1,0,0, 1,1,0,0, 0,0,1,1, 0,0,1,1)
    r=s=(1,1,1,1)
    w=(2,0,0,0, 0,0,0,0, 0,0,3,0, 0,0,0,0)
    poly=histogram_dp(b,c,K,r,s,w)
    assert poly=={0:1,2:1,3:1,5:1},poly
    assert cycle_gcd(b,c,K,w)==1
    # A four-edge cycle, one diagonal indicator counts 0 or 2, skipping 1.
    K2=(1,1,1,1)
    p2=histogram_dp(2,2,K2,(1,1),(1,1),(1,0,0,1))
    assert p2=={0:1,2:1}
    assert cycle_gcd(2,2,K2,(1,0,0,1))==2
    return dict(two_cycle_query_histogram={str(k):v for k,v in sorted(poly.items())},two_cycle_gcd=1,diagonal_query_histogram={str(k):v for k,v in sorted(p2.items())},diagonal_cycle_gcd=2,assertions=4)


def main():
    cases=[check_family(2,2,2),check_family(2,3,1),check_family(3,3,1,stride=7)]
    ex=examples()
    summary={'schema':'PREFIX798_R6_WEIGHTED_PROVENANCE_HISTOGRAM_V1','arithmetic':'exact_nonnegative_integers','family_checks':cases,'counterexamples':ex,'assertions':sum(z['assertions'] for z in cases)+ex['assertions'],'status':'ALL_CHECKS_PASS','scope':'bounded_transportation_fibers;synthetic_abstract_provenance_counts'}
    print(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':main()

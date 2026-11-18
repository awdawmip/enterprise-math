"""Finite-ring column spans, defect queries, and universal single-column probe menus."""
from collections import Counter
from itertools import combinations, product
from math import comb
import json


def gaussian(n,j,p):
    row=[1]
    for i in range(1,n+1):
        row=[1]+[row[k]+p**(i-k)*row[k-1] for k in range(1,i)]+[1]
    return row[j]


def submodule_count(p,k,r):
    # Walk forward from the final 0 column of Birkhoff's decreasing chain.
    v=[1]+[0]*r
    for _ in range(k):
        v=[sum(p**(b*(r-a))*gaussian(r-b,a-b,p)*v[b] for b in range(a+1))
           for a in range(r+1)]
    return sum(v)


def log_p(n,p):
    k=0
    while n>1:
        assert n%p==0
        n//=p
        k+=1
    return k


def elements(bits):
    while bits:
        term=bits&-bits
        yield term.bit_length()-1
        bits^=term


class Ambient:
    def __init__(self,p,k,r):
        self.p=p
        self.k=k
        self.r=r
        self.q=q=p**k
        self.vec=list(product(range(q),repeat=r))
        self.index={x:i for i,x in enumerate(self.vec)}
        self.direction=[0]*len(self.vec)
        self.generators=[0]
        self.cyclic=[[0]]
        known={(0,):0}
        for i,x in enumerate(self.vec[1:],1):
            multiples=[]
            for a in range(q):
                v=self.index[tuple(a*t%q for t in x)]
                if a and v==0: break
                multiples.append(v)
            key=tuple(sorted(multiples))
            if key not in known:
                known[key]=len(self.generators)
                self.generators.append(i)
                self.cyclic.append(multiples)
            self.direction[i]=known[key]
        self.plus=[[self.index[tuple((a+b)%q for a,b in zip(x,y))] for y in self.vec]
                   for x in self.vec]
        self.spaces=[1]
        self.words=[()]
        self.labels={1:0}
        self.transitions=[]
        for idx,space in enumerate(self.spaces):
            row=[]
            for j,generator in enumerate(self.generators):
                new=space
                if not (space>>generator)&1:
                    members=tuple(elements(space))
                    for a in self.cyclic[j][1:]:
                        if (space>>a)&1: break
                        new|=sum(1<<self.plus[a][x] for x in members)
                if new not in self.labels:
                    self.labels[new]=len(self.spaces)
                    self.spaces.append(new)
                    self.words.append(self.words[idx]+(generator,))
                row.append(self.labels[new])
            self.transitions.append(row)
        assert len(self.spaces)==submodule_count(p,k,r)

    def validate(self,s):
        t=self.r-s
        zero=(0,)*s
        vert=sum(1<<i for i,x in enumerate(self.vec) if x[:s]==zero)
        defect=[log_p((m&vert).bit_count(),self.p) for m in self.spaces]
        signatures={}
        delta_checks=member_checks=0
        for j,X in enumerate(self.spaces):
            row=tuple(defect[g] for g in self.transitions[j])
            signatures.setdefault((defect[j],row),[]).append(j)
            # Rebuild the frozen row-module quotient directly from this history's A and B.
            columns=[self.vec[g] for g in self.words[j]]
            rows=[tuple(c[i] for c in columns) for i in range(self.r)]
            H={(0,)*len(columns)}
            sizes=[1]
            for w in rows:
                H={tuple((v+a*x)%self.q for v,x in zip(h,w))
                   for h in H for a in range(self.q)}
                sizes.append(len(H))
            assert log_p(sizes[-1]//sizes[s],self.p)==defect[j]
            delta_checks+=1
            if defect[j]==self.k*t: continue
            probe=next(i for i in elements(vert) if row[self.direction[i]]==defect[j]+1)
            for i in range(len(self.vec)):
                safe=(row[self.direction[i]]==defect[j])
                next_growth=row[self.direction[self.plus[probe][i]]]-defect[j]
                assert (safe and next_growth==1)==bool((X>>i)&1)
                member_checks+=1
        expected=len(self.spaces)-submodule_count(self.p,self.k,s)+1
        assert len(signatures)==expected
        assert all(len(c)==1 or all(defect[j]==self.k*t for j in c) for c in signatures.values())
        data={'joint_submodules':len(self.spaces),'distinct_scalar_futures':len(signatures),
              'saturated_submodules':submodule_count(self.p,self.k,s),
              'row_quotient_direct_checks':delta_checks,'two_probe_memberships':member_checks}
        if self.k==1 and t:
            p=self.p
            rank_s=(p**s-1)//(p-1)
            rank_t=(p**t-1)//(p-1)
            target=rank_t-1+rank_s*max(2,p**t-1)
            def canon(v):
                first=next(x for x in v if x)
                return tuple(x*pow(first,-1,p)%p for x in v)
            vs=sorted({canon(x[s:]) for x in self.vec if x[:s]==zero and any(x[s:])})
            us=sorted({canon(x[:s]) for x in self.vec if any(x[:s])})
            safe_vertical=set(vs[:-1])
            targets=list(product(range(p),repeat=t))
            choices=targets if len(targets)==2 else targets[:-1]
            menu={self.direction[self.index[zero+v]] for v in safe_vertical}
            menu.update(self.direction[self.index[u+v]] for u in us for v in choices)
            assert len(menu)==target
            projected={(d,tuple(row[i] for i in sorted(menu))) for d,row in signatures}
            assert len(projected)==expected
            data['optimal_nonadaptive_dictionary_size']=target
            if len(self.generators)<=14:
                rows=[(d,sum((int(x>d)<<j) for j,x in enumerate(row))) for d,row in signatures]
                first=None
                for m in range(target+1):
                    for probes in combinations(range(1,len(self.generators)),m):
                        mask=sum(1<<i for i in probes)
                        if len({(d,b&mask) for d,b in rows})==expected:
                            first=m
                            break
                    if first is not None: break
                assert first==target
                data['all_subset_minimum']=first
        return data


def slope_checks(p,k):
    q=p**k
    def val(z):
        level=0
        while level<k and z%p==0:
            z//=p
            level+=1
        return level
    # Keep all but one leaf in each residue class modulo p^(k-1).
    menu=[v for v in range(q) if v//(q//p)!=p-1]
    assert len({tuple(k-val(v-z) for v in menu) for z in range(q)})==q
    for base in range(q//p):
        z,w=base,base+q//p
        for u,v in product(range(q),repeat=2):
            if u%p and v*pow(u,-1,q)%q in (z,w): continue
            assert val(v-u*z)==val(v-u*w)
    return len(menu)


def main():
    result={}
    for p,k,r,ss in [(2,1,2,[0,1,2]),(2,1,3,[1,2]),(2,1,4,[2]),
                      (3,1,2,[1]),(3,1,3,[1,2]),(5,1,2,[1]),
                      (2,2,2,[1]),(2,2,3,[1,2]),(2,3,2,[1]),(2,4,2,[1]),
                      (3,2,2,[1]),(5,2,2,[1])]:
        F=Ambient(p,k,r)
        for s in ss: result[f'p{p}_k{k}_s{s}_t{r-s}']=F.validate(s)
    print(json.dumps({'complete_submodule_enumerations':result,
                      'graph_slope_leaf_probe_counts':{f'{p}^{k}':slope_checks(p,k) for p,k in ((2,1),(2,3),(2,4),(3,2),(5,2))},
                      'Birkhoff_Sr_for_p2_k1_to4':{r:[submodule_count(2,k,r) for k in range(1,5)]
                                                   for r in range(1,6)}},indent=2,sort_keys=True))


if __name__=='__main__':
    main()

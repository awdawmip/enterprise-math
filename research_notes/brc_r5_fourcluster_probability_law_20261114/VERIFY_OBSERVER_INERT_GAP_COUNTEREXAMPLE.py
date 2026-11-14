#!/usr/bin/env python3
"""Exact radius-two observer-separation counterexample and all n<5 tests."""
from itertools import combinations,product

def optimum(points,radius=2):
    n=len(points);out={}
    for k in range(1,n+1):
        feasible=[]
        for chosen in combinations(points,k):
            distances=[min(abs(x-s) for s in chosen) for x in points]
            if max(distances)<=radius:feasible.append((sum(distances),chosen))
        if feasible:
            v=min(cost for cost,_ in feasible)
            out[k]={"cost":v,"witnesses":[s for cost,s in feasible if cost==v]}
    return out

def main():
    result={}
    for n in range(2,5):
        tested=stable=changed=0
        for gaps in product((1,2,3),repeat=n-1):
            pts=(0,)
            for gap in gaps:pts+=(pts[-1]+gap,)
            old=optimum(pts)
            for cut,gap in enumerate(gaps):
                if gap!=3:continue
                tested+=1
                shifted=tuple(x-int(i>cut) for i,x in enumerate(pts))
                new=optimum(shifted)
                if min(old)==min(new):
                    stable+=1
                    for k in set(old)&set(new):
                        if old[k]["cost"]!=new[k]["cost"]:changed+=1
        assert changed==0
        result[n]=[tested,stable,changed]
    assert result=={2:[1,0,0],3:[6,0,0],4:[27,10,0]},result
    a=optimum((0,1,2,4,7));b=optimum((0,1,2,4,6))
    assert min(a)==min(b)==2
    assert a[2]=={"cost":5,"witnesses":[(2,7)]},a[2]
    assert b[2]=={"cost":4,"witnesses":[(1,4),(1,6)]},b[2]
    assert [a[k]["cost"] for k in range(2,6)]==[5,2,1,0]
    assert [b[k]["cost"] for k in range(2,6)]==[4,2,1,0]
    print("PASS_EXACT_R2_MINIMUM_OBSERVER_SEPARATION",result)

if __name__=="__main__":main()

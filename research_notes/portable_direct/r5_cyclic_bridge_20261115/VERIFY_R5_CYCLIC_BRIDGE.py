#!/usr/bin/env python3
"""Deterministic R5 cycle checks. Python >=3.10; SciPy needed for MILP cross-check."""
import json
OLD=('0125','0135','0235','0245','0246')
NEW_A=(('1235',1),('1245',1),('1246',1),('1345',0),('1346',0))
NEW_AB=NEW_A+(('1236',1),)
def edges(k):
    assert k>=3
    return tuple(e for i in range(k) for e in
        ((i,(i+1)%k),(i,k+i),((i+1)%k,k+i)))
def distance(c,t,y,o,s,x):
    return len(set(c)-set(o))+int(t!=s)+(y^x).bit_count()
def unc(E,S):
    return sum(a not in S and b not in S for a,b in E)
def predicted(k,spine):
    missing=set(range(k))-set(spine)
    return 5*k+sum(i in missing and (i+1)%k in missing for i in range(k))
def witness(k,spine):
    E=edges(k); Y=[(1<<a)|(1<<b) for a,b in E]; S=set(spine)
    old=[(OLD[1],0,y) for y in Y]
    for v in sorted(S):
        old.extend(((OLD[0],1,1<<v),(OLD[4],1,1<<v)))
    for (a,b),y in zip(E,Y):
        if a not in S and b not in S:
            old.append((OLD[0],1,y))
    return old,Y
def full_set_cover(k,W,joint=False):
    from scipy.optimize import milp,Bounds,LinearConstraint
    from scipy.sparse import lil_matrix
    Y=tuple((1<<a)|(1<<b) for a,b in edges(k))
    X=Y+tuple(1<<v for v in sorted(W))
    old=tuple((o,s,x) for x in X for o in OLD for s in (0,1))
    new=tuple((c,t,y) for y in Y for c,t in (NEW_AB if joint else NEW_A))
    mat=lil_matrix((len(new),len(old)),dtype=float)
    for i,(c,t,y) in enumerate(new):
        for j,(o,s,x) in enumerate(old):
            if distance(c,t,y,o,s,x)<=2: mat[i,j]=1
    r=milp([1.]*len(old),integrality=[1]*len(old),bounds=Bounds(0,1),
        constraints=LinearConstraint(mat.tocsr(),1,float('inf')),
        options={'time_limit':20})
    assert r.status==0 and r.mip_gap==0,(r.status,r.message)
    return int(round(r.fun))
def main():
    exhaustive=0
    for k in range(3,8):
        E=edges(k)
        for mask in range(1<<k):
            W={i for i in range(k) if mask>>i&1}
            avail=tuple(sorted(W|set(range(k,2*k))))
            optimum=min(3*k+2*len(S)+unc(E,S)
                for b in range(1<<len(avail))
                for S in ({v for j,v in enumerate(avail) if b>>j&1},))
            assert optimum==predicted(k,W),(k,mask)
            exhaustive+=1
    covers=0; diagnostics=0; deltas=0
    for k in range(3,10):
        for mask in range(1<<k):
            W={i for i in range(k) if mask>>i&1}
            old,Y=witness(k,W)
            assert len(old)==predicted(k,W)
            for y in Y:
                for c,t in NEW_A:
                    assert any(distance(c,t,y,o,s,x)<=2 for o,s,x in old)
            covers+=1
            miss=set(range(k))-W
            def q(U):
                return sum(i in U and (i+1)%k in U for i in range(k))
            for i in range(k):
                diagnostic={(i-1)%k}|({i} if i in miss else set())
                assert q(diagnostic)==int(i in miss)
                diagnostics+=1
                if i not in miss:
                    assert q(miss|{i})-q(miss)==int((i-1)%k in miss)+int((i+1)%k in miss)
                    deltas+=1
    lucas=[]
    for k in range(3,11):
        n=sum(all(not (mask>>i&1 and mask>>((i+1)%k)&1) for i in range(k))
              for mask in range(1<<k))
        opt=sum(3*k+2*mask.bit_count()+
                unc(edges(k),{i for i in range(k) if mask>>i&1})==5*k
                for mask in range(1<<k))
        assert n==opt
        lucas.append([k,n])
    checks=[]
    for k in (3,4,5):
        for W in (set(),{0},set(range(k))-{0},set(range(k))):
            avail=W|set(range(k,2*k))
            a=full_set_cover(k,avail)
            ab=full_set_cover(k,avail,True)
            assert (a,ab)==(predicted(k,W),6*k)
            checks.append({'k':k,'spine':sorted(W),'a':a,'ab':ab})
    for k in range(3,9):
        W0=set(range(k))-{0}; W1=set(range(k))-{1}
        assert predicted(k,W0)==predicted(k,W1)==5*k
        assert predicted(k,W0&W1)==5*k+1
    print(json.dumps({
      'result':'PASS_R5_CYCLIC_TRIANGLE_RESIDUAL',
      'pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
      'graph_exhaustive_cases':exhaustive,
      'direct_labeled_cover_cases':covers,
      'named_bit_diagnostics':diagnostics,
      'toggle_delta_cases':deltas,
      'lucas_k3_to_k10':lucas,
      'milp_source_matrix_checks':checks,
      'status':'AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED'
    },indent=2,sort_keys=True))
if __name__=='__main__': main()

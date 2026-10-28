#!/usr/bin/env python3
"""Exact author-side check for split 2+2 gauge orbits, finite prime fields.

This verifies a self-contained auxiliary finite-field classification, not a
native Enterprise Math/H0-B0 computation or independent mathematical review.
"""
from collections import deque
from itertools import product
from json import dumps


def mm(a, b, p):
    return ((a[0]*b[0]+a[1]*b[2])%p, (a[0]*b[1]+a[1]*b[3])%p,
            (a[2]*b[0]+a[3]*b[2])%p, (a[2]*b[1]+a[3]*b[3])%p)


def inv(a, p):
    d = (a[0]*a[3]-a[1]*a[2]) % p
    if not d:
        raise ValueError('noninvertible matrix')
    z = pow(d, -1, p)
    return ((a[3]*z)%p, (-a[1]*z)%p, (-a[2]*z)%p, (a[0]*z)%p)


def rank(a, p):
    if all(v%p==0 for v in a):
        return 0
    return 2 if (a[0]*a[3]-a[1]*a[2])%p else 1


def primitive(p):
    for g in range(2,p):
        if len({pow(g,i,p) for i in range(1,p)})==p-1:
            return g
    return 1


def gens(p):
    g=primitive(p)
    return ((1,1,0,1),(1,0,1,1),(g,0,0,1))


def sim_label(y,p):
    t=(y[0]+y[3])%p
    d=(y[0]*y[3]-y[1]*y[2])%p
    repeated = (t*t-4*d)%p == 0 if p!=2 else t==0
    scalar = y[1]==0 and y[2]==0 and y[0]==y[3]
    return ('X2',t,d, int(repeated and not scalar))


def rank1_label(y,p):
    u,v,w,z=y
    if u:
        return ('X1',u,'rankY',rank(y,p))
    return ('X1',0,int(v!=0),int(w!=0),int(v==0 and w==0 and z!=0))


def partition(objects, actions, label):
    remaining=set(objects)
    sizes={}
    transitions=0
    while remaining:
        root=remaining.pop()
        key=label(root)
        seen={root}
        q=deque([root])
        while q:
            o=q.popleft()
            for action in actions:
                v=action(o)
                transitions+=1
                assert label(v)==key,(o,v,key,label(v))
                if v not in seen:
                    seen.add(v)
                    remaining.remove(v)
                    q.append(v)
        assert key not in sizes,('invariant_not_complete',key)
        sizes[key]=len(seen)
    return sizes,transitions


def checked_fixed_x(p):
    all_y=list(product(range(p),repeat=4))
    gs=gens(p)
    # X=I. Stabilizer is diagonal GL2, acting on Y by similarity.
    conjugations=[(g,inv(g,p)) for g in gs]
    sim_actions=[lambda y,g=g,h=h:mm(mm(g,y,p),h,p) for g,h in conjugations]
    sim,st=partition(all_y,sim_actions,lambda y:sim_label(y,p))
    assert len(sim)==p*p+p
    # X=E11. Stabilizer P X=X Q with P upper, Q lower, same upper-left a.
    g=primitive(p)
    variants=[((g,0,0,1),(g,0,0,1)),
              ((1,0,0,g),(1,0,0,1)),
              ((1,0,0,1),(1,0,0,g)),
              ((1,1,0,1),(1,0,0,1)),
              ((1,0,0,1),(1,0,1,1))]
    e=(1,0,0,0)
    assert all(mm(P,e,p)==mm(e,Q,p) for P,Q in variants)
    rank1_actions=[lambda y,P=P,Qi=inv(P,p),Q=Q:mm(mm(Q,y,p),Qi,p) for P,Q in variants]
    one,ot=partition(all_y,rank1_actions,lambda y:rank1_label(y,p))
    assert len(one)==2*p+3
    assert sum(one.values())==p**4
    assert sum(sim.values())==p**4
    assert one[('X1',0,0,0,0)]==1
    assert one[('X1',0,0,0,1)]==p-1
    assert one[('X1',0,1,0,0)]==p*(p-1)
    assert one[('X1',0,0,1,0)]==p*(p-1)
    assert one[('X1',0,1,1,0)]==p*(p-1)**2
    for u in range(1,p):
        assert one[('X1',u,'rankY',1)]==p*p
        assert one[('X1',u,'rankY',2)]==p*p*(p-1)
    return dict(p=p,rank2_similarity_orbits=len(sim),rank1_stabilizer_orbits=len(one),rank0_orbits=3,
                total_predicted=p*p+3*p+6,checked_fixed_states=2*p**4,
                fixed_generator_transitions=st+ot)


def encode_pair(x,y,p):
    v=0
    for a in x+y:
        v=v*p+a
    return v


def decode_pair(v,p):
    a=[0]*8
    for i in range(7,-1,-1):
        a[i]=v%p
        v//=p
    return tuple(a[:4]),tuple(a[4:])


def full_label(x,y,p):
    r=rank(x,p)
    if r==0:
        return ('X0',rank(y,p))
    if r==2:
        return sim_label(mm(y,x,p),p)
    # Rank one: u=tr(YX). XY, YX are oriented future-operation observers.
    xy=mm(x,y,p)
    yx=mm(y,x,p)
    u=(yx[0]+yx[3])%p
    if u:
        return ('X1',u,'rankY',rank(y,p))
    a=int(rank(xy,p)!=0)
    b=int(rank(yx,p)!=0)
    return ('X1',0,a,b,int(a==0 and b==0 and rank(y,p)!=0))


def check_full(p):
    gl=gens(p)
    I=(1,0,0,1)
    changes=[(g,I) for g in gl]+[(I,g) for g in gl]
    actions=[]
    for P,Q in changes:
        Pi,Qi=inv(P,p),inv(Q,p)
        def operate(v,P=P,Q=Q,Pi=Pi,Qi=Qi):
            x,y=decode_pair(v,p)
            return encode_pair(mm(mm(P,x,p),Qi,p),mm(mm(Q,y,p),Pi,p),p)
        actions.append(operate)
    remaining=set(range(p**8))
    seen_keys=set()
    orbits=0
    transitions=0
    while remaining:
        root=remaining.pop()
        root_pair=decode_pair(root,p)
        k=full_label(*root_pair,p)
        assert k not in seen_keys,('invariant_incomplete',p,k)
        seen_keys.add(k)
        queue=deque([root])
        while queue:
            v=queue.popleft()
            for action in actions:
                target=action(v)
                transitions+=1
                assert full_label(*decode_pair(target,p),p)==k,(p,v,target,k)
                if target in remaining:
                    remaining.remove(target)
                    queue.append(target)
        orbits+=1
    assert orbits==p*p+3*p+6
    return dict(p=p,whole_pair_states=p**8,whole_pair_orbits=orbits,
                whole_generator_transitions=transitions)


def check_witness(p=373):
    x=(1,0,0,0)
    ya=(0,1,0,0)
    yb=(0,0,1,0)
    a=full_label(x,ya,p)
    b=full_label(x,yb,p)
    assert a!=b
    assert rank(ya,p)==rank(yb,p)==1
    assert (mm(ya,x,p)[0]+mm(ya,x,p)[3])%p == 0
    assert (mm(yb,x,p)[0]+mm(yb,x,p)[3])%p == 0
    assert mm(x,ya,p)!=(0,0,0,0) and mm(ya,x,p)==(0,0,0,0)
    assert mm(x,yb,p)==(0,0,0,0) and mm(yb,x,p)!=(0,0,0,0)
    return {'p':p,'X':x,'Y_forward':ya,'Y_backward':yb,
            'forward_rank_XY':rank(mm(x,ya,p),p),'forward_rank_YX':rank(mm(ya,x,p),p),
            'backward_rank_XY':rank(mm(x,yb,p),p),'backward_rank_YX':rank(mm(yb,x,p),p)}


def main():
    fixed=[checked_fixed_x(p) for p in (2,3,5,7,11,13)]
    whole=[check_full(p) for p in (2,3)]
    witness=check_witness()
    data={'schema':'D25_BALANCED_22_ALLRANK_AUTHOR_CHECK_V1',
          'type':'AUTHOR_LOCAL_EXACT_CHECK_NOT_NATIVE_NOT_INDEPENDENT',
          'result':'PASS','fixed_cases':fixed,'whole_pair_exhaustive':whole,
          'p373_orbit_prediction':373*373+3*373+6,'p373_witness':witness,
          'coverage':'All fixed canonical X=I,E11 pairs over prime fields 2,3,5,7,11,13; all (X,Y) over F2,F3; not native H0/B0.'}
    print(dumps(data,ensure_ascii=False,indent=2,sort_keys=True))


if __name__=='__main__':
    main()

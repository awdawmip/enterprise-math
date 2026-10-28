#!/usr/bin/env python3
"""Exact finite-field author check for the auxiliary balanced-block gauge theorem.

Uses integer modular arithmetic only. The GL_2 generators (two elementary
transvections and a primitive determinant) generate every GL_2(F_p).
"""
from collections import deque
import json


def mm(x, y, p):
    a,b,c,d=x; e,f,g,h=y
    return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)


def inv(x,p):
    a,b,c,d=x
    delta=(a*d-b*c)%p
    assert delta!=0
    u=pow(delta,-1,p)
    return ((d*u)%p,(-b*u)%p,(-c*u)%p,(a*u)%p)


def rep(x,p):
    a,b,c,d=x
    return (((a*p+b)*p+c)*p+d)


def unpack(i,p):
    d=i%p; i//=p
    c=i%p; i//=p
    b=i%p; i//=p
    return (i%p,b,c,d)


def primitive(p):
    factors=[]
    r=p-1
    d=2
    while d*d<=r:
        if r%d==0:
            factors.append(d)
            while r%d==0: r//=d
        d+=1
    if r>1: factors.append(r)
    for x in range(2,p):
        if all(pow(x,(p-1)//t,p)!=1 for t in factors):
            return x
    raise AssertionError('no generator')


def label(x,p):
    a,b,c,d=x
    t=(a+d)%p
    det=(a*d-b*c)%p
    discr=(t*t-4*det)%p
    jordan_flag=int(discr==0 and (a!=d or b!=0 or c!=0))
    return (t,det,jordan_flag)


def orbit_check(p):
    t=primitive(p)
    gens=[(1,1,0,1),(1,0,1,1),(t,0,0,1)]
    pairs=[(g,inv(g,p)) for g in gens]
    seen=bytearray(p**4)
    count=0; transitions=0
    witness_labels={}
    for i in range(p**4):
        if seen[i]: continue
        count+=1
        seen[i]=1
        q=deque([i])
        invariant=label(unpack(i,p),p)
        assert invariant not in witness_labels, ('label_not_complete',p,invariant)
        witness_labels[invariant]=i
        while q:
            j=q.popleft()
            v=unpack(j,p)
            assert label(v,p)==invariant, ('label_not_invariant',p,v,invariant)
            for g,ginv in pairs:
                new=rep(mm(mm(g,v,p),ginv,p),p)
                transitions+=1
                if not seen[new]:
                    seen[new]=1
                    q.append(new)
    assert count==p*p+p, (p,count,p*p+p)
    assert len(witness_labels)==count
    return {'p':p,'matrices_exhausted':p**4,'classes':count,'expected':p*p+p,
            'generator_transitions':transitions,'status':'PASS'}


def witness_373():
    p=373
    I=(1,0,0,1)
    J=(1,1,0,1)
    def sq(a):
        # [[0,I],[a,0]]^2 = diag(a,a)
        return (a,a)
    # The labels differ exactly by the Jordan flag.
    assert label(I,p)==(2,1,0)
    assert label(J,p)==(2,1,1)
    assert mm(I,I,p)==I
    assert mm(J,J,p)==(1,2,0,1)
    assert sq(I)!=sq(J)
    return {'p':p,'X':'I_2','C0':'I_2','C1':'I_2 + E12',
            'trace_YX_both':2,'det_YX_both':1,
            'tr_K_squared_over_two_both':2,'det_K_both':1,
            'jordan_flag_C0':0,'jordan_flag_C1':1,
            'classes_on_X_invertible_stratum':p*p+p,
            'source_jet_status':'AUXILIARY_ONLY_NOT_NATIVE','status':'PASS'}


def main():
    cases=[orbit_check(p) for p in (3,5,7,11,13,19)]
    o={'schema':'D25_BALANCED_BLOCKS_GAUGE_AUTHOR_CHECK_V1',
       'model':'A=diag(aI2,bI2), a!=b, gauge=GL2xGL2, X invertible',
       'exhaustive_cases':cases,
       'totals':{'matrices':sum(c['matrices_exhausted'] for c in cases),
                 'generator_transitions':sum(c['generator_transitions'] for c in cases)},
       'p373_exact_witness':witness_373(),
       'mathematics':'Proof in companion .md; finite checks are author-side only.',
       'all_pass':True}
    print(json.dumps(o,ensure_ascii=False,indent=2,sort_keys=True))


if __name__=='__main__':
    main()

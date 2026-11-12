#!/usr/bin/env python3
"""R105 exact finite-rational patchwork rank-shield certificate audit.
Scientific arithmetic uses fractions.Fraction only.
"""
from fractions import Fraction as Q
import random
import json

PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'

def frac(x):
    return x - (x.numerator // x.denominator)

def eligible(u,theta,sigma):
    t,branch=u
    j,x,a,b=sigma
    s=frac(x+(t-j)*theta); A=frac(a*theta); B=frac(b*theta)
    if A==B:return False
    return (A<=s<B) if A<B else (s>=A or s<B)

def topk(S,theta,sigma,k):
    return tuple(sorted((u for u in S if eligible(u,theta,sigma)),reverse=True)[:k])

def cutpoints(S,sigma,L,U):
    j,x,a,b=sigma
    cuts={L,U}
    for t,branch in S:
        for c,d in ((a,Q(0)),(b,Q(0)),(t-j,x),(t-j-a,x),(t-j-b,x),(a-b,Q(0))):
            if not c:continue
            e0=c*L+d; e1=c*U+d
            mn=min(e0,e1);mx=max(e0,e1)
            low=mn.numerator//mn.denominator-1
            high=mx.numerator//mx.denominator+2
            for n in range(low,high+1):
                z=(Q(n)-d)/c
                if L<=z<=U:cuts.add(z)
    return sorted(cuts)

def atomic_reps(cuts):
    return sorted(set(cuts)|{(u+v)/2 for u,v in zip(cuts,cuts[1:])})

def inspect(F,G,k,sigma,L,U):
    C=F&G; D=F^G
    cuts=cutpoints(F|G,sigma,L,U)
    atoms=atomic_reps(cuts)
    proof={}
    for u in sorted(D):
        entries=[]
        for theta in atoms:
            if not eligible(u,theta,sigma):
                entries.append(('OUT',theta,()))
            else:
                guards=tuple(v for v in sorted(C,reverse=True)
                             if v>u and eligible(v,theta,sigma))
                if len(guards)<k:
                    assert topk(F,theta,sigma,k)!=topk(G,theta,sigma,k)
                    return {'equal':False,'witness':(u,theta),'atoms':len(atoms)}
                entries.append(('IN',theta,guards))
        proof[u]=entries
    assert all(topk(F,z,sigma,k)==topk(G,z,sigma,k) for z in atoms)
    return {'equal':True,'proof':proof,'atoms':len(atoms),'cuts':cuts}

def verify_transfer(proof,newF,newG,k,sigma,L,U):
    """Proof atoms must be retained with their original verified exact cuts.
    The check is sufficient for versions whose symmetric difference is a subset
    of the original and whose retained guards meet the requested rank.
    """
    C=newF&newG; D=newF^newG
    if not D <= set(proof):return False
    for u in D:
        for typ,theta,guards in proof[u]:
            if typ=='OUT':
                assert not eligible(u,theta,sigma)
            elif len(C.intersection(guards))<k:
                return False
            else:
                assert eligible(u,theta,sigma)
                assert all(v>u and eligible(v,theta,sigma) for v in C.intersection(guards))
    return True

def main():
    rng=random.Random(10520261113)
    total=equal=unequal=transfer=cert_atom=total_wit=transfer_after_delete=0
    universe=[(t,r) for t in range(-3,5) for r in range(2)]
    for h in range(220):
        F={u for u in universe if rng.randrange(3)==0}
        G={u for u in universe if rng.randrange(3)==0}
        sig=(rng.randint(-1,1),Q(rng.randrange(1,6),7),rng.randint(-2,2),rng.randint(-2,2))
        k=rng.randint(1,3)
        L=Q(0);U=Q(1)
        r=inspect(F,G,k,sig,L,U); total+=1; cert_atom+=r['atoms']
        allreps=atomic_reps(cutpoints(F|G,sig,L,U))
        exact_equal=all(topk(F,z,sig,k)==topk(G,z,sig,k) for z in allreps)
        assert r['equal']==exact_equal
        if r['equal']:
            equal+=1
            assert verify_transfer(r['proof'],F,G,k,sig,L,U)
            transfer+=1
            C=F&G
            for v in sorted(C):
                FF=F-{v};GG=G-{v}
                if verify_transfer(r['proof'],FF,GG,k,sig,L,U):
                    assert all(topk(FF,z,sig,k)==topk(GG,z,sig,k) for z in allreps)
                    transfer_after_delete+=1
        else:
            unequal+=1;total_wit+=1
            u,z=r['witness']
            assert u in F^G and eligible(u,z,sig)
            assert len([v for v in F&G if v>u and eligible(v,z,sig)])<k
    assert equal+unequal==total

    sig=(0,Q(1,4),0,1);L=Q(2,5);U=Q(4,5)
    C={(1,0),(2,0)};u=(0,0); F=C|{u};G=C
    r=inspect(F,G,1,sig,L,U)
    assert r['equal']
    reps=atomic_reps(cutpoints(F|G,sig,L,U))
    assert all(eligible(u,z,sig) for z in reps)
    assert all(any(eligible(v,z,sig) for v in C) for z in reps)
    assert all(any(not eligible(v,z,sig) for z in reps) for v in C)
    assert eligible((2,0),Q(2,5),sig)
    assert eligible((2,0),Q(749,1000),sig)
    assert not eligible((2,0),Q(3,4),sig)
    assert eligible((1,0),Q(3,4),sig)
    assert eligible((1,0),Q(4,5),sig)
    assert not eligible((1,0),Q(2,5),sig)
    assert verify_transfer(r['proof'],F,G,1,sig,L,U)
    assert not verify_transfer(r['proof'],{u},set(),1,sig,L,U)
    assert topk({u},Q(1,2),sig,1)!=topk(set(),Q(1,2),sig,1)

    sig2=(0,Q(1,4),0,1);I=(Q(1,2),Q(2,3))
    S={(0,10),(0,11),(0,12),(0,13)};v=(0,0)
    p=inspect(S|{v},S,2,sig2,*I)
    assert p['equal']
    assert verify_transfer(p['proof'],(S-{(0,13)})|{v}, S-{(0,13)},2,sig2,*I)
    assert verify_transfer(p['proof'],(S-{(0,13),(0,12)})|{v}, S-{(0,13),(0,12)},2,sig2,*I)
    assert not verify_transfer(p['proof'],(S-{(0,13),(0,12),(0,11)})|{v}, S-{(0,13),(0,12),(0,11)},2,sig2,*I)
    assert topk({(0,10),v},Q(1,2),sig2,2)!=topk({(0,10)},Q(1,2),sig2,2)

    result={'schema':'R105_PATCHWORK_SHIELD_CERTIFICATE_V1','scientific_input_pin':PIN,
      'historical_frontier':'R104:869af6d9115bec00913af228cef7b9793b771cf3',
      'random_seed':10520261113,'random_version_pairs':total,'equal':equal,
      'unequal':unequal,'exact_rational_witnesses':total_wit,
      'exact_atom_representatives':cert_atom,
      'certificate_transfer_identity_checks':transfer,
      'guard_retaining_one_common_deletion_transfers':transfer_after_delete,
      'patchwork':{'interval':['2/5','4/5'],'k':1,'u':[0,0],
                   'common':[[1,0],[2,0]],'left_guard':[2,0],
                   'left_interval':'[2/5,3/4)','right_guard':[1,0],
                   'right_interval':'[3/4,4/5]','no_uniform_guard':True},
      'slack_example':{'k':2,'guard_count':4,'certified_common_deletion_budget':2,
                       'counterexample_at_three_deletions':'1/2'},
      'arithmetic':'exact Fraction and finite complete affine phase cuts',
      'execution':'All assertions passed'}
    with open('verification_r105.json','w') as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
    print('R105_PASS',total,equal,unequal,cert_atom,transfer_after_delete)
    return result

if __name__=='__main__':main()

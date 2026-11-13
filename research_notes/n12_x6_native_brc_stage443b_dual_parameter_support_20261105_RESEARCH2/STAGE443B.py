#!/usr/bin/env python3
"""Exact budget-parameterized native-X6 defect quotient: stdlib Python3 only."""
from collections import defaultdict, Counter
from itertools import combinations
from hashlib import sha256
import json

A, B = 0, 1
DIRECTIONS=range(12)  # +E1,-E1,...,+E6,-E6


def positions(length, defect_count):
    # Internal positions, 1-based and non-adjacent.
    for t in combinations(range(2,length),defect_count):
        if all(t[i]+1<t[i+1] for i in range(len(t)-1)):
            yield t


def path_from_positions(length, defects):
    z=[A]*length
    for i in defects: z[i-1]=B
    return tuple(z)


def slots(m,n,pP,pQ,rP,rQ):
    t=min(m,n); c=min(m-pP,n-pQ)
    v=[('P',i) for i in range(m-pP,m+1)]
    v += [('Q',i) for i in range(n-pQ,n+1)]
    if rQ:
        v += [('P',i) for i in range(n-pQ+1,min(m,n+rQ)+1)]
    if rP:
        v += [('Q',i) for i in range(m-pP+1,min(n,m+rP)+1)]
    v += [('E',i) for i in range(c+1,t+1)]
    return tuple(v)


def observed_key(P,Q,slotlist):
    return tuple((P[i-1] if typ=='P' else Q[i-1] if typ=='Q' else int(P[i-1]==Q[i-1])) for typ,i in slotlist)


def fiber_counts(m,n,kP,kQ,K,slotlist=None,key=None):
    """Weighted prefix transfer; if key given, restrict to its prescribed R bits."""
    N=max(m,n); t=min(m,n); target_d=t-K
    restrictions={}
    if key is not None:
        for (typ,i),value in zip(slotlist,key):
            c=restrictions.setdefault(i,{})
            if typ in c and c[typ]!=value: return 0
            c[typ]=value
    T={(0,0,0,0,0):1} # used P defects, used Q defects, mismatches, previous P/Q bits
    for i in range(1,N+1):
        new=defaultdict(int); req=restrictions.get(i,{})
        pxs=(0,1) if 1<i<m else (0,)
        qys=(0,1) if 1<i<n else (0,)
        for (a,b,d,u,v),weight in T.items():
            for x in pxs:
                if a+x>kP or u*x or ('P' in req and req['P']!=x): continue
                for y in qys:
                    if b+y>kQ or v*y or ('Q' in req and req['Q']!=y): continue
                    if 'E' in req and req['E']!=int(x==y): continue
                    nd=d+(int(x!=y) if i<=t else 0)
                    if nd>target_d: continue
                    new[(a+x,b+y,nd,x,y)]+=weight
        T=new
        if not T:return 0
    return sum(weight for (a,b,d,u,v),weight in T.items() if (a,b,d)==(kP,kQ,target_d))


def support_by_output_enumeration(params):
    m,n,kP,kQ,K,pP,pQ,rP,rQ=params
    ss=slots(m,n,pP,pQ,rP,rQ); mass={}; tested=0
    for code in range(1<<len(ss)):
        bits=tuple((code>>(len(ss)-1-j))&1 for j in range(len(ss)))
        tested+=1
        value=fiber_counts(m,n,kP,kQ,K,ss,bits)
        if value:mass[''.join(map(str,bits))]=value
    baseline=fiber_counts(m,n,kP,kQ,K)
    assert sum(mass.values())==baseline,(params,sum(mass.values()),baseline)
    return ss,mass,tested,baseline


def raw_fiber(params):
    m,n,kP,kQ,K,*_=params
    t=min(m,n)
    for ps in positions(m,kP):
        P=path_from_positions(m,ps)
        for qs in positions(n,kQ):
            Q=path_from_positions(n,qs)
            if sum(P[i]==Q[i] for i in range(t))==K:
                yield (P,Q)


def obs(P,Q):
    def vector(X):
        v=[0]*6
        for x in X:v[x//2]+=1 if x%2==0 else -1
        return tuple(v)
    def J(X):return tuple(sorted(Counter(zip(X,X[1:])).items()))
    return (len(P),len(Q),vector(P),vector(Q),J(P),J(Q),sum(x==y for x,y in zip(P,Q)))


def full_future_partition(histories,pP,pQ,rP,rQ):
    """Exact interning of all 12-direction labelled futures, every intermediate O."""
    memo={}; intern={}; count=0
    def signature(P,Q,ap,aq,rp,rq):
        nonlocal count
        state=(P,Q,ap,aq,rp,rq)
        if state in memo:return memo[state]
        edges=[]
        if ap<pP and len(P)>1: edges.append(('P_POP',signature(P[:-1],Q,ap+1,aq,rp,rq)))
        if aq<pQ and len(Q)>1: edges.append(('Q_POP',signature(P,Q[:-1],ap,aq+1,rp,rq)))
        if rp<rP:
            for x in DIRECTIONS:edges.append((('P_APPEND',x),signature(P+(x,),Q,ap,aq,rp+1,rq)))
        if rq<rQ:
            for y in DIRECTIONS:edges.append((('Q_APPEND',y),signature(P,Q+(y,),ap,aq,rp,rq+1)))
        sig=(obs(P,Q),tuple(edges))
        if sig not in intern:intern[sig]=len(intern)
        memo[state]=intern[sig]; count+=1
        return memo[state]
    ids=[signature(P,Q,0,0,0,0) for P,Q in histories]
    return ids,len(memo),len(intern)


def case(params, full=False, exhaustive=True):
    ss,mass,tests,total=support_by_output_enumeration(params)
    result={'parameters':params,'repair_slots':len(ss),'tested_bitstrings':tests,'raw_mass':total,'future_classes':len(mass),'max_class_mass':max(mass.values(),default=0),'min_class_mass':min(mass.values(),default=0),'mass_sha256':sha256(json.dumps(sorted(mass.items()),separators=(',',':')).encode()).hexdigest()}
    H=4*(params[2]+1)*(params[3]+1)*(min(params[0],params[1])-params[4]+1)
    result['original_transfer_H']=H
    if exhaustive:
        histories=list(raw_fiber(params))
        direct=Counter(''.join(map(str,observed_key(P,Q,ss))) for P,Q in histories)
        assert dict(direct)==mass,(params,direct,mass)
        result['raw_explicit_pairs_checked']=len(histories)
    if full:
        histories=list(raw_fiber(params)); ids,states,unique=full_future_partition(histories,params[5],params[6],params[7],params[8]);
        keys=[''.join(map(str,observed_key(P,Q,ss))) for P,Q in histories]
        assert all((ids[i]==ids[j])==(keys[i]==keys[j]) for i in range(len(keys)) for j in range(i))
        result.update({'independent_future_pairs':len(histories)*(len(histories)-1)//2,'independent_future_states':states,'unique_observation_subtrees':unique,'independent_future_classes':len(set(ids))})
    return result


def main():
    testcases=[
        ((8,8,2,1,5,2,1,1,1),False,True),
        ((9,7,2,1,4,2,1,2,1),False,True),
        ((7,8,1,2,4,1,2,1,2),False,True),
        ((8,8,2,1,7,2,1,1,1),False,True),
        ((7,8,1,2,6,1,2,1,2),False,True),
        ((5,4,1,1,2,1,1,1,1),True,True),
        ((6,4,1,1,2,1,1,1,1),True,True),
        ((7,5,1,1,3,1,1,1,1),True,True),
        ((12,11,3,3,7,1,1,1,1),False,False),
        ((17,16,5,4,9,1,1,1,1),False,False),
        ((12,11,3,3,7,0,0,0,0),False,False)
    ]
    results=[case(*p) for p in testcases]
    print(json.dumps({'marker':'STAGE443B_DUAL_PARAMETER_OUTPUT_ENUMERATION_PASS','cases':results,'all_checked':True},sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()

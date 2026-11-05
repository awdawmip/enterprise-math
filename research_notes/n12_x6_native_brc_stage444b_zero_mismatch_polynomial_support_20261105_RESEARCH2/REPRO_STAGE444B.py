#!/usr/bin/env python3
"""Stage444-B: exact positive-integer BRC support on zero-mismatch joint X6 fibers."""
from collections import Counter, defaultdict
from itertools import combinations
from hashlib import sha256
import json

A,B = 0,1
DIRECTIONS = range(12)  # 0:+E1,1:-E1,...,10:+E6,11:-E6

def slots(m,n,pP,pQ,rP,rQ):
    t=min(m,n); c=min(m-pP,n-pQ)
    z=[('P',i) for i in range(m-pP,m+1)]
    z += [('Q',i) for i in range(n-pQ,n+1)]
    if rQ: z += [('P',i) for i in range(n-pQ+1,min(m,n+rQ)+1)]
    if rP: z += [('Q',i) for i in range(m-pP+1,min(n,m+rP)+1)]
    z += [('E',i) for i in range(c+1,t+1)
          if 1<=i<=t]
    return tuple(z)

def visible_sets(m,n,pP,pQ,rP,rQ):
    """All variable observed source bits: E fixed to 1 for K=t; all zeros at endpoints."""
    u0=set();u1=set();t=min(m,n)
    for typ,i in slots(m,n,pP,pQ,rP,rQ):
        if typ=='E':continue
        j=i  # both raw paths equal at the overlap, longer path owns the tail
        if j<=t:
            if 1<j<t:u0.add(j)
        elif j<max(m,n):
            u1.add(j-t+1)
    return tuple(sorted(u0)), tuple(sorted(u1))

def cap(g,l,r):
    """Max hidden nonadjacent defects between fixed neighboring boundary bits."""
    if g==0 and l==r==1:return None
    return (max(0,g-l-r)+1)//2

def support_dp(length,k,visible):
    """Count visible binary patterns with at least one nonadjacent raw completion."""
    if k<0:return {'q':0,'visited_states':0,'transitions':0,'max_layer':0}
    anchors=(1,)+tuple(visible)+(length,)
    if not (length>=2 and tuple(sorted(set(visible)))==tuple(visible) and all(1<i<length for i in visible)):
        raise ValueError((length,visible))
    D={(0,0,0):1} # count visible ones, sum hidden capacities, previous bit
    visited=1; trans=0; maxlayer=1
    for step in range(1,len(anchors)):
        g=anchors[step]-anchors[step-1]-1
        final=step==len(anchors)-1
        nd=defaultdict(int)
        for (c,C,v),freq in D.items():
            for w in ((0,) if final else (0,1)):
                z=cap(g,v,w)
                if z is None:continue
                if c+w>k:continue
                nd[(c+w,C+z,w)]+=freq
                trans+=1
        D=nd; visited+=len(D); maxlayer=max(maxlayer,len(D))
    return {'q':sum(freq for (c,C,v),freq in D.items() if c<=k<=c+C),
            'visited_states':visited,'transitions':trans,'max_layer':maxlayer}

def gap_poly(g,l,r):
    """Coefficients: number of hidden placements of h defects, arbitrary-precision integers."""
    z=cap(g,l,r)
    if z is None:return ()
    from math import comb
    q=max(0,g-l-r)
    return tuple(comb(q-h+1,h) for h in range(z+1))

def class_mass(length,k,visible,pattern):
    assert len(visible)==len(pattern)
    anchors=(1,)+visible+(length,)
    vals=(0,)+pattern+(0,)
    c=sum(pattern)
    w=[1]
    for step in range(1,len(anchors)):
        poly=gap_poly(anchors[step]-anchors[step-1]-1,vals[step-1],vals[step])
        if not poly:return 0
        t=[0]*(len(w)+len(poly)-1)
        for i,x in enumerate(w):
            for j,y in enumerate(poly):t[i+j]+=x*y
        w=t
    return w[k-c] if 0<=k-c<len(w) else 0

def feasible_positions(length,k):
    for defects in combinations(range(2,length),k):
        if all(a+1<b for a,b in zip(defects,defects[1:])):yield defects

def raw_fiber(params):
    m,n,kP,kQ,K,*_=params
    t=min(m,n)
    if K!=t:return
    if m>=n:
        kT=kP-kQ
        if kT<0:return
        for pre in feasible_positions(n,kQ):
            for tail in feasible_positions(m-n+1,kT):
                positions=pre+tuple(n+x-1 for x in tail)
                p=[A]*m
                for i in positions:p[i-1]=B
                P=tuple(p);Q=P[:n]
                yield P,Q
    else:
        kT=kQ-kP
        if kT<0:return
        for pre in feasible_positions(m,kP):
            for tail in feasible_positions(n-m+1,kT):
                positions=pre+tuple(m+x-1 for x in tail)
                q=[A]*n
                for i in positions:q[i-1]=B
                Q=tuple(q);P=Q[:m]
                yield P,Q

def key(P,Q,ss):
    return tuple(P[i-1] if t=='P' else Q[i-1] if t=='Q' else int(P[i-1]==Q[i-1]) for t,i in ss)

def obs(P,Q):
    def v(path):
        o=[0]*6
        for z in path:o[z//2]+=1 if z%2==0 else -1
        return tuple(o)
    def J(path):return tuple(sorted(Counter(zip(path,path[1:])).items()))
    return len(P),len(Q),v(P),v(Q),J(P),J(Q),sum(a==b for a,b in zip(P,Q))

def exhaustive_future_ids(histories,pP,pQ,rP,rQ):
    memo={};intern={}
    def sig(P,Q,ap,aq,rp,rq):
        state=(P,Q,ap,aq,rp,rq)
        if state in memo:return memo[state]
        ed=[]
        if ap<pP and len(P)>1:ed.append(('P_POP',sig(P[:-1],Q,ap+1,aq,rp,rq)))
        if aq<pQ and len(Q)>1:ed.append(('Q_POP',sig(P,Q[:-1],ap,aq+1,rp,rq)))
        if rp<rP:
            for z in DIRECTIONS:ed.append((('P_APPEND',z),sig(P+(z,),Q,ap,aq,rp+1,rq)))
        if rq<rQ:
            for z in DIRECTIONS:ed.append((('Q_APPEND',z),sig(P,Q+(z,),ap,aq,rp,rq+1)))
        s=(obs(P,Q),tuple(ed))
        if s not in intern:intern[s]=len(intern)
        memo[state]=intern[s]
        return memo[state]
    return [sig(P,Q,0,0,0,0) for P,Q in histories],len(memo),len(intern)

def subset_determinization(params, max_states=100000):
    """Stage442-style NFA subset construction with exact output-prefix populations."""
    m,n,kP,kQ,K,pP,pQ,rP,rQ=params
    t=min(m,n);d=t-K;N=max(m,n)
    per_index=defaultdict(list)
    for typ,i in slots(m,n,pP,pQ,rP,rQ):per_index[i].append(typ)
    D={frozenset({(0,0,0,0,0)}):1}
    tested=1; maxlayer=1; transitions=0
    for i in range(1,N+1):
        nxt=defaultdict(int)
        for S,mass in D.items():
            by_symbol=defaultdict(set)
            for (a,b,h,u,v) in S:
                px=(0,1) if 1<i<m else (0,)
                qy=(0,1) if 1<i<n else (0,)
                for x in px:
                    if a+x>kP or (u and x):continue
                    for y in qy:
                        if b+y>kQ or (v and y):continue
                        nh=h+(int(x!=y) if i<=t else 0)
                        if nh>d:continue
                        sym=tuple((x if typ=='P' else y if typ=='Q' else int(x==y)) for typ in per_index.get(i,()))
                        by_symbol[sym].add((a+x,b+y,nh,x,y))
            for T in by_symbol.values():
                nxt[frozenset(T)]+=mass
                transitions+=1
        D=dict(nxt)
        tested+=len(D);maxlayer=max(maxlayer,len(D))
        if tested>max_states:
            return {'status':'LIMIT_REACHED','visited_subset_states':tested,'max_subset_layer':maxlayer,'subset_transitions':transitions}
    q=sum(mass for S,mass in D.items() if any((a,b,h)==(kP,kQ,d) for a,b,h,u,v in S))
    return {'status':'EXACT','q':q,'visited_subset_states':tested,'max_subset_layer':maxlayer,'subset_transitions':transitions}

def case(params, direct=False, future=False, subset=True):
    m,n,kP,kQ,K,pP,pQ,rP,rQ=params
    assert m>=3 and n>=3 and K==min(m,n) and 0<=pP<m and 0<=pQ<n
    u0,u1=visible_sets(m,n,pP,pQ,rP,rQ)
    l0=min(m,n);l1=max(m,n)-l0+1
    k0=kQ if m>=n else kP; k1=(kP-kQ if m>=n else kQ-kP)
    d0=support_dp(l0,k0,u0)
    if l1>1:d1=support_dp(l1,k1,u1)
    else:d1={'q':1 if k1==0 else 0,'visited_states':1,'transitions':0,'max_layer':1}
    q=d0['q']*d1['q']; res={'params':params,'pre_visible':u0,'tail_visible':u1,'support_classes':q,'sections':(d0,d1),'repair_slots':len(slots(m,n,pP,pQ,rP,rQ)),'stage443_candidate_keys':str(1<<len(slots(m,n,pP,pQ,rP,rQ)))}
    if direct:
        ss=slots(m,n,pP,pQ,rP,rQ)
        items=list(raw_fiber(params));groups=Counter(key(P,Q,ss) for P,Q in items)
        assert len(groups)==q,(params,len(groups),q)
        checked=0
        canonical_groups=Counter()
        for P,Q in items:
            shared=P if m>=n else Q
            b0=tuple(shared[i-1] for i in u0)
            b1=tuple(shared[min(m,n)-1+i-1] for i in u1)
            canonical_groups[(b0,b1)]+=1
        assert len(canonical_groups)==q and sorted(canonical_groups.values())==sorted(groups.values())
        for (b0,b1),mass in canonical_groups.items():
            x=class_mass(l0,k0,u0,b0)
            y=class_mass(l1,k1,u1,b1) if l1>1 else 1
            assert x*y==mass,(params,b0,b1,mass,x,y)
            checked+=1
        res.update({'raw_histories_checked':len(items),'explicit_classes':len(groups),'class_population_checks':checked,'population_sha256':sha256(json.dumps(sorted(groups.values()),separators=(',',':')).encode()).hexdigest()})
        if future:
            ids,states,unique=exhaustive_future_ids(items,pP,pQ,rP,rQ)
            keys=[key(P,Q,ss) for P,Q in items]
            assert all((ids[i]==ids[j])==(keys[i]==keys[j]) for i in range(len(items)) for j in range(i)),params
            res.update({'full_future_states':states,'full_future_observation_subtrees':unique,'full_future_pair_checks':len(items)*(len(items)-1)//2})
    if subset and max(m,n)<=32:
        sub=subset_determinization(params)
        res['subset_dfa']=sub
        if sub['status']=='EXACT':assert sub['q']==q,(params,sub['q'],q)
    return res

def main():
    tests=[
        ((7,5,1,1,5,1,1,1,1),True,True),
        ((5,7,1,1,5,1,1,1,1),True,True),
        ((6,8,1,2,6,1,1,1,1),True,True),
        ((9,12,2,4,9,2,3,2,3),True,False),
        ((8,6,2,1,6,1,1,1,1),True,True),
        ((6,6,1,1,6,1,1,1,1),True,True),
        ((9,7,2,1,7,2,1,1,2),True,False),
        ((10,8,3,2,8,2,1,2,1),True,False),
        ((12,9,3,2,9,3,2,2,2),True,False),
        ((13,9,4,2,9,3,2,2,3),True,False),
        ((15,10,4,2,10,4,3,3,2),True,False),
        ((12,12,3,3,12,4,2,2,2),True,False),
        ((18,14,5,3,14,5,3,4,4),True,False),
        ((24,19,7,5,19,8,6,6,5),False,False),
        ((32,25,10,7,25,10,9,8,10),False,False),
        ((64,48,20,14,48,25,20,20,20),False,False)
    ]
    r=[case(*x) for x in tests]
    assert all(x['support_classes']>=0 for x in r)
    sweep_cases=0;sweep_valid=0;sweep_histories=0;sweep_sum_q=0
    sweep_hash=sha256()
    for m in range(4,9):
        for n in range(4,9):
            for kp in range(3):
                for kq in range(3):
                    for pp in range(3):
                        for pq in range(3):
                            for rp in range(2):
                                for rq in range(2):
                                    params=(m,n,kp,kq,min(m,n),pp,pq,rp,rq)
                                    t=case(params,direct=True,subset=False)
                                    sweep_cases+=1
                                    sweep_valid+=int(t['support_classes']>0)
                                    sweep_histories+=t['raw_histories_checked']
                                    sweep_sum_q+=t['support_classes']
                                    sweep_hash.update((repr(params)+':'+str(t['support_classes'])+':'+str(t['raw_histories_checked'])+'\n').encode())
    sweep={'cases':sweep_cases,'nonempty_fibers':sweep_valid,'raw_history_instances':sweep_histories,'class_count_sum':sweep_sum_q,'result_sha256':sweep_hash.hexdigest()}
    print(json.dumps({'marker':'STAGE444B_ZERO_MISMATCH_POLYNOMIAL_SUPPORT_PASS','model':'positive_integer_BRC_joint_X6','method':'capacity_automaton_visible_word_count','results':r,'exhaustive_parameter_sweep':sweep,'all_checked':True},sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Stage484-B exact verifier: nonconstant native X6 shared T, 12-way future."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product
import json

D = 'ABCDEFGHIJKL'
VEC = {d: tuple((1 if j==i else 0)*sign for j in range(6))
       for i in range(6) for sign,d in [(1,D[i]),(-1,D[i+6])]}
ALPHABET = 'ABG'

def edges(w):
    return Counter(zip(w,w[1:]))

def as_edge_tuple(c):
    return tuple(c.get((a,b),0) for a in D for b in D)

def displacement(w):
    return tuple(sum(VEC[x][i] for x in w) for i in range(6))

def obs(p,q):
    return (len(p),len(q),displacement(p),displacement(q),
            as_edge_tuple(edges(p)),as_edge_tuple(edges(q)),
            sum(x==y for x,y in zip(p,q)))

def subedges(a,b):
    c=a.copy()
    for edge,n in b.items():
        c[edge]-=n
        if c[edge]<0: return None
        if c[edge]==0: del c[edge]
    return c

@lru_cache(maxsize=None)
def euler_count(length,start,end,remaining):
    if sum(t[2] for t in remaining)!=length-1:
        return 0
    if length==1:
        return int(start==end and not remaining)
    e={(a,b):n for a,b,n in remaining}
    total=0
    for (a,b),n in list(e.items()):
        if a!=start or n==0:
            continue
        e[(a,b)]-=1
        if e[(a,b)]==0: del e[(a,b)]
        total+=euler_count(length-1,b,end,
                          tuple(sorted((x,y,c) for (x,y),c in e.items())))
        e[(a,b)]=n
    return total

def ecount(length,start,end,e):
    return euler_count(length,start,end,
                       tuple(sorted((x,y,n) for (x,y),n in e.items() if n)))

def suffix_population(r,u,R,S):
    if r==0:
        return ecount(u+2,'A','A',R)
    rem=subedges(R,edges(S+'A'))
    if rem is None: return 0
    return ecount(u-r+2,'A',S[0],rem)

def exact_future_equivalence(T,q1,q2,k,h):
    initial=(T,q1,q2,0,0,0,0,())
    todo=deque([initial]); seen=set(); scanned=0
    while todo:
        p,a,b,pp,pa,qp,qa,path=todo.popleft()
        state=(p,a,b,pp,pa,qp,qa)
        if state in seen: continue
        seen.add(state); scanned+=1
        if obs(p,a)!=obs(p,b):
            return False,list(path),scanned
        if pp<k and len(p)>1:
            todo.append((p[:-1],a,b,pp+1,pa,qp,qa,path+('P_POP',)))
        if pa<k:
            for d in D:
                todo.append((p+d,a,b,pp,pa+1,qp,qa,path+('P_APPEND_'+d,)))
        if qp<h and len(a)>1 and len(b)>1:
            todo.append((p,a[:-1],b[:-1],pp,pa,qp+1,qa,path+('Q_POP',)))
        if qa<1:
            for d in D:
                todo.append((p,a+d,b+d,pp,pa,qp,qa+1,path+('Q_APPEND_'+d,)))
    return True,[],scanned

def run():
    cases=[]; total_fibers=total_pairs=total_states=total_rank=0
    max_fiber=0; strict_witnesses=[]; nontrivial_same=0
    for T in ('ABGA','ABGB','GABA','BGAB'):
        assert len(T)==4 and len(set(T))>1
        k,u=1,2
        history=[]
        for Wt in product(ALPHABET,repeat=k):
            W=''.join(Wt)
            for Ht in product(ALPHABET,repeat=u):
                H=''.join(Ht); Q=T+W+'A'+H+'A'
                history.append((Q,W,H))
        fibers=defaultdict(list)
        for Q,W,H in history:
            fibers[obs(T,Q)].append((Q,W,H))
        assert sum(map(len,fibers.values()))==len(history)
        for h in (0,1,2,3):
            r=min(h,u); case={'T':T,'k':k,'u':u,'h':h,'fiber_count':len(fibers),
                      'nontrivial_fibers':0,'class_count':0,'raw_history_count':len(history),
                      'states_scanned':0,'pair_checks':0,'rank_roundtrips':0}
            for initial,F in fibers.items():
                max_fiber=max(max_fiber,len(F))
                groups=defaultdict(list)
                for Q,W,H in F: groups[(W,H[-r:] if r else '')].append(Q)
                case['class_count']+=len(groups)
                if len(F)>1: case['nontrivial_fibers']+=1
                theta=edges(F[0][0]); rank_keys=sorted(groups)
                for idx,key in enumerate(rank_keys):
                    assert rank_keys[idx]==key
                    W,S=key
                    R=subedges(theta,edges(T+W+'A'))
                    assert R is not None
                    pop=suffix_population(r,u,R,S)
                    assert pop==len(groups[key]),(T,h,key,pop,len(groups[key]))
                    case['rank_roundtrips']+=1
                total_rank+=len(rank_keys)
                for i in range(len(F)):
                    for j in range(i+1,len(F)):
                        Q1,W1,H1=F[i]; Q2,W2,H2=F[j]
                        same_key=(W1,H1[-r:] if r else '')==(W2,H2[-r:] if r else '')
                        same_future,witness,scanned=exact_future_equivalence(T,Q1,Q2,k,h)
                        assert same_future==same_key,(T,h,F[i],F[j],witness)
                        if same_future: nontrivial_same+=1
                        elif len(strict_witnesses)<8:
                            strict_witnesses.append({'T':T,'h':h,'Q1':Q1,'Q2':Q2,
                                                      'W1':W1,'W2':W2,'H1':H1,'H2':H2,
                                                      'witness':witness})
                        case['pair_checks']+=1; case['states_scanned']+=scanned
                total_pairs+=case['pair_checks']; total_states+=case['states_scanned']
            cases.append(case); total_fibers+=len(fibers)
    return {'schema':'STAGE484B_EXACT_FINITE_V1',
            'ambient_directions':list(D),'historic_alphabet':ALPHABET,
            'T_values':['ABGA','ABGB','GABA','BGAB'],
            'fully_synchronous_future_12_direction':True,
            'cases':cases,'totals':{'configs':len(cases),
                'initial_observation_fibers_across_configs':total_fibers,
                'pair_checks':total_pairs,'visited_pair_states':total_states,
                'rank_and_population_checks':total_rank,'max_fiber_size':max_fiber,
                'same_key_distinct_raw_history_pairs':nontrivial_same,
                'example_strict_witnesses':strict_witnesses},
            'assertions':'passed'}

if __name__=='__main__':
    result=run()
    with open('STAGE484B_EXECUTED.json','w') as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
    print(json.dumps(result['totals'],ensure_ascii=False))
    for c in result['cases']:
        print(c['T'],c['h'],c['fiber_count'],c['class_count'],
              c['pair_checks'],c['states_scanned'])

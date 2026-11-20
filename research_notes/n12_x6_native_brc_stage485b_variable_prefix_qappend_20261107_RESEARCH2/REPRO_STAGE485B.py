#!/usr/bin/env python3
"""Stage485-B: exact Euler–BRC class populations and future equivalence checks."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product
import json
from pathlib import Path

D='ABCDEFGHIJKL'  # A..F = +E1..+E6; G..L = -E1..-E6
BASE='ABG'
VEC={d:tuple((1 if j==i else 0)*sgn for j in range(6))
     for i in range(6) for sgn,d in [(1,D[i]),(-1,D[i+6])]}

def edges(w): return Counter(zip(w,w[1:]))
def edgevec(c): return tuple(c.get((a,b),0) for a in D for b in D)
def disp(w): return tuple(sum(VEC[x][i] for x in w) for i in range(6))
def obs(p,q):
    return (len(p),len(q),disp(p),disp(q),edgevec(edges(p)),edgevec(edges(q)),
            sum(a==b for a,b in zip(p,q)))
def subtract(a,b):
    c=a.copy()
    for e,n in b.items():
        c[e]-=n
        if c[e]<0: return None
        if c[e]==0: del c[e]
    return c

@lru_cache(None)
def N(length,s,t,eedges):
    if sum(x[2] for x in eedges)!=length-1: return 0
    if length==1: return int(s==t and not eedges)
    e={(a,b):n for a,b,n in eedges}
    z=0
    for (a,b),n in tuple(e.items()):
        if a!=s: continue
        e[(a,b)]-=1
        if not e[(a,b)]: del e[(a,b)]
        z+=N(length-1,b,t,tuple(sorted((x,y,n) for (x,y),n in e.items())))
        e[(a,b)]=n
    return z
def ecount(length,s,t,e):
    return N(length,s,t,tuple(sorted((a,b,n) for (a,b),n in e.items() if n)))

def population_from_source(key,thetaP,thetaQ,s,m,k,u,h):
    sigma,W,S=key; r=min(h,u)
    tp=subtract(thetaP,edges(sigma))
    if tp is None: return 0
    nt=ecount(m-k,s,sigma[0],tp)
    if nt==0: return 0
    qbase=thetaP+Counter({(sigma[-1],W[0]):1})+edges(W)+Counter({(W[-1],'A'):1})
    R=subtract(thetaQ,qbase)
    if R is None: return 0
    if r==0: nh=ecount(u+2,'A','A',R)
    else:
        remain=subtract(R,edges(S+'A'))
        nh=ecount(u-r+2,'A',S[0],remain) if remain is not None else 0
    return nt*nh

def future_equal(t1,q1,t2,q2,k,h,q_append_budget=2):
    start=(t1,q1,t2,q2,0,0,0,0)
    todo=deque([start]); seen={start}; scanned=0
    while todo:
        p,a,z,b,pp,pa,qp,qa=todo.popleft(); scanned+=1
        if obs(p,a)!=obs(z,b): return False,scanned
        nxt=[]
        if pp<k and min(len(p),len(z))>1:
            nxt.append((p[:-1],a,z[:-1],b,pp+1,pa,qp,qa))
        if pa<k: nxt.extend((p+d,a,z+d,b,pp,pa+1,qp,qa) for d in D)
        if qp<h and min(len(a),len(b))>1:
            nxt.append((p,a[:-1],z,b[:-1],pp,pa,qp+1,qa))
        if qa<q_append_budget:
            nxt.extend((p,a+d,z,b+d,pp,pa,qp,qa+1) for d in D)
        for state in nxt:
            if state not in seen: seen.add(state); todo.append(state)
    return True,scanned

def run():
    k=1;u=2;m=4
    histories=[]
    for wt in product(BASE,repeat=m):
        T=''.join(wt)
        for w,h1,h2 in product(BASE,repeat=k+u):
            W=w; H=h1+h2; histories.append((T,T+W+'A'+H+'A',W,H))
    fibers=defaultdict(list)
    for x in histories: fibers[obs(x[0],x[1])].append(x)
    assert len(histories)==2187
    result={'native_future_alphabet':D,'source_alphabet':BASE,'m':m,'k':k,'u':u,
            'source_population':len(histories),'initial_fibers':len(fibers),'cases':[],
            'pair_future_checks':[],'same_key_future_checks':[]}
    candidates=[]; same=[]; used=set()
    for h in (0,1,2):
        class_count=pop_checks=max_fiber=max_class=cross_different=0
        for xs in fibers.values():
            thetaP=edges(xs[0][0]);thetaQ=edges(xs[0][1]);s=xs[0][0][0]
            r=min(h,u); groups=defaultdict(list)
            for T,Q,W,H in xs: groups[(T[-(k+1):],W,H[-r:] if r else '')].append((T,Q,W,H))
            for key,ls in groups.items():
                assert population_from_source(key,thetaP,thetaQ,s,m,k,u,h)==len(ls)
                pop_checks+=1;max_class=max(max_class,len(ls))
            class_count+=len(groups);max_fiber=max(max_fiber,len(xs))
            for i in range(len(xs)):
                for j in range(i+1,len(xs)):
                    x,y=xs[i],xs[j]
                    if x[0]!=y[0]:
                        cross_different+=1
                        if h==0 and len(candidates)<14: candidates.append((h,x,y,False))
                    if h==1 and x[0]==y[0] and x[1]!=y[1] and len(same)<14:
                        eq=(x[0][-(k+1):],x[2],x[3][-r:])==(y[0][-(k+1):],y[2],y[3][-r:])
                        same.append((h,x,y,eq))
        result['cases'].append({'h':h,'classes':class_count,'population_checks':pop_checks,
          'max_fiber':max_fiber,'max_class_population':max_class,
          'cross_T_different_key_pairs':cross_different})
    for h,x,y,eq in candidates+same:
        got,states=future_equal(x[0],x[1],y[0],y[1],k,h,2)
        assert got==eq
        result['pair_future_checks'].append({'h':h,'same_key':eq,'same_all_futures':got,'visited_states':states})
    special=[
        ('fixed_prefix_h0','ABGB','ABGB'+'A'+'A'+'AB'+'A','ABGB','ABGB'+'A'+'A'+'BA'+'A',1,0),
        ('fixed_prefix_h1','ABGB','ABGB'+'A'+'A'+'ABA'+'A','ABGB','ABGB'+'A'+'A'+'BAA'+'A',1,1),
        ('variable_prefix_h0','AABAAA','AABAAA'+'AB'+'A'+'AB'+'A','ABAAAA','ABAAAA'+'AB'+'A'+'AB'+'A',2,0)
    ]
    for label,t1,q1,t2,q2,kk,hh in special:
        assert obs(t1,q1)==obs(t2,q2)
        assert t1[-(kk+1):]==t2[-(kk+1):]
        eq,states=future_equal(t1,q1,t2,q2,kk,hh,2)
        assert eq
        result['same_key_future_checks'].append({'label':label,'k':kk,'h':hh,'visited_states':states})
    result['total_future_states']=sum(x['visited_states'] for x in result['pair_future_checks'])+sum(x['visited_states'] for x in result['same_key_future_checks'])
    result['all_assertions']='PASS'
    return result

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('STAGE485B_REPRO_OUTPUT.json').write_text(json.dumps(result,indent=2),encoding='utf8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('pair_future_checks','same_key_future_checks')},indent=2))

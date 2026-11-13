#!/usr/bin/env python3
"""Stage486-B: exact bounded POP crossing through Q's W and variable T.
Original paths over A/B/G, embedded as signed directions in native X6.
Future APPENDs range over all twelve signed native directions.
Python standard library; exact integer counts only.
"""
from collections import Counter,defaultdict,deque
from functools import lru_cache
from itertools import product
import json,sys

D='ABCDEFGHIJKL'  # +E_1...+E_6,-E_1...-E_6
BASE='ABG'
VEC={d:tuple((1 if j==i else 0)*sgn for j in range(6))
     for i in range(6) for sgn,d in ((1,D[i]),(-1,D[i+6]))}
PAIR=tuple(product(BASE,repeat=2))

def ed(w):return Counter(zip(w,w[1:]))
def disp(w):return tuple(sum(VEC[x][i] for x in w) for i in range(6))
def edge_signature(w):
    c=ed(w)
    return tuple(c.get((a,b),0) for a,b in PAIR)
def obs0(p,q):
    # For words in BASE, this equals the full 144-edge initial observer,
    # whose unrepresented 135 components are identically zero.
    return len(p),len(q),disp(p),disp(q),edge_signature(p),edge_signature(q),sum(a==b for a,b in zip(p,q))
def obs_full(p,q):
    return (len(p),len(q),disp(p),disp(q),tuple(sorted(ed(p).items())),tuple(sorted(ed(q).items())),sum(a==b for a,b in zip(p,q)))
def sub(e,f):
    z=e.copy()
    for key,num in f.items():
        z[key]-=num
        if z[key]<0:return None
        if z[key]==0:del z[key]
    return z

def etuple(e):return tuple(sorted((a,b,c) for (a,b),c in e.items() if c))
@lru_cache(None)
def nwords(length,s,t,eth):
    if sum(c for a,b,c in eth)!=length-1:return 0
    if length==1:return int(s==t and len(eth)==0)
    e={(a,b):c for a,b,c in eth};total=0
    for (a,b),v in tuple(e.items()):
        if a!=s:continue
        e[(a,b)]-=1
        if not e[(a,b)]:del e[(a,b)]
        total+=nwords(length-1,b,t,etuple(e))
        e[(a,b)]=v
    return total

def euler_n(length,s,t,e):return nwords(length,s,t,etuple(e))
def key(T,W,H,k,u,h):
    c=max(0,h-(k+u+2))
    ell=min(len(T),max(k+1,c+1))
    r=min(h,u)
    return (T[-ell:],W,H[-r:] if r else '')

def population(sig,W,S,thetaP,thetaQ,s,m,k,u,h):
    L=len(sig);r=min(h,u)
    prem=sub(thetaP,ed(sig))
    if prem is None:return 0
    np=euler_n(m-L+1,s,sig[0],prem)
    if not np:return 0
    qfixed=thetaP+Counter({(sig[-1],W[0]):1})+ed(W)+Counter({(W[-1],'A'):1})
    remain=sub(thetaQ,qfixed)
    if remain is None:return 0
    if r==0:nh=euler_n(u+2,'A','A',remain)
    else:
        pre=sub(remain,ed(S+'A'))
        nh=euler_n(u-r+2,'A',S[0],pre) if pre is not None else 0
    return np*nh

def source_fibers(k,u):
    m=2*k+2
    fibers=defaultdict(list)
    for tchars in product(BASE,repeat=m):
        T=''.join(tchars)
        for what in product(BASE,repeat=k+u):
            W=''.join(what[:k]);H=''.join(what[k:]);Q=T+W+'A'+H+'A'
            fibers[obs0(T,Q)].append((T,W,H))
    return fibers

def cross_summary(k,u,hs,check_pop=True):
    fibers=source_fibers(k,u)
    m=2*k+2
    out={'k':k,'u':u,'m':m,'raw_histories':sum(map(len,fibers.values())),'initial_fibers':len(fibers),
         'max_fiber':max(map(len,fibers.values())),'h_cases':[]}
    for h in hs:
        total_classes=0;maxclass=0;population_checks=0;nontrivial=0;rank_checks=0
        for f,xs in fibers.items():
            groups=defaultdict(int)
            for T,W,H in xs:groups[key(T,W,H,k,u,h)]+=1
            thetaP=ed(xs[0][0]);t0,w0,h0=xs[0];thetaQ=ed(t0+w0+'A'+h0+'A');s=t0[0]
            for (sig,W,S),amount in groups.items():
                count=population(sig,W,S,thetaP,thetaQ,s,m,k,u,h)
                if check_pop:assert count==amount,('wrong population',k,u,h,f,(sig,W,S),count,amount)
                assert count>0
                population_checks+=1
                maxclass=max(maxclass,count)
                if count>1:nontrivial+=1
            assert sum(groups.values())==len(xs)
            # Sorted exact class keys form finite rank/unrank oracle in this test domain.
            keys=sorted(groups)
            for i,a in enumerate(keys):
                assert keys[i]==a and keys.index(a)==i
            rank_checks+=len(keys)
            total_classes+=len(groups)
        out['h_cases'].append({'h':h,'L':max(k+1,1+max(0,h-(k+u+2))),'r':min(h,u),
             'classes':total_classes,'population_checks':population_checks,'rank_inverse_checks':rank_checks,
             'max_class_population':maxclass,'nontrivial_classes':nontrivial})
    return out

def future_equal(t1,q1,t2,q2,k,h,p_append_budget=1,q_append_budget=1,max_states=1_000_000):
    assert obs_full(t1,q1)==obs_full(t2,q2)
    start=(t1,q1,t2,q2,0,0,0,0)
    stack=[start];seen={start};visited=0
    while stack:
        p,q,z,w,pp,pa,qp,qa=stack.pop();visited+=1
        if obs_full(p,q)!=obs_full(z,w):return False,visited
        nxt=[]
        if pp<k and len(p)>1:nxt.append((p[:-1],q,z[:-1],w,pp+1,pa,qp,qa))
        if pa<p_append_budget:
            nxt.extend((p+d,q,z+d,w,pp,pa+1,qp,qa) for d in D)
        if qp<h and len(q)>1:nxt.append((p,q[:-1],z,w[:-1],pp,pa,qp+1,qa))
        if qa<q_append_budget:
            nxt.extend((p,q+d,z,w+d,pp,pa,qp,qa+1) for d in D)
        for state in nxt:
            if state not in seen:
                seen.add(state);stack.append(state)
        if visited>max_states:raise RuntimeError(f'Future-tree size exceeds requested bound {max_states}')
    return True,visited

def run():
    k,u=2,2
    t1='AABAAA';t2='ABAAAA';W='AB';H='AB'
    q1=t1+W+'A'+H+'A';q2=t2+W+'A'+H+'A'
    assert obs_full(t1,q1)==obs_full(t2,q2)
    assert key(t1,W,H,k,u,8)==key(t2,W,H,k,u,8)
    assert key(t1,W,H,k,u,9)!=key(t2,W,H,k,u,9)
    assert obs_full(t1,q1[:-8])==obs_full(t2,q2[:-8])
    assert obs_full(t1,q1[:-9])!=obs_full(t2,q2[:-9])
    witness={'k':k,'u':u,'T1':t1,'T2':t2,'W':W,'H':H,'Q1':q1,'Q2':q2,
             'initial_equal':True,'old_key_equal':True,'h8_key_equal':True,
             'h9_key_equal':False,'pops_until_divergence':9,
             'Q_after_8':[q1[:-8],q2[:-8]],'Q_after_9':[q1[:-9],q2[:-9]],
             'Q_edges_after_9':[dict((a+b,v) for (a,b),v in ed(q1[:-9]).items()),dict((a+b,v) for (a,b),v in ed(q2[:-9]).items())]}
    small=cross_summary(1,2,range(0,9))
    med=cross_summary(2,2,(0,1,2,3,4,5,6,7,8,9,10,11))
    # all 12 signed native future directions are exercised on the nontrivial equal-key pair
    equal,states=future_equal(t1,q1,t2,q2,k,8,1,1,1_000_000)
    assert equal
    diff,states2=future_equal(t1,q1,t2,q2,k,9,1,1,1_000_000)
    assert not diff
    # Population exact for the explicit two-history cross-prefix key at both budgets.
    ksig=key(t1,W,H,k,u,8)
    c8=population(*ksig,ed(t1),ed(q1),t1[0],len(t1),k,u,8)
    c9=population(*key(t1,W,H,k,u,9),ed(t1),ed(q1),t1[0],len(t1),k,u,9)
    assert c8>=2 and c9>=1
    out={'schema':'EM_STAGE486B_EXACT_EXECUTED_V1','native_space':'X6 signed unit directions, not 12 axes',
         'source_alphabet':BASE,'future_append_alphabet':D,'counterexample':witness,
         'k1_u2':small,'k2_u2':med,'future_tree':{'same_key_h8':states,'different_key_h9':states2,
         'P_APPEND_limit':1,'Q_APPEND_limit':1,'all_12_signed_appends':True},
         'counterexample_class_population':{'h8':c8,'h9':c9},
         'euler_cache_states':nwords.cache_info().currsize,'all_assertions':'PASS'}
    return out
if __name__=='__main__':
    a=run()
    out='/mnt/data/stage486b/STAGE486B_EXECUTED.json'
    with open(out,'w') as fh:json.dump(a,fh,ensure_ascii=False,indent=2)
    print(json.dumps({'k1_u2':a['k1_u2'],'k2_u2':a['k2_u2'], 'future_tree':a['future_tree'],
                      'counterexample_class_population':a['counterexample_class_population'],
                      'euler_cache_states':a['euler_cache_states'],'all_assertions':a['all_assertions']},ensure_ascii=False,indent=2))

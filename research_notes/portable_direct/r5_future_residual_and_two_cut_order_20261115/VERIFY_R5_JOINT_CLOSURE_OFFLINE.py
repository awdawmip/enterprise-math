#!/usr/bin/env python3
"""R5 two-cut exact OFFLINE max-new/min-old recourse; deterministic integer DP.
Derived strictly increasing 954-index coordinate observer; frozen source input.
Earlier single-cut 256 table is independently regenerated and compared.
"""
import json,hashlib
from collections import Counter,defaultdict
from fractions import Fraction
from bisect import bisect_right

W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
INF=10**15
NEG=-10**9
E=(3,8,9,10,27)

def frozen():
    pools={3:set(),12:set(),15:set()};n=k=mask=0
    for t in range(1,1<<15):
        bit=t&-t;i=bit.bit_length()-1;mask^=bit;sgn=1 if mask&bit else -1
        n+=sgn*W[i]; k+=sgn*K0[i]
        if n>=3 and k%36==0 and k//36 in pools:pools[k//36].add(n)
    freq=Counter(Fraction(v,q) for q,vals in pools.items() for v in vals)
    x=[0]
    for rat in sorted(freq):x.append(x[-1]+freq[rat])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]==3]
    assert len(x)==954 and len(cuts)==28
    return x,cuts

def close(x,cuts,mask):
    active={cuts[i] for i in range(len(cuts)) if (mask>>i)&1};delta=0;z=[]
    for j,v in enumerate(x):
        z.append(v-delta)
        if j in active:delta+=1
    return z

def optimizer(z,max_k=221):
    n=len(z);out=[[] for _ in z];inc=[[] for _ in z]
    pref=[INF]*n;tail=[INF]*n
    for j in range(n):
        if z[j]-z[0]<=2:pref[j]=sum(z[j]-z[t] for t in range(j))
        if z[-1]-z[j]<=2:tail[j]=sum(z[t]-z[j] for t in range(j+1,n))
        for i in range(j-1,-1,-1):
            if z[j]-z[i]>7:break
            ds=[min(z[t]-z[i],z[j]-z[t]) for t in range(i+1,j)]
            if max(ds,default=0)<=2:
                w=sum(ds);inc[j].append((i,w));out[i].append((j,w))
    C=[pref];D=[tail]
    for k in range(1,max_k):
        pr=C[-1];C.append([min((pr[i]+w for i,w in inc[j]),default=INF) for j in range(n)])
        pr=D[-1];D.append([min((w+pr[j] for j,w in out[i]),default=INF) for i in range(n)])
    J=[min(C[k-1][j]+tail[j] for j in range(n)) for k in range(1,max_k+1)]
    return out,C,D,J

def language(dp,K):
    out,C,D,J=dp;best=J[K-1];n=len(out)
    L=[{i for i in range(n) if C[r][i]+D[K-1-r][i]==best} for r in range(K)]
    A=[{i:tuple(q for q,w in out[i] if q in L[r+1] and C[r][i]+w==C[r+1][q])
        for i in L[r]} for r in range(K-1)]
    return L,A,best

def insertion(bucket,vec,path):
    if any(all(a<=b for a,b in zip(v,vec)) for v in bucket): return
    for v in list(bucket):
        if all(a<=b for a,b in zip(vec,v)):del bucket[v]
    bucket[vec]=path

def minimax(old,new,K,keep_witness=True):
    OL,OE,oj=old;NL,NE,nj=new
    a=3;b=K-85;start=16;finish=536
    assert oj==nj==2134-5*K
    assert OL[a]==NL[a]=={start} and OL[b]==NL[b]=={finish}
    verts=sorted((i,r) for r in range(a,b+1) for i in OL[r]);
    ix={v:t for t,v in enumerate(verts)};pos=[p for p,r in verts]
    preds=[[] for _ in verts];last=[-1]*len(verts)
    for r in range(a,b):
        for i in OL[r]:
            for q in OE[r][i]:
                p,t=ix[i,r],ix[q,r+1]
                preds[t].append(p)
                last[p]=max(last[p],q)
    terminal=ix[finish,b];last[terminal]=finish
    def frontier(j):
        return tuple(t for t in range(bisect_right(pos,j))
                     if last[t]>j or (j==finish and t==terminal))
    F={j:frontier(j) for r in range(a,b+1) for j in NL[r]}
    assert F[start]==(ix[start,a],) and F[finish]==(terminal,)
    def advance(i,j,vec):
        mem=dict(zip(F[i],vec))
        for t in range(bisect_right(pos,i),bisect_right(pos,j)):
            v=max((mem.get(p,NEG) for p in preds[t]),default=NEG)
            mem[t]=v+(pos[t]==j and j!=finish) if v!=NEG else NEG
        return tuple(mem.get(t,NEG) for t in F[j])
    state={start:{(0,):()}}
    max_total=1;transactions=0
    for r in range(a,b):
        nxt=defaultdict(dict)
        for i,V in state.items():
            for q in NE[r][i]:
                for vec,path in V.items():
                    insertion(nxt[q],advance(i,q,vec),path+((q,) if q!=finish else ()))
                    transactions+=1
        state=nxt
        max_total=max(max_total,sum(len(s) for s in state.values()))
    assert tuple(state)==(finish,) and len(F[finish])==1
    best=min(state[finish]);overlap=best[0]
    assert overlap>=0
    core=state[finish][best];assert len(core)==K-89
    if not keep_witness:return K-89-overlap,None,max_total,transactions
    prefix=[min(NL[0])]
    for r in range(a):prefix.append(min(NE[r][prefix[-1]]))
    assert prefix[-1]==start
    suffix=[finish]
    for r in range(b,K-1):suffix.append(min(NE[r][suffix[-1]]))
    S=prefix+list(core)+suffix
    assert len(S)==K and len(set(S))==K
    return K-89-overlap,S,max_total,transactions

def old_overlap(old,S):
    L,A,_=old;chosen=set(S)
    dp={i:int(i in chosen) for i in L[0]}
    for r in range(len(A)):
        nxt={j:NEG for j in L[r+1]}
        for i,score in dp.items():
            for j in A[r][i]:nxt[j]=max(nxt[j],score+int(j in chosen))
        dp=nxt
    return max(dp.values())

def check_geometry(z,S):
    ds=[min(abs(z[t]-z[j]) for j in S) for t in range(len(z))]
    return max(ds),sum(ds)

def run(baseline):
    x,cuts=frozen();coord={};dp={}
    for mask in range(32):
        closed=sum(1<<cut for j,cut in enumerate(E) if mask>>j&1)
        coord[mask]=close(x,cuts,closed)
        dp[mask]=optimizer(coord[mask])
    single_checks=0;full_checks=0;results=[]
    for K in range(214,222):
        languages={mask:language(dp[mask],K) for mask in range(32)}
        for cut in (8,9):
            flag=1<<E.index(cut)
            row=baseline['rows'][f'{K}_{cut}']
            expected=dict(zip(row['old_effective_mask_order'],row['recourse_by_old_mask']))
            for oldmask,ans in expected.items():
                actual,_,_,_=minimax(languages[oldmask],languages[oldmask|flag],K,False)
                assert actual==ans,(K,cut,oldmask,actual,ans)
                single_checks+=1
        for oldmask in range(32):
            if oldmask & 6:continue
            newmask=oldmask|6
            actual,S,max_total,transitions=minimax(languages[oldmask],languages[newmask],K,True)
            assert check_geometry(coord[newmask],S)==(2,2134-5*K)
            assert old_overlap(languages[oldmask],S)==K-actual
            single={cut:dict(zip(baseline['rows'][f'{K}_{cut}']['old_effective_mask_order'],baseline['rows'][f'{K}_{cut}']['recourse_by_old_mask']))
                    for cut in (8,9)}
            lb=max(single[8][oldmask],single[9][oldmask]);
            u89=single[8][oldmask]+single[9][oldmask|2];u98=single[9][oldmask]+single[8][oldmask|4]
            assert actual==lb,(K,oldmask,actual,lb)
            assert lb<=actual<=min(u89,u98)
            results.append({'K':K,'old_effective_mask':oldmask,'new_effective_mask':newmask,
                            'joint_exact_recourse':actual,'lower_from_singles':lb,
                            'upper_8then9':u89,'upper_9then8':u98,
                            'max_pareto_states_per_rank':max_total,'states_examined':transitions,
                            'witness_sha256':hashlib.sha256(json.dumps(S,separators=(',',':')).encode()).hexdigest()})
            full_checks+=1
    assert single_checks==256 and full_checks==64
    print(json.dumps({'status':'PASS_R5_JOINT_OFFLINE_MAXMIN','frozen_science_commit':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
                      'model':'derived 954-event 1D indexed-center radius-2','independent_single_cut_table_recheck':single_checks,
                      'exact_joint_checks':full_checks,
                      'largest_pareto_rank_sum':max(t['max_pareto_states_per_rank'] for t in results),
                      'results':results},indent=2,sort_keys=True))

if __name__=='__main__':
    import sys
    if len(sys.argv)!=2:raise SystemExit('Usage: script.py <committed compact single-cut table JSON>')
    run(json.load(open(sys.argv[1])))

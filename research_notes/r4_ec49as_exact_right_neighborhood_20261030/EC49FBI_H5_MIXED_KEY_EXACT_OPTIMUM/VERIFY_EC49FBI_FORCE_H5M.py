#!/usr/bin/env python3
"""Finite exact primitive-X6 candidate generation + MILP joint-trie experiment.
Frozen scientific input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Requires scipy; observation/endpoint integer exact, MILP return statuses explicitly reported.
"""
from itertools import product, permutations
from collections import defaultdict
import json,time,sys
import numpy as np
from scipy.sparse import coo_matrix
from scipy.optimize import milp, Bounds, LinearConstraint
OP={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]]
SIG=[0,0,4,1,16,32,8,2,0]
IDX={s:i for i,s in enumerate('acdefg')}
CLAUSES=[18,20,33,40]
BASE=['fe','ge','feg','gef']
L=(4,2,1);M=(6,4,1)
def key_word(w):
    st=[s for c in w for s in OP[c]]
    return tuple(sum(v==j for v in st) for j in (1,2,3))
def candidate_words(h,k):
    x,y,z=k
    a=z-1;e=z;r=x+y-h-1;f=h+1-y-2*z;g=h+1-x
    if min(a,e,r,f,g)<0: return []
    out=set()
    for i in range(r+1):
        v='a'*a+'e'*e+'c'*i+'d'*(r-i)+'f'*f+'g'*g
        if len(v)!=h: raise ValueError((h,k,v))
        out.update(''.join(q) for q in permutations(v))
    return sorted(out)
def obs(w):
    s=0
    for c in w:s=T[s][IDX[c]]
    return SIG[s]
def valid(w):
    st=[s for c in w for s in OP[c]]
    p=[0]*6
    for u in st: p[abs(u)-1]+=1 if u>0 else -1
    return p==[2,0,0,0,0,0] and obs(w)!=0

def run(limit=40, gap=0.0):
    st=time.time()
    # Trie each edge holds one signed native-X6 primitive step
    parent=[-1]; symbol=[0]; children=[{}]; termmasks=[0]
    fixed=set(); h5M_nodes=[]
    def insert(w,mask):
        at=0;st=[]
        for c in w:
            for step in OP[c]:
                st.append(step)
                if step not in children[at]:
                    children[at][step]=len(parent)
                    parent.append(at);symbol.append(step);children.append({});termmasks.append(0)
                at=children[at][step]
                if mask==-1: fixed.add(at)
        if mask>=0: termmasks[at] |= mask
    for w in BASE:insert(w,-1)
    counts={}
    for h in range(4,10):
        keys=[L,M] if h==5 else ([L] if h==4 else [M])
        wset=set().union(*(candidate_words(h,k) for k in keys))
        good=[w for w in wset if valid(w)]
        counts[h]={'raw':len(wset),'eligible':len(good),'by_key':{','.join(map(str,k)):sum(key_word(w)==k for w in good) for k in keys}}
        for w in good:
            s=obs(w); mask=0
            # clauses H4 through H8; H9 has only F/G (final two)
            if h<9:
                for i,c in enumerate(CLAUSES):
                    if s&c:mask|=1<<(4*(h-4)+i)
            else:
                if s==16:mask=1<<20
                elif s==32:mask=1<<21
            if mask:
                insert(w,mask)
                if h==5 and key_word(w)==M:
                    at=0
                    for c2 in w:
                        for step in OP[c2]:at=children[at][step]
                    h5M_nodes.append(at)
    n=len(parent)-1
    print('NODES',n,'CANDIDATE_COUNTS',json.dumps(counts,ensure_ascii=False),'BUILD_SECONDS',round(time.time()-st,2),flush=True)
    # min cost selected edges. Tree downward closure. Put all fixed nodes cost0 and lb=1.
    rows=[];cols=[];vals=[];lo=[];hi=[]
    # each x_child <= x_parent, except root
    for idx in range(1,n+1):
        par=parent[idx]
        if par>0:
            row=len(lo);rows += [row,row];cols += [idx-1,par-1];vals += [1,-1];lo.append(-np.inf);hi.append(0)
    clause_dict=[[] for _ in range(22)]
    for idx in range(1,n+1):
        mask=termmasks[idx]
        for j in range(22):
            if (mask>>j)&1:clause_dict[j].append(idx-1)
    print('CLAUSE_TERMINALS',list(map(len,clause_dict)),flush=True)
    if not all(clause_dict):raise ValueError('no eligible signature')
    for j,arr in enumerate(clause_dict):
        row=len(lo);rows.extend([row]*len(arr));cols.extend(arr);vals.extend([1]*len(arr));lo.append(1);hi.append(np.inf)
    row=len(lo);rows.extend([row]*len(h5M_nodes));cols.extend([j-1 for j in h5M_nodes]);vals.extend([1]*len(h5M_nodes));lo.append(1);hi.append(np.inf)
    A=coo_matrix((np.array(vals,dtype=float),(rows,cols)),shape=(len(lo),n)).tocsr()
    c=np.ones(n);lb=np.zeros(n);ub=np.ones(n)
    for idx in fixed: c[idx-1]=0;lb[idx-1]=1
    print('MILP',n,'constraints',len(lo),'nnz',A.nnz,'init_s',round(time.time()-st,2),flush=True)
    sol=milp(c,integrality=np.ones(n),bounds=Bounds(lb,ub),constraints=LinearConstraint(A,np.array(lo),np.array(hi)),options={'time_limit':limit,'mip_rel_gap':gap})
    report={'schema':'EC49FBI_FIXED_PAIR_JOINT_MILP','science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab', 'horizon_keys': {'H4':list(L),'H5':[list(L),list(M)],'H6_H9':list(M)}, 'frozen_H2_H3':BASE, 'candidate_counts':counts,'primitive_trie_edges':n,'prepaid_early_edges':len(fixed), 'milp_constraints':len(lo),'milp_nonzero':int(A.nnz),'forced_H5M_at_least_one':True,'optimizer_status':int(sol.status),'optimizer_message':str(sol.message),'lower_bound':float(sol.mip_dual_bound) if getattr(sol,'mip_dual_bound',None) is not None else None,'mip_gap':float(sol.mip_gap) if getattr(sol,'mip_gap',None) is not None else None,'incumbent_cost':float(sol.fun)+len(fixed) if sol.fun is not None else None,'elapsed_seconds':time.time()-st}
    if sol.x is not None:
        selected=[]
        for h in range(4,10):
            for w in set().union(*(candidate_words(h,k) for k in ([L,M] if h==5 else ([L] if h==4 else [M])))):
                if not valid(w):continue
                at=0
                for c2 in w:
                    for step in OP[c2]:at=children[at][step]
                if sol.x[at-1]>.5:selected.append([h,w,obs(w),list(key_word(w))])
        report['selected_words']=selected
    print('RESULT',json.dumps(report,ensure_ascii=False),flush=True)
    with open('/mnt/data/EC49FBI_FORCE_H5M_REPORT.json','w') as f:json.dump(report,f,indent=2,ensure_ascii=False)
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 35)

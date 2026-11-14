#!/usr/bin/env python3
"""Exact signed-X6 prefix census kernel for EC49FGC. Frozen science:
fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Requires SciPy+NumPy for MILP; all operation words are enumerated exactly.
"""
from collections import Counter,defaultdict
from functools import lru_cache
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
       'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
BASE={(2,1):'de',(2,2):'ed',(2,4):'ce',(2,8):'ec',
      (3,16):'feg',(3,32):'gef'}
PROFILE={2:'L',3:'H',4:'L',5:'H',6:'L',7:'H',8:'L',9:'H'}
SIGS={'L':(1,2,4,8),'H':(16,32)}

def unique_perms(n,cnt):
    if n==0:
        yield ''
    else:
        for ch in 'cdefg':
            if cnt[ch]>0:
                cnt[ch]-=1
                for suf in unique_perms(n-1,cnt):
                    yield ch+suf
                cnt[ch]+=1

@lru_cache(None)
def by_key(h,mode,K):
    x,y,z=K
    r=int(mode=='L')
    f=h+1-y-2*z
    g=h+1-x
    if z!=1 or x+y!=h+1+r or min(x,y,z)<1 or min(f,g)<0 or f+g!=h-1-r:
        return {}
    out=defaultdict(list)
    for c in range(r+1):
        cnt=Counter({'c':c,'d':r-c,'e':1,'f':f,'g':g})
        for w in unique_perms(h,cnt):
            q=0
            for ch in w:
                q=T[q][OPS.index(ch)]
            label=SIG[q]
            if label in SIGS[mode]:
                out[label].append(w)
    return dict(out)

def pair_keys(h):
    out=[]
    for x in range(1,h+3):
        K=(x,h+2-x,1)
        if min(K)>0 and set(by_key(h,'L',K))==set(SIGS['L']) and set(by_key(h+1,'H',K))==set(SIGS['H']):
            out.append(K)
    return out

def solve_schedule(keys,time_limit=30):
    import numpy as np
    from scipy.optimize import milp,Bounds,LinearConstraint
    from scipy.sparse import coo_matrix
    pair={h:keys[(h-4)//2] for h in range(4,10)}
    words={k:[w] for k,w in BASE.items()}
    for h in range(4,10):
        for label,options in by_key(h,PROFILE[h],pair[h]).items():
            words[h,label]=options
    assert len(words)==24 and all(words.values())
    index={():-1}; parents=[]; terminal={}
    for (h,label),options in sorted(words.items()):
        for word in options:
            signed=tuple(step for code in word for step in STEPS[code])
            par=-1
            for depth in range(1,len(signed)+1):
                prefix=signed[:depth]
                if prefix not in index:
                    index[prefix]=len(parents)
                    parents.append(par)
                par=index[prefix]
            terminal.setdefault((h,label),set()).add(par)
    n=len(parents)
    row=[];col=[];data=[];lo=[];hi=[]
    for i,parent in enumerate(parents):
        if parent>=0:
            j=len(lo)
            row.extend([j,j]);col.extend([i,parent]);data.extend([1,-1])
            lo.append(-np.inf);hi.append(0)
    for key,ends in terminal.items():
        j=len(lo)
        for i in ends:
            row.append(j);col.append(i);data.append(1)
        lo.append(1);hi.append(np.inf)
    A=coo_matrix((np.asarray(data,dtype=float),(np.asarray(row,dtype=int),np.asarray(col,dtype=int))),shape=(len(lo),n)).tocsr()
    result=milp(c=np.ones(n),integrality=np.ones(n),
        bounds=Bounds(np.zeros(n),np.ones(n)),
        constraints=LinearConstraint(A,np.array(lo),np.array(hi)),
        options={'time_limit':time_limit,'mip_rel_gap':0.0})
    info={'keys':keys,'native_prefix_variables':n,'legal_words':sum(map(len,words.values())),
          'status':result.status,'objective':result.fun,'dual':result.mip_dual_bound,
          'gap':result.mip_gap,'mip_branch_nodes':result.mip_node_count}
    if result.x is not None:
        reverse={i:p for p,i in index.items() if i>=0}
        selected={}
        for key,ends in terminal.items():
            avail=[v for v in ends if result.x[v]>.5]
            if avail:
                idx=min(avail,key=lambda i:reverse[i])
                selected[str(key)]=list(reverse[idx])
        info['selected_primitive_microstep_words']=selected
    return info

if __name__=='__main__':
    from itertools import product
    import argparse,json
    parser=argparse.ArgumentParser()
    parser.add_argument('--all',action='store_true',help='solve all 105 cases')
    parser.add_argument('--case',nargs=3,type=int,metavar=('X45','X67','X89'),
                        help='solve one schedule using first key coordinate for each pair')
    parser.add_argument('--time-limit',type=int,default=60)
    options=parser.parse_args()
    key_lists=[pair_keys(h) for h in (4,6,8)]
    assert tuple(map(len,key_lists))==(3,5,7)
    if options.case:
        keys=[(x,h+2-x,1) for h,x in zip((4,6,8),options.case)]
        assert all(k in choices for k,choices in zip(keys,key_lists))
        schedules=[tuple(keys)]
    elif options.all:
        schedules=list(product(*key_lists))
    else:
        schedules=[((4,2,1),(5,3,1),(6,4,1))]
    rows=[]
    for schedule in schedules:
        data=solve_schedule(schedule,options.time_limit)
        if data['status']!=0 or data['gap']>1e-6 or abs(data['objective']-data['dual'])>1e-5:
            raise RuntimeError('Uncertified MILP optimum: '+str(data))
        assert abs(data['objective']-round(data['objective']))<1e-5
        data['objective_integer']=round(data['objective'])
        data.pop('selected_primitive_microstep_words',None)
        rows.append(data)
        print('OPTIMUM',str(schedule),data['objective_integer'],flush=True)
    print(json.dumps({'count':len(rows),'minimum':min(r['objective_integer'] for r in rows),
                      'rows':rows},indent=2))

#!/usr/bin/env python3
"""Exact integer dual bounds for all 16 original BRC five-cache-key profiles.
Scientific input pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Original frozen model Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859.
Needs Python, numpy and scipy/HiGHS. Float duals propose an integer certificate;
all claimed bounds are checked with exact signed integer arithmetic.
"""
import json
from collections import defaultdict
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
       'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
     6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
BASE=((3,0,1),(2,1,1),(3,1,1))
EARLY=((3,3,1),(4,2,1),(5,1,1),(5,1,2))
LATE=((5,5,1),(6,4,1),(7,3,1),(7,3,2))

def words(h,key):
    x,y,z=key
    a=z-1; b=x+y-h-1; f=h+1-y-2*z; g=h+1-x
    if min(a,b,f,g)<0:return
    for c in range(b+1):
        n=[a,c,b-c,z,f,g]
        def walk(w,q):
            if len(w)==h:
                if SIG[q] in REQ[h]:yield SIG[q],w
                return
            for j,op in enumerate(OPS):
                if n[j] and T[q][j]!=8:
                    n[j]-=1
                    yield from walk(w+op,T[q][j])
                    n[j]+=1
        yield from walk('',0)

def build(keys):
    ids={'':0};par=[-1];cost=[0];kids=[{}];need=defaultdict(set)
    for h in REQ:
        for key in sorted(keys):
            for sig,w in words(h,key):
                p=0;prefix=''
                for op in w:
                    prefix+=op
                    if prefix not in ids:
                        j=len(par);ids[prefix]=j;par.append(p)
                        cost.append(len(STEPS[op]));kids.append({});kids[p][op]=j
                    p=ids[prefix]
                need[h,sig].add(p)
    assert set(need)=={(h,s) for h in REQ for s in REQ[h]}
    N=len(par)-1;rows=[];cols=[];values=[];rhs=[]
    def add(terms,b):
        row=len(rhs)
        for col,v in terms:rows.append(row);cols.append(col);values.append(v)
        rhs.append(b)
    for j in range(1,len(par)):
        if par[j]:add(((j-1,1),(par[j]-1,-1)),0)
    for h in REQ:
        for sig in REQ[h]:add(((j-1,-1) for j in need[h,sig]),-1)
    discounts=0
    for p,child in enumerate(kids):
        for a,b in (('c','f'),('d','g')):
            if a in child and b in child:
                j=N+discounts;discounts+=1
                add(((j,1),(child[a]-1,-1)),0)
                add(((j,1),(child[b]-1,-1)),0)
    c=np.asarray(cost[1:]+[-1]*discounts,dtype=np.int64)
    G=coo_matrix((np.asarray(values,dtype=np.int64),(rows,cols)),
                 shape=(len(rhs),len(c))).tocsr()
    return c,G,np.asarray(rhs,dtype=np.int64),N,discounts

def certify(c,G,h,marginals,scale=16):
    # G*x<=h, 0<=x<=1, z<=0 imply:
    # scale*c*x >= z*h + sum_j min(0,scale*c_j-(G.T*z)_j).
    # Every operation below is exact int64; magnitudes are far below 2**63.
    z=np.minimum(np.rint(np.asarray(marginals)*scale).astype(np.int64),0)
    assert len(z)==len(h) and np.all(z<=0)
    r=scale*c-G.transpose()@z
    low=int(z@h)+int(np.minimum(r,0).sum())
    return low,int(np.count_nonzero(z))

def run():
    out={'schema':'EC49FGF_INTEGER_DUAL_V1',
         'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
         'source_model_blob':'7e97065ac9a0ff70435b92ee2f4bd718c9bf1859',
         'scale':16,'profiles':[]}
    for i,a in enumerate(EARLY):
        for j,b in enumerate(LATE):
            c,G,h,n,d=build(set(BASE)|{a,b})
            res=linprog(c.astype(float),A_ub=G,b_ub=h,bounds=(0,1),method='highs')
            assert res.success,res.message
            low,nz=certify(c,G,h,res.ineqlin.marginals)
            assert low>=1760,(i,j,low)
            row={'profile':f'A{i}B{j}','K45':a,'K69':b,
                 'bound_numerator_div16':low,'nodes':n,'discounts':d,
                 'constraints':G.shape[0],'marginals_nonzero':nz,
                 'lp_approximation':float(res.fun)}
            out['profiles'].append(row)
            print(row['profile'],f'{low}/16',flush=True)
    out['global_bound_numerator_div16']=min(r['bound_numerator_div16'] for r in out['profiles'])
    assert len(out['profiles'])==16 and out['global_bound_numerator_div16']==1760
    with open('EXACT_REPORT_EC49FGF.json','w') as f:
        json.dump(out,f,indent=2);f.write('\n')
    print('CERTIFIED_16_PROFILE_GLOBAL_LOWER_BOUND',1760,'/16=110',flush=True)
if __name__=='__main__':run()

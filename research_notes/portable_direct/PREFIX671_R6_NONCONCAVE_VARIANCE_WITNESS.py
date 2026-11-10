#!/usr/bin/env python3
"""Exact BRC nonconcavity witness; 189-layer frozen statistical observer.
Standalone Python 3 standard-library Fraction/integer computation.
Scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
import json

N,DEN=189,2**18
PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
Q=F(19,128)
SAMPLE={'a':F(1,8),'b':F(5,32),'c':F(7,32),'d':F(9,32),'e':F(3,32)}

@lru_cache(None)
def inside(n,k,a):
    return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n

@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    mid=k*DEN//n
    assert inside(n,k,mid),('central',n,k)
    if k==0: left_low,left_high=0,0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            m=(lo+hi)//2
            if inside(n,k,m):hi=m
            else:lo=m
        left_low,left_high=lo,hi
    lo,hi=mid,DEN
    while hi-lo>1:
        m=(lo+hi)//2
        if inside(n,k,m):lo=m
        else:hi=m
    right_low,right_high=lo,hi
    if 4*(right_low-left_high)>DEN:return True
    if 4*(right_high-left_low)<DEN:return False
    raise AssertionError(('ambiguous predicate',n,k))

def survivor_rows():
    state={0:1};rows=[state.copy()]
    for n in range(1,N+1):
        nx=defaultdict(int)
        for k,v in state.items():nx[k]+=v;nx[k+1]+=v
        state={k:v for k,v in nx.items() if wide(n,k)}
        rows.append(state.copy())
    assert len(rows)==N+1 and not rows[N]
    assert all(sum(rows[n].values())==2**n for n in range(25))
    assert all(0<=v<=comb(n,k) for n,row in enumerate(rows) for k,v in row.items())
    return rows[:N]

def survival_vector(rows,u):
    num,den=u.numerator,u.denominator
    ps=[num**i for i in range(N+1)]
    qs=[(den-num)**i for i in range(N+1)]
    return [F(sum(v*ps[k]*qs[n-k] for k,v in row.items()),den**n) for n,row in enumerate(rows)]

def moments_at_points(rows):
    sz=survival_vector(rows,Q)
    # E[Y]=sum_n a_n(z)*s_n(p)+sum_m s_m(z);
    # E[Y^2]/2=sum_n b_n(z)*s_n(p)+sum_m(m+1)*s_m(z).
    aa=[];bb=[]
    for n in range(N):
        a,b=F(1),F(n+1)
        for m,t in enumerate(sz):
            if t==0:continue
            w=F(comb(n+m,n),2**(n+m+1))
            a-=w*t
            b-=F(n+m+1,2)*w*t
        aa.append(a);bb.append(b)
    assert all(0<=a<=1 for a in aa)
    assert all(0<=b<=n+1 for n,b in enumerate(bb))
    base_mu=sum(sz,F(0))
    base_H=sum(((m+1)*t for m,t in enumerate(sz)),F(0))
    result={}
    for tag,u in SAMPLE.items():
        sp=survival_vector(rows,u)
        mu=base_mu+sum((x*t for x,t in zip(aa,sp)),F(0))
        H=base_H+sum((x*t for x,t in zip(bb,sp)),F(0))
        W=2*H-mu**2
        assert W>0
        result[tag]=(mu,W)
    return result

def check():
    checks=0
    def ck(test,msg):
        nonlocal checks
        assert test,msg
        checks+=1
    rows=survivor_rows()
    ck(len(rows)==189 and len(rows[0])==1,'frozen row count')
    ck(rows[24].get(0)==1 and rows[25].get(0,0)==0,'25 layer boundary')
    ck(sum(map(len,rows))==9529,'count of exact surviving state entries')
    data=moments_at_points(rows)
    vals={}
    for q in (12,24):
        v={tag:q*q*W-q*mu for tag,(mu,W) in data.items()}
        for name,expr in [('a_above_b',v['a']-v['b']),
                          ('c_above_b',v['c']-v['b']),
                          ('c_above_d',v['c']-v['d'])]:
            ck(expr>0,f'{name}, q={q}')
        ck(SAMPLE['b']==(SAMPLE['e']+SAMPLE['c'])/2,'first midpoint')
        ck(SAMPLE['c']==(SAMPLE['b']+SAMPLE['d'])/2,'second midpoint')
        ck(v['b']*2<v['e']+v['c'],f'nonconcavity q={q}')
        ck(v['c']*2>v['b']+v['d'],f'nonconvexity q={q}')
        vals[q]=v
    for x,y in [('a','b'),('c','b'),('c','d')]:
        ck(vals[12][x]>vals[12][y] and vals[24][x]>vals[24][y],f'affine gap {x}-{y}')
    for x,y,z,sign in [('e','b','c','lt'),('b','c','d','gt')]:
        c12=vals[12][x]+vals[12][z]-2*vals[12][y]
        c24=vals[24][x]+vals[24][z]-2*vals[24][y]
        ck(c12>0 and c24>0 if sign=='lt' else c12<0 and c24<0,f'affine Jensen sign {y}')
    ranges={12:{'a':(51348,51349),'b':(47154,47155),'c':(49214,49215),'d':(43303,43304),'e':(61801,61802)},24:{}}
    for tag,(lo,hi) in ranges[12].items():
        ck(lo<vals[12][tag]<hi,f'q=12 rational bracket {tag}')
    gaps={}
    for q in (12,24):
        gaps[str(q)]={}
        for x,y in [('a','b'),('c','b'),('c','d')]:
            diff=vals[q][x]-vals[q][y]
            low=diff.numerator//diff.denominator
            ck(F(low)<diff<F(low+1),f'{q} gap strict unit bracket {x}-{y}')
            gaps[str(q)][f'{x}-{y}']={'lower_integer':low,'upper_integer':low+1}
        for x,y,z in [('e','b','c'),('b','c','d')]:
            diff=vals[q][x]+vals[q][z]-2*vals[q][y]
            low=diff.numerator//diff.denominator
            ck(F(low)<diff<F(low+1),f'{q} Jensen strict unit bracket {x}-{y}-{z}')
            gaps[str(q)][f'{x}-2{y}+{z}']={'lower_integer':low,'upper_integer':low+1}
    return {'schema':'EM_PREFIX671_R6_NONCONCAVE_VARIANCE_WITNESS_V1',
        'science_pin':PIN,'observer':'189_layer_two_direction_first_stop',
        'z':'19/128','p':{k:str(v) for k,v in SAMPLE.items()},
        'q_scope':'all real q in [12,24]',
        'replay':{'survivor_rows':len(rows),'surviving_coefficient_entries':sum(map(len,rows)),'arithmetic':'exact Python fractions; no floats'},
        'strict_gaps':gaps,'checks_passed':checks,'result':'ALL_CHECKS_PASS',
        'theorem':'For every real q in [12,24], Vq(p,19/128) has >=2 distinct interior stationary points on [1/8,9/32]; neither convex nor concave on that interval.',
        'status':'AUTHOR_DERIVED / EXACT_RATIONAL_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED'}

if __name__=='__main__':
    out=check()
    print(json.dumps(out,indent=2))
    print('ALL_CHECKS_PASS',out['checks_passed'])

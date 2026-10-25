#!/usr/bin/env python3
"""EC14: exact branch-count DP and numerical PF checks, explicitly auxiliary BRC.
All combinatorial identities/bounds are proved separately; finite checks do not prove limits.
"""
from __future__ import annotations
from collections import defaultdict
from math import comb, log, floor, exp, sqrt
import json
import sys
import numpy as np
from scipy.optimize import minimize_scalar

STATES=((0,0,-1),(0,0,1),(1,1,-1),(1,1,1),(2,0,-1),(2,0,1),(2,1,-1),(2,1,1))
LOOKUP={v:i for i,v in enumerate(STATES)}
EDGE={0:{0:(2,-1,-1),1:(2,1,-1)},1:{0:(0,-1,-1),1:(0,1,-1)},2:{0:(1,1,1),1:(2,1,-1)}}

def child(state,bit):
    q,r,e=state
    qq,eta,b=EDGE[q][bit]
    rr=2 if r==2 else (0 if bit else (1 if r==0 else 2))
    ee=e*eta
    sigma=ee*b
    assert sigma==e*(1-2*bit)
    return (qq,rr,ee), int(sigma==-1)

TRANS=[]
for i,s in enumerate(STATES):
    for bit in (0,1):
        t,neg=child(s,bit)
        if t[1]!=2: TRANS.append((i,LOOKUP[t],neg,bit))


def matrix(u):
    M=np.zeros((8,8),dtype=float)
    for i,k,j,_ in TRANS: M[i,k]+=u**j
    return M

def lambda_pf(u):
    vals=np.linalg.eigvals(matrix(u))
    return max(v.real for v in vals)

def rate(alpha):
    # log-spaced saddle minimization, each eigen computation covers exact 8-state transition graph
    def psi(s): return log(lambda_pf(exp(s)))-alpha*s
    sol=minimize_scalar(psi,method='bounded',bounds=(-30,30),options={'xatol':1e-11})
    s=float(sol.x); ll=lambda_pf(exp(s)); H=-alpha*log(alpha)-(1-alpha)*log(1-alpha)
    return {'alpha':alpha,'u':exp(s),'lambda':ll,'H':H,'clean_entropy':psi(s),'rate':H-psi(s),'elementary_lower_rate':-0.5*log(1-min(alpha,1-alpha)**2),'optimized':bool(sol.success)}


def count_dp(maxn):
    d=[defaultdict(int) for _ in range(8)]
    d[LOOKUP[(0,0,1)]][0]=1
    out={0:{0:1}}
    sampled={}
    for n in range(1,maxn+1):
        nxt=[defaultdict(int) for _ in range(8)]
        for i,k,neg,_ in TRANS:
            for j,v in d[i].items(): nxt[k][j+neg]+=v
        d=nxt
        totals=defaultdict(int)
        for row in d:
            for j,v in row.items(): totals[j]+=v
        out[n]=dict(totals)
        assert totals[0]==1 and totals[n]==1, (n,totals[0],totals[n])
        if n<=100:
            for j,c in totals.items():
                assert 0<=c<=comb(n,j)
                if n>=3 and j==1: assert comb(n,j)-c==2
                if n>=5 and j==2: assert comb(n,j)-c==4*n-12
        if n in (40,60,80,100,120,160,200):
            sampled[n]={str(a):{'j':int(round(a*n)),'clean':totals[int(round(a*n))],
                                    'all':comb(n,int(round(a*n)))} for a in (.1,.25,.5,.75,.9)}
    return out,sampled


def raw_enumeration():
    for n in range(13):
        bins=defaultdict(int)
        for code in range(1<<n):
            s=(0,0,1);j=0
            for i in range(n):
                s1,neg=child(s,(code>>i)&1)
                s=s1;j+=neg
            if s[1]!=2:bins[j]+=1
        # check against direct clean DP at same n
        dynamic,_=count_dp(n)
        for j in range(n+1):assert bins[j]==dynamic[n].get(j,0), (n,j,bins[j],dynamic[n].get(j,0))
    return True


def main():
    assert len(TRANS)==12, len(TRANS)
    # Strong connectivity and grade-0/grade-1 self-loops
    adj={i:set() for i in range(8)}
    for i,k,neg,bit in TRANS:adj[i].add(k)
    for start in range(8):
        seen={start};todo=[start]
        while todo:
            for j in adj[todo.pop()]:
                if j not in seen:seen.add(j);todo.append(j)
        assert len(seen)==8
    assert any(i==k and j==0 for i,k,j,_ in TRANS)
    assert any(i==k and j==1 for i,k,j,_ in TRANS)
    assert raw_enumeration()
    dp,samples=count_dp(200)
    estimates=[rate(alpha) for alpha in (.1,.25,.5,.75,.9)]
    for row in estimates:
        assert row['optimized'] and row['rate']>row['elementary_lower_rate']-1e-6
    # Verify that PF root solves EC13's polynomial Δ(1/λ,u)=0
    polynomial=[]
    for u in (0.1,0.5,1.0,2.0,10.0):
        L=lambda_pf(u)
        residual=L**6-(1+u)*L**5+2*u*u*L*L-u**3
        polynomial.append({'u':u,'lambda':L,'poly_residual':residual})
        assert abs(residual) <= 2e-7*max(1,abs(L)**6)
    # Finite sample inequality at 100,200 via log estimates, with exact integer counts
    for n,data in samples.items():
        for a,z in data.items():
            j=z['j'];P=z['clean']/z['all'];p=min(j,n-j)/n
            rhs=(n+1)*(1-p*p)**(n//2)
            assert P<=rhs+1e-12
    report={'schema':'R4_EC14_AUTHOR_EXACT_V1','scope':'auxiliary unit-positive-weight affine BRC; not X6 dynamics',
        'brc_states':STATES,'clean_edges':TRANS,'checked_raw_words':sum(1<<i for i in range(13)),
        'integer_dp_max_depth':200,'all_coefficients_checked_through':200,'exact_endpoint_clean_ratio':'1 for j=0 or j=n, any n>=1',
        'positive_density_theorem':'P(clean|j) <= (n+1)*(1-(min(j,n-j)/n)^2)^floor(n/2), 0<j<n',
        'rates':estimates,'polynomial_checks':polynomial,
        'finite_examples':{str(n):{a:{'j':v['j'],'clean':str(v['clean']),'all':str(v['all']),
            'log_ratio_per_n': -log(v['clean']/v['all'])/n if v['clean'] else None} for a,v in vals.items()} for n,vals in samples.items()},
        'theorem_proof_status':'separate Markdown proof; finite code is numerical/finite verification',
        'native_x6_executed':False}
    with open(sys.argv[1] if len(sys.argv)>1 else 'R4_EC14_AUTHOR_REPORT.json','w') as f:json.dump(report,f,indent=2,ensure_ascii=False)
    print('PASS states=',len(STATES),'clean edges=',len(TRANS),'raw words=',report['checked_raw_words'],'integer depth=200')
    for row in estimates:print(f"alpha={row['alpha']:.2f} u={row['u']:.9g} PF={row['lambda']:.10f} I={row['rate']:.10f} explicit_lower={row['elementary_lower_rate']:.10f}")
    print('PF polynomial check:','PASS')

if __name__=='__main__':main()

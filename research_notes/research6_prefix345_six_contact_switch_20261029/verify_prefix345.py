#!/usr/bin/env python3
"""Exact rational endpoint certificates for auxiliary S7-3 BRC six-orbit fibre.

Requires verified PREFIX342 source file verify_prefix342.py in same directory.
All decisions use rational interval arithmetic; no floating-point tests.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json, runpy
from sympy import Matrix, Rational as Q

upstream=Path(__file__).with_name('verify_prefix342.py')
assert upstream.is_file(), 'Supply exact PREFIX342 verifier alongside this extension.'
v=runpy.run_path(str(upstream)) # Re-evaluate upstream Banach boxes and ordered BRC path pairs.
IV=v['IV']; ci=v['ci']; zmul=v['zmul']; zconj=v['zconj']; zscalar=v['zscalar']
zdotconj=v['zdotconj']; rvec=v['rvec']; rdot=v['rdot']; imax=v['imax']; mid=v['mid']; round_frac=v['round_frac']
sources=v['sources']; ports=v['ports']; q3=v['q3']; L=v['L']; refined=v['refined']
contact5=[(0,'-'),(1,'+'),(3,'+'),(4,'+'),(5,'-')]
contact6=[(0,'-'),(1,'+'),(3,'+'),(3,'-'),(4,'+'),(5,'-')]
assert all(F(0)<x<1 for x in v['q'])

def certificate(h,contact,mode):
    # The 3rd-Port image z=phase*w lies on |z|²=q3, Im z>=h-1.
    # For 1<h<1+sqrt(q3) it is a single closed upper arc.
    y=h-1;rad=q3-y*y
    assert y>0 and rad>0
    scale=10**35
    k=isqrt(rad.numerator*scale*scale//rad.denominator)
    lo,hi=F(k,scale),F(k+1,scale)
    assert lo*lo<rad<hi*hi
    s=IV(lo,hi)
    zpm={'+':ci(s,y),'-':ci(-s,y)}
    endpoints={}
    for j,(a,w) in enumerate(zip(sources,ports)):
        for side,z in zpm.items():
            phase=zscalar(F(1)/q3,zmul(z,zconj(w)))
            endpoints[j,side]=[zmul(phase,ak) for ak in a]
    P=[rvec(endpoints[key]) for key in contact]
    dim=len(contact)-1
    D=[[b-a for a,b in zip(P[0],P[j])] for j in range(1,len(P))]
    G=[[rdot(D[i],D[j]) for j in range(dim)] for i in range(dim)]
    rhs=[G[i][i]/2 for i in range(dim)]
    G0=Matrix([[Q(t.numerator,t.denominator) for t in row] for row in
               [[round_frac(mid(G[i][j]),10**14) for j in range(dim)] for i in range(dim)]])
    assert G0.det()!=0
    B=G0.inv()
    Bf=[[F(int(B[i,j].p),int(B[i,j].q)) for j in range(dim)] for i in range(dim)]
    beta0=[sum((Bf[i][k]*mid(rhs[k]) for k in range(dim)),F(0)) for i in range(dim)]
    E=[[IV(int(i==j))-sum((Bf[i][k]*G[k][j] for k in range(dim)),IV(0))
        for j in range(dim)] for i in range(dim)]
    e=max(sum(imax(E[i][j]) for j in range(dim)) for i in range(dim))
    assert e<F(1,10**6),('Neumann failure',h,e)
    resid=[rhs[i]-sum((G[i][j]*beta0[j] for j in range(dim)),IV(0)) for i in range(dim)]
    u=[sum((Bf[i][k]*resid[k] for k in range(dim)),IV(0)) for i in range(dim)]
    delta=max(imax(t) for t in u)/(1-e)
    assert delta<F(1,10**9),('beta enclosure too broad',h,delta)
    beta=[IV(t-delta,t+delta) for t in beta0]
    weight0=IV(1)-sum(beta,IV(0))
    assert weight0.lo>F(1,100) and all(x.lo>F(1,100) for x in beta),('nonpositive weight',h)
    center_vec=[P[0][i]+sum((beta[j]*D[j][i] for j in range(dim)),IV(0)) for i in range(6)]
    center=[(center_vec[2*j],center_vec[2*j+1]) for j in range(3)]
    r2=rdot([center_vec[k]-P[0][k] for k in range(6)],
            [center_vec[k]-P[0][k] for k in range(6)])
    slacks={}
    for key,p in endpoints.items():
        if key in contact:continue
        dist2=rdot([x-y for x,y in zip(rvec(p),center_vec)],
                   [x-y for x,y in zip(rvec(p),center_vec)])
        slacks[key]=r2-dist2
    t={}
    for j,(a,w) in enumerate(zip(sources,ports)):
        tj=zscalar(F(1)/q3,zmul(zdotconj(center,a),zconj(w)))
        assert tj[1].hi<-F(3,4), ('non-convex arc',h,j)
        t[j]=tj
    if mode=='valid':
        threshold=F(1,1000) if len(contact)==5 else F(1,100)
        assert all(x.lo>threshold for x in slacks.values()),('outside candidate ball',h,slacks)
    elif mode=='old5_fails':
        assert (3,'-') in slacks and slacks[3,'-'].hi<-F(1,2000), ('old support still fits',slacks[3,'-'])
    else:raise ValueError(mode)
    # Exact algebraic Gram solution beta=G^-1 diag(G)/2, rational interval
    # enclosures above imply positivity and (if valid) full-arc containment.
    return {
      'h':str(h),'contact':[[j,side] for j,side in contact],
      'mode':mode,'R2_bracket':[str(r2.lo),str(r2.hi)],
      'minimal_contact_weight_lower':str(min([weight0.lo]+[b.lo for b in beta])),
      'max_gram_inverse_defect':str(e),'max_beta_error':str(delta),
      'endpoint_slack':{str(k):[str(v.lo),str(v.hi)] for k,v in slacks.items()},
      'imag_t_upper':{str(j):str(tj[1].hi) for j,tj in t.items()},
    }

checks=[]
checks.append(certificate(F(31,20),contact5,'valid'))
checks.append(certificate(F(39,25),contact5,'old5_fails'))
checks.append(certificate(F(39,25),contact6,'valid'))
checks.append(certificate(F(33,20),contact6,'valid'))
low,high=[F(x) for x in checks[-1]['R2_bracket']]
assert F(23503,10000)<low<=high<F(23505,10000)
assert F(23503,10000)>L
# For ALL complete sources, S(h1) contains S(h2) if 1<h1<h2,
# so MEB²(S(h)) >= MEB²(T6(33/20)) for each 1<h<=33/20.
# Antipodal pair would require Im(z) and Im(-z) >=h-1>0: impossible.
result={
 'schema':'PREFIX345_SIX_CONTACT_SUPPORT_CHANGE_CERTIFICATE_V1',
 'status':'PASS_AUTHOR_SIDE_EXACT_RATIONAL',
 'main_claim':'For every 1<h<=33/20, full S(h) is nonempty and has no antipodal feasible pair, while MEB²(S(h))>23503/10000>L. At h=33/20, the six constructed orbits have an exact algebraic 6-contact MEB; no global exhaustion used for the lower bound.',
 'precise_scope':'Static auxiliary S7-3 five-port ordered BRC path pairs; fixed exact q; retained C^3 phase; not native X6 nor phase quotient.',
 'support_change':'The old five-contact candidate is strictly valid at h=31/20; its unique five-point circumcenter fails to cover endpoint (3,-) at h=39/25. A six-contact candidate is strictly valid at h=39/25. Continuity implies at least one support transition in (31/20,39/25); first-transition uniqueness not established.',
 'six_orbit_global_exhaustiveness':'not assumed, six explicit root existence boxes rechecked using predecessor certificate',
 'source_check':'runpy executes full PREFIX342 verifier with exact 45 labeled BRC path-pair check and Banach root boxes',
 'reported_lower':'23503/10000','reported_upper_at_h_33_20':'23505/10000',
 'checks':checks,
 'next_problem':'Isolate the first support-switch root in (31/20,39/25) by a Sturm/interval monotonicity certificate; characterize the risk L-crossing near h=5/3 and independently audit full fibre exhaustiveness.'}
Path(__file__).with_name('RESULTS_PREFIX345.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(result['status'])
print('h=33/20: 23503/10000 < MEB²(T6) < 23505/10000, and > L')
print('for every 1<h<=33/20: full fibre MEB²(S(h)) > 23503/10000')
print('five-contact support fails between h=31/20 and 39/25; six-contact verified at 39/25')

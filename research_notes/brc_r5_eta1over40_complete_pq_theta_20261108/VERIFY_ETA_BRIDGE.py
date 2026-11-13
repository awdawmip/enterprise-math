#!/usr/bin/env python3
"""Exact all-real low-ratio eta bridge checker; stdlib Fraction only.
Consumes VERIFY.py, CERTIFICATES.json, ETA0_F_CERTIFICATES.json.
All-real proof is the explicit barycentric construction in LOW_RATIO_ALL_THETA.md.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from VERIFY import (ZERO,ONE,E0,E1,source,mix,check,anchor,identity)

ADD=json.loads((Path(__file__).parent/'ETA0_F_CERTIFICATES.json').read_text())

def anchor0F(p,q):
    d=ADD['certificates'][f'F_eta0_t0_p{p}_q{q}']
    y=tuple(map(F,d['y']))
    Q=[[ZERO for j in range(7)] for i in range(7)]
    for i,j,v in d['edges']:
        Q[i][j]=F(v)
    tr=(source(ZERO,p,q,ZERO),y,tuple(tuple(row) for row in Q))
    check(tr,'F')
    return tr

def normalized_eta(eta,theta,p,q):
    assert 0<=eta<=F(1,40) and 0<=theta<=1 and 0<=p<=1 and 0<=q<=1
    lam=40*eta
    theta_star=1-lam/4
    def boundary(vp,vq):
        return mix((identity(source(ONE,vp,vq,ZERO)),
                    anchor('F',F(3,4),vp,vq)),(1-lam,lam))
    if theta<=theta_star:
        wt_theta=(1-theta/theta_star,theta/theta_star)
        def G_at(vp,vq):
            low=mix((identity(source(ZERO,vp,vq,ZERO)),
                     anchor('G',ZERO,vp,vq)),(1-lam,lam))
            high=mix((identity(source(ONE,vp,vq,ZERO)),
                      anchor('G',F(3,4),vp,vq)),(1-lam,lam))
            return mix((low,high),wt_theta)
        def F_at(vp,vq):
            low=mix((anchor0F(vp,vq),anchor('F',ZERO,vp,vq)),(1-lam,lam))
            high=boundary(vp,vq)
            return mix((low,high),wt_theta)
        if 2*q<=p:
            tr=mix((G_at(ZERO,ZERO),G_at(ONE,ZERO),G_at(ONE,F(1,2))),
                   (1-p,p-2*q,2*q))
            check(tr,'G')
        else:
            a=(q-p/2)/(1-p/2)
            tr=mix((F_at(ZERO,ZERO),F_at(ZERO,ONE),
                    F_at(ONE,ONE),F_at(ONE,F(1,2))),
                   ((1-a)*(1-p),a*(1-p),a*p,(1-a)*p))
            check(tr,'F')
    else:
        h=(theta-theta_star)/(1-theta_star)
        corners=[]
        for pp,qq in ((ZERO,ZERO),(ZERO,ONE),(ONE,ZERO),(ONE,ONE)):
            corners.append(mix((boundary(pp,qq),
                                identity(source(ONE,pp,qq,eta))),(1-h,h)))
        tr=mix(corners,((1-p)*(1-q),(1-p)*q,p*(1-q),p*q))
        check(tr,'F')
    assert tr[0]==source(theta,p,q,eta)
    return tr

def scaled_eta(eta,theta,p,q,s,g,h):
    tr=normalized_eta(eta,theta,p,q)
    vv=mix((identity(E0),identity(E1),tr),(1-g,g-s,s))
    ans=mix((vv,identity(vv[1])),(1-h,h))
    assert vv[0]==(g,s,eta*s,
                   s*(F(13,40)+eta/80)*p,
                   s*(F(9,40)*eta+theta/10),
                   s*(F(3,40)+F(21,80)*eta)*q,s*theta/10)
    check(ans)
    return ans

def main():
    for key,d in ADD['certificates'].items():
        anchor0F(F(d['p']),F(d['q']))
    n=0
    for eta in map(F,('0','1/400','1/160','1/80','1/40')):
        theta_star=1-10*eta
        thetas=sorted(set(map(F,('0','1/10','29/112','1/2','2/3',
                                 '3/4','7/8','1')))|
                      {theta_star,theta_star/2,(1+theta_star)/2})
        for theta in thetas:
            for p in map(F,('0','1/4','1/2','1')):
                for q in map(F,('0','1/4','1/2','1')):
                    scaled_eta(eta,theta,p,q,ONE,ONE,ZERO)
                    n+=1
    for eta in map(F,('0','1/160','1/80','1/40')):
        for theta in map(F,('0','1/2','3/4','7/8','1')):
            for p,q in ((ZERO,ZERO),(ONE,ZERO),
                        (ONE,ONE),(F(1,3),F(3,4))):
                for g,s,h in ((F(1,2),F(1,4),F(1,3)),
                              (ONE,ZERO,ONE),(ONE,ONE,F(1,2))):
                    scaled_eta(eta,theta,p,q,s,g,h)
                    n+=1
    print('NEW_ETA_ZERO_F_ANCHORS_PASS',len(ADD['certificates']))
    print('ALL_LOW_ETA_THETA_PQ_EXACT_REGRESSIONS_PASS',n)
    print('PASS_R5_ETA_0_TO_1_OVER_40_FULL_PQ_THETA_ALL_REAL_TWO_FACE_BRIDGE')

if __name__=='__main__':
    main()

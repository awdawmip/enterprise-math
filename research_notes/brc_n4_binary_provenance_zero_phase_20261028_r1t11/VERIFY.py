#!/usr/bin/env python3
"""Exact-rational verification of the BRC N4 binary provenance zero-loss phase.
The analytic necessity proof is in PROOF.md; a finite grid is not a universal proof.
"""
from fractions import Fraction as F
from itertools import product
import json

Z, O = F(0), F(1)
N = {1: {'A': (F(1,2),F(1,2)), 'B': (F(1,2),F(3,2))},
     2: {'AU': (F(1,6),O),'AV':(F(1,3),F(1,4)),
         'BU': (F(1,4),O),'BV':(F(1,4),F(2))}}
for t in (3,4):
    N[t] = {}
    for h, (q,r) in N[t-1].items():
        e = ({'AU':F(1,10),'AV':Z,'BU':F(4,5),'BV':Z}[h] if t==3
             else Z if h=='AV0' else F(3,50) if h=='AV1' else F(1,20))
        for j,s in (('0',-1),('1',1)):
            N[t][h+j] = (q/2, r*(1+s*e))
for t in N:
    assert len(N[t])==2**t
    assert all(q>0 and r>0 for q,r in N[t].values())
    assert sum((q for q,r in N[t].values()),Z)==O
    assert sum((q*r for q,r in N[t].values()),Z)==O
    if t==2:
        for h in ('A','B'):
            q,r=N[1][h]
            kids=[N[2][h+'U'],N[2][h+'V']]
            assert sum((qq for qq,rr in kids),Z)==q
            assert sum((qq*rr for qq,rr in kids),Z)==q*r
    if t>2:
        for h, (q,r) in N[t-1].items():
            kids=[N[t][h+j] for j in ('0','1')]
            assert sum((qq for qq,rr in kids),Z)==q
            assert sum((qq*rr for qq,rr in kids),Z)==q*r

def target(a,b,ca,cb):
    assert Z<a<=O and Z<b<=O and Z<=ca<=O and Z<=cb<=O
    g={(1,'A'):(Z,O-a,a), (1,'B'):(Z,O-b,b)}
    for h,c in (('AU',ca),('BU',cb),('AV',Z),('BV',Z)):
        g[2,h]=(Z,O-c,c)
    for h in N[3]:
        g[3,h]=(O,Z,Z) if h.startswith('AU') else (Z,O,Z)
    for h in N[4]:g[4,h]=(Z,O,Z)
    return g

def necessary(a,b,ca,cb,tag):
    if tag=='AU':
        shared=ca
        m=b*(cb-ca)/4
    else:
        assert tag=='BU'
        shared=cb
        m=a*(ca-cb)/6
    x=4*m/7
    y=3*m/7
    av=3*x/a
    bv=4*y/b
    good=(m>=0 and Z<=av<=O and Z<=bv<=O)
    assert x+y==m and x/4+2*y==m
    return shared,m,x,y,av,bv,good

def repair(a,b,ca,cb,tag):
    c,m,x,y,av,bv,good=necessary(a,b,ca,cb,tag)
    assert good
    g={(1,'A'):(Z,O-a,a),(1,'B'):(Z,O-b,b)}
    for h,v in (('AU',c),('BU',c),('AV',av),('BV',bv)):
        g[2,h]=(Z,O-v,v)
    for h in N[3]:
        p=h.startswith('AU') if tag=='AU' else not h.startswith('BU')
        g[3,h]=(O,Z,Z) if p else (Z,O,Z)
    for h in N[4]:g[4,h]=(Z,O,Z)
    for t in N:
        byratio={}
        for h,(_,r) in N[t].items():
            row=g[t,h]
            assert min(row)>=Z and sum(row,Z)==O
            if t>=2:
                if r in byratio: assert row==byratio[r]
                byratio[r]=row
            if t==4:assert row[2]==Z
    return g

def law(g,tag):
    out={m:{} for m in ('Q','P')}
    for leaf,(q,r) in N[4].items():
        live=O
        for t in (1,2,3,4):
            h=leaf[:t]
            pp,qq,cc=g[t,h]
            z=int(t>=3 and h.startswith(tag))
            for dec,pr in (('P',pp),('Q',qq)):
                key=(t,dec,z)
                for m,base in (('Q',q),('P',q*r)):
                    out[m][key]=out[m].get(key,Z)+base*live*pr
            live*=cc
        assert live==Z
    for m in out:assert sum(out[m].values(),Z)==O
    return out

def case(a,b,ca,cb,tag):
    c,m,x,y,av,bv,good=necessary(a,b,ca,cb,tag)
    qf=a*(F(1,2)-ca/6)+b*(F(1,2)-cb/4)
    pf=a*(F(1,4)-ca/6)+b*(F(3,4)-cb/4)
    qg=a*(F(1,2)-c/6)+b*(F(1,2)-c/4)-x-y
    pg=a*(F(1,4)-c/6)+b*(F(3,4)-c/4)-x/4-2*y
    assert (qf,pf)==(qg,pg)
    if good:
        assert law(target(a,b,ca,cb),tag)==law(repair(a,b,ca,cb,tag),tag)
    else:
        assert m<0 or x<0 or y<0 or x>a/3 or y>b/4
    return good

def main():
    ab=(F(1,20),F(1,4),F(1,2),F(3,4),O)
    cs=(Z,F(1,4),F(1,2),F(3,4),O)
    ok={'AU':0,'BU':0}
    fail={'AU':0,'BU':0}
    for a,b,ca,cb in product(ab,ab,cs,cs):
        for tag in ('AU','BU'):
            (ok if case(a,b,ca,cb,tag) else fail)[tag]+=1
    w=(F(3,4),F(3,4),F(5,12),F(1,3))
    assert not case(*w,'AU') and case(*w,'BU')
    wb=(F(3,4),F(3,4),F(1,3),F(5,12))
    assert case(*wb,'AU') and not case(*wb,'BU')
    c,m,x,y,av,bv,_=necessary(*wb,'AU')
    assert (c,m,x,y,av,bv)==(F(1,3),F(1,64),F(1,112),F(3,448),F(1,28),F(1,28))
    assert not case(F(1,20),O,Z,O,'AU')
    assert not case(O,F(1,20),O,Z,'BU')
    print(json.dumps({'status':'PASS_EXACT_BRC_N4_BINARY_ZERO_PHASE_BOTH_ORIENTATIONS',
                      'grid_parameters':625,'grid_observer_checks':1250,
                      'zero_cases':ok,'nonzero_necessary_failure_cases':fail,
                      'positive_minimax_values':'NOT_CALCULATED',
                      'native_X6_bridge':'NOT_ESTABLISHED',
                      'admission':'AUTHOR_UNREVIEWED_NOT_ADMITTED'},
                     ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__': main()

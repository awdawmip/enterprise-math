#!/usr/bin/env python3
"""Exact Fraction verification: crossed arrivals, positive continuation, S23 repair."""
from fractions import Fraction as F
from itertools import product
import json
Z,O=F(0),F(1)
N={1:{'A':(F(1,2),F(1,2),None),'B':(F(1,2),F(3,2),None)},
   2:{'AU':(F(1,6),O,'A'),'AV':(F(1,3),F(1,4),'A'),
      'BU':(F(1,4),O,'B'),'BV':(F(1,4),F(2),'B')}}
for t in (3,4):
    N[t]={}
    for parent,(q,r,_) in N[t-1].items():
        e=({'AU':F(1,10),'AV':Z,'BU':F(4,5),'BV':Z}[parent] if t==3
           else Z if parent=='AV0' else F(3,50) if parent=='AV1' else F(1,20))
        for j,s in enumerate((-1,1)):
            N[t][parent+str(j)]=(q/2,r*(1+s*e),parent)
for t in N:
    assert len(N[t])==2**t and all(q>0 and r>0 for q,r,_ in N[t].values())
    assert sum((q for q,r,_ in N[t].values()),Z)==O
    assert sum((q*r for q,r,_ in N[t].values()),Z)==O
    if t>1:
        for parent,(q,r,_) in N[t-1].items():
            children=[(qc,rc) for qc,rc,p in N[t].values() if p==parent]
            assert len(children)==2
            assert sum((qc for qc,rc in children),Z)==q
            assert sum((qc*rc for qc,rc in children),Z)==q*r
assert N[2]['AU'][1]==N[2]['BU'][1]==O

def policy(sa,sb,cA,cB,relabel_B=Z,relabel_A=Z):
    assert all(Z<=x<=O for x in (sa,sb,cA,cB,relabel_A,relabel_B))
    d={(1,'A'):(Z,1-sa,sa),(1,'B'):(Z,1-sb,sb)}
    d[2,'AU']=(Z,1-cA,cA);d[2,'BU']=(Z,1-cB,cB)
    d[2,'AV']=(Z,O,Z);d[2,'BV']=(Z,O,Z)
    for h in N[3]:
        if h.startswith('AU'):d[3,h]=(1-relabel_A,relabel_A,Z)
        elif h.startswith('BU'):d[3,h]=(relabel_B,1-relabel_B,Z)
        else:d[3,h]=(Z,O,Z)
    for h in N[4]:d[4,h]=(Z,O,Z)
    for t in N:
        for h in N[t]:
            row=d[t,h]
            assert len(row)==3 and all(x>=0 for x in row) and sum(row,Z)==O
            assert t<4 or row[2]==Z
    return d

def law(d):
    ans={m:{(t,u):Z for t in range(1,5) for u in ('P','Q')} for m in ('Q','P')}
    for leaf,(q,r,_) in N[4].items():
        alive=O
        for t,h in enumerate((leaf[:1],leaf[:2],leaf[:3],leaf),1):
            p,qu,c=d[t,h]
            ans['Q'][t,'P']+=q*alive*p;ans['Q'][t,'Q']+=q*alive*qu
            ans['P'][t,'P']+=q*r*alive*p;ans['P'][t,'Q']+=q*r*alive*qu
            alive*=c
        assert alive==Z
    for m in ans:assert sum(ans[m].values(),Z)==O
    return ans

def tv(x,y,m):return sum((abs(x[m][k]-y[m][k]) for k in x[m]),Z)/2

def admissible_S23(d):
    for t in (2,3,4):
        groups={}
        for h,(_,r,_) in N[t].items():groups.setdefault(r,[]).append(h)
        for group in groups.values():
            assert all(d[t,h]==d[t,group[0]] for h in group)

def run(delta,theta,c0,c1):
    sa0,sb0=O,O-delta;sa1,sb1=O-delta,O
    a=(1-theta)*sa0+theta*sa1
    b=(1-theta)*sb0+theta*sb1
    assert a>0 and b>0
    xA=(1-theta)*sa0*c0+theta*sa1*c1
    xB=(1-theta)*sb0*c0+theta*sb1*c1
    cA,cB=xA/a,xB/b
    target=law(policy(a,b,cA,cB))
    e0=law(policy(sa0,sb0,c0,c0));e1=law(policy(sa1,sb1,c1,c1))
    for m in ('Q','P'):
        for k in target[m]:assert target[m][k]==(1-theta)*e0[m][k]+theta*e1[m][k]
    defect=xA*b-xB*a
    assert defect==theta*(1-theta)*delta*(2-delta)*(c0-c1)
    wA=a/F(6);wB=b/F(4);W=wA+wB
    cbar=(wA*cA+wB*cB)/W
    if cA>=cB:
        fB=wA*(cA-cB)/(W*cbar) if cbar else Z
        fA=Z
    else:
        fA=wB*(cB-cA)/(W*cbar) if cbar else Z
        fB=Z
    assert Z<=fA<=O and Z<=fB<=O
    repaired=policy(a,b,cbar,cbar,relabel_B=fB,relabel_A=fA)
    admissible_S23(repaired)
    assert law(repaired)==target
    frozen=law(policy(a,b,cbar,cbar))
    val=wA*wB/W*abs(cA-cB)
    assert tv(frozen,target,'Q')==tv(frozen,target,'P')==val
    assert val==abs(defect)/(2*(2*a+3*b))
    return dict(delta=str(delta),theta=str(theta),c0=str(c0),c1=str(c1),
                cA=str(cA),cB=str(cB),cross_defect_C=str(defect),
                q_arrival_A=str(wA),q_arrival_B=str(wB),
                shared_continue=str(cbar),relabel_A_Q=str(fA),
                relabel_B_P=str(fB),frozen_future_minimax=str(val),
                full_S23_tv_Q='0',full_S23_tv_P='0')

def main():
    count=0
    for d,t,c0,c1 in product([F(0),F(1,5),F(1,2),F(3,4)],
                             [F(0),F(1,6),F(1,2),F(5,6),F(1)],
                             [F(0),F(1,4),F(1,2),F(3,4),F(1)],
                             [F(0),F(1,4),F(1,2),F(3,4),F(1)]):
        run(d,t,c0,c1);count+=1
    w=run(F(1,2),F(1,2),F(1,2),F(1,4))
    assert w['cross_defect_C']=='3/64'
    assert w['cA']=='5/12' and w['cB']=='1/3'
    assert w['q_arrival_A']=='1/8' and w['q_arrival_B']=='3/16'
    assert w['shared_continue']=='11/30'
    assert w['relabel_B_P']=='1/11' and w['relabel_A_Q']=='0'
    assert w['frozen_future_minimax']=='1/160'
    print(json.dumps({'status':'PASS_EXACT_N4_POSITIVE_CONTINUATION_TAIL_RELABEL',
                      'grid_count':count,'witness':w,
                      'all_real_claim':'algebraic theorem in PROOF.md'},
                     ensure_ascii=False,indent=2,sort_keys=True))
if __name__=='__main__':main()

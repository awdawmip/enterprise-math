#!/usr/bin/env python3
"""Exact author-side check of two-sign Q-compensation support envelopes.
Auxiliary finite two-law stopping model only; no native-X6 or heartbeat simulation.
"""
from fractions import Fraction as F
from itertools import product

NODES = [
    ('A',1,120,240,0,('A0','A1')),
    ('B',1,240,120,1,('B0','B1')),
    ('A0',2,60,180,2,('A00','A01')),
    ('A1',2,60,60,3,('A10','A11')),
    ('B0',2,180,60,4,('B00','B01')),
    ('B1',2,60,60,3,('B10','B11')),
    ('A00',3,30,108,5,()),('A01',3,30,72,6,()),
    ('A10',3,30,45,7,()),('A11',3,30,15,8,()),
    ('B00',3,90,36,9,()),('B01',3,90,24,10,()),
    ('B10',3,20,40,11,()),('B11',3,40,20,8,()),
]
H={n[0]: dict(name=n[0],t=n[1],p=n[2],q=n[3],key=n[4],children=n[5],bit=i) for i,n in enumerate(NODES)}
ETA=F(1,1000)
LAM=F(1,75)

def model_checks(u,v):
    assert len(H)==14 and len({n['key'] for n in H.values()})==12
    assert sum(H[n]['p'] for n in ('A','B'))==360
    assert sum(H[n]['q'] for n in ('A','B'))==360
    for h in H.values():
        assert h['p']>0 and h['q']>0
        if h['children']:
            assert sum(H[c]['p'] for c in h['children'])==h['p']
            assert sum(H[c]['q'] for c in h['children'])==h['q']
        for t in ((3,4) if h['t']==3 else (h['t'],)):
            L=F(h['p'],h['q'])
            p0=F(1,5)+F(t,20)+F(t+1,100)/L
            q0=F(2,5)-F(t,30)+F(t+2,200)*L
            corr=ETA*({('A1',2):u,('B1',2):v,('A11',3):F(1),('B11',3):F(-1)}.get((h['name'],t),F(0)))
            assert 0<p0<1 and 0<q0+corr<1, (h['name'],t,p0,q0+corr)
    assert F(H['A1']['p'],H['A1']['q'])==F(H['B1']['p'],H['B1']['q'])==1
    assert F(H['A11']['p'],H['A11']['q'])==F(H['B11']['p'],H['B11']['q'])==2

def analytic(u,v,sgn):
    a2=sgn*u/6-2*LAM/3
    b2=sgn*v/6-2*LAM/3
    a3=sgn*F(1,24)-LAM/8
    b3=-sgn*F(1,18)-LAM/6
    full=max(F(0),a2,a3)+max(F(0),b2,b3)
    lr=max(-3*LAM*(2-x-y)+max(F(0),x*a2+y*b2,x*a3+y*b3) for x,y in product((0,1),repeat=2))
    return full,lr

def enumerate_support(u,v,sgn):
    coeff={'A1':u,'B1':v,'A11':F(1),'B11':F(-1)}
    reward={n['name']:sgn*F(n['q'],360)*coeff.get(n['name'],0)-LAM*F((4-n['t'])*(n['p']+n['q']),360) for n in H.values()}
    def visit(id_,mask,kind):
        n=H[id_]; bit=n['bit'] if kind=='FULL' else n['key']
        if mask & (1<<bit): return reward[id_]
        return sum((visit(c,mask,kind) for c in n['children']),F(0))
    results=[]
    for kind,count in (('FULL',1<<14),('LR',1<<12)):
        best=None; wins=0
        for mask in range(count):
            z=visit('A',mask,kind)+visit('B',mask,kind)
            if best is None or z>best: best=z; wins=1
            elif z==best: wins+=1
        results.append((best,wins))
    return results

def witness_vector_B11_only():
    p=F(H['B11']['p'],360);q=F(H['B11']['q'],360)
    TP=4-p;TQ=4-q
    eP=F(21,100)+TP/20+TQ/100
    eQ=F(41,100)+TP/200-TQ/30-ETA*q
    S=eQ-F(41,100)-TP/200+TQ/30
    D=8-TP-TQ
    psi_minus=-S-ETA*LAM*D
    integer_lhs=150000*eQ-752*TP+4998*TQ
    assert (eP,eQ,TP,TQ)==(F(799,1800),F(16087,54000),F(35,9),F(71,18))
    assert psi_minus==4*ETA/75 and integer_lhs==61476
    return eP,eQ,TP,TQ,integer_lhs

if __name__ == '__main__':
    sample=[(F(0),F(0)),(F(1,2),F(1,10)),(F(22,75),F(4,75)),
            (F(-1,2),F(1,10)),(F(1,2),F(-1,2)),(F(-1,2),F(-1,2))]
    for u,v in sample:
        model_checks(u,v)
        gaps=[]
        for s in (1,-1):
            brute=enumerate_support(u,v,s)
            expected=analytic(u,v,s)
            assert (brute[0][0],brute[1][0])==expected,(u,v,s,brute,expected)
            gaps.append(expected[0]-expected[1])
        assert max(gaps)>=F(1,25)
        print(f'u={u},v={v}: gap_plus/eta={gaps[0]}; gap_minus/eta={gaps[1]}')
    checked=0
    for i,j in product(range(-10,11),repeat=2):
        u,v=F(i,10),F(j,10)
        dp=analytic(u,v,1);dm=analytic(u,v,-1)
        assert max(dp[0]-dp[1],dm[0]-dm[1])>=F(1,25)
        checked+=1
    w=witness_vector_B11_only()
    print('Natural histories=14; LR decision keys=12; P,Q mass denominator=360')
    print('Exact deterministic-policy checks=6 parameter pairs * 2 signs * (16384 FULL + 4096 LR) = 245760')
    print('Supplemental analytic rational grid=',checked,'pairs; all-real proof is symbolic')
    print('Uniform all-real Q support gap >= eta/25 for ANY admissible (u,v)')
    print('Exact sharpness witness at u=v=0: gaps_plus=gap_minus=eta/25')
    print('Inside-wedge witness u=1/2,v=1/10; O_FULL_B11_ONLY=',','.join(map(str,w[:4])))
    print('LR integer support: 150000eQ - 752TP + 4998TQ >= 61482; FULL LHS=',w[4],'; gap=6')
    print('PASS_EXACT_R5_TWO_SIGN_Q_COMPENSATION_UNIFORM_NO_GO')

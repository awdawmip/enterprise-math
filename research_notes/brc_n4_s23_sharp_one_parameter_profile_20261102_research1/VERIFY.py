#!/usr/bin/env python3
"""Exact BRC S23 six-witness one-parameter minimax certificate.

Python standard library only. Executed finite checks certify the explicit dual
hypergraph and primal endpoint data. Continuum inference uses affine/convex
interpolation as established in PROOF.md.
"""
from fractions import Fraction as F
from itertools import combinations
import json

M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
   (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
AA=(0,0,0,1,1,1);BB=(2,2,3,2,2,4);CC=(5,6,7,8,9,10)
GROUP=(0,0,1,2,2,3)
BASE=('34 24 34 24','34 23 34 34','34 34 34 23',
      '24 24 12 12','12 12 24 34','12 13 23 24',
      '23 34 12 13','24 34 12 14')

def prepared(z):
    latent=[]
    for s in range(6):
        a,b,c=z[AA[s]],z[BB[s]],z[CC[s]]
        latent.append((a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c)))
    return tuple(tuple(sum((F(M[i][s],20)*latent[s][j] for s in range(6)),F(0))
                       for j in range(4)) for i in range(6))

def decoded(d):
    return tuple(tuple(sum((F(M[i][s],20)*d[GROUP[s]][j] for s in range(6)),F(0))
                       for j in range(4)) for i in range(6))

def pair(s):
    rows=[]
    for ab in s.split():
        row=[F(0)]*4
        for c in ab:row[int(c)-1]+=F(1,2)
        rows.append(tuple(row))
    return tuple(rows)

def tv(p,q):return sum((abs(a-b) for a,b in zip(p,q)),F(0))/2
def loss(p,q):return max(tv(a,b) for a,b in zip(p,q))
def O(s,t):return (s,t,F(0),F(0),F(0),F(0),F(1),F(1),F(1),F(0),F(1))
def N(s,t):return (s,t,F(0),F(0),F(0),F(1),F(0),F(0),F(0),F(0),F(0))

Z={'W':(F(1),F(0),F(0),F(0),F(1),F(0),F(0),F(0),F(0),F(0),F(0)),
   'J':(F(1),F(1,3),F(0),F(0),F(0),F(0),F(0),F(0),F(0),F(1),F(0)),
   'A':O(F(1,7),F(1)),'B':O(F(1),F(1,7)),
   'C':N(F(1,7),F(1))}
P={k:prepared(v) for k,v in Z.items()}
Q=[decoded(pair(s)) for s in BASE]

D9=((F(9,14),F(0),F(5,14),F(0)),
    (F(9,14),F(0),F(0),F(5,14)),
    (F(1,2),F(0),F(0),F(1,2)),
    (F(1,2),F(1,2),F(0),F(0)))
D10=((F(41,63),F(0),F(22,63),F(0)),
     (F(41,63),F(0),F(22,63),F(0)),
     (F(29,45),F(0),F(29,315),F(83,315)),
     (F(31,63),F(0),F(22,63),F(10,63)))
D2RIGHT=((F(41,63),F(0),F(22,63),F(0)),
     (F(41,63),F(0),F(0),F(22,63)),
     (F(29,45),F(0),F(29,315),F(83,315)),
     (F(31,63),F(0),F(22,63),F(10,63)))
D1=((F(9,14),F(0),F(5,14),F(0)),
    (F(9,14),F(0),F(5,14),F(0)),
    (F(1,2),F(0),F(0),F(1,2)),
    (F(1,2),F(1,2),F(0),F(0)))
D2LEFT=((F(71,105),F(0),F(34,105),F(0)),
        (F(71,105),F(0),F(0),F(34,105)),
        (F(3,5),F(0),F(1,15),F(1,3)),
        (F(7,15),F(0),F(2,5),F(2,15)))

def d2(t):
    w=(t-F(1,15))/(F(1,7)-F(1,15))
    assert F(0)<=w<=F(1)
    return tuple(tuple((1-w)*a+w*b for a,b in zip(x,y))
                 for x,y in zip(D2LEFT,D2RIGHT))

def probs(t):
    out=dict(P);out['X']=prepared(O(F(1),t))
    return out

def event_sum(pp,letters,row,event_string):
    es=event_string.split('/')
    assert len(es)==len(letters)
    atoms=[int(c)-1 for part in es for c in part if c!='-']
    assert len(atoms)==len(set(atoms)) and all(0<=a<=3 for a in atoms)
    return sum((sum((pp[k][row-1][int(c)-1] for c in ev if c!='-'),F(0))
                for k,ev in zip(letters,es)),F(0))

FIVE={
  'WJA':(6,'2/4/13',F(8,3)),
  'WJB':(6,'2/14/3',F(20,7)),
  'WJC':(6,'2/4/13',F(8,3)),
  'WAB':(6,'2/1/34',F(20,7)),
  'WAC':(3,'1/3/24',F(19,7)),
  'JAB':(6,'4/1/23',F(53,21)),
  'JAC':(3,'1/3/24',F(19,7)),
  'JBC':(6,'4/3/12',F(53,21)),
  'WBC':(6,'2/3/14',F(20,7)),
  'ABC':(3,'3/1/24',F(19,7))}
SIX={
  'WJX':(6,'2/14/3','three_minus_t'),
  'JAC':(3,'1/3/24','nineteen_over_seven'),
  'WAX':(6,'2/1/34','three_minus_t'),
  'JCX':(6,'4/1/23','eight_thirds_minus_t'),
  'WJC':(6,'2/4/13','eight_thirds'),
  'WJA':(6,'2/4/13','eight_thirds'),
  'WCX':(6,'2/1/34','three_minus_t'),
  'WAC':(3,'1/3/24','nineteen_over_seven'),
  'JAX':(6,'4/1/23','eight_thirds_minus_t'),
  'ACX':(3,'3/4/12','nineteen_over_seven')}

def expected(kind,t):
    return {'three_minus_t':F(3)-t,
            'nineteen_over_seven':F(19,7),
            'eight_thirds_minus_t':F(8,3)-t,
            'eight_thirds':F(8,3)}[kind]

def radius(t):return max(F(32,63),min(F(1,2)+t/2,F(5,9)-t/3))

def check():
    assert len(FIVE)==10 and set(FIVE)==set(''.join(x) for x in combinations('WJABC',3))
    assert len(SIX)==10
    assert len(Q)==8 and len(P)==5
    for k,p in P.items():
        assert all(sum(row)==1 and min(row)>=0 for row in p)
    for d in (D9,D10,D1,D2LEFT,D2RIGHT):
        assert len(d)==4 and all(sum(row)==1 and min(row)>=0 for row in d)
    old_min={k:min(loss(p,q) for q in Q) for k,p in P.items()}
    assert old_min=={'W':F(1),'J':F(2,3),'A':F(4,7),'B':F(4,7),'C':F(4,7)}
    for letters,(row,events,total) in FIVE.items():
        assert event_sum(P,letters,row,events)==total
        assert (total-1)/3>=F(32,63)
    colors_32=[]
    for mask in range(32):
        colors={'W':0}
        colors.update((k,(mask>>i)&1) for i,k in enumerate('JABCX'))
        mono=[tri for tri in SIX if len({colors[k] for k in tri})==1]
        assert mono,(mask,colors)
        colors_32.append(mono[0])
    verified_endpoints=[]
    for t in (F(0),F(1,63),F(1,15),F(1,7)):
        pp=probs(t)
        assert all(sum(row)==1 and min(row)>=0 for p in pp.values() for row in p)
        r1=F(1,2)+t/2; r2=F(5,9)-t/3
        assert all(loss(pp['X'],q)==1 for q in (Q[i] for i in (0,1,2,3,5,6,7)))
        assert loss(pp['X'],Q[4])==r1
        for tri,(row,events,kind) in SIX.items():
            total=event_sum(pp,tri,row,events)
            assert total==expected(kind,t),(tri,t,total)
            assert (total-1)/3>=min(r1,r2),(tri,t)
        verified_endpoints.append({'t':str(t),'r':str(radius(t)),
            'X_fixed8_min':str(min(loss(pp['X'],q) for q in Q))})
    q9,q10=decoded(D9),decoded(D10)
    assert all(min(loss(P[k],q9),loss(P[k],q10))<=F(32,63) for k in 'WJABC')
    q1=decoded(D1)
    assert all(loss(P[k],q1)<=F(1,2) for k in 'WA')
    endpoint_risks={}
    for t in (F(1,15),F(1,7)):
        pp=probs(t);D=d2(t);q2=decoded(D)
        assert all(sum(row)==1 and min(row)>=0 for row in D)
        rr=F(5,9)-t/3
        assert all(loss(pp[k],q2)<=rr for k in 'JBCX')
        endpoint_risks[str(t)]={k:str(loss(pp[k],q2)) for k in 'JBCX'}
    samples=105
    for i in range(samples):
        t=F(i,7*(samples-1));pp=probs(t)
        if t<=F(1,15):bank=Q+[q9,q10]
        else:bank=Q+[q1,decoded(d2(t))]
        risk=max(min(loss(pp[k],q) for q in bank) for k in 'WJABCX')
        assert risk==radius(t),(t,risk,radius(t))
    return {
      'result':'PASS_BRC_N4_S23_SIX_WITNESS_SHARP_ONE_PARAMETER_PROFILE_20261102',
      'scientific_input_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
      'theorem':'inf over arbitrary real stochastic D9,D10; fixed D1..D8; six full prepared rows',
      'formula':'max(32/63, min(1/2+t/2, 5/9-t/3)), t in [0,1/7]',
      'unique_peak_t':'1/15','unique_peak_radius':'8/15',
      'flat_region':'[0,1/63]','flat_radius':'32/63',
      'five_triple_exact_certificates':len(FIVE),
      'six_triple_exact_certificates':len(SIX),
      'six_witness_two_colorings_exhausted':len(colors_32),
      'all_32_colorings_blocked':True,
      'exact_endpoint_checks':verified_endpoints,
      'second_interval_endpoint_D2_risks':endpoint_risks,
      'rational_regression_points':samples,
      'analytic_continuum_basis':'affine event sums and signed TV-event lower bounds; convexity of TV under affine interpolation of source and decoded distributions',
      'status':'AUTHOR_PROOF_AND_EXACT_EXECUTION;UNREVIEWED;NOT_ADMITTED'
    }

if __name__=='__main__':print(json.dumps(check(),sort_keys=True,indent=2))

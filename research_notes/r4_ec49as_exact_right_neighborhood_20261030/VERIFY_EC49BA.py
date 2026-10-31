"""EC49BA: exact all-real causal 18+18 auxiliary positive-BRC optimum at eta=43/100.
Requires sibling VERIFY_EC49AX.py and SymPy; all enumeration arithmetic uses Fraction.
This is an author-side portable certificate, not Source/Driver admission.
"""
from fractions import Fraction as F
from collections import Counter
import json
import sympy as S
import VERIFY_EC49AX as old

ETA=F(43,100)
CAP=F(151,1250)
ZERO=F(0)
ONE=F(1)


def price_interval(x):
    T,V=old.fibers(x,ETA)
    knots=sorted({ZERO,ONE}|{v/t for t,v in zip(T,V) if t})
    spans=[]
    for a,b in zip(knots,knots[1:]):
        u,v=old.dual(x,ETA,a),old.dual(x,ETA,b)
        if u<=CAP and v<=CAP: spans.append((a,b))
        elif u<=CAP<v: spans.append((a,a+(b-a)*(CAP-u)/(v-u)))
        elif v<=CAP<u: spans.append((a+(b-a)*(CAP-u)/(v-u),b))
    return (min(s[0] for s in spans),max(s[1] for s in spans)) if spans else None


def check():
    regular={};special=[];impossible=0
    for ids,x,y in old.edges(old.vertices()):
        pair=old.clip(x,y)
        if pair is None:
            impossible+=1;continue
        ends=[price_interval(z) for z in pair]
        if all(v is not None for v in ends) and max(v[0] for v in ends)<=min(v[1] for v in ends):
            lam=max(v[0] for v in ends)
            assert ZERO<=lam<=ONE
            assert all(old.dual(z,ETA,lam)<=CAP for z in pair)
            regular[','.join(map(str,ids))]=str(lam)
        else:special.append((ids,pair))
    assert (impossible,len(regular),len(special))==(720,196,8)
    sig=old.signature(special[0][1])
    assert all(old.signature(pair)==sig for _,pair in special)
    assert set(ids for ids,pair in special)=={
      (0,2,4,6,10),(0,3,4,6,10),(0,6,10,12,14),(0,6,10,13,14),
      (1,2,4,5,11),(1,3,4,5,11),(1,5,11,12,14),(1,5,11,13,14)}
    x0,x1=special[0][1]
    assert (x0[0],x1[0])==(F(11,16),F(3,16))
    # All accept-score signs are fixed along the affine edge.
    for cc in range(4):
        for u in range(2):
            for w in range(3):
                scores=[]
                for x in (x0,x1):
                    q=[old.qval(x,ETA,cc,u,j) for j in range(3)]
                    scores.append(43*q[w]-16*sum(q))
                assert scores[0]*scores[1]>=0
    d=27-10*ETA;f=8+16*ETA
    a=344*(1-4*ETA**2)
    b=2436*ETA**2+1568*ETA-1201
    c=2060*ETA**2-5096*ETA+1769
    assert (a,b,c,d,f)==(F(55986,625),F(-190859,2500),F(-20693,500),F(227,10),F(372,25))
    # The actual purchase LP discards only fiber (c,u)=(0,1).
    # For all t, every fiber has density >= that of fiber 1;
    # degree-2 Bernstein coefficients prove it on the full interval.
    observations=[]
    for t in (ZERO,F(1,2),ONE):
        x=tuple((1-t)*z+t*y for z,y in zip(x0,x1))
        T,V=old.fibers(x,ETA)
        assert T[1]>(1-t)/12
        Hbest=sum(V)-(1-t)*V[1]/(12*T[1])
        assert (old.h(ETA)-Hbest)*2064*(d-f*t)==a*t*t+b*t+c
        observations.append((T,V))
    density_bern={}
    for j in range(8):
        values=[V[j]*T[1]-V[1]*T[j] for T,V in observations]
        c0=values[0];c1=4*values[1]-3*c0-values[2]
        c2=2*values[2]+2*c0-4*values[1]
        be=old.bern([c0,c1,c2],ZERO,ONE)
        assert all(v>=0 for v in be)
        density_bern[str(j)]=list(map(str,be))
    # Exact optimization in Q(sqrt(782)); square identity for ALL real t.
    eta=S.Rational(43,100)
    t=S.symbols('t',real=True)
    r=S.sqrt(782)
    ts=S.Rational(1135,744)-5*r/186
    ps=S.Rational(43,93)+5*r/372
    Hs=S.Rational(267209,2132800)-7*r/44640
    def sr(v):return S.Rational(v.numerator,v.denominator)
    assert S.simplify(sr(a)*t**2+sr(b)*t+sr(c)
        +2064*(Hs-sr(old.h(ETA)))*(sr(d)-sr(f)*t)-sr(a)*(t-ts)**2)==0
    assert 27<r<28
    assert bool(0<ts<1) and bool(0<ps<1)
    Hlower=S.Rational(267209,2132800)-S.Rational(7*28,44640)
    assert Hlower==S.Rational(2320601,19195200)
    assert Hlower-CAP==S.Rational(45521,479880000)>0
    assert S.simplify(1-8*(1-ts)/(sr(d)-sr(f)*ts)-ps)==0
    rows=(((11-8*ts)/16,0,ts/4,0,(5+4*ts)/16),
          (0,1,0,0,0),(1,0,0,0,0))
    assert all(S.simplify(sum(row)-1)==0 for row in rows)
    assert all(not S.simplify(v).is_negative for row in rows for v in row)
    alpha=beta=paid=S.Integer(0);events=[]
    for cc in range(4):
        for u in range(2):
            q=[rows[w][cc]*(S.Rational(1,2)+(2*u-1)*(1-w)*eta)/3 for w in range(3)]
            T=sum(q);p=ps if (cc,u)==(0,1) else 1
            paid+=p*T
            for w,v in enumerate(q):
                if S.simplify(43*v-16*T).is_positive:
                    events.append((cc,u,w))
                    alpha+=p*(T+v)/4
                    beta+=p*T/3
    assert events==[(0,0,2),(0,1,0),(1,0,1),(1,1,1),(2,0,0),(2,1,0)]
    assert S.simplify(paid)==S.Rational(13,16)
    assert S.simplify(alpha)==S.Rational(10019,24800)-7*r/44640
    assert S.simplify(beta)==S.Rational(13,48)
    assert S.simplify(alpha-S.Rational(177,172)*beta-Hs)==0
    assert S.simplify(sum(rows[w][cc]*(1,1,2,2,0)[cc] for w in range(3) for cc in range(5)))==S.Rational(43,16)
    return dict(schema='EC49BA_EXACT_POINT_OPTIMUM_V1',date='2026-10-30',eta='43/100',
        vertices=168,edges=924,cost_infeasible_edges=impossible,dual_certified_edges=len(regular),
        exceptional_edges=len(special),regular_cap=str(CAP),regular_prices=regular,
        exceptional_supports=[list(ids) for ids,pair in special],
        density_bernstein=density_bern,tstar=str(ts),pstar=str(ps),
        H_exact=str(Hs),H_decimal=str(S.N(Hs,28)),alpha=str(S.simplify(alpha)),
        beta=str(S.simplify(beta)),cost1='43/48',cost2=str(S.simplify(paid)),
        accepted_events=events,source='VERIFY_EC49AX.py and EC49AV sparse-vertex/edge lemma',
        status='AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_SYMPY_PASS / UNREVIEWED / NOT_ADMITTED')

if __name__=='__main__':print(json.dumps(check(),ensure_ascii=False,indent=2))

"""EC49AZ point certificate: Python 3, fractions, SymPy 1.14, sibling VERIFY_EC49AX.py."""
from fractions import Fraction as F
import json, sympy as s
import VERIFY_EC49AX as old
eta=F(21,50);h=old.h(eta);cap=h+F(13,10000)

def interval(x):
    T,V=old.fibers(x,eta)
    K=sorted({F(0),F(1)}|{v/t for t,v in zip(T,V) if t})
    S=[]
    for a,b in zip(K,K[1:]):
        u,v=old.dual(x,eta,a),old.dual(x,eta,b)
        if u<=cap and v<=cap:S.append((a,b))
        elif u<=cap<v:S.append((a,a+(b-a)*(cap-u)/(v-u)))
        elif v<=cap<u:S.append((a+(b-a)*(cap-u)/(v-u),b))
    return (min(z[0] for z in S),max(z[1] for z in S)) if S else None

def check():
    regular={};special=[];impossible=0
    for ids,x,y in old.edges(old.vertices()):
        pair=old.clip(x,y)
        if pair is None:impossible+=1;continue
        intervals=[interval(z) for z in pair]
        if all(p is not None for p in intervals) and max(p[0] for p in intervals)<=min(p[1] for p in intervals):
            lam=max(p[0] for p in intervals)
            assert all(old.dual(z,eta,lam)<=cap for z in pair)
            regular[','.join(map(str,ids))]=str(lam)
        else:special.append((ids,pair))
    assert (impossible,len(regular),len(special))==(720,196,8)
    signature=old.signature(special[0][1]);assert all(old.signature(pair)==signature for _,pair in special)
    x0,x1=special[0][1];assert (x0[0],x1[0])==(F(11,16),F(3,16))
    for c in range(4):
        for u in range(2):
            for z in range(3):
                L=[]
                for x in (x0,x1):
                    q=[old.qval(x,eta,c,u,w) for w in range(3)]
                    L.append(43*q[z]-16*sum(q))
                assert L[0]*L[1]>=0
    d=27-10*eta;f=8+16*eta
    assert (19*eta-4)/(2*(2*eta+1))>1
    for t in (F(0),F(1)):
        assert f*t-d<0 and (432*eta-216)*t+41-1106*eta<0
        assert 19-eta*(10+16*t)>0
    a=344*(1-4*eta**2);b=2436*eta**2+1568*eta-1201;c=2060*eta**2-5096*eta+1769
    for t in (F(0),F(1,2),F(1)):
        x=[(1-t)*z+t*y for z,y in zip(x0,x1)];T,V=old.fibers(x,eta)
        assert T[1]>(1-t)/12
        Hbest=sum(V)-(1-t)*V[1]/(12*T[1])
        assert (h-Hbest)*2064*(d-f*t)==a*t*t+b*t+c
    e=s.Rational(21,50);r=s.sqrt(202);z=s.symbols('z')
    tt=s.Rational(285,184)-5*r/92
    pp=s.Rational(21,46)+5*r/184
    HH=s.Rational(593779,4747200)-r/2760
    g=HH-s.Rational(h.numerator,h.denominator)
    A=s.Rational(a.numerator,a.denominator);B=s.Rational(b.numerator,b.denominator);C=s.Rational(c.numerator,c.denominator)
    D=s.Rational(d.numerator,d.denominator);E=s.Rational(f.numerator,f.denominator)
    assert s.simplify(A*z*z+B*z+C+2064*g*(D-E*z)-A*(z-tt)**2)==0
    assert 14<r<s.Rational(143,10) and 0<tt<1 and 0<pp<1
    assert F(15703,2373600)-F(143,10)/2760>F(13,10000)
    rows=(((11-8*tt)/16,0,tt/4,0,(5+4*tt)/16),(0,1,0,0,0),(1,0,0,0,0))
    alpha=beta=paid=s.Integer(0);accept=[]
    for cc in range(4):
        for u in range(2):
            q=[rows[w][cc]*(s.Rational(1,2)+(2*u-1)*(1-w)*e)/3 for w in range(3)]
            T=sum(q);p=pp if (cc,u)==(0,1) else 1;paid+=p*T
            for w,v in enumerate(q):
                if s.simplify(43*v-16*T)>0:
                    accept.append((cc,u,w));alpha+=p*(T+v)/4;beta+=p*T/3
    assert s.simplify(paid)==s.Rational(13,16)
    assert s.simplify(beta)==s.Rational(13,48)
    assert s.simplify(alpha-s.Rational(177,172)*beta-HH)==0
    assert accept==[(0,0,2),(0,1,0),(1,0,1),(1,1,1),(2,0,0),(2,1,0)]
    return {'schema':'EC49AZ_EXACT_POINT_OPTIMUM_V1','eta':'21/50','vertices':168,'edges':924,
      'infeasible':impossible,'dual_certified':len(regular),'exceptional':len(special),
      'regular_cap':str(cap),'prices':regular,'special_supports':[list(t) for t,_ in special],
      'tstar':str(tt),'pstar':str(pp),'Hstar':str(HH),'alpha':str(s.simplify(alpha)),
      'beta':str(s.simplify(beta)),'scope':'auxiliary positive 18+18 causal BRC; author-side exact checks; unreviewed, not admitted'}
if __name__=='__main__':print(json.dumps(check(),indent=2))

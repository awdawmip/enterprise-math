"""Exact quadratic-drift-invariant 4-point nearest-scalar decoder, M=K=2."""
from fractions import Fraction as Q
from itertools import product
from math import comb,lcm
from pathlib import Path
import json

P=(455,-295,-25,185,-25,-295)
W=(-1,3,-3,1);J=range(4);BASE=4000
S=tuple(sum(w*P[(a+j)%6] for j,w in enumerate(W)) for a in range(6))
assert S==(-1080,-360,360,1080,-2520,2520)
assert all(sum(w*j**k for j,w in enumerate(W))==0 for k in range(3))
assert min(y-x for x,y in zip(sorted(S),sorted(S)[1:]))==720
errs=tuple(product(range(-2,3),repeat=2))

def counts(n):
    # Coefficient recurrence of z/[(1-z)^3(1-z²)(1-z³)(1-z⁶)].
    polynomial=[1]
    for w in (1,1,1,2,3,6):
        v=polynomial+[0]*w
        for i,c in enumerate(polynomial):v[i+w]-=c
        polynomial=v
    C=[0,1];T=[0,0]
    for q in range(2,n+1):
        C.append(-sum(polynomial[j]*C[q-j] for j in range(1,min(q,len(polynomial)-1)+1)))
        T.append(T[-1]+C[q-1])
    return C,T
C,T=counts(BASE+72)
def baseline(q):
    return 18*q**4+54*q**3-345*q*q+2070*q-16315
def check_tail():
    # C and T have poles only at sixth roots of unity, of order <=6,7.
    # On q>=1 each mod-six branch is polynomial of degree <=5,6.
    # After denominator clearing, +/- (1 - |Y-P/36|) positivity only
    # needs sign checks on the forward coefficients of a degree <=9 polynomial.
    for q0 in range(BASE,BASE+6):
        for (e,d),sign in product(errs,(-1,1)):
            def poly(t):
                q=q0+6*t;den=C[q]+d
                return 108*den+sign*(108*q**3*(T[q]+e)-(baseline(q)+3*P[q%6])*den)
            v=[poly(t) for t in range(10)]
            coeff=[]
            while v:
                coeff.append(v[0]);v=[b-a for a,b in zip(v,v[1:])]
            assert coeff[0]>0 and all(c>=0 for c in coeff)
            assert sum(c*comb(10,j) for j,c in enumerate(coeff))==poly(10)
    assert C[BASE]>2 and sum(map(abs,W))==8
    # Individual error <1 implies the absolute third-difference error <8<10.
def raw(q):
    return tuple((108*q**3*(T[q]+e)-baseline(q)*(C[q]+d),3*(C[q]+d)) if C[q]+d>0 else None for e,d in errs)
coordinates=[None]+[raw(q) for q in range(1,BASE+4)]
def failures(r):
    a=r%6;cols=coordinates[r:r+4]
    scale=lcm(*(v[1] for c in cols for v in c if v is not None))
    z=[{i:w*v[0]*(scale//v[1]) for i,v in enumerate(c) if v is not None} for w,c in zip(W,cols)]
    out={}
    lv,uv=None,None;srt=sorted(S);k=srt.index(S[a])
    if k>0:lv=scale*(srt[k-1]+S[a])
    if k<5:uv=scale*(srt[k+1]+S[a])
    for mode in ('independent','common'):
        if mode=='independent':
            imin=[min(c,key=c.get) for c in z];imax=[max(c,key=c.get) for c in z]
            extremes=[(sum(c[i] for c,i in zip(z,ii)),ii) for ii in (imin,imax)]
        else:
            valid=set.intersection(*(set(c) for c in z))
            V=[(sum(c[i] for c in z),[i]*4) for i in valid]
            extremes=[min(V),max(V)]
        for (v,idx),side in zip(extremes,(-1,1)):
            if side==-1 and (lv is None or 2*v>lv):continue
            if side==1 and (uv is None or 2*v<uv):continue
            b=S.index(srt[k+side])
            true=abs(v-scale*S[a]);rival=abs(v-scale*S[b]);assert rival<=true
            out[mode]=dict(r=r,phase=a,rival=b,errors=[errs[i] for i in idx],
                           scalar=str(Q(v,36*scale)),true_distance=str(Q(true,36*scale)),
                           rival_distance=str(Q(rival,36*scale)))
            break
        if mode=='independent' and mode not in out:break
    return out
def audit(r,mode):
    # Independent direct brute force at both sharp thresholds, no interval shortcut.
    a=r%6
    y=[[w*(Q(q**3*(T[q]+e),C[q]+d)-Q(baseline(q),108))
        for e,d in errs] for q,w in zip(range(r,r+4),W)]
    scale=lcm(36,*(v.denominator for c in y for v in c))
    Z=[[int(scale*v) for v in c] for c in y];Qp=[s*scale//36 for s in S]
    it=product(range(25),repeat=4) if mode=='independent' else ((i,)*4 for i in range(25))
    for i,j,k,h in it:
        val=Z[0][i]+Z[1][j]+Z[2][k]+Z[3][h]
        da=abs(val-Qp[a])
        if any(abs(val-z)<=da for b,z in enumerate(Qp) if b!=a):return True
    return False
if __name__=='__main__':
    check_tail()
    last={}
    for r in range(BASE-1,0,-1):
        for mode,w in failures(r).items():last.setdefault(mode,w)
        if len(last)==2:break
    for mode,w in last.items():
        assert audit(w['r'],mode) and not audit(w['r']+1,mode)
    result=dict(offsets=list(J),weights=W,ideal_times_36=S,
                thresholds={m:w['r']+1 for m,w in last.items()},witnesses=last,
                audit='all four boundary tests passed including exhaustive 25^4 independent candidates')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

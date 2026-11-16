"""Six-phase affine-nuisance contrast with exact joint count-error certificates.

Python standard library only. Run this file to write JSON next to the script.
The finite sweep and the forward-difference proof of the infinite tail use
arbitrary-precision integers. A common or individual error is an integer
in [-2,2] at budget 2. Rows of the cutoff table partition denominator
errors; columns partition numerator errors.
"""
from fractions import Fraction
from itertools import product
from math import comb, lcm
from pathlib import Path
import json

J = (0,1,5)
A = (4,-5,1)
P = (455,-295,-25,185,-25,-295)
S = tuple(sum(w*P[(a+j)%6] for j,w in zip(J,A)) for a in range(6))
assert S == (3000,-600,-1320,840,1560,-3480)
assert sum(A) == sum(j*w for j,w in zip(J,A)) == 0
order = sorted(S)
assert min(y-x for x,y in zip(order,order[1:]))==720
PARTS = ((0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,1,2))
NAMES = ('all-common','01|2','02|1','12|0','independent')
BASE=4000
BUDGET=2
choices=tuple(range(-BUDGET,BUDGET+1))
def gen(p):
    return tuple(tuple(x[i] for i in p) for x in product(choices,repeat=max(p)+1))
DENS = tuple(gen(p) for p in PARTS)
def counts(top):
    c,t=[0]*top,[0]*top
    c[0]=1
    for i,w in enumerate((1,1,2,3,6)):
        for n in range(w,top):
            t[n]+=t[n-w]+(0 if i else c[n-w])
            c[n]+=c[n-w]
    C,T=[0],[0]
    for v,w in zip(c,t):
        C.append(C[-1]+v);T.append(T[-1]+w)
    return C,T
C,T=counts(BASE+72)
def bpoly(q):
    return 18*q**4+54*q**3-345*q*q+2070*q-16315
def tail_polynomial(q,e,d,sign):
    den=C[q]+d
    return 108*den+sign*(108*q**3*(T[q]+e)-(bpoly(q)+3*P[q%6])*den)
def diffs(v):
    coefficients=[]
    while v:
        coefficients.append(v[0])
        v=[y-x for x,y in zip(v,v[1:])]
    return coefficients
def tail_certificate():
    # C(q) and T(q) are quasipolynomials with period 6, degrees <=5 and
    # <=6, for q>=1. Their GFs in q-1 are 1/[(1-z)^3(1-z²)(1-z³)(1-z⁶)]
    # and z/[(1-z)^4(1-z²)(1-z³)(1-z⁶)]. Partial fractions at sixth
    # roots of unity establish the claimed degrees on each residue class.
    # Thus the integer expression below in t (q=q0+6t) has degree <=9.
    # Nonnegative Newton forward coefficients with positive constant imply
    # positivity for every t>=0 (Newton basis binomial(t,j)).
    smallest=None
    for q0 in range(BASE,BASE+6):
        for e,d,sign in product(choices,choices,(-1,1)):
            v=[tail_polynomial(q0+6*t,e,d,sign) for t in range(10)]
            coeff=diffs(v)
            assert coeff[0]>0 and all(x>=0 for x in coeff)
            assert sum(x*comb(10,k) for k,x in enumerate(coeff)) == tail_polynomial(q0+60,e,d,sign)
            smallest=min(smallest,coeff[0]) if smallest is not None else coeff[0]
    # |Y(q)-P(q)/36|<1, hence |contrast-ideal| < sum |A_i| = 10.
    assert C[BASE]>BUDGET and min(y-x for x,y in zip(order,order[1:]))>=20*36
    return smallest

def build(r):
    qs=tuple(r+j for j in J)
    sc=lcm(*(3*(C[q]+d) for q in qs for d in choices if C[q]+d>0))
    byj=[]
    for q,w in zip(qs,A):
        t={}
        for d in choices:
            den=C[q]+d
            if den<=0: continue
            scale=sc//(3*den)
            # Coordinates give 36Y scaled by sc. Pair = (nominal, slope in e).
            t[d]=(scale*w*(108*q**3*T[q]-bpoly(q)*den),scale*w*108*q**3)
        byj.append(t)
    return byj,sc

def bounds(a,sc):
    t=order.index(S[a])
    low=None if t==0 else sc*(order[t-1]+order[t])
    high=None if t==5 else sc*(order[t+1]+order[t])
    return low,high

def test(r,live):
    byj,sc=build(r);a=r%6
    low,high=bounds(a,sc)
    def failed(x,y):
        return (low is not None and 2*x<=low) or (high is not None and 2*y>=high)
    # Fast encompassing interval (both numerator and denominator free).
    minfree=sum(min(z-2*abs(v) for z,v in t.values()) for t in byj)
    maxfree=sum(max(z+2*abs(v) for z,v in t.values()) for t in byj)
    if not failed(minfree,maxfree):return {}
    out={}
    for di,dslist in enumerate(DENS):
        pending={ei for ei in range(5) if (di,ei) in live}
        if not pending:continue
        for ds in dslist:
            try: vals=[t[d] for t,d in zip(byj,ds)]
            except KeyError: continue
            B=sum(z for z,_ in vals);c0,c1,c2=(v for _,v in vals)
            coeffs=((c0+c1+c2,),(c0+c1,c2),(c0+c2,c1),(c1+c2,c0),(c0,c1,c2))
            for ei in tuple(pending):
                coeff=coeffs[ei]
                amp=2*sum(abs(x) for x in coeff)
                if not failed(B-amp,B+amp): continue
                sign=-1 if low is not None and 2*(B-amp)<=low else 1
                ee=[sign*BUDGET*(1 if x>=0 else -1) for x in coeff]
                es=[ee[g] for g in PARTS[ei]]
                val=B+sum(e*y for e,(_,y) in zip(es,vals))
                assert val==B+sign*amp
                k=order.index(S[a]);other=order[k+sign]
                dtrue=abs(val-sc*S[a]);drival=abs(val-sc*other)
                assert drival<=dtrue
                out[(di,ei)]={'r':r,'phase':a,'rival':S.index(other),
                    'e':es,'d':ds,'scalar':str(Fraction(val,36*sc)),
                    'true_distance':str(Fraction(dtrue,36*sc)),
                    'rival_distance':str(Fraction(drival,36*sc))}
                pending.remove(ei)
            if not pending:break
    return out

def compute():
    tail = tail_certificate()
    live=set(product(range(5),repeat=2)); allw={}
    for r in range(BASE-1,0,-1):
        found=test(r,live);allw.update(found);live.difference_update(found)
        if not live:break
    assert not live
    table=[[allw[i,j]['r']+1 for j in range(5)] for i in range(5)]
    return {'offsets':J,'contrast':A,'ideal_times_36':S,'partitions':NAMES,
        'budget':2,'tail_start':BASE,'tail_positive_minimum_constant':tail,
        'thresholds_denominator_rows_numerator_columns':table,
        'last_failure_witnesses':[[allw[i,j] for j in range(5)] for i in range(5)]}
if __name__=='__main__':
    res=compute()
    print(*res['thresholds_denominator_rows_numerator_columns'],sep='\n')
    print('common',res['last_failure_witnesses'][0][0])
    print('independent',res['last_failure_witnesses'][4][4])
    out=Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(res,indent=2)+'\n')

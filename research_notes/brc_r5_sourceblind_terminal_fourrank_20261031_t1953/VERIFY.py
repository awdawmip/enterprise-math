#!/usr/bin/env python3
"""Exact Fraction check: observable terminal-only errors, compensated source kernels.

Independent auxiliary finite stochastic stopping model; not native X6.
"""
from fractions import Fraction as F
from itertools import product

Z, O, HALF = F(0), F(1), F(1, 2)
ALPHA = (F(1, 4), F(1, 5))
KAPPA = (F(3, 4), F(1, 6))
EPS, ETA = F(1, 4), F(1, 64)


def paths(bits, lr=False):
    def act(i, key):
        if lr:
            return bits[{'A': 0, 'D': 1, 'Y': 2, 'L': 3}[key[0]]]
        if key == 'A':
            return bits[i]
        if key == 'D':
            return bits[2 + i]
        if key == 'Y':
            return bits[4 + i]
        return bits[6 + 3*i + {'LC': 0, 'LD': 1, 'LY': 2}[key]]

    for i, (alpha, kappa) in enumerate(zip(ALPHA, KAPPA)):
        q = HALF
        if not act(i, 'A'):
            yield i, 'A_STOP', q, O, 1
            continue
        d, c, y = q*alpha, q*(O-2*alpha), q*alpha
        if not act(i, 'D'):
            yield i, 'D_STOP', d, HALF, 2
        else:
            yield i, 'D_HIGH', d*F(2,3), F(1,4), 3
            yield i, 'LD', d*F(1,3), O, 3+act(i,'LD')
        yield i, 'C_STOP', c*(O-kappa), O, 2
        yield i, 'LC', c*kappa, O, 3+act(i,'LC')
        if not act(i, 'Y'):
            yield i, 'Y_STOP', y, F(3,2), 2
        else:
            yield i, 'Y_HIGH', y*HALF, F(2), 3
            yield i, 'LY', y*HALF, O, 3+act(i,'LY')


def response(route, lam, time):
    # These events are determined solely by final observable (time, LR).
    # C_STOP = (2,1); D_HIGH = (3,1/4).
    if route == 'C_STOP':
        assert (time,lam) == (2,O)
    if route == 'D_HIGH':
        assert (time,lam) == (3,F(1,4))
    r = HALF+EPS*(time==2 and lam==O)+ETA*(time==3 and lam==F(1,4))
    assert HALF <= r < O
    return r


def observe(bits, lr=False):
    eP=eQ=TP=TQ=P=Q=Z
    originP=[Z,Z];originQ=[Z,Z]
    for i,route,q,lam,t in paths(bits,lr):
        p=q*lam
        r=response(route,lam,t)
        eP+=p*r; eQ+=q*r; TP+=p*t; TQ+=q*t
        P+=p;Q+=q;originP[i]+=p;originQ[i]+=q
    assert P==Q==O and originP==originQ==[HALF,HALF]
    return eP,eQ,TP,TQ


def determinant(vs):
    m=[list(x) for x in vs]
    n=len(m); d=O
    for col in range(n):
        k=next((i for i in range(col,n) if m[i][col]),None)
        if k is None: return Z
        if k!=col: m[k],m[col]=m[col],m[k];d=-d
        pivot=m[col][col];d*=pivot
        for i in range(col+1,n):
            k=m[i][col]/pivot
            m[i]=[m[i][j]-k*m[col][j] for j in range(n)]
    return d


def convex_polygon(points):
    p=sorted(set(points))
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[];hi=[]
    for v in p:
        while len(lo)>=2 and cross(lo[-2],lo[-1],v)<=0:lo.pop()
        lo.append(v)
    for v in reversed(p):
        while len(hi)>=2 and cross(hi[-2],hi[-1],v)<=0:hi.pop()
        hi.append(v)
    return lo[:-1]+hi[:-1]


def inside(poly,v):
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    return len(poly)>=3 and all(cross(poly[i],poly[(i+1)%len(poly)],v)>=0 for i in range(len(poly)))


def main():
    theta=[(O+k*(O-2*a))/a for a,k in zip(ALPHA,KAPPA)]
    b=[(O-2*a)*(O-k) for a,k in zip(ALPHA,KAPPA)]
    assert theta == [F(11,2)]*2 and b == [F(1,8),HALF]
    t=theta[0]-EPS*sum(b)/sum(ALPHA)
    assert t==F(371,72)
    # H_t = eQ + 2(t+1) TP - (2t+3) TQ, J = 36 H_t
    assert (36, 36*2*(t+1), -36*(2*t+3)) == (36,443,-479)
    LR=[observe(bits,True) for bits in product((0,1),repeat=4)]
    FULL=[observe(bits,False) for bits in product((0,1),repeat=12)]
    assert len(LR)==16 and len(FULL)==4096
    poly=convex_polygon([(x[2],x[3]) for x in LR])
    assert len(poly)==6 and all(inside(poly,(x[2],x[3])) for x in FULL)
    J=lambda x:36*x[1]+443*x[2]-479*x[3]
    fm,lm=max(map(J,FULL)),max(map(J,LR))
    gap=fm-lm
    assert (fm,lm,gap)==(F(-17),F(-18),O)
    assert gap==36*EPS*abs(ALPHA[0]-ALPHA[1])/sum(ALPHA)
    ids=(0,8,9,10,12)
    base=LR[ids[0]]
    mat=[[LR[k][j]-base[j] for j in range(4)] for k in ids[1:]]
    det=determinant(mat)
    assert det==F(-1539,419430400)
    witness_bits=(0,1,0,0,0,1,0,0,0,0,0,0)
    witness=observe(witness_bits,False)
    assert witness==(F(9,16),F(9,16),F(17,10),F(33,20))
    assert J(witness)==fm
    print('frozen alpha',ALPHA,'kappa',KAPPA,'theta',theta,'b',b,'epsilon',EPS,'eta',ETA)
    print('derived t_star',t,'integer J=(36eQ+443TP-479TQ)')
    print('enumerated FULL',len(FULL),'LR',len(LR),'unique four-points',len(set(FULL)),len(set(LR)))
    print('Q/P mass each origin 1/2 for every policy; all terminal errors strict interior')
    print('time hull vertices',poly,'FULL_outside=0')
    print('support max FULL',fm,'LR',lm,'gap',gap)
    print('rank4 LR point IDs',ids,'determinant',det)
    print('rank4 LR points',[(k,LR[k]) for k in ids])
    print('FULL witness bits',witness_bits,'O',witness,'J',J(witness))
    print('L_infinity distance bound to complete LR convex hull =',gap/F(36+443+479))
    print('PASS_EXACT_R5_COMPENSATED_SOURCEBLIND_TERMINAL_RANK4_SEPARATOR')

if __name__ == '__main__':
    main()

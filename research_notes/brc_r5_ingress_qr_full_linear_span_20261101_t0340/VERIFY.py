"""Exact rational checker for the two-parameter R5 ingress observer no-go.

This is an auxiliary two-origin P/Q stopping model; not native X6 execution.
Python standard library only; deterministic vertices enumerated exhaustively.
The all-real step is algebraic: rank minors, exposed-face fiber equalities,
the explicit parametric Farkas family and the exact zero-observer hull.
"""
from fractions import Fraction as F
from itertools import product, combinations

ALPHA=(F(1,4), F(1,5)); KAPPA=(F(3,4), F(1,6))
LEAVES=('A','D','Y','C','DH','YH','LD','LY','LC','L4D','L4Y','L4C')
TIMES=(1,2,2,2,3,3,3,3,3,4,4,4)
RATIOS=(F(1),F(1,2),F(3,2),F(1),F(1,4),F(2),F(1),F(1),F(1),F(1),F(1))
IX={k:i for i,k in enumerate(LEAVES)}

def masses(bits):
    assert len(bits)==12
    z=[F(0)]*12
    def add(k,w):z[IX[k]]+=w
    for i,(a,k) in enumerate(zip(ALPHA,KAPPA)):
        A,D,Y,LD,LY,LC=bits[6*i:6*i+6]
        cont=F(A,2)
        add('A',F(1,2)-cont)
        d=cont*a; y=cont*a; c=cont*(1-2*a)
        if D:
            add('DH',F(2,3)*d)
            add('L4D' if LD else 'LD',d/3)
        else:add('D',d)
        if Y:
            add('YH',y/2)
            add('L4Y' if LY else 'LY',y/2)
        else:add('Y',y)
        add('C',c*(1-k))
        add('L4C' if LC else 'LC',c*k)
    assert min(z)>=0
    assert sum(z)==sum(w*l for w,l in zip(z,RATIOS))==1
    return tuple(z)

def reduced(z):
    return (z[IX['DH']], z[IX['YH']],sum(w*t for w,t in zip(z,TIMES)),
            z[IX['L4D']]+z[IX['L4Y']]+z[IX['L4C']],
            z[IX['LC']],z[IX['LD']])

def general_observation(v,a,b,d):return v[:3]+(a*v[3]+b*v[4]+d*v[5],)
def observation(v,q,r):return general_observation(v,F(1),q,r)

def det4(a):
    a=[list(row) for row in a]; result=F(1)
    for k in range(4):
        j=next((j for j in range(k,4) if a[j][k]),None)
        if j is None:return F(0)
        if j!=k: a[k],a[j]=a[j],a[k];result=-result
        pivot=a[k][k];result*=pivot
        for j in range(k+1,4):
            ratio=a[j][k]/pivot
            for l in range(k,4):a[j][l]-=ratio*a[k][l]
    return result

def general_minor(vertices,indices,a,b,d):
    p=general_observation(vertices[indices[0]],a,b,d)
    return det4([[general_observation(vertices[i],a,b,d)[j]-p[j] for j in range(4)]
                 for i in indices[1:]])
def minor(vertices,indices,q,r):return general_minor(vertices,indices,F(1),q,r)

def bits_to_str(b):return ''.join(str(i) for i in b)

def main():
    assert all((1+k*(1-2*a))/a==F(11,2) for a,k in zip(ALPHA,KAPPA))
    fbits=list(product((0,1),repeat=12))
    lbits=list(product((0,1),repeat=4))
    full=[reduced(masses(b)) for b in fbits]
    lr=[reduced(masses((b[0],b[1],b[2],b[3],b[3],b[3])*2)) for b in lbits]
    assert len(full)==4096 and len(lr)==16
    print('FULL=4096 LR=16 P/Q normalization=EXACT_PASS')
    ids=(0,9,11,12,14);constant=F(24057,10240000)
    for q,r in ((F(0),F(0)),(F(1),F(0)),(F(0),F(1)),(F(7,3),-F(11,5))):
        assert minor(lr,ids,q,r)==constant
    ranks=(((0,9,11,12,14), (F(24057,10240000),F(0),F(0))),
           ((0,8,9,10,12), (-F(513*99,10240000),F(513*118,10240000),F(0))),
           ((0,9,10,13,14), (F(81*99,5120000),F(0),-F(81*118,5120000))))
    for ids,coeff in ranks:
        for i in range(3):
            selector=[F(0)]*3;selector[i]=F(1)
            assert general_minor(lr,ids,*selector)==coeff[i]
        assert general_minor(lr,ids,F(2),F(-3,5),F(7,11)) == sum(x*y for x,y in zip(coeff,(F(2),-F(3,5),F(7,11))))
    print('GENERAL_RANK_MINORS: a*(24057/10240000), 513*(118*b-99*a)/10240000, -81*(118*d-99*a)/5120000')
    print('GENERAL_LR_RANK: 4 iff (a,b,d)!=0; 3 at zero')
    xstar,ustar=F(3,20),F(9,80)
    assert lr[14][:2]==lr[15][:2]==(xstar,ustar)
    distances=[(xstar-v[0])+(ustar-v[1]) for j,v in enumerate(lr) if j not in(14,15)]
    assert min(distances)==F(9,80)
    print('EXPOSED_LR_EDGE endpoints=(14,15) x=3/20 u=9/80 other_LR_d>=9/80')
    t0,t1=lr[14][2],lr[15][2]
    assert (t0,t1)==(F(43,16),F(249,80)) and t1-t0==F(17,40)
    witnesses=((3643,'111000111011',F(4,17),(F(0),F(1,170),F(3,170))),
               (3647,'111000111111',F(16,51),(F(0),F(5,204),-F(1,102))))
    for j,bs,lam,expected in witnesses:
        v=full[j]
        assert bits_to_str(fbits[j])==bs
        assert v[:2]==(xstar,ustar)
        assert (v[2]-t0)/(t1-t0)==lam
        diff=tuple(v[k]-(1-lam)*lr[14][k]-lam*lr[15][k] for k in (3,4,5))
        assert diff==expected
        print('EDGE_WITNESS',j,bs,'lambda',lam,'delta(y,c,ld)',','.join(map(str,diff)))
    assert F(1)*(-2)-F(3)*5==-17
    print('EDGE_CONSTRAINTS b+3d=0 AND 5b-2d=0 => b=d=0 (det=-17)')
    coeff=(-21,-61,-19,118);bound=F(-19)
    def score(v):return sum(a*b for a,b in zip(coeff,v[:4]))
    assert max(score(v) for v in lr)==bound
    witness=4032
    assert bits_to_str(fbits[witness])=='111111000000'
    assert score(full[witness])==F(-27,2)
    assert score(full[witness])-bound==F(11,2)
    print('ZERO_PARAMETER_FARKAS H=-21x-61u-19t+118y <= -19 LR16; FULL4032=-27/2; gap=11/2')
    for q,r in [(F(0),F(1)),(F(1),F(0)),(F(1),-F(1,3)),(F(7,11),F(2,9)),(-F(9,4),F(1,7))]:
        deltas=[q*e[3][1]+r*e[3][2] for e in witnesses]
        assert any(d!=0 for d in deltas)
        widx=next(i for i,d in enumerate(deltas) if d!=0)
        j=witnesses[widx][0]; sigma=1 if deltas[widx]>0 else -1
        M=40*(1+abs(q)+abs(r))
        s0=observation(lr[14],q,r)[3]
        s1=observation(lr[15],q,r)[3]
        def g(t):return s0+(s1-s0)*(t-t0)/(t1-t0)
        def sep(v):
            x,u,t,s=observation(v,q,r)
            return sigma*(s-g(t))+M*((x-xstar)+(u-ustar))
        assert max(sep(v) for v in lr)==0
        assert sep(full[j])==abs(deltas[widx])>0
    print('NONZERO_PARAMETER_FARKAS family algebraic bound + 5 rational regression cases PASS')
    facets=((-1,0,0,0),(0,-1,0,0),(3,26,-2,2),(39,8,-4,4),
            (-80,-120,40,-99),(0,80,0,-9),(20,0,0,-3))
    def holds(z):
        return all(sum(F(co)*w for co,w in zip(p,(*z[:3],F(1))))<=0 for p in facets)
    assert all(holds(v) for v in full+lr)
    def d3(a):
        return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
                -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
                +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
    def intersection(planes):
        A=[p[:3] for p in planes]; b=[-p[3] for p in planes]; det=d3(A)
        if not det:return None
        return tuple(F(d3([[(b[i] if j==k else A[i][j]) for j in range(3)] for i in range(3)]),det) for k in range(3))
    polyvertices={z for fac in combinations(facets,3)
                  if (z:=intersection(fac)) is not None and holds(z)}
    assert polyvertices=={v[:3] for v in lr if v[:3] in polyvertices}
    assert len(polyvertices)==8
    print('ZERO_OBSERVER_3D_HULL_EQUAL seven facets, all 4096 FULL inside, eight exact LR vertices')
    print('GENERAL_CLASSIFICATION (a,b,d)=0 -> 3D hull equality; nonzero -> rank4 and strict hull inequality')
    print('ALL_REAL_QR_THEOREM rank(LR4)=4 AND conv(FULL4)!=conv(LR4) for every (q,r) in R^2')
    print('AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED')
    print('PASS_EXACT_R5_INGRESS_LINEAR_SPAN_GLOBAL_CLASSIFICATION')
if __name__=='__main__':main()

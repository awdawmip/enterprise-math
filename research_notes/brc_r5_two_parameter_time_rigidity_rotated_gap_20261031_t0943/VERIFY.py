"""Exact R5 natural-kernel escape/rotated-separator certificate.
Auxiliary positive P/Q stopping tree; Python standard library only.
Finite rational tests plus analytic all-real proof in sibling RESEARCH.md.
"""
from fractions import Fraction as Q
from itertools import permutations, product
R=(Q(1),Q(3,2),Q(2),Q(3))
ELL=Q(1,4)
ERR_L=Q(1,16)
def kernel(y):
    return (y,ELL,1-2*y-Q(3,2)*ELL,y+ELL/2)
def observer(bits,y,lr=False):
    if lr:
        x,u,z,v=bits
        bits=(x,x,u,u,u,z,z,v,v)
    x0,x1,u0,u1,ub,z0,z1,v0,v1=map(Q,bits)
    x=(x0+x1)/2
    z=(z0+z1)/2
    Y=y*(x0*u0+x1*u1)
    E=ELL*(x0*v0+x1*v1)
    F=ELL*(ERR_L-Q(1,8))*(x0+x1)
    return (Q(1,8)+ub/8+(1-z)/8+Q(3,16)*F,
            Q(1,8)+ub/8+(1-z)/4+F/8,
            Q(3,2)+x+z/2-ub/4-Y/8+3*E/16,
            Q(3,2)+x/2+z-ub/4-Y/8+E/8)
def direct_observer(bits,y):
    x0,x1,u0,u1,ub,z0,z1,v0,v1=bits
    qacc=[Q(0),Q(0),Q(0)]
    pacc=[Q(0),Q(0),Q(0)]
    def add(qm,pm,t,err):
        for ac,m in ((qacc,qm),(pacc,pm)):
            ac[0]+=m
            ac[1]+=m*err
            ac[2]+=m*t
    for xi,ui,vi in ((x0,u0,v0),(x1,u1,v1)):
        if not xi:
            add(Q(1,8),Q(1,4),1,Q(1,8))
            continue
        for lab,k,r in zip(('Y','L','M','H'),kernel(y),R):
            mq=k/8
            mp=k*r/8
            if lab=='Y':
                add(mq,mp,2 if ui else 3,Q(1,8))
            elif lab=='L':
                add(mq,mp,4 if vi else 3,ERR_L)
            else:
                add(mq,mp,3,Q(1,8))
    add(Q(1,4),Q(1,4),2 if ub else 3,Q(5,8) if ub else Q(1,8))
    for zi in (z0,z1):
        add(Q(1,4),Q(1,8),3 if zi else 1,Q(1,8) if zi else Q(5,8))
    assert qacc[0]==pacc[0]==1
    return pacc[1],qacc[1],pacc[2],qacc[2]
def dot(c,v):
    return sum((a*b for a,b in zip(c,v)),Q(0))
def hull(points):
    pts=sorted(set(points))
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in pts:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:
            lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>1 and cross(up[-2],up[-1],p)<=0:
            up.pop()
        up.append(p)
    return tuple(lo[:-1]+up[:-1])
def det(cols):
    out=Q(0)
    for perm in permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        t=Q(1)
        for i in range(4): t*=cols[i][perm[i]]
        out+=(-1 if inv%2 else 1)*t
    return out
Fbits=list(product((0,1),repeat=9))
Lbits=list(product((0,1),repeat=4))
assert len(Fbits)==512 and len(Lbits)==16
J=(14,-19,2,-4)
H=(514,-643,65,-129)
for y in (Q(1,512),Q(1,128),Q(1,64),Q(1,32),Q(1,4)):
    k=kernel(y)
    assert 0<y<Q(5,16) and all(q>0 for q in k)
    assert sum(k)==1 and dot(R,k)==2
    assert sum(r*p/2 for r,p in zip(R,k))==1
    fv=[observer(b,y) for b in Fbits]
    lv=[observer(b,y,True) for b in Lbits]
    assert all(observer(b,y)==direct_observer(b,y) for b in Fbits)
    assert hull([v[2:] for v in fv])==hull([v[2:] for v in lv])
    fm=max(dot(H,v) for v in fv)
    lm=max(dot(H,v) for v in lv)
    assert fm==-Q(1669,8)+16*y
    assert lm==-Q(1669,8)+max(Q(0),16*y-Q(1,8))
    assert fm-lm==min(16*y,Q(1,8))>0
    jgap=max(dot(J,v) for v in fv)-max(dot(J,v) for v in lv)
    if y<=Q(1,64): assert jgap==0
    base=observer((0,0,0,0),y,True)
    choices=((1,0,0,0),(0,1,0,0),(0,0,1,0),(1,0,0,1))
    cols=[[a-b for a,b in zip(observer(p,y,True),base)] for p in choices]
    assert det(cols)==-Q(31,131072)
    witness=observer((1,1,1,1,0,0,0,0,0),y)
    assert dot(H,witness)==fm
    if y==Q(1,128):
        assert witness==(Q(125,512),Q(95,256),Q(1279,512),Q(1023,512))
        assert fm-lm==Q(1,8)
        print('witness_y_1_128:',tuple(map(str,witness)),
              'Linf_distance_from_LR_at_least=1/10808')
    print(f'y={y}: Q_kernel={tuple(map(str,k))} J_gap={jgap} '
          f'H_full={fm} H_LR={lm} H_gap={fm-lm} '
          f'LR_rank_det=-31/131072 time_hulls_equal=True policies=512/16')
def time_general(bits,yy,ee,lr=False):
    if lr:
        x,u,z,v=bits
        bits=(x,x,u,u,u,z,z,v,v)
    x0,x1,u0,u1,ub,z0,z1,v0,v1=map(Q,bits)
    x=(x0+x1)/2
    z=(z0+z1)/2
    Y=yy[0]*x0*u0+yy[1]*x1*u1
    E=ee[0]*x0*v0+ee[1]*x1*v1
    return (Q(3,2)+x+z/2-ub/4-Y/8+3*E/16,
            Q(3,2)+x/2+z-ub/4-Y/8+E/8)
cases=(
  ((Q(1,128),Q(1,128)),(Q(1,4),Q(1,4))),
  ((Q(1,128),Q(1,64)),(Q(1,4),Q(1,4))),
  ((Q(1,128),Q(1,128)),(Q(1,4),Q(1,8))),
  ((Q(1,128),Q(1,32)),(Q(1,4),Q(1,8))),
)
for yy,ee in cases:
    for yi,li in zip(yy,ee):
        k=(yi,li,1-2*yi-Q(3,2)*li,yi+li/2)
        assert all(q>0 for q in k) and sum(k)==1 and dot(R,k)==2
    tf=[time_general(p,yy,ee) for p in Fbits]
    tl=[time_general(p,yy,ee,True) for p in Lbits]
    ty=sum(yy)/2
    te=sum(ee)/2
    cy=(1-ty/2,-2+ty/2)
    ce=(-(4+2*te),8+3*te)
    dy=max(dot(cy,t) for t in tf)-max(dot(cy,t) for t in tl)
    de=max(dot(ce,t) for t in tf)-max(dot(ce,t) for t in tl)
    assert dy==abs(yy[1]-yy[0])/16
    assert de==abs(ee[1]-ee[0])/8
    equal=hull(tf)==hull(tl)
    assert equal==(yy[0]==yy[1] and ee[0]==ee[1])
    Ky=yy[1]-yy[0]; Ke=ee[1]-ee[0]
    tv=(abs(Ky)+abs(Ke)+abs(2*Ky+Q(3,2)*Ke)+abs(Ky+Ke/2))/2
    assert max(16*dy,8*de)<=tv<=32*dy+12*de
    print(f'general_y={tuple(map(str,yy))} general_ell={tuple(map(str,ee))} '
          f'time_hulls_equal={equal} gap_y={dy} gap_ell={de} '
          f'BRC_TV={tv} policies=512/16')
print('PASS_EXACT_R5_TWO_PARAMETER_TIME_HULL_CLASSIFICATION_AND_ROTATED_SEPARATOR')

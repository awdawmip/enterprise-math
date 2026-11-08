#!/usr/bin/env python3
"""Exact affine 14-edge Blackwell chamber for R5 g=b and seedless F-face targets."""
from fractions import Fraction as F

R=tuple(map(F,'1/10 1/2 3/4 1 5/4 3/2 19/10'.split()))
EDGES=((0,0),(0,1),(1,1),(6,1),(0,2),(2,2),(3,2),(4,2),
       (3,3),(0,5),(4,5),(5,5),(6,5),(6,6))

def mass(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
        F(13,40)*a+b/80-u,(g-a)/2,
        1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
        (g-b)/2,F(3,40)*a+F(21,80)*b-w,
        u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def tp(f):
    g,a,b,u,v,w,z=f
    return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w

def tq(f):
    g,a,b,u,v,w,z=f
    return 1+g+(a+b)/2+u+v+w

def model(p):
    g,a,u,v,w,z,G,A,B=p
    x=(g,a,g,u,v,w,z)
    P,Q=tp(x),tq(x)
    U=-F(17,40)*A-F(19,80)*B-G/2-P+F(3,2)*Q-F(1,2)
    W=-F(7,40)*A-F(39,80)*B-G/2+P-Q/2-F(1,2)
    return x,(G,A,B,U,A/10+F(9,40)*B,W,A/10)

def entries(x,y):
    mu,nu=mass(y),mass(x)
    d1=nu[1]-mu[1];d2=nu[2]-mu[2]
    d3=mu[3]-nu[3];d5=nu[5]-mu[5]
    alpha=(10*d2-5*d3)/23
    beta=(13*d2-18*d3)/23
    gamma=mu[6]-nu[6]-F(2,9)*d1
    delta=mu[4]-beta
    eta=d5-delta-gamma
    return (nu[0],F(7,9)*d1,mu[1],F(2,9)*d1,
            alpha,mu[2],d3,beta,nu[3],
            eta,delta,mu[5],gamma,nu[6])

def residual(p):
    x,y=model(p);mu,nu=mass(y),mass(x)
    E=dict(zip(EDGES,entries(x,y)))
    z=F(0)
    rows=tuple(sum(E.get((i,j),z) for j in range(7))-mu[i] for i in range(7))
    cols=tuple(sum(E.get((i,j),z) for i in range(7))-nu[j] for j in range(7))
    moms=tuple(sum(R[i]*E.get((i,j),z) for i in range(7))-R[j]*nu[j] for j in range(7))
    return rows+cols+moms

def slack(p):
    x,y=model(p)
    g,a,b,u,v,w,z=x
    G,A,B,U,V,W,Z=y
    d={
        'src_g':g,'src_1_minus_g':1-g,'src_a':a,'src_g_minus_a':g-a,
        'src_u':u,'src_cu_minus_u':F(13,40)*a+b/80-u,
        'src_w':w,'src_cw_minus_w':F(3,40)*a+F(21,80)*b-w,
        'src_z':z,'src_az_minus_z':a/10-z,
        'src_v_minus_z':v-z,'src_bv_minus_vz':F(9,40)*b-(v-z),
        'tgt_G':G,'tgt_1_minus_G':1-G,
        'tgt_A':A,'tgt_G_minus_A':G-A,
        'tgt_B':B,'tgt_G_minus_B':G-B,
        'tgt_U':U,'tgt_cu_minus_U':F(13,40)*A+B/80-U,
        'tgt_W':W,'tgt_cw_minus_W':F(3,40)*A+F(21,80)*B-W,
        'tgt_Z':Z,'tgt_V_minus_Z':V-Z
    }
    for (i,j),val in zip(EDGES,entries(x,y)):
        d['edge_%d_%d'%(i,j)]=val
    for i,m in enumerate(mass(x)):
        if i!=4:d['src_mass_%d'%i]=m
    for i,m in enumerate(mass(y)):d['tgt_mass_%d'%i]=m
    return d

def determinant(a):
    a=[list(row) for row in a];out=F(1);n=len(a)
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None:return F(0)
        if k!=j:a[k],a[j]=a[j],a[k];out=-out
        pivot=a[j][j];out*=pivot
        for k in range(j+1,n):
            if a[k][j]:
                ratio=a[k][j]/pivot
                for l in range(j+1,n):a[k][l]-=ratio*a[j][l]
                a[k][j]=F(0)
    return out

p0=tuple(map(F,'999/1000 1/6 1/20 29/240 11/160 1/120 871/1000 9/40 5/6'.split()))
x0,y0=model(p0)
assert tp(x0)==tp(y0) and tq(x0)==tq(y0)
assert sum(mass(x0))==sum(mass(y0))==1
assert sum(r*m for r,m in zip(R,mass(x0)))==sum(r*m for r,m in zip(R,mass(y0)))==1
assert residual(p0)==(F(0),)*21
assert len(EDGES)==14 and min(entries(x0,y0))==F(109,360000)
print('BASE_PASS 14_EDGES',min(entries(x0,y0)))

for k in range(9):
    p=list(p0);p[k]+=1
    assert residual(p)==(F(0),)*21
print('EXACT_ALL_REAL_AFFINE_IDENTITIES 10_BASIS_POINTS_21_EQUATIONS')

c0=slack(p0)
slopes=[]
for k in range(9):
    p=list(p0);p[k]+=1
    ck=slack(p)
    slopes.append({key:ck[key]-c0[key] for key in c0})
L={key:sum(abs(d[key]) for d in slopes) for key in c0}
ratio={key:c0[key]/L[key] for key in c0 if L[key]>0}
worst=min(ratio,key=ratio.get)
assert worst=='edge_4_2'
assert ratio[worst]==F(585,3227428)
print('BOX_RADIUS_EXACT_LIMITING_FACET',worst,ratio[worst],
      'center_slack',c0[worst],'L1',L[worst])
epsilon=F(1,10000)
assert all(c0[key]>epsilon*L[key] for key in c0)
print('EXACT_OPEN_NINE_PARAMETER_BOX_ALL_LAWFUL_ALL_14_EDGES_RADIUS',epsilon)

def phi(p):
    x,y=model(p)
    return mass(y)[:5]+mass(x)[:3]

phi0=phi(p0)
cols=[]
for k in (0,1,2,3,4,6,7,8):
    p=list(p0);p[k]+=1
    cols.append(tuple(a-b for a,b in zip(phi(p),phi0)))
d=determinant(tuple(zip(*cols)))
assert d==F(-1111424393,139968000000)
print('EXACT_8D_AFFINE_IMAGE_MINOR',d)

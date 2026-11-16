#!/usr/bin/env python3
"""R603: exact rational two-contour argument-principle and Rouche certificate.

Auxiliary scalar F(z)=24 sum_{j>=0}(-8z)^j/(2j+4)!; finite F_k is
R590's Catalan-derived polynomial at k=2^42. The script proves both
contour counts for F and F_k, using the R602 exact coefficient envelope.
All branch decisions are comparisons of arbitrary-precision integers/Fraction.
"""
from fractions import Fraction as Q
from math import factorial

J, M = 18, 4096
k, L = 1 << 42, 64
A = tuple(Q(24*8**j, factorial(2*j+4)) for j in range(J+2))

# R602 closed-disk upper bound, valid through |z|<=113/8.
S = Q(3*L, 2*k) + Q(L*(L+1)*(L+5), 12*k*k)
B = Q(3*(L+1), 2*(2*k-L))
E = S+B
assert 0 < E < 1 and 6*k > L*(L+3)
Ulo = 24*3**11*E/(1-E)
Utail = 24*(1 + 21*(k+1)*(2*k+1))*Q(100,99)*Q(113**65,factorial(130))
U = Ulo+Utail
assert U < Q(1,6720)

def cmul(a,b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def fj(z):
    w=(Q(0),Q(0))
    for j in range(J,-1,-1):
        w=cmul(w,z)
        w=(w[0]+(-1)**j*A[j],w[1])
    return w

def upper_nodes(r):
    # Circle traversed CCW from +r through +ir to -r.
    for m in range(M+1):
        t=Q(m,M); den=1+t*t
        yield fj((r*(1-t*t)/den, r*2*t/den))
    for m in range(M-1,-1,-1):
        t=Q(m,M); den=1+t*t
        yield fj((-r*(1-t*t)/den, r*2*t/den))

def winding_at_45_degrees(nodes):
    # Positive 45-degree ray: U=x+y>0, V=y-x=0.
    # Any crossing is transverse and no vertex lies on the ray.
    out = 0
    n=len(nodes)
    for i,p in enumerate(nodes):
        q=nodes[(i+1)%n]
        up,vp=p[0]+p[1],p[1]-p[0]
        uq,vq=q[0]+q[1],q[1]-q[0]
        det=up*vq-uq*vp
        if vp<=0<vq and det>0: out+=1
        if vq<=0<vp and det<0: out-=1
    return out

for r in (Q(13),Q(14)):
    T=A[J+1]*r**(J+1)/(1-Q(8)*r/((2*J+6)*(2*J+5)))
    D=sum((j*A[j]*r**(j-1) for j in range(1,J+1)),Q(0))
    # |F(z)-F_J(z_start)| <= T + 2*r*D/M on each circular arc.
    arc=T+2*r*D/M
    # All values exact rationals, incl. 4*M vertices.
    upper=list(upper_nodes(r))
    lower=[(w[0],-w[1]) for w in upper[-2:0:-1]]
    nodes=upper+lower
    assert len(nodes)==4*M
    nearest=min(w[0]*w[0]+w[1]*w[1] for w in upper)
    node_floor = Q(69,1000) if r==13 else Q(96,1000)
    error_ceiling = Q(46,1000) if r==13 else Q(61,1000)
    assert nearest>node_floor**2
    assert arc+U<error_ceiling
    assert node_floor>error_ceiling
    assert nearest>(arc+U)**2, ('not separated',int(r))
    assert all(w[0]!=w[1] for w in nodes)
    count=winding_at_45_degrees(nodes)
    assert count==2,('unexpected winding',int(r),count)
    print('R603_CONTOUR_CERT', 'radius',int(r),'M',M,'nodes',len(nodes),
          'node_mod_gt',round(float(nearest)**.5,11),
          'total_arc_and_Fk_error_lt',round(float(arc+U),11),
          'winding_F_and_Fk',count)

# Since rho_(2^42) lies in (13,14) (R602), both F and Fk have exactly
# two zeros inside the moving circle, counting multiplicity. No zeros
# lie in the closed annulus 13<=|z|<=14 by the two equal counts.
print('R603_COMPLETE_DYADIC_WINDOW_ZERO_COUNT_PASS')

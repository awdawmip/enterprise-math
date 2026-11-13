"""R593: two exact rational winding-number and Rouché certificates for
F(z) = 24 sum_{j>=0} (-8z)^j / (2j+4)! .
The finite calculation concerns the auxiliary scalar inverse spectrum only.
"""
from fractions import Fraction as Q
from math import factorial, comb

J = 18
A = tuple(Q(24 * 8**j, factorial(2*j + 4)) for j in range(J+2))

def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]

def eval_poly(z):
    w = (Q(0), Q(0))
    for j in range(J, -1, -1):
        w = cmul(w, z)
        w = (w[0] + (-1)**j*A[j], w[1])
    return w

def top_nodes(r, M):
    # Continuous upper half-circle, including both real endpoints.
    for m in range(M+1):
        t = Q(m,M)
        den = 1+t*t
        yield eval_poly((r*(1-t*t)/den, r*2*t/den))
    for m in range(M-1,-1,-1):
        t = Q(m,M)
        den = 1+t*t
        yield eval_poly((-r*(1-t*t)/den, r*2*t/den))

def ray_crossings(points):
    # Count oriented crossings of the ray arg(w)=pi/4; coordinates (u,v)=(x+y,y-x).
    out = 0
    for p, q in zip(points, points[1:]+points[:1]):
        up, vp = p[0]+p[1], p[1]-p[0]
        uq, vq = q[0]+q[1], q[1]-q[0]
        det = up*vq-uq*vp
        if vp <= 0 < vq and det>0: out += 1
        if vq <= 0 < vp and det<0: out -= 1
    return out

def ratio(k, j):
    # Exact factorization of a_(k,j)/a_j, with Catalan quotient recurrence.
    P=Q(1)
    for h in range(1,j+1):
        P *= (1+Q(h+3,2*k))*(1-Q(h,2*k))
    R=Q(1)
    weighted=Q(0)
    for q in range((j+1)//2+1):
        if q: R *= 1+Q(3,2*(k-q+1)-1)
        weighted += comb(j+1,2*q)*R
    return P*weighted/Q(2**j)

def cert_error(k, r, L=32):
    # Source finite polynomial degree 2k-1; j>L uses the proven R590
    # global coefficient envelope a_k,j < 21(k+1)(2k+1) a_j.
    head=sum((abs(ratio(k,j)-1)*Q(24*8**j,factorial(2*j+4))*r**j
        for j in range(L+1)),Q(0))
    first=Q(24*8**(L+1), factorial(2*(L+1)+4))*r**(L+1)
    q=Q(8)*r/((2*L+8)*(2*L+7))
    assert q<1
    return head+(1+21*(k+1)*(2*k+1))*first/(1-q)

for r,M in [(Q(10),2048),(Q(13),8192)]:
    tail=A[J+1]*r**(J+1)/(1-Q(8)*r/((2*J+6)*(2*J+5)))
    D=sum((j*A[j]*r**(j-1) for j in range(1,J+1)),Q(0))
    bound=tail+Q(2)*r*D/M
    upper=list(top_nodes(r,M))
    lower=[(w[0], -w[1]) for w in upper[-2:0:-1]]
    points=upper+lower
    worst=min(w[0]**2+w[1]**2 for w in upper)
    assert worst>bound**2
    assert all(w[1]!=w[0] for w in points)  # ray crossings never hit polygon vertices
    count=ray_crossings(points)
    assert count==(0 if r==10 else 2),(r,count)
    E=cert_error(4096,r)
    assert worst>(bound+E)**2, ('finite mismatch',r,float(E))
    if r==13:
        assert E<Q(75,676)  # F(x) >= 75/676 on [-13,13]
        print('R593_REAL_AXIS_EXCLUSION', 'k',4096, 'radius',13,'lower_F',str(Q(75,676)),'upper_diff_lt',float(E))
    print('R593_FINITE_POLY_ROUCHE', 'k',4096, 'radius',r,'error_lt',float(E),'node_bound_plus_E_lt',float(bound+E),'min_node_mod_gt',float(worst)**.5)
    print('R593_EXACT_WINDING_CERT', 'radius', r,'J',J,'M',M,
          'nodes', len(points), 'min_node_mod_gt', float(worst)**.5,
          'bound_lt',float(bound),'winding',count)
print('R593_TWO_RADIUS_EXACT_WINDING_AND_CONJUGATE_PAIR_PASS')

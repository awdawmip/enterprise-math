#!/usr/bin/env python3
"""R577 author-side exact rational certificate for F's minimal conjugate zero pair.
Frozen R462 scientific input, building on R576 auxiliary-scalar entire limit.
No floating point arithmetic in acceptance checks.
"""
from fractions import Fraction as F
from math import factorial
from sys import version

R, N, B = 14, 14, 4096

def a(j):
    return F(24 * 8**j, factorial(2*j + 4))

# Uniform positive term bounds, exact.
M = sum(j*a(j)*R**(j-1) for j in range(1,N+1))
assert M < 9, M
first = a(N+1)*R**(N+1)
q = F(8*R, (2*(N+1)+6)*(2*(N+1)+5))
tail = first/(1-q)
assert tail < F(1,10**6)
assert F(1,12) - F(2*R*9,B) > tail

# Integer polynomial D*P_N, with P_N(z)=sum (-1)^j a(j)*z^j.
D = factorial(2*N+4)//24
coeff = [(-1)**j * 8**j * factorial(2*N+4)//factorial(2*j+4) for j in range(N+1)]
assert all(F(coeff[j],D) == (-1)**j*a(j) for j in range(N+1))

# Integer Gaussian evaluation: numerator of D*d^N * P_N((x+i*y)/d).
def gaussian_poly(x,y,d):
    re, im = coeff[N], 0
    dp = d
    for j in range(N-1,-1,-1):
        re,im = re*x - im*y + coeff[j]*dp, re*y + im*x
        dp *= d
    return re,im

nodes = []
node_min_bound = F(1,12)
for qtr in range(4):
    for t in range(B):
        u = B*B
        v = t*t
        d = u+v
        x = R*(u-v)
        y = 2*R*B*t
        if qtr==1: x,y = -y,x
        elif qtr==2: x,y = -x,-y
        elif qtr==3: x,y = y,-x
        re,im = gaussian_poly(x,y,d)
        den = D * d**N
        assert 144*(re*re+im*im) > den*den, ('node lower bound',qtr,t)
        wr,wi = 37*re-im, re+37*im
        assert wi != 0, ('ray vertex', qtr,t)
        nodes.append((wr,wi))

# Polygon winding by strictly positive-real-axis crossings.
winding=0
crossings=[]
for idx,(x1,y1) in enumerate(nodes):
    x2,y2=nodes[(idx+1)%len(nodes)]
    if y1<0<y2:
        det=x1*y2-x2*y1
        assert det != 0, ('polygon hits origin', idx)
        if det>0:
            winding+=1
            crossings.append((idx,1))
    elif y1>0>y2:
        det=x1*y2-x2*y1
        assert det != 0, ('polygon hits origin', idx)
        if det<0:
            winding-=1
            crossings.append((idx,-1))
assert winding == 2, (winding,crossings)

# Exact local one-zero certificate about an explicit rational center.
cx,cy = F(63392345102, 10**10), F(94809517165,10**10)
def pair_mul(A,B):
    return (A[0]*B[0]-A[1]*B[1], A[0]*B[1]+A[1]*B[0])
def poly_pair_at(coefs, c):
    v=(coefs[-1],F(0))
    for h in reversed(coefs[:-1]):
        v=pair_mul(v,c)
        v=(v[0]+h,v[1])
    return v
P=20
c=(cx,cy)
val=poly_pair_at([(-1)**j*a(j) for j in range(P+1)],c)
der=poly_pair_at([(-1)**j*j*a(j) for j in range(1,P+1)],c)
def abs2(v):return v[0]**2+v[1]**2
assert abs2(val)<F(1,10**11)**2
assert abs2(der)>F(1,25)**2
S=12
j=P+1
q0=F(8*S,(2*j+6)*(2*j+5))
e0=a(j)*S**j/(1-q0)
q1=F(j+1,j)*q0
e1=j*a(j)*S**(j-1)/(1-q1)
assert e0 < F(1,10**13)
assert e1 < F(1,10**13)
assert F(1,25) - e1 > F(1,26)
Mq=sum(i*(i-1)*a(i)*S**(i-2) for i in range(2,P+1))
q2=F(j+1,j-1)*q0
e2=j*(j-1)*a(j)*S**(j-2)/(1-q2)
assert Mq + e2 < 2
radius=F(1,10**9)
assert F(1,10**11)+e0 + radius**2 < radius/F(26)
lo = F(114050137933,10**10)
hi = F(114050137934,10**10)
assert lo**2 < cx*cx+cy*cy < hi**2
assert (hi + radius) < R

print('R577_SOURCE_R462', '18783e01e3646c72b7aab3b16d3f565e83e6446f')
print('PYTHON', version.split()[0], 'EXACT_FRACTION_INTEGER_ONLY')
print('GLOBAL_CONTOUR radius',R,'degree',N,'nodes',len(nodes))
print('GLOBAL_MIN_VERTEX_MODULUS_GT',str(node_min_bound))
print('GLOBAL_DERIVATIVE_SUM_LT',9,'GLOBAL_TAIL_LT','1/1000000')
print('GLOBAL_POLYGON_POSITIVE_RAY_CROSSINGS',crossings)
print('GLOBAL_WINDING',winding,'=> F has two zeros in |z|<14')
print('LOCAL_CENTER',str(cx),str(cy),'LOCAL_RADIUS',radius)
print('LOCAL_APPROX_F_NORM_SQUARED_LT',str(F(1,10**11)**2))
print('LOCAL_APPROX_DF_NORM_SQUARED_GT',str(F(1,25)**2))
print('LOCAL_TAIL_BOUNDS',float(e0),float(e1),'LOCAL_F2_BOUND_LT',2)
print('NEAREST_ZERO_MODULUS_LOWER',lo-radius, 'UPPER',hi+radius)
print('SPECTRAL_CONSTANT_LOWER',1/(hi+radius),'UPPER',1/(lo-radius))
print('R577_RATIONAL_WINDING_AND_MINIMAL_PAIR_CERT_PASS')

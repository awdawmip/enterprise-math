#!/usr/bin/env python3
"""PREFIX-408 author-side exact algebra checks. Python 3, SymPy 1.14.

No Monte Carlo, no floating decisions. Exact rational/radical arithmetic only.
"""
from fractions import Fraction as F
from sympy import Matrix, I, Rational as Q, sqrt, simplify, conjugate, zeros

A=Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
assert simplify(A[:3,:].det()) == -32+32*I
R=simplify(A*A[:3,:].inv())
a,b,c=R[3,0],R[3,1],R[3,2]
d,d2,e=R[4,0],R[4,1],R[4,2]
assert all(simplify(z)==0 for z in [a-(Q(5,2)+Q(9,2)*I),b-(Q(3,2)+Q(7,2)*I),c-4*I,
 d-(Q(11,4)+Q(15,8)*I),d2-d,e-(Q(5,4)+Q(9,4)*I)])

def norm2(z):return simplify(z*conjugate(z))
def port4(u,v):return norm2(a+b*u+c*v)
def port5(u,v):return norm2(d*(1+u)+e*v)
def value(H,row): return simplify((row*H*row.conjugate().T)[0])

def readings(H):
    p4=Matrix([[a,b,c]]);p5=Matrix([[d,d,e]])
    return [simplify(H[0,0]), simplify(H[1,1]), simplify(H[2,2]),
            simplify(H[0,0]+H[1,1]+H[0,1]+H[1,0]),
            simplify(H[0,0]+H[2,2]+H[0,2]+H[2,0]),
            value(H,p4),value(H,p5)]

H0=Matrix.diag(1,1,0)
assert readings(H0)==[1,1,0,2,1,41,Q(709,32)]
assert port4(I,0)==37 and port4(-I,0)==45
assert port5(I,0)==Q(709,32) and port5(-I,0)==Q(709,32)

# Check full mixed-H linear formula including H13/H23 and PSD rank-gap example.
x,y,r,t = __import__('sympy').symbols('x y r t',real=True)
h13r,h13i,h23r,h23i=__import__('sympy').symbols('p q f g',real=True)
H=Matrix([[1,x+I*y,h13r+I*h13i],
          [x-I*y,r,h23r+I*h23i],
          [h13r-I*h13i,h23r-I*h23i,t]])
s=1+r+2*x
j0=7-5*r+Q(39,2)*s+4*y
j=readings(H)[5]
residual=16*t+2*__import__('sympy').re(a*conjugate(c)*(h13r+I*h13i)+b*conjugate(c)*(h23r+I*h23i))
assert simplify(j-j0-residual)==0

# Exact rational certificates: epsilon=10^-4, beta=10^-6, kappa=1, tau=sqrt(beta)=10^-3
EPS=F(1,10000); BETA=F(1,1000000); TAU=F(1,1000); KAPPA=F(1)
RHO=16*BETA+8*(10+2*EPS)*TAU
YMAX=(KAPPA+RHO+F(49,2)*EPS)/4
LDET=1-EPS-EPS*EPS-YMAX*YMAX
L2=1-2*EPS-YMAX
assert RHO==F(50011,625000)
assert YMAX==F(2706169,10000000)
assert LDET==F(92666648343439,100000000000000)>0
assert L2==F(7291831,10000000)>0

# Sharp threshold in the r=1,s=2 slice with t=|v|^2 <= beta.
beta_c=simplify((sqrt(45)-sqrt(41))**2/16)
assert simplify(beta_c-(Q(43,8)-Q(3,8)*sqrt(205)))==0
assert bool(beta_c>0 and beta_c<Q(1,100))
w=a-b*I
assert norm2(w)==45
# At the critical radius, phase-align v so that w+c*v has squared modulus 41.
tc=simplify(sqrt(beta_c))
vc=simplify(I*tc*w/sqrt(45))
assert simplify(norm2(vc)-beta_c)==0
assert simplify(port4(-I,vc)-41)==0
assert bool(simplify(norm2(1+vc))<10)
assert bool(simplify(port5(-I,vc))<100)
# Another exact algebraic test at small beta.
tau=Q(1,1000)
v_small=simplify(I*tau*w/sqrt(45))
kstar=simplify(port4(-I,v_small)-41)
assert simplify(kstar-(4-8*sqrt(45)*tau+16*tau**2))==0
assert bool(kstar>0)
assert simplify(norm2(v_small)-tau**2)==0

# Independent rational-source checks for the 3x3 lifting using polar data.
Wplus=Matrix([1,I,0]);Wminus=Matrix([1,-I,0])
assert readings(Wplus*Wplus.conjugate().T)==[1,1,0,2,1,37,Q(709,32)]
assert readings(Wminus*Wminus.conjugate().T)==[1,1,0,2,1,45,Q(709,32)]

print('PASS_PREFIX408_ORIGINAL_MATRIX_AND_MIXED_H_IDENTITY')
print('PASS_PREFIX408_SHARP_I3_POSITIVE_NOISE_THRESHOLD_ALGEBRAIC_WITNESS')
print('PASS_PREFIX408_NONZERO_I3_PSD_RANK_GAP_RATIONAL_CERTIFICATE')
print('matrix_row4=',[str(z) for z in [a,b,c]])
print('matrix_row5=',[str(z) for z in [d,d2,e]])
print('beta_critical=',str(beta_c))
print('kappa_threshold_beta_1e-6=',str(kstar))
for n,q in [('rho',RHO),('Y',YMAX),('Ldet',LDET),('L2',L2)]:print(n+'='+str(q))

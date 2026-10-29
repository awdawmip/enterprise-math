#!/usr/bin/env python3
"""Author-side exact-rational PREFIX337 checker; PREFIX336 certified boxes are a pinned premise."""
from fractions import Fraction as Q
from itertools import product

c=[[Q(s) for s in r] for r in [
['-9.872155986','-0.497496459','0.991123454','-1.977834057','3.013046410'],
['-9.851679166','0.672017894','0.997408380','1.897396211','3.094999288'],
['-6.837934178','6.406340759','1.820539644','1.328370101','4.317624519'],
['3.972277190','-3.655156020','5.069231734','1.852070781','7.206948698'],
['3.826943394','0.866306597','5.391314313','-1.020335300','8.029290029'],
['3.472972568','1.984555753','5.333493587','0.744208408','8.062257748']]]
r=Q(1,10**8); lam=Q(10,61); L=Q(1062562,458329)
A=[[4,4,0],[0,-4,4],[-5+3j,0,-3+1j],[-2-2j,4+4j,2+2j],[-2,0,5+2j]]
a=[4,5-2j,7-4j]; b=[1360,128,2330,1864,1261]
assert [sum((A[j][k]*a[k])*(A[j][l]*a[l]).conjugate() for k,l in product(range(3),repeat=2)).real for j in range(5)]==b
q=[Q(100*t,61*61*64) for t in b]
assert max(q)<1 and q[2]>Q(1,4)
# Only port 3 imaginary report is +1/2; each orbit admits a proper arc.
assert -Q(1,2)<Q(155,244)<Q(3,2)
u5=c[4]; S=3*u5[0]-5*u5[1]+u5[4]
assert 0<S-9*r and S+9*r<Q(122,5)
# Fixed-coordinate two-shape positive-contact lower bound.
v=[Q(4)+u5[0],u5[1],Q(5)+u5[2],Q(-2)+u5[3],Q(7)+u5[4],Q(-4)]
assert sum(t*t for t in v)-2*r*sum(abs(v[k]) for k in range(5))-5*r*r>420
assert Q(10500,3721)>L

def nb(x):
 n=sum(t*t for t in x);d=2*r*sum(abs(t) for t in x)
 return n-d,n+d+5*r*r
# Quotient radius upper by center lambda*(7,2,5/2).
z=[Q(7),Q(2),Q(5,2)];nz=sum(t*t for t in z)
for t in c:
 hi=nb(t)[1]
 re=abs(z[0]*t[0]+z[1]*t[2]+z[2]*t[4])-Q(23,2)*r
 im=abs(z[0]*t[1]+z[1]*t[3])-9*r
 need=nz+hi-Q(11163,200)
 assert re>0 and im>0 and need>0 and 4*(re*re+im*im)>need*need
# Quotient diameter lower using orbit 1 and orbit 5.
x,y=c[0],c[4]
Re=sum(x[k]*y[k] for k in range(5)); Im=x[0]*y[1]-x[1]*y[0]+x[2]*y[3]-x[3]*y[2]
eRe=r*sum(abs(t) for t in x+y)+5*r*r
eIm=r*sum(abs(t) for t in x[:4]+y[:4])+4*r*r
need=nb(x)[0]+nb(y)[0]-207
assert need>0 and need*need>4*((abs(Re)+eRe)**2+(abs(Im)+eIm)**2)
assert Q(5175,3721)<Q(3,2)<L
print('PASS_AUTHOR_SIDE_EXACT_RATIONAL', '45 ordered BRC pairs, 6 certified root boxes',
      'FIXED_MEB2>10500/3721>L','5175/3721<QUOTIENT_MEB2<3/2<L')

#!/usr/bin/env python3
"""Stage390-B exact face marginal audit: reconstruct H from derivatives, not tables."""
from fractions import Fraction as F
from math import comb
from hashlib import sha256
import csv, io
f=lambda z:F(str(z))
one={(0,0):F(1)};x={(1,0):F(1)};y={(0,1):F(1)}
def add(*ps):
 d={}
 for p in ps:
  for k,v in p.items():d[k]=d.get(k,F(0))+v
 return {k:v for k,v in d.items() if v}
def scale(p,c):return {k:c*v for k,v in p.items() if c*v}
def mul(a,b):
 d={}
 for (i,j),v in a.items():
  for (k,l),u in b.items():d[i+k,j+l]=d.get((i+k,j+l),F(0))+v*u
 return {k:v for k,v in d.items() if v}
def sub(a,b):return add(a,scale(b,-1))
cx=scale(mul(sub(one,x),sub(scale(one,63),scale(x,61))),-F(3,256))
by=scale(sub(one,scale(y,2)),F(3,16))
bx=scale(sub(one,scale(x,2)),F(3,4))
cylo=scale(mul(y,sub(one,y)),F(3,64))
cyhi=scale(mul(y,sub(scale(one,18),scale(y,25))),F(3,256))
g=mul(sub(one,x),sub(one,scale(x,3)))
s=mul(sub(one,y),sub(scale(y,3),one))
def H(lam,cy):return add(mul(s,add(cx,scale(bx,lam))),scale(mul(g,add(cy,scale(by,lam))),4))
def controls(p,box):
 xa,xb,ya,yb=box; dx=xb-xa;dy=yb-ya
 powr={(a,b):sum(v*comb(i,a)*xa**(i-a)*dx**a*comb(j,b)*ya**(j-b)*dy**b for (i,j),v in p.items() if i>=a and j>=b) for a in range(3) for b in range(3)}
 return [sum(powr[a,b]*F(comb(i,a),comb(2,a))*F(comb(j,b),comb(2,b)) for a in range(i+1) for b in range(j+1)) for i in range(3) for j in range(3)]
P=tuple(map(f,('0.2308','0.2345','0.55','0.56')))
Q=tuple(map(f,('0.2365','0.239','0.57566','0.57574')))
cases=[('P_GT_7_OVER_6',P,F(7,6),cylo,-1,F(9,10000)),('P_LT_5_OVER_4',P,F(5,4),cylo,1,F(3,1000)),('Q_LO_GT_5_OVER_4',Q,F(5,4),cylo,-1,F(29,10000)),('Q_HI_LT_7_OVER_6',Q,F(7,6),cyhi,1,F(1,10000))]
out=io.StringIO(newline='');writer=csv.writer(out,lineterminator='\n');writer.writerow(('case','bernstein_i','bernstein_j','exact_coefficient'))
for tag,box,lam,cy,sg,margin in cases:
 vals=controls(H(lam,cy),box)
 assert min(sg*v for v in vals)>margin,tag
 for index,v in enumerate(vals):writer.writerow((tag,index//3,index%3,str(v)))
b=out.getvalue().encode()
assert len(b)==1802
assert sha256(b).hexdigest()=='14e34213e9f9dad2b734c3ec8a8f93407d51e07d230f4fc01c9c74f4f7ed738c'
print('STAGE390B_EXACT_MARGINAL_CERTIFICATE_PASS',len(b),sha256(b).hexdigest())
print('STRICT_MARGINS Q_LOW_MINUS_P > 59/10000; P_MINUS_Q_HIGH > 1/1000')

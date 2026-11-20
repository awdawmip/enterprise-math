#!/usr/bin/env python3
"""Exact 36-control Bernstein certificate; Stage381-B. Python standard library."""
from fractions import Fraction as F
from math import comb
from hashlib import sha256
import csv,io
P=tuple(map(F,('0.2308','0.2345','0.55','0.56')))
Q=tuple(map(F,('0.2365','0.239','0.57566','0.57574')))
CO={
'P_GT_7_OVER_6':(P,-1,{(2,2):405,(2,1):-1932,(2,0):855,(1,2):420,(1,1):1296,(1,0):-820,(0,2):-153,(0,1):-260,(0,0):189}),
'P_LT_5_OVER_4':(P,1,{(2,2):405,(2,1):-2028,(2,0):903,(1,2):516,(1,1):1296,(1,0):-852,(0,2):-201,(0,1):-228,(0,0):189}),
'Q_LO_GT_5_OVER_4':(Q,-1,{(2,2):405,(2,1):-2028,(2,0):903,(1,2):516,(1,1):1296,(1,0):-852,(0,2):-201,(0,1):-228,(0,0):189}),
'Q_HI_LT_7_OVER_6':(Q,1,{(2,2):-351,(2,1):-1428,(2,0):855,(1,2):1428,(1,1):624,(1,0):-820,(0,2):-405,(0,1):-92,(0,0):189})}
def cert():
 out=io.StringIO(newline=''); w=csv.writer(out,lineterminator='\n'); w.writerow(('case','bernstein_i','bernstein_j','exact_coefficient'))
 for tag,(box,sg,coef) in CO.items():
  xa,xb,ya,yb=box;dx=xb-xa;dy=yb-ya
  power={(i,j):sum(F(a,256)*comb(k,i)*xa**(k-i)*dx**i*comb(l,j)*ya**(l-j)*dy**j for (k,l),a in coef.items() if k>=i and l>=j) for i in range(3) for j in range(3)}
  for i in range(3):
   for j in range(3):
    b=sum(power[(k,l)]*F(comb(i,k),comb(2,k))*F(comb(j,l),comb(2,l)) for k in range(i+1) for l in range(j+1))
    assert sg*b>0,(tag,i,j,b)
    w.writerow((tag,i,j,str(b)))
 return out.getvalue().encode()
if __name__=='__main__':
 result=cert()
 assert len(result)==1802
 assert sha256(result).hexdigest()=='14e34213e9f9dad2b734c3ec8a8f93407d51e07d230f4fc01c9c74f4f7ed738c'
 print('STAGE381B_SIGN_CERTIFICATE_MINI_PASS',len(result),sha256(result).hexdigest())

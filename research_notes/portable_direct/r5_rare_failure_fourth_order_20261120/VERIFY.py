#!/usr/bin/env python3
"""R5 N^92 coefficient: exact standard-library audit (no floats)."""
import json,sys,hashlib,zipfile
from math import comb
from fractions import Fraction

PIN='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
C=lambda n,r:comb(n,r) if n>=r>=0 else 0
S=sum(range(219,315));Q=sum(k*k for k in range(219,315))
R=sum(range(214,219));T=sum(k*k for k in range(214,219))
U=sum(k**3 for k in range(214,219))
E=sum(range(222,315));J=219*220*221
R1=sum([214,216,217,218,219,220,221])
R2=sum([215,216,217,218,219,220,221])
def ints(m):
    # Independent micro-multiplicity enumeration: a,b singletons, c,d triple sums
    i01=i02=i12=i012=0
    for a in range(m):
      for b in range(m):
       for c in range(m):
        for d in range(m):
         w=C(c+2,2)*C(d+2,2)
         x=a+b+c<m;y=a+c+d<m;v=b+c+d<m
         i01+=w*(x and y);i02+=w*(x and v)
         i12+=w*(y and v);i012+=w*(x and y and v)
    return int(i01),int(i02),int(i12),int(i012)
def k_closed(m):
    if m%2==0:return m*(m+2)*(m+4)*(m+6)*(65*m**4+660*m**3+2170*m**2+2616*m+768)//322560
    return (m+1)*(m+3)*(m+5)*(65*m**5+855*m**4+3760*m**3+6336*m**2+2991*m-567)//322560
def formula(m):
    b,c,d,g=(C(m+4,r) for r in (5,6,7,8))
    h,j=C(m+6,7),C(m+6,8)
    A2=Fraction(S*S,8)-Fraction(Q,24)
    A3=Fraction(S**3-S*Q,48)
    M2=d*(R*R+T)+c*T
    M3=g*R**3+3*(g+d)*R*T+(2*g+3*d+c)*U
    five=b*A3-c*R*A2+Fraction(S*M2,4)-Fraction(M3,6)
    seven=J*(Fraction(h*(E+215),2*215)-Fraction(j*R1,215)+Fraction(h*(E+214),2*214)-Fraction(j*R2,214))
    return five+seven-J*k_closed(m)
def vectors(r,t):
    if r==1:
      yield (t,)
    else:
      for x in range(t+1):
        for rest in vectors(r-1,t-x):yield (x,)+rest
def moments(m,prices):
    a=[0,0,0,0]
    for t in range(m):
      for v in vectors(len(prices),t):
       w=sum(x*y for x,y in zip(prices,v))
       for j in range(4):a[j]+=w**j
    return a
def main():
    if len(sys.argv)>1:
      p=sys.argv[1]
      if p.endswith('.zip'):
        with zipfile.ZipFile(p) as z:raw=z.read('EXACT_R5_ALL_101_BUDGETS.json')
      else:raw=open(p,'rb').read()
      assert hashlib.sha256(raw).hexdigest()==PIN
      assert json.loads(raw)['budget_range']==[214,314]
    assert (S,Q,R,T,U,J,E,R1,R2)==(25584,6891856,1080,233290,50394960,10647780,24924,1525,1526)
    for m in range(1,21):
      i01,i02,i12,i012=ints(m)
      assert i01==i02
      assert i01==m*(m+1)**2*(m+2)*(m+3)*(m+4)*(m+5)*(m+6)//10080
      assert i12==m*(m+1)*(m+2)*(m+3)**2*(m+4)*(m+5)*(m+6)//20160
      assert i01+i02+i12-i012==k_closed(m)
    for m in (1,2,3,8,17):
      b,c,d,g=(C(m+4,r) for r in (5,6,7,8))
      v=moments(m,list(range(214,219)))
      assert v==[b,c*R,d*(R*R+T)+c*T,g*R**3+3*(g+d)*R*T+(2*g+3*d+c)*U]
      h,j=C(m+6,7),C(m+6,8)
      for prices,r in (([214,*range(216,222)],R1),([215,*range(216,222)],R2)):
        w=moments(m,prices)
        assert w[:2]==[h,j*r]
      print('PASS',m,'K',k_closed(m),'B92',formula(m))
    print('PASS exact source-pin check if supplied; overlap enumeration and moment identities')
if __name__=='__main__':main()

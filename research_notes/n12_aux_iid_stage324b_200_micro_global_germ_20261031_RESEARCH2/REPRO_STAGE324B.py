#!/usr/bin/env python3
"""Stage324-B. Exact rational global-exterior/local-interval certificate.

Only Python standard-library Fraction; no floating-point inference.
Scope: Stage323-B named auxiliary BRC Bernoulli model, conditional on the
already cited Stage307-B.2, Stage315-B, Stage316-B author proofs.
"""
from fractions import Fraction as Q
from math import comb
class I:
 def __init__(self,a,b=None):
  self.lo,self.hi=Q(a),Q(a if b is None else b)
  assert self.lo<=self.hi
 @staticmethod
 def cast(x):return x if isinstance(x,I) else I(x)
 def __add__(self,x):
  x=I.cast(x);return I(self.lo+x.lo,self.hi+x.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,x):return self + -I.cast(x)
 def __rsub__(self,x):return I.cast(x)+-self
 def __mul__(self,x):
  x=I.cast(x);a=[u*v for u in (self.lo,self.hi) for v in (x.lo,x.hi)];return I(min(a),max(a))
 __rmul__=__mul__
 def __truediv__(self,x):
  x=I.cast(x);assert x.lo*x.hi>0,(x.lo,x.hi)
  return self*I(1/x.hi,1/x.lo)
 def __rtruediv__(self,x):return I.cast(x)/self
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  if n==0:return I(1)
  if n%2:return I(self.lo**n,self.hi**n)
  return I(0 if self.lo<=0<=self.hi else min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
 def within(self,a,b):return self.lo>Q(a) and self.hi<Q(b)
 def __repr__(self):return f'I({self.lo},{self.hi})'
p=(Q(61,160),Q(21,160),Q(9,160),Q(9,160))
def B(k,z):return z**k*(1-z)**(3-k)
def r(k,x,y):return Q(4,5)*B(k,x)+Q(1,5)*B(k,y)-p[k]
def d(x,y):return sum((Q(comb(3,k),2)*abs(r(k,x,y)) for k in range(4)),Q(0))
def extrema(k,a,b):
 out=[B(k,a),B(k,b)]
 if k in (1,2) and a<=Q(k,3)<=b:out.append(B(k,Q(k,3)))
 return min(out),max(out)
def lower(A):
 a,b,c,e=A; ans=Q(0)
 for k in range(4):
  l,h=extrema(k,a,b);v,w=extrema(k,c,e)
  lo=Q(4,5)*l+Q(1,5)*v-p[k]; hi=Q(4,5)*h+Q(1,5)*w-p[k]
  ans+=Q(comb(3,k),2)*max(0,lo,-hi)
 return ans
def split(A):
 a,b,c,e=A
 if b-a >= e-c:
  m=(a+b)/2;return (a,m,c,e),(m,b,c,e)
 m=(c+e)/2;return (a,b,c,m),(a,b,m,e)
W=(Q(231083940855,10**12),Q(555508857277,10**12))
U=d(*W)
ROOT_X_LO=Q(231083940855521,10**15)
ROOT_X_HI=Q(231083940855522,10**15)
ROOT_Y_LO=Q(555508857277,10**12)
ROOT_Y_HI=Q(555508857278,10**12)
def exterior(RX,RY,delta):
 x0,x1=RX;y0,y1=RY
 bases=((Q(0),x0,Q(0),Q(1)),(x1,Q(1),Q(0),Q(1)),(x0,x1,Q(0),y0),(x0,x1,y1,Q(1)))
 threshold=Q(16,5)*delta
 counts=[];mingap=None
 for rect in bases:
  todo=[rect];nodes=leaves=0
  while todo:
   v=todo.pop();nodes+=1
   z=lower(v)-U
   if z>threshold:
    leaves+=1
    if mingap is None or z<mingap:mingap=z
   else:
    if nodes>80000:return False,counts,nodes,v,z
    todo.extend(split(v))
  counts.append((nodes,leaves))
 return True,counts,mingap,mingap-threshold

def gradients(x,y):
 g0=(-Q(12,5)*(1-x)**2,-Q(3,5)*(1-y)**2)
 g1=(Q(4,5)*(1-x)*(1-3*x),Q(1,5)*(1-y)*(1-3*y))
 g2=(Q(4,5)*x*(2-3*x),Q(1,5)*y*(2-3*y))
 gc=(-(1-x)*(189-183*x)/256,Q(3,64)*y*(1-y))
 return g0,g1,g2,gc

def certify_tv_chambers(RX,RY):
    cases=(
        ('quarter-x',Q(1,4),RX,(-1,+1,+1,+1)),
        ('threequarter-x',Q(3,4),RX,(-1,-1,+1,+1)),
        ('quarter-y',Q(1,4),RY,(+1,+1,-1,-1)),
        ('threequarter-y',Q(3,4),RY,(-1,-1,+1,+1)),
    )
    for name,anchor,(a,b),signs in cases:
        for k,s in enumerate(signs):
            lo,hi=extrema(k,a,b); ref=B(k,anchor)
            assert (ref>hi if s>0 else ref<lo),(name,k,s)
    print('ALL_16_TV_SIGNS_STRICT_EXACT')

def tiles(RX,RY,N):
 slopes={('r0','right'):(Q(-11,10),Q(-7,10)),('r1','right'):(Q(-13,10),Q(-11,10)),('r1','left'):(Q(8,5),Q(2)),('r0','left'):(Q(5,2),Q(41,10))}
 for i in range(N):
  for j in range(N):
   x=I(RX[0]+(RX[1]-RX[0])*i/N,RX[0]+(RX[1]-RX[0])*(i+1)/N)
   y=I(RY[0]+(RY[1]-RY[0])*j/N,RY[0]+(RY[1]-RY[0])*(j+1)/N)
   if not(r(2,x,y).lo>0 and r(3,x,y).hi<0):return False,('r23',i,j)
   g0,g1,g2,gc=gradients(x,y)
   if not(gc[0].hi<0 and gc[1].lo>0):return False,('gc',i,j)
   for t0,t1 in ((0,0),(0,1),(1,0),(1,1)):
    bx=Q(5,16)*(3*g2[0]+t0*g0[0]+3*t1*g1[0]);by=Q(5,16)*(3*g2[1]+t0*g0[1]+3*t1*g1[1])
    det=bx*gc[1]-by*gc[0]
    if not((det.lo>0) if (t0,t1)==(0,0) else (det.hi<0)):return False,('det',i,j,t0,t1,det)
   for kind,g,other in (('r0',g0,g1),('r1',g1,g0)):
    if not g[1].hi<0:return False,('gy',i,j,kind)
    v=-g[0]/g[1]
    if not v.within(-Q(27,2),Q(27,2)):return False,('v',i,j,kind,v)
    cross=other[0]+other[1]*v
    if not(cross.lo>0 if kind=='r0' else cross.hi<0):return False,('cross',i,j,kind,cross)
    dc=gc[0]+gc[1]*v
    for side in ('right','left'):
     if kind=='r0':t0,t1=0,1 if side=='right' else 0
     else:t0,t1=(0 if side=='right' else 1),0
     bx=Q(5,16)*(3*g2[0]+t0*g0[0]+3*t1*g1[0]);by=Q(5,16)*(3*g2[1]+t0*g0[1]+3*t1*g1[1]);db=bx+by*v
     if not(db.lo>Q(7,50) if side=='right' else db.hi< -Q(7,50)):return False,('db',i,j,kind,side,db)
     lo,hi=slopes[kind,side]
     if not (dc/db).within(lo,hi):return False,('slope',i,j,kind,side,dc/db)
   v=-g1[0]/g1[1]
   ypp=-(Q(4,5)*(-4+6*x)+Q(1,5)*(-4+6*y)*v**2)/g1[1]
   bx=Q(15,16)*g2[0];by=Q(15,16)*g2[1]
   bxx=Q(15,16)*Q(4,5)*(2-6*x);byy=Q(15,16)*Q(1,5)*(2-6*y)
   cxx=(372-366*x)/256;cyy=(3-6*y)/64
   bd=bx+by*v;cd=gc[0]+gc[1]*v
   bdd=bxx+byy*v**2+by*ypp
   cdd=cxx+cyy*v**2+gc[1]*ypp
   curvature=(cdd*bd-cd*bdd)/bd**3
   if not (bd.lo>0 and curvature.within(-48,-34)):return False,('curve',i,j,curvature)
 return True,N*N

if __name__=='__main__':
    # Fixed rational region; no floats enter the proof.
    RX=(Q(9,40),Q(237,1000))
    RY=(Q(107,200),Q(1151,2000))
    DELTA=Q(1,5000)
    N=32
    print('STAGE324B_REGION',RX,RY,'DELTA',DELTA)
    certify_tv_chambers(RX,RY)
    ok,counts,mingap,margin=exterior(RX,RY,DELTA)
    assert ok and counts==[(127,64),(61,31),(31,16),(283,142)]
    assert sum(b for a,b in counts)==253 and margin>0
    print('EXTERIOR_COUNTS',counts,'TOTAL_LEAVES',253)
    print('MIN_RIGOROUS_GAP',mingap)
    print('THRESHOLD',Q(16,5)*DELTA,'STRICT_MARGIN',margin)
    ok,tiles_pass=tiles(RX,RY,N)
    assert ok and tiles_pass==N*N
    print('LOCAL_EXACT_INTERVAL_TILES',tiles_pass)
    print('CHAMBERS_AND_SLOPES_STRICT_EXACT')
    print('CURVATURE_BOUND', '-48 < C3_second_derivative < -34')
    L=Q(29,20000)
    assert Q(7,50)*L>DELTA
    assert L<min(ROOT_X_LO-RX[0], RX[1]-ROOT_X_HI)
    assert Q(27,2)*L<min(ROOT_Y_LO-RY[0], RY[1]-ROOT_Y_HI)
    print('EXACT_BRANCH_REACH',L,'BUDGET_RISE_LOWER',Q(7,50)*L)
    print('STAGE324B_200_MICRO_GLOBAL_PARETO_EXACT_PASS')

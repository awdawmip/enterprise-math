"""R141 exact certificate: sharp lower one-sided uniform D-radius of 52."""
from fractions import Fraction as Q
from x6_r140_sharp_uniform_D_tube_verify import population,TARGET,CELLS,capacity,affine_diff,nonnegative,f

# Refine the first B-cell exactly at the prospective first-contact B=20.
CELLS8=[(Q(0),Q(20),6,500,1,(1,0,0)),
        (Q(20),Q(316,7),6,500,1,(1,0,0))]+CELLS[1:]

def multiply(p,q):
 out=[Q(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):out[i+j]+=x*y
 return out

def polynomial_nonnegative(poly,lo,hi):
 p=list(map(Q,poly))
 while len(p)>1 and p[-1]==0:p.pop()
 def value(v):return sum(c*v**k for k,c in enumerate(p))
 if value(lo)<0:return False
 if hi is None:
  return len(p)<=2 and (len(p)==1 or p[1]>=0)
 if value(hi)<0:return False
 if len(p)==3 and p[2]>0:
  vertex=-p[1]/(2*p[2])
  if lo<vertex<hi and value(vertex)<0:return False
 return True

def outsider_certificate(g,lo,hi,K,L0,L1):
 # m=min(B,136). For B<=136: m=B, for B>=136: m=136.
 m0,m1=(0,1) if hi is not None and hi<=136 else (136,0)
 for j,gj in enumerate(g):
  s0,s1=capacity(j,500)
  left=multiply([2*gj*L0,2*gj*L1],[448+m0,m1])
  right=multiply([3*K*s0,3*K*s1],[500+m0,m1])
  poly=[a-b for a,b in zip(left,right)]
  if polynomial_nonnegative(poly,lo,hi):return j
 return None

def main():
 pop=population();assert len(pop)==1935
 inside=outside=sharp_lower=sharp_upper=0
 for lo,hi,K,L0,L1,_ in CELLS8:
  for a,g in pop.items():
   if a in TARGET:
    for j in range(6):
     assert nonnegative(affine_diff(g,j,K,L0,L1,448,125,88),lo,hi),('inside',lo,a,j)
     inside+=1
   else:
    pair=outsider_certificate(g,lo,hi,K,L0,L1)
    assert pair is not None,('outsider',lo,a)
    outside+=1
 assert (inside,outside)==(8*4*6,8*1931)
 # On B=20, D in [440,448] the 1,935 directions all satisfy F_D>=6/(20+D).
 # The direction (1,0,0) attains equality throughout; hence eta_D=6/(20+D).
 for a,g in pop.items():
  if any(all(g[j]*(D+20)>=6*(capacity(j,D)[0]+capacity(j,D)[1]*20)
             for D in [Q(440),Q(448)]) for j in range(6)):
   sharp_lower+=1
  else:raise AssertionError(('sharp_optimizer_lower',a))
 for D in [Q(440),Q(444),Q(447),Q(448)]:
  B=Q(20)
  assert f((1,0,0),B,D)==Q(6,B+D)
  assert f((6,-1,0),B,D)==Q(1,52)
  eta=min(f(a,B,D) for a in pop)
  assert eta==Q(6,B+D)
  if D<448:
   assert 2*f((6,-1,0),B,D)<3*eta
  else:
   assert 2*f((6,-1,0),B,D)==3*eta
  sharp_upper+=1
 # Representative exact 1,935-direction replays across unbounded B and the lower contact.
 replays=0
 for B in [Q(1,1000),Q(1),Q(8),Q(20),Q(30),Q(46),Q(100),Q(136),Q(1000000)]:
  for D in [Q(448),Q(449),Q(460),Q(472),Q(490),Q(500)]:
   e=min(f(a,B,D) for a in pop)
   near={a for a in pop if 2*f(a,B,D)<3*e}
   assert near==TARGET,('near',B,D,near^TARGET)
   replays+=1
 print('R141 SHARP LOWER ONE-SIDED UNIFORM D-TUBE CERTIFICATE PASS')
 print('population',len(pop),'inside_448',inside,'outsider_quadratic',outside)
 print('sharpness_lower_witness_checks',sharp_lower,'sharpness_full_optimizer_replays',sharp_upper)
 print('full_fraction_near_replays',replays,'D_interval',(448,500),'lower_open_radius',52)

if __name__=='__main__':main()

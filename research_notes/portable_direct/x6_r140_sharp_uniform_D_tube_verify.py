"""Exact Port-10 six-pair BRC R140 certificate. No third-party packages.
Scope: w=(136,B,176,D), B>0, |D-500|<28.
"""
from fractions import Fraction as Q

TARGET={(1,0,0),(5,-4,1),(5,-1,0),(9,-5,1)}
# (B lower, B upper [None=+infinity], eta_0 numerator, denominator base, B slope, witness)
CELLS=[
 (Q(0),Q(316,7),6,500,1,(1,0,0)),
 (Q(316,7),Q(320,7),7,636,0,(1,0,0)),
 (Q(320,7),Q(46),2,136,1,(5,-1,0)),
 (Q(46),Q(556,7),6,500,1,(5,-1,0)),
 (Q(556,7),Q(796,7),7,676,0,(5,-1,0)),
 (Q(796,7),Q(136),3,176,1,(9,-5,1)),
 (Q(136),None,1,104,0,(9,-5,1)),
]

def gaps(a):
 x,y,z=a
 h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
 return tuple(abs(h[i]-h[j]) for i in range(4) for j in range(i+1,4))

def population():
 return {(x,y,z):gaps((x,y,z))
   for x in range(-10,11) for y in range(-10,11) for z in range(-10,11)
   if (x,y,z)!=(0,0,0)
   and max(sum(max(a,0) for a in (x,y,z)), sum(max(-a,0) for a in (x,y,z)))<=10
   and next(a for a in (x,y,z) if a)!=-abs(next(a for a in (x,y,z) if a))}

def capacity(j,d):
 return [(136,1),(312,0),(136+d,0),(176,1),(d,1),(176+d,0)][j]

def affine_diff(g,j,K,L0,L1,d,n_left,n_right):
 """n_left*K*s(B,d)-n_right*g*L(B)."""
 c,s=capacity(j,d)
 return n_left*K*c-n_right*g[j]*L0,n_left*K*s-n_right*g[j]*L1

def nonnegative(aff,lo,hi):
 a,b=aff
 return (a+b*lo>=0 and (b>=0 if hi is None else a+b*hi>=0))

def f(a,B,d):
 return max(Q(v,capacity(j,d)[0]+capacity(j,d)[1]*B) for j,v in enumerate(gaps(a)))

def main():
 pop=population();assert len(pop)==1935 and TARGET<=pop.keys()
 count={'optimizer_lower':0,'optimizer_upper':0,'outsider_8_5':0,'inside_125_88_D500':0,'inside_125_88_D472':0}
 for lo,hi,K,L0,L1,wit in CELLS:
  # Proof of exact eta at D=500: every vector's score >= proposed eta,
  # and an explicit witness attains it.
  wg=pop[wit]
  assert any(affine_diff(wg,j,K,L0,L1,500,1,1)==(0,0) for j in range(6))
  for j in range(6):
   assert nonnegative(affine_diff(wg,j,K,L0,L1,500,1,1),lo,hi)
   count['optimizer_upper']+=1
  for a,g in pop.items():
   # exists a pair with g/s>=eta0; multiply by positive denominators.
   assert any(nonnegative(tuple(-x for x in affine_diff(g,j,K,L0,L1,500,1,1)),lo,hi) for j in range(6)),('lower',lo,a)
   count['optimizer_lower']+=1
   if a in TARGET:
    # Every pair of each insider at D=500 and D=472 is <=125/88 eta0.
    for d,label in [(500,'inside_125_88_D500'),(472,'inside_125_88_D472')]:
     for j in range(6):
      assert nonnegative(affine_diff(g,j,K,L0,L1,d,125,88),lo,hi),('inside',d,lo,a,j)
      count[label]+=1
   else:
    # One fixed pair on this entire B-cell has F0>=8/5 eta0.
    assert any(nonnegative(tuple(-x for x in affine_diff(g,j,K,L0,L1,500,8,5)),lo,hi) for j in range(6)),('outside',lo,a)
    count['outsider_8_5']+=1
 assert count=={'optimizer_lower':13545,'optimizer_upper':42,'outsider_8_5':13517,'inside_125_88_D500':168,'inside_125_88_D472':168},count
 assert Q(125,88)*Q(528,500)==Q(3,2)
 assert Q(8,5)*Q(472,500)>Q(3,2)
 assert Q(8,5)*Q(500,528)>Q(3,2)
 # Sharpness: B>0 can approach zero; D=528+2B,
 # eta<=F_(1,0,0)=2/(176+B), while F_(9,-5,1)>=3/(176+B).
 for B in [Q(1,1000),Q(1),Q(20)]:
  D=Q(528)+2*B
  e=min(f(a,B,D) for a in pop)
  assert f((1,0,0),B,D)==Q(2,176+B)==e
  assert f((9,-5,1),B,D)>=Q(3,176+B) and 2*f((9,-5,1),B,D)>=3*e
 # Supplementary complete exact replays, including boundary/interior and huge B.
 replays=0
 for B in [Q(1,1000),Q(1),Q(8),Q(20),Q(46),Q(100),Q(136),Q(1000000)]:
  for D in [Q(472),Q(473),Q(486),Q(500),Q(514),Q(527),Q(528)]:
   e=min(f(a,B,D) for a in pop)
   near={a for a in pop if 2*f(a,B,D)<3*e}
   assert near==TARGET,(B,D,e,near^TARGET)
   replays+=1
 print('R140 SHARP UNIFORM OPEN D-TUBE EXACT CERTIFICATE PASS')
 print('population',len(pop),'target',sorted(TARGET))
 print('certificates',count)
 print('full_fraction_replays',replays,'sharp_open_radius',28,'uniform_D_interval',(472,528))

if __name__=='__main__':main()

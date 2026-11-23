"""R138: exact certificate for (136,B,176,500), B>0, Port=10."""
from fractions import Fraction as Q

BASE=(136,312,636,176,500,676)
SLOPE=(1,0,0,1,1,0)
TARGET={(1,0,0),(5,-4,1),(5,-1,0),(9,-5,1)}
# B_low, B_high (None = +infinity), eta=K/(L0+L1*B), optimizing witness
CELLS=[
 (Q(0),Q(316,7),6,500,1,(1,0,0)),
 (Q(316,7),Q(320,7),7,636,0,(1,0,0)),
 (Q(320,7),Q(46),2,136,1,(5,-1,0)),
 (Q(46),Q(556,7),6,500,1,(5,-1,0)),
 (Q(556,7),Q(796,7),7,676,0,(5,-1,0)),
 (Q(796,7),Q(136),3,176,1,(9,-5,1)),
 (Q(136),None,1,104,0,(9,-5,1)),
]

def gaps(x,y,z):
 h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
 return tuple(abs(h[i]-h[j]) for i in range(4) for j in range(i+1,4))

def all_directions():
 return {
  (x,y,z):gaps(x,y,z)
  for x in range(-10,11) for y in range(-10,11) for z in range(-10,11)
  if (x,y,z)!=(0,0,0)
  and max(sum(v for v in (x,y,z) if v>0),-sum(v for v in (x,y,z) if v<0))<=10
  and next(v for v in (x,y,z) if v)!=-abs(next(v for v in (x,y,z) if v))
 }

# (g*L-K*s)(B) in exact affine form, with multiplicative coefficients.
def affine(g,j,K,L0,L1,ng,ns):
 return (ng*g[j]*L0-ns*K*BASE[j],ng*g[j]*L1-ns*K*SLOPE[j])

def nonnegative(coeff,lo,hi,strict=False):
 c,d=coeff
 if hi is None and d<0:return False
 v=c+d*lo
 if hi is not None:v=min(v,c+d*hi)
 return v>0 if strict else v>=0

def f(B,g):
 return max(Q(g[j],BASE[j]+SLOPE[j]*B) for j in range(6))

def run():
 D=all_directions()
 assert len(D)==1935
 assert len(D.keys() - TARGET)==1931
 lower=excluded=upper=inside=0
 for lo,hi,K,L0,L1,wit in CELLS:
  assert all(BASE[j]+SLOPE[j]*lo>0 for j in range(6))
  # Check proposed witness upper bound and one identically tight pair.
  assert any(affine(D[wit],j,K,L0,L1,1,1)==(0,0) for j in range(6))
  for j in range(6):
   assert nonnegative(affine(D[wit],j,K,L0,L1,-1,-1),lo,hi)
   upper+=1
  for a,g in D.items():
   assert any(nonnegative(affine(g,j,K,L0,L1,1,1),lo,hi) for j in range(6)),('lower',a,lo)
   lower+=1
   if a not in TARGET:
    assert any(nonnegative(affine(g,j,K,L0,L1,2,3),lo,hi) for j in range(6)),('outsider',a,lo)
    excluded+=1
   else:
    for j in range(6):
     assert nonnegative(affine(g,j,K,L0,L1,-2,-3),lo,hi,strict=True),('inside',a,j,lo)
     inside+=1
  for B in [lo+(hi-lo)/3, (lo+hi)/2, lo+2*(hi-lo)/3] if hi is not None else [lo+Q(1,3),lo+100,lo+1000000]:
   eta=min(f(B,g) for g in D.values())
   near={a for a,g in D.items() if 2*f(B,g)<3*eta}
   assert eta==Q(K,L0+L1*B) and near==TARGET
  if hi is not None:
   B=hi; eta=min(f(B,g) for g in D.values())
   assert eta==Q(K,L0+L1*B)
   assert {a for a,g in D.items() if 2*f(B,g)<3*eta}==TARGET
 print('R138 CERTIFICATE PASS')
 print('unoriented_directions',len(D),'optimizer_lower_certificates',lower,
       'outsider_exclusion_certificates',excluded,'witness_pair_checks',upper,
       'insider_strict_pair_checks',inside)
 print('optimizer_breakpoints',[str(c[0]) for c in CELLS[1:]])
 print('near_set',sorted(TARGET),'independent_exact_replays',3*7+6)
if __name__=='__main__':run()

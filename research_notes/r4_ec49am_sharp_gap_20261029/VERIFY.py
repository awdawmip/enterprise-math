from fractions import Fraction as F
from itertools import product,combinations
import json
C=(1,1,2,2,0);CUT=F(25,32);A=F(27,172)
G=F(216,473);LAM=A-G;B=G*CUT;ETA=F(41,1106)
verts={}
for m in range(3):
 other=[w for w in range(3) if w!=m]
 for i,j in product(range(5),repeat=2):
  target=F(43,16)-C[i]-C[j]
  for a,b in combinations(range(5),2):
   if not min(C[a],C[b])<target<max(C[a],C[b]):continue
   p=(target-C[b])/(C[a]-C[b]);x=[[F(0)]*5 for _ in range(3)]
   x[other[0]][i]=x[other[1]][j]=F(1)
   x[m][a]=p;x[m][b]=1-p
   assert all(sum(row)==1 for row in x)
   assert sum(C[c]*x[w][c] for w in range(3) for c in range(5))==F(43,16)
   key=tuple(tuple(row) for row in x);verts[key]=key
assert len(verts)==168

def atoms(x,eta):
 for c,u in product(range(4),range(2)):
  q=[x[w][c]*(F(1,2)+(2*u-1)*(1-w)*eta)/3 for w in range(3)]
  T=sum(q);V=sum(max(F(0),43*t-16*T) for t in q)
  yield T,V

def dual(x,eta):return sum((max(F(0),V/172-LAM*T) for T,V in atoms(x,eta)),F())
def full(x,eta):
 z=list(atoms(x,eta));return sum((T for T,V in z),F()),sum((V/172 for T,V in z),F())
cert={}
for eta in (F(0),ETA):
 values=[dual(x,eta) for x in verts]
 assert max(values)==B and all(v<=B for v in values)
 assert sum(v==B for v in values)==24
 cert[str(eta)]={'maximum':str(max(values)),'tight':24,'strict':144}
Z=F();O=F(1)
sat=((O,Z,Z,Z,Z),(Z,O,Z,Z,Z),(Z,Z,F(11,32),Z,F(21,32)))
high=((F(11,16),Z,Z,Z,F(5,16)),(O,Z,Z,Z,Z),(Z,O,Z,Z,Z))
swap=((Z,F(11,16),Z,Z,F(5,16)),(O,Z,Z,Z,Z),(Z,O,Z,Z,Z))
for eta in (F(0),ETA):
 assert full(sat,eta)==(CUT,A*CUT)
 assert full(high,eta)==full(swap,eta)==(F(43,48),F(243,2752))
assert full(swap,F(1,26))[1]-F(243,2752)==F(5,53664)
assert (A*F(43,48)-F(243,2752))/(F(43,48)-CUT)==G
print(json.dumps({'schema':'EC49AM_EXACT_FRACTION_V1','status':'PASS_EXACT_AUTHOR_UNREVIEWED',
 'model':'18+18 positive auxiliary BRC','C1':'43/48','eta_interval':'[0,41/1106]',
 'support':'H<=-567*C2/1892+675/1892','gap_slope':str(G),'distinct_vertices':len(verts),
 'fibre_checks':len(verts)*8*2,'dual_endpoint_certificate':cert,
 'saturation_C2':'25/32','sharp_C2':'43/48','sharp_H':'243/2752',
 'postcritical_eta':'1/26','postcritical_excess':'5/53664'},indent=2))

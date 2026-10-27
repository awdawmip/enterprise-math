"""Exact standard-library certificate for BRC N=3 reverse-crossing (2/5,1/3)."""
from fractions import Fraction as F
from itertools import product
import json
L=(874,1131,121,-53);D=240
# t,state,Q*D,P*D,children
N={'':(0,0,240,240,('a','b')),
'a':(1,2,120,180,('ax','ay')),
'b':(1,1,120,60,('bu','bv')),
'ax':(2,4,60,60,('axL','axM','axH')),
'ay':(2,5,60,120,('ayT',)),
'bu':(2,4,30,30,('buL','buM','buH')),
'bv':(2,3,90,30,('bvT',)),
'axL':(3,7,24,12,()),'axM':(3,8,12,12,()),'axH':(3,9,24,36,()),
'ayT':(3,10,60,120,()),
'buL':(3,7,10,5,()),'buM':(3,8,10,10,()),'buH':(3,9,10,15,()),
'bvT':(3,6,90,30,())}
def check():
 assert len(N)==15 and sum(not z[4] for z in N.values())==8
 assert N['ax'][1]==N['bu'][1]==4
 for h,(t,s,q,p,ch) in N.items():
  assert q>0 and p>0
  if ch:
   assert all(N[k][0]==t+1 for k in ch)
   assert sum(N[k][2] for k in ch)==q
   assert sum(N[k][3] for k in ch)==p
 assert F(N['axL'][2],N['ax'][2])==F(2,5)
 assert F(N['buL'][2],N['bu'][2])==F(1,3)
def obs(policy,history=False):
 def rec(h):
  t,s,q,p,ch=N[h];a=policy[h] if history else policy[s]
  if a==2:
   assert ch
   return tuple(sum(v) for v in zip(*(rec(k) for k in ch)))
  assert a in (0,1)
  return (p if a==1 else 0,q if a==0 else 0,t*p,t*q)
 return rec('')
def dot(v):return sum(a*b for a,b in zip(L,v))
def rank(rows):
 a=[[F(x) for x in r] for r in rows]
 if not a:return 0
 r=0
 for k in range(len(a[0])):
  j=next((i for i in range(r,len(a)) if a[i][k]),None)
  if j is None:continue
  a[r],a[j]=a[j],a[r];z=a[r][k]
  a[r]=[v/z for v in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][k]:
    z=a[i][k];a[i]=[x-z*y for x,y in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r
def bellman():
 choices={}
 def rec(h):
  t,s,q,p,ch=N[h]
  v=[L[1]*q+t*(L[2]*p+L[3]*q),L[0]*p+t*(L[2]*p+L[3]*q)]
  if ch:v.append(sum(rec(k) for k in ch))
  a=min(range(len(v)),key=lambda x:v[x]);choices[h]=a
  return v[a]
 return rec(''),choices
def main():
 check()
 points={};tables=0
 for nt in product(range(3),repeat=6):
  for tr in product(range(2),repeat=5):
   v=obs(nt+tr);points.setdefault(v,nt+tr);tables+=1
 assert tables==23328 and len(points)==326
 C=min(map(dot,points))
 assert C==851*D
 eq=sorted(v for v in points if dot(v)==C)
 assert eq==sorted([(84,84,480,420),(60,120,330,450),
                    (120,60,510,570),(69,94,600,660)])
 assert rank([[v[i]-eq[0][i] for i in range(4)] for v in eq[1:]])==3
 ambient=[(0,240,0,0),(240,0,0,0),(0,240,240,240),
          (180,120,240,240),(0,240,420,360)]
 assert all(v in points for v in ambient)
 assert rank([[v[i]-ambient[0][i] for i in range(4)] for v in ambient[1:]])==4
 Fmin,acts=bellman()
 w=obs(acts,True)
 assert Fmin==850*D and w==(84,84,570,630) and dot(w)==Fmin
 coll=lambda s:(F(1131),F(874),F(942)-180*s)
 assert coll(F(2,5))==(1131,874,870)
 assert coll(F(1,3))==(1131,874,882)
 forced=[]
 for a in range(3):
  va=min(F(1131),F(257,2)+(coll(F(2,5))[a]+1131)/2)
  vb=min(F(437),F(15,2)+coll(F(1,3))[a]/4+F(3,4)*F(836,3))
  forced.append(min(F(1131),F(874),F(68)+(va+vb)/2))
 assert forced==[852,851,851]
 print(json.dumps({'status':'PASS_EXACT_FRACTION_INTEGER_240',
  'ordered_prefix_count':15,'positive_terminals':8,
  'compressed_policy_tables':tables,'distinct_vectors':len(points),
  'normal':list(L),'compressed_min':'851','full_min':'850','gap':'1',
  'witness':['7/20','7/20','19/8','21/8'],
  'forced_action_minima':[str(x) for x in forced],
  'facet_vectors_240':[list(x) for x in eq],
  'facet_dimension':3,'ambient_dimension':4,
  'full_policy':acts},indent=2,sort_keys=True))
if __name__=='__main__':main()

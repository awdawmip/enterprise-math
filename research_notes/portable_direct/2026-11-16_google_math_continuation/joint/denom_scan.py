import sympy as s
from itertools import product
from functools import lru_cache
D,E=s.symbols('D E'); H=(1+D)**5
A=(1+E)*(1+D)**3
B=s.expand(-4*(D**5-121*D**4+70*D**3*E+381*D**3-365*D**2*E-121*D**2+185*D*E+D-5*E))
P=(20,20,20,-100,140,-100); S=[tuple(P[(a+k)%6] for k in range(3)) for a in range(6)]
U=sorted(set(P))
C={x:s.Poly(((A-H)*x+B).subs(E,0),D) for x in U}
P_H=s.Poly(H,D)
def pol(v):return tuple(v.all_coeffs())
allkeys={}
for a,b in product(range(6),repeat=2):
 if a==b:continue
 for i,j in product(range(3),repeat=2):
  for sign in (-1,1):
   u=C[S[a][i]] - sign*(C[S[a][j]] + (S[a][j]-S[b][j])*P_H)
   if not u.is_zero:
    q=u.primitive()[1]
    if q.LC()<0:q=-q
    allkeys[pol(q)]=q
roots=[]
for _,poly in allkeys.items():
 for iv,m in poly.intervals(eps=s.Rational(1,10**18),inf=s.Rational(-1,2),sup=s.Rational(1,2)):
  (l,h)=iv
  roots.append((l,h,poly))
def classify(param):
 out=[]
 for aa,sa in enumerate(S):
  y=[(A*x+B).subs({D:param,E:0}) for x in sa]; h=H.subs(D,param)
  dt=max(abs(val-h*t) for val,t in zip(y,sa))
  for bb,sb in enumerate(S):
   dr=max(abs(val-h*t) for val,t in zip(y,sb))
   if aa!=bb and dr<=dt:out.append((aa,bb,s.sign(dt-dr)))
 return out
R=sorted(roots,key=lambda v: (v[0]+v[1])/2)
# concatenate intervals which overlap: duplicate polynomial factors give the same real root.
groups=[]
for l,u,poly in R:
 if groups and l<=groups[-1][1]:
  groups[-1][0]=max(groups[-1][0],l);groups[-1][1]=min(groups[-1][1],u);groups[-1][2].append(poly)
 else:groups.append([l,u,[poly]])
for sg in (1,-1):
 seq=[z for z in groups if sg*(z[0]+z[1])>0]
 seq.sort(key=lambda z:sg*(z[0]+z[1])/2)
 prev=0
 for l,u,ps in seq:
  boundary=(l+u)/2
  if sg>0: right=u+s.Rational(1,10**15)
  else:right=l-s.Rational(1,10**15)
  bad=classify(right)
  if bad:
   print('direction',sg,'boundary',float(boundary),'poly',[v.as_expr().factor() for v in ps], 'after',bad)
   break
  prev=boundary
print('npolys',len(allkeys),'rootgroups',len(groups))

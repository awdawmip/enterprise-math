from fractions import Fraction as F
from math import gcd, floor, ceil
from pathlib import Path
import hashlib,json,itertools
raw=Path('root_8800_result.json').read_bytes(); assert hashlib.sha256(raw).hexdigest()=='367ed5c982ef92405623cfe6633aa29ce1449bfa2e1cb2e355fd8692d84355a9'
G=10**85; E=400000
D=json.loads(raw); R,C,T=[tuple(F(int(v),G) for v in D[k]) for k in ('rho','c','d')]
R=tuple(F(int(v),G) for v in json.load(open('root_9200_only.json'))['rho'])
V=((13241695572016246280452795405,-614903515325433031059117378,-586453816401334287434546),(1182616791650392258028253444,-74796824988556406807726418,4246778208283374384362279),(-7752265403315380654172299023,382363756442351370763912993,-4494886358260478563501531))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
W=tuple(zip(cross(V[1],V[2]),cross(V[2],V[0]),cross(V[0],V[1])))
assert tuple(tuple(dot(v,w) for w in zip(*W)) for v in V)==((1,0,0),(0,1,0),(0,0,1))
qmin=2655223732550132521125580881859760580045275386620690; Q=10**53; J=4*E/T[0]; K=9*T[1]/8; H=2*T[1]+F(4*E,qmin)
# Triple signed envelope from inherited q^2<=JL and q>qmin-1.
up=K*J**2/qmin**3; uh=H*J/qmin
# qmin<=q<=Q, rho_l*q-up<=p<=rho_u*q, c_l*q<=h<=c_u*q+uh.
ineq=[((1,0,0),Q),((-1,0,0),-qmin),((R[0],-1,0),up),((-R[1],1,0),0),((C[0],0,-1),0),((-C[1],0,1),uh)]
# Bounds on integer coordinates V*(q,p,h) from corners of the relaxed envelope.
ranges=[]
for a,b,c in V:
 vals=[q*(a+b*r+c*s)+b*dp+c*dh for q,r,s,dp,dh in itertools.product((qmin,Q),R,C,(-up,0),(0,uh))]
 ranges.append((ceil(min(vals)),floor(max(vals))))
print('ranges',ranges)
# Solve six linear rational inequalities for n3 given n1,n2; no point omitted.
lin=[(tuple(dot(v,w) for w in zip(*W)),F(z)) for v,z in ineq]
ans=[]; loops=0
for i in range(ranges[0][0],ranges[0][1]+1):
 for j in range(ranges[1][0],ranges[1][1]+1):
  loops+=1; lo,hi=ranges[2]
  for (a,b,c),z in lin:
   t=z-a*i-b*j
   if c>0:hi=min(hi,floor(t/c))
   elif c<0:lo=max(lo,ceil(t/c))
   elif t<0:lo,hi=1,0;break
   if lo>hi:break
  for k in range(lo,hi+1):
   v=tuple(dot(w,(i,j,k)) for w in W)
   assert all(dot(a,v)<=b for a,b in ineq)
   if gcd(v[0],v[1])==1:ans.append(v)
ans.sort(); assert ans
q,p,h=ans[0]; print('loops',loops,'primitive',len(ans),'first',ans[0]); print('interior',R[0]<F(p,q)<R[1],C[0]<F(h,q)<C[1]); print('L lower',float(F(q*q)/J))
# Earliest admissible fixed dyadic window using the sharpened curvature bound.
M=16225927682921336339157801028812800000000
Lmin=F(q*q)/J; Ldy=M
while Ldy<Lmin:Ldy*=2
print('dyadic',Ldy, float(Ldy))
# Witness for an alternative parameter tuple in the very first possible window.
# Start with a,z exact, then add half the middle deficit to all three.
d=sum(T)/2; r=F(p,q); c=F(h,q); assert R[0]<r<R[1] and C[0]<c<C[1]
res=(-h*pow(p,-1,q))%q
U=2*Ldy-2*q-1
a=U-(U-res)%q; b=a+q; z=a+2*q
assert Ldy<=a<b<z<2*Ldy
half=d*q*q/(2*a*b*z)
rho=r+d/(a*z); cc=c-d*(F(1,a)+F(1,z))+half
assert R[0]<rho<R[1] and C[0]<cc<C[1]
es=[]
for m in (a,b,z):
 j=(p*m+h)//q;assert (p*m+h)%q==0
 e=rho*m+cc+d/m-j;assert abs(e)<=F(E,m*m);es.append(str(e))
assert list(map(F,es))==[half,-half,half]
print('witness a',a,'max paid ratio',float(half*z*z/E))
Lw=Ldy
out={'root_sha256':hashlib.sha256(raw).hexdigest(),'qmin':qmin,'Q':Q,'V':V,'W':W,'ranges':ranges,'loops':loops,'primitive_count':len(ans),'minimum':ans[0],'minimum_L':str(Lmin),'minimum_dyadic_L':Ldy,'alternate_witness':{'L':Lw,'a':a,'b':b,'z':z,'rho':str(rho),'c':str(cc),'d':str(d),'residuals':es}}
Path('prefix1122_triple_result.json').write_text(json.dumps(out,indent=2)+'\n')

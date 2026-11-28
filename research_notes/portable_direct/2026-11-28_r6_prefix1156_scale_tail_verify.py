from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import ceil,floor,gcd
import json
exec(Path('compact1155.py').read_text().split('for k,Q,count,first in ')[0])
Dlo,Dhi=map(F,D['d']);E=400000
V1=[[20839059154566493384795139689658450197601238,-26897700663133634638294416165316484982146692,5606646818542096015328933697759139119704985],[280996554924487750583611309046779829147806595,-364607240431463813767031909913007015267323883,76014920921031980974219288911332178174259181],[-139443533935683305293461051245667161836382364,180532933108698600546845964376267214502343919,-37635174028234959492787411148405626852076432]]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
det=dot(V1[0],cross(V1[1],V1[2]));assert abs(det)==1
W1=[[det*x for x in row] for row in zip(cross(V1[1],V1[2]),cross(V1[2],V1[0]),cross(V1[0],V1[1]))]
qmin=1139688307034066686122654499404718613400485815666141431682213091323282338737490244883
for k,Q,count,firstq in [(10**12,3*10**82,0,None),(10**12,10**83,1,70837709903771231385867098177167500596835781776090002534552248252159934499565934467),(10**14,10**84,9,623497620077981545738456090529212339213639795828531044223845536973068296063582237766),(10**15,10**84,2,852374384268198652888669476357277045986335990106224723976582814891224520119456349115),(10**16,3*10**84,40,qmin),(10**18,3*10**84,36,qmin),(10**38,3*10**84,36,qmin)]:
    box,N,pts,ls=search(k,Q,V1,W1);assert len(ls)==count and (ls[0][0] if ls else None)==firstq
    print('PASS',k,Q,box,N,pts,count,firstq)
    if k==10**16:minimum=ls[0]
# Exact proof of the two-sided positive scale envelope on the first two dyadic windows.
first=10**8
while first<L:first*=2
assert first*4>=F(4077,1000)*L
kl=Dlo/4-F(2*E,q0);hl=Dlo-F(4*E,q0);assert kl>0 and hl>0
def signed(line,l):
    q,p,h=line
    return all(a*p+b*h<=q*(z+max(-a*kl/l**2,-a*K/l**2)+max(b*hl/l,b*H/l)) for a,b,z in J)
assert [[signed(line,first*2**i) for i in range(2)] for line in lines]==[[False,False],[True,False],[False,True]]
assert not search(F(4077,1000),10**79,V,W)[3]
# Minimum candidate is an interior point of the zero-scale full affine model.
G=10**140;aj,am,dj=map(F,(D['aj'],D['am'],D['dj']));E1=json.load(open('point1153.json'));m,e,C=[E1[t] for t in ('m','e','cols')];N=len(m);U=C+[[e[i] if i==j else 0 for i in range(N)] for j in range(N)]
A=[-G*aj,-G*dj]+[0]*(N-2);B=[0,G*am]+[0]*(N-2)
q,p,h=minimum;v=[a*(F(p,q)-r)+b*(F(h,q)-u)-c for a,b,c in zip(A,B,m)]
piv=[5,0,14,15,16,17,18,19,3,21,22,23,1,4,2];free=[j for j in range(27) if j not in piv]
z=[F(0)]*27
for j,x in zip(free,[-627115483651,-627115483651,-627115483651,627115483651,627115483651,-627115483651,-627115483651,-627115483651,-627115483651,627115483651,-627115483651,-160007696567]):z[j]=F(x,10**12)
M=[[F(U[j][i]) for j in piv]+[v[i]-sum(z[j]*U[j][i] for j in free)] for i in range(N)]
for i in range(N):
    j=next(j for j in range(i,N) if M[j][i]);M[i],M[j]=M[j],M[i];x=M[i][i];M[i]=[a/x for a in M[i]]
    for j in range(N):
        if j!=i:
            x=M[j][i];M[j]=[a-x*b for a,b in zip(M[j],M[i])]
for j,row in zip(piv,M):z[j]=row[-1]
assert all(dot(z,c)==x for c,x in zip(zip(*U),v));assert 1-max(map(abs,z))>F(3728,10000)
oldq=lines[0][0];old3=old2=new3=new2=10**8
while old3<=Dlo*oldq**2/(4*E):old3*=2
while old2<oldq**2:old2*=2
assert min(old3,old2)>10**130
while new3<=Dlo*qmin**2/(4*E):new3*=2
while new2<qmin**2:new2*=2
assert new3//old3==new2//old2==2**35
print('PASS dyadic and zero-fiber; windows',new3,new2)

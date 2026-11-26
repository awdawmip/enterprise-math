"""Exact finite certificate; assumes PREFIX-1107 sign and PREFIX-1114 density correspondence."""
from fractions import Fraction as F
from math import lcm, gcd
from collections import defaultdict
import hashlib, json
G=10**85; E=400000
A=[(214400367204046439832747905320189591538351105920951930768238591471336985753828331576226,214400367204046439832747905320189591538351105920951930768238591471337016618243377672837),(991410104376806546245006442360370506919542722555360711737697284896267798454119146866295,991410104376806546245006442360370506919542722555360711737697284896271170423247861515800),(96908626596415488199625924806903600960651737707918479478269855624901489595100026049591,96908626596415488199625924806903600960651737707918479478269855625221421002362182677574)]
B=[(214400367204046439832747905320189591538351105920951930768238591471337001196109386645552,214400367204046439832747905320189591538351105920951930768238591471337001196656728356815),(991410104376806546245006442360370506919542722555360711737697284896269484458469127177428,991410104376806546245006442360370506919542722555360711737697284896269484518264379180719),(96908626596415488199625924806903600960651737707918479478269855625061452448312226656203,96908626596415488199625924806903600960651737707918479478269855625061458121669367665141)]
assert all(l<=u<=v<=h for (l,h),(u,v) in zip(A,B))
A,B=[[(F(l,G),F(h,G)) for l,h in box] for box in (A,B)]
R,C,T=A
def fs(n,m,a,b):
    q,a=divmod(a,m);ans=q*n*(n-1)//2
    q,b=divmod(b,m);ans+=q*n
    while True:
        if a>=m:q,a=divmod(a,m);ans+=q*n*(n-1)//2
        if b>=m:q,b=divmod(b,m);ans+=q*n
        y=a*n+b
        if y<m:return ans
        n,b=divmod(y,m);m,a=a,m
def sf(l,h,a,b):
    w=lcm(a.denominator,b.denominator)
    return fs(h-l+1,w,int(a*w),int((a*l+b)*w))
def band(box,m):
    r,c,d=box
    return r[0]*m+c[0]+d[0]/m-F(E,m*m),r[1]*m+c[1]+d[1]/m+F(E,m*m)
def strip(l,h):
    x=F(l+h,2)
    al=R[0]-T[0]/x**2;bl=C[0]+2*T[0]/x-F(E,l*l)
    au=R[1]-T[1]/(l*h);bu=C[1]+T[1]*F(l+h,l*h)+F(E,l*l)
    return sf(l,h,au,bu)+sf(l,h,-al,-bl)+h-l+1
def isolate(l,h):
    stack=[(l,h)];pts=[];nodes=covered=0
    while stack:
        a,b=stack.pop();cnt=strip(a,b);nodes+=1;assert cnt>=0
        if cnt==0:covered+=b-a+1;continue
        if a==b:
            lo,hi=band(A,a);jl=-((-lo.numerator)//lo.denominator);jh=hi.numerator//hi.denominator
            assert cnt==jh-jl+1;pts.extend((a,j) for j in range(jl,jh+1));continue
        mid=(a+b)//2;stack.extend([(mid+1,b),(a,mid)])
    assert covered+len({a for a,j in pts})==h-l+1
    return nodes,pts
l=10**8;pts=[];nodes=windows=0
while l<10**35:
    h=2*l-1
    assert (R[1]-R[0])*h+C[1]-C[0]+(T[1]-T[0])/l+F(2*E,l*l)<1
    n,p=isolate(l,h);pts+=p;nodes+=n;windows+=1;l*=2
assert (windows,nodes,len(pts),l)==(90,5170,22,123794003928538027489912422400000000)
assert hashlib.sha256(json.dumps(pts,separators=(',',':')).encode()).hexdigest()=='c000cf55b3d47848c40c44c1054616a8de93606fb5033268f57bcc2d19ee96e5'
thresholds=[]
for i,(m,j) in enumerate(pts,1):
    lo=(j-C[1]-T[1]/m-F(E,m*m))/m
    hi=(j-C[0]-T[0]/m+F(E,m*m))/m
    assert R[0]<lo<=hi<R[1];thresholds.append((lo,hi,i,m,j))
thresholds.sort();gaps=[b[0]-a[1] for a,b in zip(thresholds,thresholds[1:])]
assert min(gaps)>0
order=[i for _,_,i,_,_ in thresholds]
assert order==[13,1,11,9,7,21,6,19,2,5,17,4,3,15,14,22,12,20,10,18,8,16]
p=pts[1][1]-pts[0][1];q=pts[1][0]-pts[0][0];assert gcd(p,q)==1
lines=defaultdict(list)
for i,(m,j) in enumerate(pts,1):lines[q*j-p*m].append(i)
assert list(lines.values())==[[1,2,3,4,5,6,7,9,11,13],[8,10,12,14,15,17,19,21],[16,18,20,22]]
mid=[F((int(a*G)+int(b*G))//2,G) for a,b in B]
neg=[];pos=[];final=[]
for _,_,i,m,j in thresholds:
    lo,hi=band(B,m);assert j<lo or j>hi
    final.append(max(lo-j,j-hi));(neg if j<lo else pos).append(i)
    assert (mid[0]*m+mid[1]+mid[2]/m).__floor__()==(j if j<lo else j-1)
assert neg==order[:14] and pos==order[14:]
print('windows',windows,'nodes',nodes,'candidates',len(pts),'closed',len(final),'cut',len(neg))
print('threshold gap > 0:',min(gaps)>0,'minimum final gap > 0:',min(final)>0)
print('certified scales',l-10**8)

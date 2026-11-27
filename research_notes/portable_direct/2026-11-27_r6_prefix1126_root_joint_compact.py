from replay_9600_n300_gmp import *
from math import isqrt,floor,ceil
G=10**180
class I:
    def __init__(self,a,b=None):
        self.a=F(floor(F(a)*G),G); self.b=F(ceil(F(a if b is None else b)*G),G);assert self.a<=self.b
    @staticmethod
    def cast(x):return x if isinstance(x,I) else I(x)
    def __add__(self,x):x=I.cast(x);return I(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,x):return self+-I.cast(x)
    def __rsub__(self,x):return I.cast(x)+-self
    def __mul__(self,x):
        x=I.cast(x);a=[u*v for u in (self.a,self.b) for v in (x.a,x.b)];return I(min(a),max(a))
    __rmul__=__mul__
    def __truediv__(self,x):x=I.cast(x);assert x.a*x.b>0;return self*I(1/x.b,1/x.a)
    def __rtruediv__(self,x):return I.cast(x)/self
    def __pow__(self,n):
        assert n>=0;v=I(1)
        for _ in range(n):v*=self
        return v
    def mag(self):return max(abs(self.a),abs(self.b))
    def out(self):return [str(floor(self.a*10**95)),str(ceil(self.b*10**95))]
    def show(self):return [float(self.a),float(self.b),float(self.b-self.a)]

def fall(n,j):return prod(range(n-j+1,n+1)) if n>=j else 0
def dp(p,j):return [p[n]*fall(n,j) for n in range(j,len(p))]
def grid_pair(a):
    a=F(a)*G
    return floor(a),ceil(a)
def grid_horner(p,t):
    l=u=0; tl,tu=floor(t.a*G),ceil(t.b*G)
    for al,au in reversed(p):
        vv=(l*tl,l*tu,u*tl,u*tu)
        l=min(vv)//G+al;u=-(-max(vv)//G)+au
    return I(F(l,G),F(u,G))
def horner(p,t):return grid_horner([grid_pair(a) for a in p],t)
Tmax=F(127,100);cut=N;degree=2*(cut+2+10)
def norm(p,j):return sum(abs(v)*Tmax**i for i,v in enumerate(dp(p,j)))
# Exact previously verified BRC anchor construction, same frozen source.
# Reuse the completed exact packet; no repeated anchor reconstruction.
packet=json.load(open('anchor_compact.json'))
cc=[F(int(v),10**120) for v in packet['center']];inv=[[F(int(v),10**140) for v in row] for row in packet['weighted_columns_rows']];eps=[F(1)]*6;dr=[F(int(v),10**140) for v in packet['rounding_radii']];rad=[sum(map(abs,row))+d for row,d in zip(inv,dr)]
def dual(v):return sum(abs(sum(v[i]*inv[i][j] for i in range(6)))*eps[j] for j in range(6))+sum(abs(a)*b for a,b in zip(v,dr))
boxes=json.load(open('joint_result.json'))['bounds']; parent=json.load(open('root_9200_only.json'));rl,ru=[F(int(v),10**85) for v in parent['rho']]
blo,bhi=1/(1+ru),1/(1+rl);b=I(blo,bhi)
# t=sqrt(36*b), use integer square root of scaled rational; enclose exactly.
lo=isqrt(floor(36*blo*G*G));hi=isqrt(floor(36*bhi*G*G))+1
t=I(F(lo,G),F(hi,G));assert t.a>F(5,4) and t.b<Tmax
assert t.a*t.a<=36*blo<=36*bhi<=t.b*t.b
pp=[];tails=[]
rowp=[[F(rr[i//2]) if i%2==0 else F(0) for i in range(2*len(rr)-1)] for rr in nums]
rowbound=[sum(norm(p,j) for p in rowp) for j in range(6)]
for a,z,h,err,T in basis:
    p=[F(0)]*(degree+1);off=int(2*a)
    for n in range(cut+1):
        for i,v in enumerate(z[n]+[h[0][n],h[1][n]]):
            for k,w in enumerate(nums[i]):p[off+2*(n+k)]+=v*w
    pp.append(p);tail=[]
    for j in range(6):
        n=N+1;power=off+2*n
        ratio=Tmax*Tmax/2*F(power+2-j+1,power-j+1)**j;assert ratio<1
        tail.append(64*T*F(1,2)**n*fall(power,j)*Tmax**(power-j)/(1-ratio))
    tails.append(tail)
for j in range(2):
    p=[F(0)]*(degree+1)
    for k,w in enumerate(nums[7+j]):p[2*(k+j)]=F(w)
    pp.append(p);tails.append([F(0)]*6)
# Point enclosure and interval Newton; use signed F' on entire parent box.
oldjet=json.load(open('root_8800_result.json'));D0=10**85
slope=I(*[F(int(x),D0) for x in oldjet['F_jets'][1]]);assert slope.b<0
print("polynomials ready",flush=True)
newton=[]
for it in range(3):
    x=F(floor((t.a+t.b)*G/2),G)
    vals=[horner(p,I(x)) for p in pp]
    mids=[(v.a+v.b)/2 for v in vals];widths=[(v.b-v.a)/2 for v in vals]
    center=sum(a*v for a,v in zip(cc,mids));ar=dual(mids)
    rounding=sum((abs(a)+r)*w for a,r,w in zip(cc,rad,widths))
    tail=sum((abs(a)+r)*rowbound[0]*tr[0] for a,r,tr in zip(cc,rad,tails))
    total=ar+rounding+tail;fx=I(center-total,center+total)
    image=I(x)-fx/slope;t=I(max(t.a,image.a),min(t.b,image.b))
    newton.append(dict(t=t.out(),width=float(t.b-t.a),fx=fx.out(),payments=[str(ceil(y*10**140)) for y in (ar,rounding,tail)]));print('newton',it,newton[-1],flush=True)
b=t*t/36;rho=1/b-1
rho=I(max(rho.a,rl),min(rho.b,ru))

print('ROOT',rho.out(),rho.show(),flush=True)
json.dump(dict(rho=rho.out(),grid='10^95',t=t.out(),newton=newton,anchor=[8400,8800,9200,9600]),open('root_compact.json','w'),indent=2)
# PREFIX-1125 root-conditioned joint observer, using same anchor columns.
from itertools import combinations
c0=sum(F(int(v),D0) for v in oldjet['c'])/2
x=F(floor((t.a+t.b)*G/2),G);r=max(x-t.a,t.b-x)
xi=I(x);D=198/xi**2+216/(4-xi**2)+216/(16-xi**2)
alpha=36/xi**2-2+(1-xi**2/36)*D/2;beta=9/xi-xi/4
fval=[horner(p,xi) for p in pp];gval=[beta*horner(dp(p,2),xi)+(alpha-c0)*horner(dp(p,1),xi) for p in pp]
# Product-rule tails (tail_i[j] bounds derivative of each Frobenius tail component).
def tt(j):return sum((abs(a)+rr)*sum(comb(j,k)*rowbound[k]*tr[j-k] for k in range(j+1)) for a,rr,tr in zip(cc,rad,tails))
ft=tt(0);gt=beta.mag()*tt(2)+(alpha-c0).mag()*tt(1)
fm=[(v.a+v.b)/2 for v in fval];gm=[(v.a+v.b)/2 for v in gval]
ferr=ft+sum((abs(a)+rr)*(v.b-v.a)/2 for a,rr,v in zip(cc,rad,fval));gerr=gt+sum((abs(a)+rr)*(v.b-v.a)/2 for a,rr,v in zip(cc,rad,gval))
# Rounding the column entries outward to 10^-180 increases only axis error.
cols=[]
for j in range(6):cols.append((sum(fm[i]*inv[i][j] for i in range(6))*eps[j],sum(gm[i]*inv[i][j] for i in range(6))*eps[j]))
for i in range(6):cols.append((fm[i]*dr[i],gm[i]*dr[i]))
rounded=[]
for u,v in cols:
 uu=F(floor(u*G),G);vv=F(floor(v*G),G);ferr+=abs(u-uu);gerr+=abs(v-vv);rounded.append((uu,vv))
cols=rounded+[(F(ceil(ferr*G),G),F(0)),(F(0),F(ceil(gerr*G),G))]
f=sum(a*b for a,b in zip(cc,fm));g=sum(a*b for a,b in zip(cc,gm))
tr=json.load(open('tangent_result.json'));assert F(tr['c0'])==c0
Gp=I(*map(F,tr['Gp']));rect=((slope.a,slope.b),(Gp.a,Gp.b))
def support(f,g,cols,rect,r):
 lines=[(sg*r*v,-sg*r*u) for sg in (-1,1) for u in rect[0] for v in rect[1]];ss={F(0)}
 ss.update(v/u for u,v in cols if u)
 ss.update((c-a)/(b-d) for (a,b),(c,d) in combinations(lines,2) if b!=d)
 def upper(s):return g-s*f+sum(abs(v-s*u) for u,v in cols)+max(a+b*s for a,b in lines)
 s=min(ss,key=lambda s:(upper(s),s));return upper(s),s
hi,sh=support(f,g,cols,rect,r);neg,sl=support(f,-g,[(u,-v) for u,v in cols],(rect[0],(-rect[1][1],-rect[1][0])),r);lo=-neg
assert lo<=hi
ci=I(c0)+I(lo,hi)/slope
oldc=I(*[F(int(v),D0) for v in oldjet['c']]);assert oldc.a<ci.a<=ci.b<oldc.b
print('JOINT',ci.out(),ci.show(),'c gain',float((oldc.b-oldc.a)/(ci.b-ci.a)),flush=True)
print('G point axis errors',float(ferr),float(gerr),'G conditioned',float(lo),float(hi),'optimal s',float(sh),float(-sl),flush=True)
json.dump(dict(c=ci.out(),grid='10^95',c0=str(c0),f=str(f),g=str(g),cols=[[str(u),str(v)] for u,v in cols],rect=[[str(u) for u in a] for a in rect],radius=str(r),lo=str(lo),hi=str(hi),s_upper=str(sh),s_lower=str(sl),point_axis_errors=[str(F(ceil(ferr*G),G)),str(F(ceil(gerr*G),G))]),open('joint_compact.json','w'),indent=2)

# PREFIX-1096 derivative extension. Parent reconstruction below is verbatim PREFIX-1095 through basis construction.
# Frozen parent: dc4fcdd14e85a886f07b6484ee67acd260e5081a. Reuse certified anchors and root interval; no re-anchor.
# PREFIX-1095: exact rational certificate of the first negative lower-band edge.
# Source: frozen PREFIX-1082, 1093, 1094 and 1094b; no external numerical reference.
# Python 3 + SymPy. All decision arithmetic is integer or rational; float only display.
from collections import Counter
from itertools import product
import sympy as sy
from sympy.polys.matrices import DomainMatrix
import hashlib,json
R=sy.symbols('R')
shifts=[(3,0,0,0,0,0),(2,1,0,0,0,0),(2,0,0,0,0,0),
        (1,1,0,0,0,0),(1,0,0,0,0,0),(0,0,0,0,0,0)]
rows={}; relations=[]; repeats=0; differences=0
for a in shifts:
    g=sorted(Counter(a).items()); av=[v for v,_ in g]
    r=[n for _,n in g]; A=sum(a)
    states=list(product(*(range(n+1) for n in r)))
    ix={h:i for i,h in enumerate(states)}; n=len(states)
    U=sy.zeros(n); D=sy.zeros(n); H=sy.diag(*map(sum,states))
    J=sy.diag(*(sum(v*k for v,k in zip(av,h)) for h in states))
    I=sy.eye(n)
    bs=[tuple(sorted(v for aa,h,rr in zip(av,hs,r)
                    for v in [aa+1]*h+[aa]*(rr-h))) for hs in states]
    for h in states:
        i=ix[h]
        for k in range(len(r)):
            if h[k]<r[k]:
                U[i,ix[h[:k]+(h[k]+1,)+h[k+1:]]]=r[k]-h[k]
            if h[k]:
                D[i,ix[h[:k]+(h[k]-1,)+h[k+1:]]]=h[k]
    P=R*(I-D)-U; B=H+J-I+(I-A*I-H)*D
    dm=DomainMatrix.from_Matrix(P)
    num,den=dm.inv_den(); nm=num.to_Matrix()*B
    dv=dm.domain.to_sympy(den)
    for i,b in enumerate(bs):
        row={bb:sy.cancel(nm[i,j]/dv) for j,bb in enumerate(bs) if nm[i,j]!=0}
        if b in rows:
            repeats+=1
            rel={k:sy.cancel(rows[b].get(k,0)-row.get(k,0))
                 for k in set(rows[b])|set(row)}
            relations.append(rel)
            if any(v!=0 for v in rel.values()):differences+=1
        else:rows[b]=row
assert (len(rows),repeats,differences)==(35,43,43)
assert sum(map(len,rows.values()))==548
bs=sorted(rows)
base=[b for b in bs if max(b)<=1]; rest=[b for b in bs if max(b)>1]
order=rest+base
C=sy.Matrix([[rel.get(b,0) for b in order] for rel in relations])
dm=DomainMatrix.from_Matrix(C).to_field()
rr,piv=dm.rref()
assert piv==tuple(range(28))
T=-rr.to_Matrix()[:28,28:]
assert sum(v!=0 for v in T)==163
assert all(sy.Poly(sy.denom(sy.cancel(v)),R).degree()==0 for v in T)
assert max(sy.Poly(v,R).degree() for v in T if v!=0)==3
assert hashlib.sha256(json.dumps([[str(v) for v in row] for row in T.tolist()],
    separators=(',',':')).encode()).hexdigest()=='333adb48c52ac3c5530e8d0509a7b45b77db62a99e65557cafbd70ce38bba312'

# Reconstruct signed observer in the gauged basis.  Last block is a=0^6.
Tmap={b:T[i,:] for i,b in enumerate(rest)}
Tmap.update({b:sy.eye(7)[i,:] for i,b in enumerate(base)})
assert Tmap[tuple(sorted((2,1,0,0,0,0)))]==sy.Matrix([[-R,6,R/2,-2,0,0,0]])
L=(P.inv()*B).applyfunc(sy.cancel)
e=[(h+1)//2 for h in range(7)]; G=sy.diag(*(R**v for v in e))
A=(R*G.inv()*L*G-sy.diag(*e)).applyfunc(sy.cancel)
A9=sy.zeros(9); A9[:7,:7]=A
for Q in (1,2):
    b=tuple(sorted((Q,1,0,0,0,0)))
    A9[6+Q,:7]=-Tmap[b]*G
    A9[6+Q,6+Q]=Q
radial=R
import sympy as sy
from collections import defaultdict
from math import comb, factorial, prod
import hashlib,json
t,S,B,z,c,n=sy.symbols('t S B z c n')
R=1-t*S
def H(j):
    b=1/z; cj=b if j==0 else c; delta=int(j==0)
    U=B-6*R*b-36*t; V=B-6*R*cj-36*t
    W=B-6*R*(b+cj)+36*delta*R**2*b-36*t**2*S
    C0=1-6*R*delta-6*t*z
    N=sy.Poly(sy.expand((1-z*t)*U*V+R*t*(36-11*z*t)*W
       -10*t**2*R**2*C0-390*z*t**3*R**2-390*delta*t**2*R**3),t)
    return sy.expand(sum((n-i-1)*(n-i-2)*N.nth(i)*S**(5-i)
                         for i in range(6)))
def star(h): return h.xreplace({S:B,B:S,z:1/z,c:1/c})
H0,H1=H(0),H(1)
K=sy.expand(H0*star(H0)-H1*star(H1))
coeff=defaultdict(lambda:0)
for term in K.as_ordered_terms():
    powers=term.as_powers_dict()
    key=tuple(int(powers.get(v,0)) for v in (S,B,z,c))
    coeff[key]+=term/(S**key[0]*B**key[1]*z**key[2]*c**key[3])
coeff={k:sy.Poly(sy.expand(v),n) for k,v in coeff.items()
       if sy.expand(v)!=0}
assert len(coeff)==66 and max(v.degree() for v in coeff.values())==3

R=radial
W=[sy.zeros(1,9) for _ in range(4)]
for (u,v,a,b),pol in coeff.items():
    d=(-a,b,0,0,0,0)
    P=sum(max(i,0) for i in d); Q=sum(max(-i,0) for i in d)
    j=u-P; assert j==v-Q
    read=sy.zeros(1,9); read[:,:7]=Tmap[tuple(sorted(map(abs,d)))]*G
    if P and Q: read[6+max(P,Q)]=-max(P,Q)
    for k in range(4): W[k]+=R**j*pol.nth(k)*read
W=[w.applyfunc(sy.expand) for w in W]
row=W[3]
for k in (2,1,0):
    row=(7*row-R*row.diff(R)-row*A9+W[k]).applyfunc(sy.cancel)
Den=(R-16)**3*(R-4)**3
row[7]*=R; row[8]*=R
num=(row*Den/R**3).applyfunc(sy.cancel)
assert all(sy.denom(v)==1 and sy.Poly(v,R).degree()<=10 for v in num)
nums=[[int(sy.expand(v).coeff(R,k)) for k in range(11)] for v in num]
assert [sy.degree(v,R) for v in num]==[9,10,9,9,8,8,7,9,8]
# Regular singular basis; all eigenvectors normalized by max(abs(v)).
from fractions import Fraction as F
from math import prod
I=sy.eye(7)
assert sy.factor(sy.lcm([sy.denom(v) for v in A]))==(R-36)*(R-16)*(R-4)
A0=A.subs(R,0)
eig=list(map(sy.Rational,[-3,-2,-1,0,sy.Rational(1,2),1,2]))
V=sy.Matrix.hstack(*[(A0-a*I).nullspace()[0] for a in eig])
V=V*sy.diag(*(1/max(abs(x) for x in V[:,j]) for j in range(7)))
assert V.inv()*A0*V==sy.diag(*eig)
q=sy.prod(1-R/sy.Integer(r) for r in [4,16,36])
P=(q*V.inv()*A*V).applyfunc(sy.cancel)
assert all(sy.degree(x,R)<=3 for x in P if x)
Pks=[P.applyfunc(lambda v:sy.expand(v).coeff(R,k)) for k in range(4)]
norm=lambda M:max(sum(abs(x) for x in row) for row in M.tolist())
assert [norm(p) for p in Pks]==[3,sy.Rational(22247,2520),sy.Rational(66313,26880),sy.Rational(13409,129024)]
assert norm(V)==4
ps=[[[F(x*2**k) for x in row] for row in p.tolist()] for k,p in enumerate(Pks)]
qs=[F(sy.expand(q).coeff(R,k)*2**k) for k in range(4)]
es=list(map(F,eig)); N=200
pbound=sum(F(norm(Pks[k]))*2**k for k in range(1,4))
qbound=sum(abs(x) for x in qs[1:])
factor=(pbound+(N+1+2)*qbound)/(N+1-2)
assert factor==F(5025203,5349120)<1
basis=[]
for j in range(3,7):
    a=es[j]; v=[[F(int(i==j)) for i in range(7)]]
    for n in range(1,N+1):
        rhs=[sum(sum(ps[k][i][l]*v[n-k][l] for l in range(7))-qs[k]*(n+a-k)*v[n-k][i] for k in range(1,min(n,3)+1)) for i in range(7)]
        row=[]
        for i,b in enumerate(es):
            den=n+a-b
            if den: row.append(rhs[i]/den)
            else: assert rhs[i]==0; row.append(F(0))
        v.append(row)
    T=max(abs(x) for row in v[-3:] for x in row)
    VV=[list(map(F,row)) for row in V.tolist()]
    z=[[sum(VV[i][l]*row[l] for l in range(7))/2**n for i in range(7)] for n,row in enumerate(v)]
    # h_Q=nu_Q/R, coefficients at resonances chosen zero.
    h=[[],[]]
    for n,row in enumerate(z):
        prev=z[n-1] if n else [F(0)]*7
        f=[row[2],-row[0]+6*row[1]+prev[2]/2-2*prev[3]]
        for k in range(2):
            den=a+n-k
            if den: h[k].append(-f[k]/den)
            else: assert f[k]==0; h[k].append(F(0))
    err=100*T*F(1,2)**N
    basis.append((a,z,h,err,T))

# Strict derivative enclosure at the parent-certified simple root.
from math import prod, comb
Q=F
basis=[(a,z,h,T) for a,z,h,err,T in basis]
anchors=[[168413980883224,168413980883225],[40314418041499,40314418041500],[-10922003425169,-10922003425168],[-1,1],[33682796176644,33682796176645],[2806899681387,2806899681388]]
centers=[Q(l+u,2*10**15) for l,u in anchors]; rad=[Q(u-l,2*10**15) for l,u in anchors]
lo=Q(6800006737,5368709120); hi=Q(3400003369,2684354560); tmax=Q(13,10); assert 0<lo<hi<tmax and tmax*tmax<2
cut=40; degree=2*(cut+2+10); ppolys=[]
for a,z,h,T in basis:
    pol=[Q(0)]*(degree+1); off=int(2*a)
    for n in range(cut+1):
        vals=z[n]+[h[0][n],h[1][n]]
        for i,cc0 in enumerate(vals):
            for k,w in enumerate(nums[i]): pol[off+2*(n+k)]+=cc0*w
    ppolys.append(pol)
for j in range(2):
    pol=[Q(0)]*(degree+1)
    for k,w in enumerate(nums[7+j]): pol[2*(k+j)]=Q(w)
    ppolys.append(pol)
center=[sum(c*p[i] for c,p in zip(centers,ppolys)) for i in range(degree+1)]
class IV:
    def __init__(self,a,b=None): self.a=Q(a); self.b=Q(a if b is None else b); assert self.a<=self.b
    @staticmethod
    def cast(x): return x if isinstance(x,IV) else IV(x)
    def __add__(self,o): o=self.cast(o); return IV(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return IV(-self.b,-self.a)
    def __sub__(self,o): return self+-self.cast(o)
    def __rsub__(self,o): return self.cast(o)+-self
    def __mul__(self,o):
        o=self.cast(o); v=[self.a*o.a,self.a*o.b,self.b*o.a,self.b*o.b]; return IV(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=self.cast(o); assert o.a*o.b>0; return self*IV(1/o.b,1/o.a)
    def __rtruediv__(self,o): return self.cast(o)/self
    def __pow__(self,n):
        if n<0: return 1/(self**(-n))
        out=IV(1)
        for _ in range(n): out*=self
        return out
    def rounded(self,k=9):
        D=10**k; a=self.a*D; b=self.b*D
        return [a.numerator//a.denominator,-((-b.numerator)//b.denominator)]
def falling(n,j): return prod(range(n-j+1,n+1)) if n>=j else 0
def deriv(p,j): return [p[k]*falling(k,j) for k in range(j,len(p))]
def abs_poly_bound(p,j): return sum(abs(c)*tmax**k for k,c in enumerate(deriv(p,j)))
def evalp(p,x):
    v=IV(0)
    for c in reversed(p): v=v*x+c
    return v
# Successive ratios for tail derivative of t^(off+2n) are <=
# (tmax^2/2)*((off+2J+2-j+1)/(off+2J-j+1))^j, j<=4.
rowpolys=[]
for rr in nums:
    p=[0]*(2*len(rr)-1)
    for k,v in enumerate(rr): p[2*k]=v
    rowpolys.append(p)
rowbounds=[sum(abs_poly_bound(p,j) for p in rowpolys) for j in range(5)]
terr=[]
for a,z,h,T in basis:
    off=int(2*a); J=N+1; out=[]
    for j in range(5):
        e=sum(max(abs(v) for v in z[n]+[h[0][n],h[1][n]])*falling(off+2*n,j)*tmax**(off+2*n-j) for n in range(cut+1,N+1))
        p=off+2*J; ratio=tmax*tmax/2*Q(p+2-j+1,p-j+1)**j
        assert ratio<1
        e+=64*T*Q(1,2)**J*falling(p,j)*tmax**(p-j)/(1-ratio)
        out.append(e)
    terr.append(out)
terr.extend([[Q(0)]*5]*2)
t=IV(lo,hi); Fs=[]
for j in range(5):
    pe=sum(r*abs_poly_bound(p,j) for r,p in zip(rad,ppolys))
    se=sum((abs(c)+r)*sum(comb(j,k)*rowbounds[k]*tr[j-k] for k in range(j+1)) for c,r,tr in zip(centers,rad,terr))
    v=evalp(deriv(center,j),t)+IV(-pe-se,pe+se); Fs.append(v)
    print('F derivative',j,'bounds x 1e3:',v.rounded(3),flush=True)
assert Fs[0].a<=0<=Fs[0].b and Fs[1].b<0
ts=sy.symbols('t'); logder=6/ts-6*ts/(ts**2-16)-6*ts/(ts**2-4)
B=[sy.Integer(1)]; ratios={}
def evalrat(expr):
    num,den=sy.fraction(sy.cancel(expr)); p=list(reversed(sy.Poly(num,ts).all_coeffs())); q=list(reversed(sy.Poly(den,ts).all_coeffs())); return evalp(list(map(Q,p)),t)/evalp(list(map(Q,q)),t)
for r in range(1,5):
    B=[sy.cancel(18/ts*((sy.diff(B[j],ts)+logder*B[j] if j<len(B) else 0)+(B[j-1] if j else 0))) for j in range(len(B)+1)]
    value=sum(evalrat(B[j])*Fs[j] for j in range(1,r+1))
    if r==1: first=value; assert first.b<0
    else: ratios[r]=value/first
b=t*t/36; v=b*(1-b); L=1-2*b; A=-v*ratios[2]/2; c=(1-A)/b-2
d=-(c+2)*A+ratios[2]/2*(A*L-(c+3)*v+A*A)+ratios[3]/6*v*(2*L+3*A)+ratios[4]/8*v*v
out={'root_t':[str(lo),str(hi)],'rho_scaled_1e12':(1/b-1).rounded(12),'g_derivative_ratios_scaled_1e6':{str(i):a.rounded(6) for i,a in ratios.items()},'c_scaled_1e6':c.rounded(6),'d_scaled_1e6':d.rounded(6)}
assert out['c_scaled_1e6']==[99141009,99141012]
assert out['d_scaled_1e6']==[9690788,9690937]
print(json.dumps(out,indent=2),flush=True)

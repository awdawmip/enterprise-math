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
# Exact moments via grouped Euler occupancy recurrence (PREFIX-1093).
def moments(a,N):
    g=sorted(Counter(a).items()); av=[v for v,_ in g]; r=[n for _,n in g]; A=sum(a)
    states=sorted(product(*(range(n+1) for n in r)),key=sum,reverse=True)
    ix={h:i for i,h in enumerate(states)}
    links=[]
    for h in states:
        up=[(r[k]-h[k],ix[h[:k]+(h[k]+1,)+h[k+1:]]) for k in range(len(r)) if h[k]<r[k]]
        down=[(h[k],ix[h[:k]+(h[k]-1,)+h[k+1:]]) for k in range(len(r)) if h[k]]
        links.append((sum(v*k for v,k in zip(av,h)),up,down))
    prev=[0]*len(states); prev[-1]=factorial(A)//prod(factorial(i) for i in a)
    out=[prev[-1]]
    for j in range(1,N+1):
        cur=[0]*len(states); jj=j*(j+A)
        for i,(ah,up,down) in enumerate(links):
            num=sum(c*cur[p] for c,p in up)+jj*sum(c*prev[p] for c,p in down)
            cur[i],rem=divmod(num,j+ah); assert rem==0
        out.append(cur[-1]); prev=cur
    return out
ks=[2000,2400,2800,3200]
m0=moments((0,)*6,max(ks))
m1=moments((1,1,0,0,0,0),ks[0])
m2=moments((2,1,0,0,0,0),ks[0])
def beta_moment(m,k,Q=0):
    p=36**k; den=p; acc=0; c=1
    for j in range(k+1):
        v=m[j]
        if Q:
            v,rem=divmod(Q*v,j+Q+1); assert rem==0
        acc+=(-1 if j%2 else 1)*c*p*v
        if j<k: p//=36; c=c*(k-j)//(j+1)
    return F(acc,den*(Q or 1))
# Incomplete beta moments J_alpha(k) on [0,1], all rational.
def integ(k,half,degree):
    a=F(half,2); b=F(35,36); v=1/(a+1); p=F(1)
    for j in range(1,k+1):
        p*=b; v=(j*v+p)/(a+j+1)
    edge=p*b; vals=[v]
    for n in range(degree):
        t=a+n; vals.append(36*((t+1)*vals[-1]-edge)/(t+k+2))
    assert all(v>0 for v in vals)
    return vals
M=[]; obs=[]; errors=[]
for k in ks:
    ints={i:integ(k,i,N+5) for i in (0,1)}
    row=[]
    for a,z,h,err,T in basis:
        off=int(a); half=int(2*(a-off))
        row.append(sum(c[0]*ints[half][off+n] for n,c in enumerate(z)))
    M.append(row); obs.append(beta_moment(m0,k)); errors.append(F(35,36)**k)
MM=sy.Matrix(M); inv=MM.inv(); cc=inv*sy.Matrix(obs)
row_norms=[sum(abs(F(v)) for v in row) for row in inv.tolist()]
eb=sum(b[3] for b in basis); aerr=max(row_norms)*eb
rhs=[sum(abs(F(inv[i,j]))*errors[j] for j in range(4)) for i in range(4)]
assert aerr<1
cmax=max(abs(F(x)) for x in cc)
delta=(max(rhs)+aerr*cmax)/(1-aerr)
assert delta<F(3,10**18)
k=ks[0]; ints={i:integ(k,i,N+5) for i in (0,1)}
hcent=[]; herr=[]
for Q,mm in [(1,m1),(2,m2)]:
    rr=[]
    for a,z,h,err,T in basis:
        off=int(a); half=int(2*(a-off))
        rr.append(sum(c*ints[half][off+n+1] for n,c in enumerate(h[Q-1])))
    tv=F(6**(Q+1),Q+1); ob=beta_moment(mm,k,Q)
    baseval=sum(F(x)*y for x,y in zip(cc,rr)); div=ints[0][Q]
    c=(ob-baseval)/div
    er=(tv*F(35,36)**k+delta*sum(abs(x) for x in rr)+(cmax+delta)*eb)/div
    hcent.append(c); herr.append(er)
Pdec=10**15; out=[]
for center,er in list(zip(map(F,cc),[delta]*4))+list(zip(hcent,herr)):
    lo=(center-er)*Pdec; hi=(center+er)*Pdec
    out.append([lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator)])
assert out==[[168413980883224,168413980883225],[40314418041499,40314418041500],[-10922003425169,-10922003425168],[-1,1],[33682796176644,33682796176645],[2806899681387,2806899681388]]
print("parameter intervals / 10^15",out)
# Degree-40 series and scalar polynomial numerator in t=sqrt(R).
cut=40; degree=2*(cut+2+10); ppolys=[]
for a,z,h,err,T in basis:
    pol=[F(0)]*(degree+1); off=int(2*a)
    for n in range(cut+1):
        vals=z[n]+[h[0][n],h[1][n]]
        for i,cc0 in enumerate(vals):
            for k,w in enumerate(nums[i]): pol[off+2*(n+k)]+=cc0*w
    ppolys.append(pol)
for j in range(2):
    pol=[F(0)]*(degree+1)
    for k,w in enumerate(nums[7+j]): pol[2*(k+j)]=F(w)
    ppolys.append(pol)
centers=[F(l+u,2*Pdec) for l,u in out]
rad=[F(u-l,2*Pdec) for l,u in out]
center=[sum(c*p[i] for c,p in zip(centers,ppolys)) for i in range(degree+1)]
def bounds(tmax):
    rmax=tmax*tmax; terrs=[]; dterrs=[]
    for a,z,h,err,T in basis:
        ee=F(0); de=F(0); off=int(2*a)
        for n in range(cut+1,N+1):
            mag=max(abs(x) for x in z[n]+[h[0][n],h[1][n]])
            p=off+2*n; ee+=mag*tmax**p; de+=mag*p*tmax**(p-1)
        ratio=rmax/2; j=N+1
        ee+=64*T*tmax**off*ratio**j/(1-ratio)
        de+=64*T*tmax**(off-1)*ratio**j*((off+2*j)/(1-ratio)+2*ratio/(1-ratio)**2)
        terrs.append(ee); dterrs.append(de)
    terrs.extend([F(0)]*2); dterrs.extend([F(0)]*2)
    rownorm=sum(sum(abs(w)*rmax**k for k,w in enumerate(row)) for row in nums)
    drownorm=sum(sum(abs(w)*2*k*tmax**(2*k-1) for k,w in enumerate(row) if k) for row in nums)
    ce=sum(rr*sum(abs(w)*tmax**k for k,w in enumerate(p)) for rr,p in zip(rad,ppolys))
    dce=sum(rr*sum(abs(w)*k*tmax**(k-1) for k,w in enumerate(p) if k) for rr,p in zip(rad,ppolys))
    se=rownorm*sum((abs(c)+rr)*ee for c,rr,ee in zip(centers,rad,terrs))
    dse=sum((abs(c)+rr)*(rownorm*de+drownorm*ee) for c,rr,ee,de in zip(centers,rad,terrs,dterrs))
    return ce+se,dce+dse
def bern_on(p,l,u):
    d=len(p)-1
    power=[sum(p[j]*comb(j,i)*l**(j-i) for j in range(i,d+1))*(u-l)**i for i in range(d+1)]
    return [sum(power[k]*F(comb(i,k),comb(d,k)) for k in range(i+1)) for i in range(d+1)]
def evalp(p,t):
    out=F(0)
    for c in reversed(p): out=out*t+c
    return out
lo=F(5,4); hi=F(13,10)
ce,_=bounds(lo)
assert min(bern_on(center,F(0),lo))-ce>10**8
ce,de=bounds(hi)
assert max(bern_on([k*center[k] for k in range(1,len(center))],lo,hi))+de<-8*10**9
assert evalp(center,lo)>ce and evalp(center,hi)<-ce
for i in range(30):
    mid=(lo+hi)/2; val=evalp(center,mid)
    if val>ce: lo=mid
    elif val<-ce: hi=mid
    else: break
assert (lo,hi)==(F(6800006737,5368709120),F(3400003369,2684354560))
print("CERTIFIED first zero t:",lo,hi)
print("x:",float(lo*lo/36),float(hi*hi/36),"rho:",float(36/(hi*hi)-1),float(36/(lo*lo)-1))

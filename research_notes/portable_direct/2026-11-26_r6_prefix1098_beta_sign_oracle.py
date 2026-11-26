# PREFIX-1098: certified finite-cost sign oracle for the frozen Stage46 BRC observer.
# Run with Python 3 + SymPy. Parent file in same directory, exact SHA256 below.
# All sign decisions use Fraction, not floating point. Float only display.
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import hashlib, time

def reconstruct():
    parent=Path(__file__).with_name("2026-11-26_r6_prefix1096_edge_shift.py")
    raw=parent.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=="871317523a6634233eb94aa71abaa02b2213d1bb6a6b003d86c39cbbf280fc11"
    src=raw.decode("utf-8")
    # Execute only the frozen exact symbolic reconstruction and F40 bases.
    ns={}
    exec(compile(src.split("class IV:",1)[0],str(parent),"exec"),ns)
    basis=ns["basis"]; nums=ns["nums"]; ps=ns["ppolys"]
    T=Q(13,10); q=T*T/2; N=ns["N"]
    assert N==200 and ns["cut"]==40 and len(ps)==6
    rowabs=sum(abs(v)*T**(2*k) for rr in nums for k,v in enumerate(rr))
    terr=[]
    for a,z,h,Tj in basis:
        off=int(2*a)
        e=sum(max(abs(x) for x in z[n]+[h[0][n],h[1][n]])*T**(off+2*n) for n in range(41,N+1))
        e+=64*Tj*T**off*q**(N+1)/(1-q)
        terr.append(e*rowabs)
    terr.extend([Q(0)]*2)
    serr=sum((abs(c)+r)*e for c,r,e in zip(ns["centers"],ns["rad"],terr))
    assert serr<Q(1,100000)
    scale=10**20
    rounded=[[Q((v*scale).__floor__(),scale) for v in p] for p in ps]
    assert all(sum(abs(a-b)*T**i for i,(a,b) in enumerate(zip(p,r)))<Q(1,1000000) for p,r in zip(ps,rounded))
    print("series error",float(serr),flush=True)
    return rounded

F=reconstruct()
anchors=[[168413980883224,168413980883225],[40314418041499,40314418041500],[-10922003425169,-10922003425168],[-1,1],[33682796176644,33682796176645],[2806899681387,2806899681388]]
c=[Q(l+u,2*10**15) for l,u in anchors]; r=[Q(u-l,2*10**15) for l,u in anchors]; mag=[abs(a)+b for a,b in zip(c,r)]
T=Q(13,10); w=T*T/36; s=Q(1299,1000)**2/36; K=Q(36,4*36**8*16**3*4**3)
def mul(a,b):
    p=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:p[i+j]+=x*y
    return p
def geom(d,N):
    a=[Q(0)]*(2*N+1)
    for n in range(N+1):a[2*n]=Q(comb(n+2,2),d**n)
    u=T*T/d; j=N+1; ratio=u*Q(j+3,j+1); assert ratio<1
    return a,comb(j+2,2)*u**j/(1-ratio),(1-u)**-3
A,ea,ma=geom(4,60); B,eb,mb=geom(16,60); AB=mul(A,B)
P=[[Q(0)]*6+mul(f,AB) for f in F]; degree=len(P[0])-1; assert degree==350
Fabs=sum(a*sum(abs(x)*T**j for j,x in enumerate(f)) for a,f in zip(mag,F)); assert Fabs<10**14
local=T**6*((Q(1,100000)+sum(mag)*Q(1,1000000))*ma*mb+Fabs*(ea*mb+ma*eb)); assert local<Q(1,1000)
C=[Q(114025897,629856),Q(118208,2187),Q(1637,324),Q(4,27)]; R=[1,7,42,420]
J=sum(C[j]*sum(comb(j,i)*R[i]/(w-s)**i for i in range(j+1)) for j in range(4))
Ps=sum(a*sum(abs(x)*Q(1299,1000)**j for j,x in enumerate(p)) for a,p in zip(mag,P))
H=2**256
def ceilq(a):return -((-a.numerator)//a.denominator)
def powup(a,n):
    assert 0<=a<=1 and n>=0
    x=ceilq(a*H); y=H
    while n:
        if n&1:y=(y*x+H-1)//H
        n//=2
        if n:x=(x*x+H-1)//H
    return Q(y,H)
def outside(m,k):
    mode=Q(m,m+k); a=mode-Q(1,m); z=mode+Q(1,m); assert 0<a<z<s
    assert Q(m+6,m+6+k-3)<=s and Q(2*m+degree,2*m+degree+2*k)<=s
    def ratio(u):
        q,n=divmod(k,m); v=(1-s)/(1-u); p=(s/u)*v**q
        assert p<=1 and v<=1
        return powup(p,m)*powup(v,n)
    rho=max(ratio(a),ratio(z))/(z-a)
    return rho*(J*(1+m+k)**3/(K*(1-s)**3)+Ps)
def moments(a,T,n):
    v=[Q(1)]
    for j in range(n):v.append(v[-1]*(a+j)/(T+j))
    return v
def oracle(m,k):
    a=Q(m+1); total=Q(m+k+2); n=degree//2
    ev=moments(a,total,n); od=moments(a+Q(1,2),total+Q(1,2),n)
    root=Q(19,90); x0=root**2
    u=[sum(comb(j,i)*(-1)**(j-i)*ev[i]/x0**i for i in range(j+1)) for j in range(17)]; assert u[-1]>=0
    b=Q(1); v=Q(1)
    for j in range(1,16):b*=Q(3-2*j,2*j); v+=b*u[j]
    sq=root*v; se=root*u[-1]
    E=[36**j*ev[j] for j in range(n+1)]; O=[6*36**j*od[j] for j in range(n)]
    p0=[]; p1=[]
    for p in P:
        p0.append(sum(p[2*j]*E[j] for j in range(n+1))); p1.append(sum(p[2*j+1]*O[j] for j in range(n)))
    vals=[a+b*sq for a,b in zip(p0,p1)]
    center=sum(a*b for a,b in zip(c,vals)); sqerr=abs(sum(a*b for a,b in zip(c,p1)))*se
    ar=sum(a*(abs(b)+abs(o)*se) for a,b,o in zip(r,vals,p1)); ext=outside(m,k); err=sqerr+ar+local+ext
    return center,err,ar,ext,sqerr

if __name__=="__main__":
    print("degree",degree,"local error",float(local),"Fabs",float(Fabs))
    cases=[(100000,2144102,2144103),(1000000,21440135,21440136),
           (10000000,214400466,214400467),(100000000,2144003771,2144003772),
           (1000000000,21440036819,21440036820),(10000000000,214400367302,214400367304),
           (100000000000,2144003672135,2144003672144),(1000000000000,21440036720467,21440036720542)]
    for m,a,b in cases:
        assert m>=100000 and 5*a>=107*m
        t=time.monotonic(); ca,ea,*_=oracle(m,a); cb,eb,*_=oracle(m,b)
        assert ca<-ea and cb>eb
        print(m,a,b-1,b-a,float(ca),float(ea),float(cb),float(eb),round(time.monotonic()-t,3),flush=True)

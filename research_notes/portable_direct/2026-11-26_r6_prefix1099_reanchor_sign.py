# PREFIX-1099 exact reproduction; Python 3 + SymPy. All decisions are rational.
# Frozen parent file must be present beside this one.
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import hashlib, sympy as sy

parent=Path(__file__).with_name("2026-11-26_r6_prefix1095_frobenius_certificate.py")
raw=parent.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="1808c556464cc8d21b462697dac0bf500020367640b5557bbe01343c124665e9"
src=raw.decode("utf-8")
ns={}
# Reuse the parent's exact symbolic row, four bases, and grouped Euler moments.
exec(compile(src.split("ks=[2000,2400,2800,3200]",1)[0],str(parent),"exec"),ns)
exec(compile(src[src.index("def beta_moment("):src.index("M=[]; obs=[]; errors=[]")],str(parent),"exec"),ns)
basis=ns["basis"]; nums=ns["nums"]; N=ns["N"]; moments=ns["moments"]
beta_moment=ns["beta_moment"]; integ=ns["integ"]
assert N==200 and len(basis)==4
GRID=10**100
def down(x): return Q(x.numerator*GRID//x.denominator,GRID)
def anchor():
    ks=[2800,3200,3600,4000]
    m0=moments((0,)*6,max(ks))
    m1=moments((1,1,0,0,0,0),ks[0]); m2=moments((2,1,0,0,0,0),ks[0])
    M=[]; obs=[]; errors=[]
    eb=sum(b[3] for b in basis)+4*Q(N+1,GRID)
    for k in ks:
        ints={i:integ(k,i,N+5) for i in (0,1)}; row=[]
        for a,z,h,err,T in basis:
            off=int(a); half=int(2*(a-off))
            row.append(sum(down(c[0]*ints[half][off+n]) for n,c in enumerate(z)))
        M.append(row); obs.append(down(beta_moment(m0,k)))
        errors.append(Q(35,36)**k+Q(1,GRID))
    inv=sy.Matrix(M).inv(); cc=list(map(Q,inv*sy.Matrix(obs)))
    row_norms=[sum(abs(Q(v)) for v in row) for row in inv.tolist()]
    aerr=max(row_norms)*eb
    rhs=[sum(abs(Q(inv[i,j]))*errors[j] for j in range(4)) for i in range(4)]
    assert aerr<1
    cmax=max(abs(x) for x in cc); delta=(max(rhs)+aerr*cmax)/(1-aerr)
    assert delta<Q(3,10**27)
    k=ks[0]; ints={i:integ(k,i,N+5) for i in (0,1)}
    hcent=[]; herr=[]
    for j,mm in [(1,m1),(2,m2)]:
        rr=[]
        for a,z,h,err,T in basis:
            off=int(a); half=int(2*(a-off))
            rr.append(sum(down(c*ints[half][off+n+1]) for n,c in enumerate(h[j-1])))
        tv=Q(6**(j+1),j+1); ob=beta_moment(mm,k,j); div=ints[0][j]
        center=(ob-sum(x*y for x,y in zip(cc,rr)))/div
        er=(tv*Q(35,36)**k+delta*sum(abs(x) for x in rr)+(cmax+delta)*eb)/div
        hcent.append(center); herr.append(er)
    out=[]
    for c,r in zip(cc+hcent,[delta]*4+herr):
        lo=(c-r)*10**25; hi=(c+r)*10**25
        out.append([lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator)])
    assert out==[[1684139808832244674612244,1684139808832244674612245],[403144180414993614805275,403144180414993614805276],[-109220034251684978380170,-109220034251684978380169],[-1,1],[336827961766448934922448,336827961766448934922449],[28068996813870744576870,28068996813870744576871]]
    old=[[168413980883224,168413980883225],[40314418041499,40314418041500],[-10922003425169,-10922003425168],[-1,1],[33682796176644,33682796176645],[2806899681387,2806899681388]]
    assert all(l*10**10<=a<=b<=u*10**10 for (a,b),(l,u) in zip(out,old))
    print("anchors / 10^25",out,"delta",float(delta),"mixed",list(map(float,herr)),flush=True)
    return out

def mul(a,b):
    p=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:p[i+j]+=x*y
    return p

def make_oracle(anchors,cut,geom_n,digits):
    T=Q(13,10); w=T*T/36; s=Q(1299,1000)**2/36; K=Q(36,4*36**8*16**3*4**3)
    c=[Q(l+u,2*10**25) for l,u in anchors]; r=[Q(u-l,2*10**25) for l,u in anchors]; mag=[abs(a)+b for a,b in zip(c,r)]
    deg=2*(cut+2+10); ppolys=[]; terr=[]; q=T*T/2
    rowabs=sum(abs(v)*T**(2*k) for rr in nums for k,v in enumerate(rr))
    for a,z,h,er,Tj in basis:
        pol=[Q(0)]*(deg+1); off=int(2*a)
        for n in range(cut+1):
            for i,cc0 in enumerate(z[n]+[h[0][n],h[1][n]]):
                for k,v in enumerate(nums[i]):pol[off+2*(n+k)]+=cc0*v
        ppolys.append(pol)
        ee=sum(max(abs(x) for x in z[n]+[h[0][n],h[1][n]])*T**(off+2*n) for n in range(cut+1,N+1))
        ee+=64*Tj*T**off*q**(N+1)/(1-q); terr.append(ee*rowabs)
    for j in range(2):
        pol=[Q(0)]*(deg+1)
        for k,v in enumerate(nums[7+j]):pol[2*(k+j)]=Q(v)
        ppolys.append(pol); terr.append(Q(0))
    scale=10**digits
    Fs=[[Q((v*scale).__floor__(),scale) for v in p] for p in ppolys]
    serr=sum(a*e for a,e in zip(mag,terr))
    rounding=sum(a*sum(abs(x-y)*T**i for i,(x,y) in enumerate(zip(p,rr))) for a,p,rr in zip(mag,ppolys,Fs))
    def geom(d):
        a=[Q(0)]*(2*geom_n+1)
        for n in range(geom_n+1):a[2*n]=Q(comb(n+2,2),d**n)
        u=T*T/d; j=geom_n+1; ratio=u*Q(j+3,j+1); assert ratio<1
        return a,comb(j+2,2)*u**j/(1-ratio),(1-u)**-3
    AA,ea,ma=geom(4); BB,eb,mb=geom(16)
    AB=mul(AA,BB); P=[[Q(0)]*6+mul(f,AB) for f in Fs]; degree=len(P[0])-1
    Fabs=sum(a*sum(abs(x)*T**j for j,x in enumerate(f)) for a,f in zip(mag,Fs))
    local=T**6*((serr+rounding)*ma*mb+Fabs*(ea*mb+ma*eb))
    print("degree",degree,"local",float(local),flush=True)
    C=[Q(114025897,629856),Q(118208,2187),Q(1637,324),Q(4,27)]; Rr=[1,7,42,420]
    J=sum(C[j]*sum(comb(j,i)*Rr[i]/(w-s)**i for i in range(j+1)) for j in range(4))
    Ps=sum(a*sum(abs(x)*Q(1299,1000)**j for j,x in enumerate(p)) for a,p in zip(mag,P))
    H=2**512
    def powup(a,n):
        assert 0<=a<=1 and n>=0
        x=-((-a.numerator*H)//a.denominator); y=H
        while n:
            if n&1:y=(y*x+H-1)//H
            n//=2
            if n:x=(x*x+H-1)//H
        return Q(y,H)
    def outside(m,k):
        mode=Q(m,m+k); a=mode-Q(1,m); z=mode+Q(1,m)
        assert 0<a<z<s and Q(m+6,m+6+k-3)<=s and Q(2*m+degree,2*m+degree+2*k)<=s
        def ratio(u):
            q,n=divmod(k,m); v=(1-s)/(1-u); p=(s/u)*v**q
            assert p<=1 and v<=1
            return powup(p,m)*powup(v,n)
        rho=max(ratio(a),ratio(z))/(z-a)
        return rho*(J*(1+m+k)**3/(K*(1-s)**3)+Ps)
    def mm(a,T,n):
        v=[Q(1)]
        for j in range(n):v.append(v[-1]*(a+j)/(T+j))
        return v
    def oracle(m,k):
        a=Q(m+1); total=Q(m+k+2); n=degree//2
        ev=mm(a,total,n); od=mm(a+Q(1,2),total+Q(1,2),n); root=Q(19,90); x0=root**2
        u=[sum(comb(j,i)*(-1)**(j-i)*ev[i]/x0**i for i in range(j+1)) for j in range(17)]
        assert u[-1]>=0
        b=Q(1); v=Q(1)
        for j in range(1,16):b*=Q(3-2*j,2*j); v+=b*u[j]
        sq=root*v; se=root*u[-1]; E=[36**j*ev[j] for j in range(n+1)]; O=[6*36**j*od[j] for j in range(n)]
        p0=[]; p1=[]
        for p in P:
            p0.append(sum(p[2*j]*E[j] for j in range(n+1)))
            p1.append(sum(p[2*j+1]*O[j] for j in range(n)))
        vals=[a+b*sq for a,b in zip(p0,p1)]
        center=sum(a*b for a,b in zip(c,vals))
        sqerr=abs(sum(a*b for a,b in zip(c,p1)))*se
        ar=sum(a*(abs(b)+abs(o)*se) for a,b,o in zip(r,vals,p1))
        ext=outside(m,k); err=sqerr+ar+local+ext
        return center,err,ar,ext,sqerr
    return oracle,local,degree

CASES450=[
(10**10,214400367303,214400367304),
(10**11,2144003672139,2144003672140),
(10**12,21440036720503,21440036720504),
(10**13,214400367204145,214400367204146),
(10**14,2144003672040563,2144003672040564),
(10**15,21440036720404743,21440036720404744),
(10**16,214400367204046538,214400367204046540),
(10**17,2144003672040464497,2144003672040464498),
(10**18,21440036720404644078,21440036720404644087)]
CASES550=[
(10**16,214400367204046538,214400367204046539),
(10**18,21440036720404644082,21440036720404644083),
(10**19,214400367204046439931,214400367204046439932),
(10**20,2144003672040464398426,2144003672040464398428)]
if __name__=="__main__":
    anchors=anchor()
    for cut,gn,dig,cases,deg,limit in [(50,80,30,CASES450,450,Q(25,10**9)),(60,100,40,CASES550,550,Q(3,10**12))]:
        oracle,local,degree=make_oracle(anchors,cut,gn,dig)
        assert degree==deg and local<limit
        for m,l,u in cases:
            assert m>=100000 and 5*l>=107*m
            vl,el,*_=oracle(m,l); vu,eu,*_=oracle(m,u)
            assert vl<-el and vu>eu
            print(m,l,u-1,float(vl),float(el),float(vu),float(eu),flush=True)

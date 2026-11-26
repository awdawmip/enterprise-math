# PREFIX-1100: centered Beta denominator + correlated anchor certificate.
# Reproduction companion assembled from the frozen 1099 parent and equivalent
# locally executed implementation. Run alongside pinned 1099 and 1095 files.
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import runpy, sympy as sy
ns=runpy.run_path(str(Path(__file__).with_name("2026-11-26_r6_prefix1099_reanchor_sign.py")))
basis,nums,N,moments,beta_moment,integ,mul=[ns[k] for k in ("basis","nums","N","moments","beta_moment","integ","mul")]
old=[[1684139808832244674612244,1684139808832244674612245],[403144180414993614805275,403144180414993614805276],[-109220034251684978380170,-109220034251684978380169],[-1,1],[336827961766448934922448,336827961766448934922449],[28068996813870744576870,28068996813870744576871]]
def anchor_dual(ks):
    H=10**100; down=lambda x:Q(x.numerator*H//x.denominator,H)
    m0=moments((0,)*6,max(ks)); m1=moments((1,1,0,0,0,0),ks[0]); m2=moments((2,1,0,0,0,0),ks[0])
    M=[]; obs=[]; errors=[]
    eb=sum(b[3] for b in basis)+Q(4*(N+1)+1,H)
    for k in ks:
        ints={i:integ(k,i,N+5) for i in (0,1)}; row=[]
        for a,z,h,err,T in basis:
            off=int(a); half=int(2*(a-off))
            row.append(sum(down(c[0]*ints[half][off+n]) for n,c in enumerate(z)))
        M.append(row+[Q(0)]*2); obs.append(down(beta_moment(m0,k)))
        errors.append(Q(35,36)**k+Q(1,H))
    k=ks[0]; ints={i:integ(k,i,N+5) for i in (0,1)}
    for j,mm in [(1,m1),(2,m2)]:
        rr=[]
        for a,z,h,err,T in basis:
            off=int(a); half=int(2*(a-off))
            rr.append(sum(down(c*ints[half][off+n+1]) for n,c in enumerate(h[j-1])))
        row=rr+[Q(0)]*2; row[3+j]=down(ints[0][j]); M.append(row)
        obs.append(down(beta_moment(mm,k,j)))
        errors.append(Q(6**(j+1),j+1)*Q(35,36)**k+Q(1,H))
    assert all(-10**25<l<=u<10**25 for l,u in old)
    inv=sy.Matrix(M).inv(); cc=list(map(Q,inv*sy.Matrix(obs)))
    inv=[list(map(Q,row)) for row in inv.tolist()]
    eps=[x+eb for x in errors]
    radii=[sum(abs(v)*e for v,e in zip(row,eps)) for row in inv]
    scale=10**50
    rounded=[Q((c*scale).__floor__(),scale) for c in cc]
    dr=[abs(c-d) for c,d in zip(cc,rounded)]
    r=[a+b for a,b in zip(radii,dr)]
    assert all(Q(l,10**25)<=c-e<=c+e<=Q(u,10**25) for (l,u),c,e in zip(old,rounded,r))
    print("anchor",ks,"radii",list(map(float,r)),flush=True)
    def dual(v):
        return sum(abs(sum(v[i]*inv[i][j] for i in range(6)))*eps[j] for j in range(6))+sum(abs(a)*b for a,b in zip(v,dr))
    return rounded,r,dual

def make_oracle(anchor,cut,geom_n,digits,R0):
    T=Q(13,10); w=T*T/36; s=Q(1299,1000)**2/36; K=Q(36,4*36**8*16**3*4**3)
    c,r,dual=anchor; mag=[abs(a)+b for a,b in zip(c,r)]
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
    J=geom_n; assert J%2==1
    Qmax=max(R0,T*T-R0)
    def geom(d):
        den=d-R0; pref=(1-R0/d)**-3; u=Qmax/den; assert u<1
        p=[Q(0)]*(2*J+1)
        for n in range(J+1):
            for j in range(n+1):
                p[2*j]+=pref*comb(n+2,2)*comb(n,j)*(-R0)**(n-j)/den**n
        ratio=u*Q(J+4,J+2); assert ratio<1
        C=pref*comb(J+3,2)/den**(J+1)/(1-ratio)
        return p,C,pref*(1-u)**-3
    AA,ea,ma=geom(4); BB,eb,mb=geom(16)
    AB=mul(AA,BB); P=[[Q(0)]*6+mul(f,AB) for f in Fs]; degree=len(P[0])-1
    Fabs=sum(a*sum(abs(x)*T**j for j,x in enumerate(f)) for a,f in zip(mag,Fs))
    local=T**6*(serr+rounding)*ma*mb
    Cgeom=T**6*Fabs*(ea*mb+ma*eb)
    print("degree",degree,"local",float(local),flush=True)
    C=[Q(114025897,629856),Q(118208,2187),Q(1637,324),Q(4,27)]; Rr=[1,7,42,420]
    J=sum(C[j]*sum(comb(j,i)*Rr[i]/(w-s)**i for i in range(j+1)) for j in range(4))
    Ps=sum(a*sum(abs(x)*Q(1299,1000)**j for j,x in enumerate(p)) for a,p in zip(mag,P))
    H=2**768
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
        sqerr=(abs(sum(a*b for a,b in zip(c,p1)))+dual(p1))*se
        ar=dual(vals)
        indep=sum(a*(abs(b)+abs(o)*se) for a,b,o in zip(r,vals,p1))
        cm=sum(comb(geom_n+1,i)*(-R0)**(geom_n+1-i)*36**i*ev[i] for i in range(geom_n+2))
        assert cm>=0
        ge=Cgeom*cm; ext=outside(m,k)
        err=sqerr+ar+local+ge+ext
        return center,err,ar,indep,local,ge,ext,sqerr
    return oracle,local,degree

def check(oracle,m,l,u):
    assert m>=100000 and 5*l>=107*m
    a=oracle(m,l); b=oracle(m,u)
    assert a[0]<-a[1] and b[0]>b[1]
    print("BRACKET",m,l,u-1,list(map(float,a)),list(map(float,b)),flush=True)
    if m>=10**21: assert max(a[6],b[6])<Q(1,10**100)

if __name__=="__main__":
    anchor=anchor_dual([2800,3200,3600,4000])
    oracle,loc,degree=make_oracle(anchor,80,15,55,Q(8,5))
    assert degree==250
    check(oracle,10**20,2144003672040464398426,2144003672040464398427)
    oracle,loc,degree=make_oracle(anchor,80,7,55,Q(160427545,10**8))
    assert degree==218
    for m,l,u in [(10**5,2144102,2144103),(10**9,21440036819,21440036820),(10**20,2144003672040464398426,2144003672040464398427),(10**21,21440036720404643983373,21440036720404643983375),(10**22,214400367204046439832846,214400367204046439832848)]:
        check(oracle,m,l,u)
    anchor=anchor_dual([3200,3600,4000,4400])
    oracle,loc,degree=make_oracle(anchor,80,7,55,Q(160427545,10**8))
    assert degree==218
    check(oracle,10**21,21440036720404643983373,21440036720404643983374)
    check(oracle,10**22,214400367204046439832847,214400367204046439832848)

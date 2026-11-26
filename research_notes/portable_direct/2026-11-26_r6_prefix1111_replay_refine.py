# PREFIX-1111 reproduction wrapper, assembled from the pinned source and the
# equivalent locally executed Python reconstruction. This wrapper itself was
# not independently run before publication. Place beside the four pinned files.
# Python 3 + SymPy. All mathematical decisions are exact integer/Fraction.
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
HERE=Path(__file__).resolve().parent
PINS={
"2026-11-26_r6_prefix1095_frobenius_certificate.py":"f4e12c31e1f8f4dec0703836580a28a88bbc21de",
"2026-11-26_r6_prefix1099_reanchor_sign.py":"245b70ae2c5ef67938865af2a6558df66d8b08e2",
"2026-11-26_r6_prefix1100_centered_beta_dual.py":"1d6c34d1f5858368f291ef95ef8ff6a0f9591463",
"2026-11-26_r6_prefix1110_amplitude_reverse_strip.md":"7d94c52be7e68d03f8392438f66c67250ebaa12f"}
def pinned(name):
    raw=(HERE/name).read_bytes()
    assert hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()==PINS[name]
    return raw.decode()
for name in PINS:pinned(name)
# Exact floor recovery, not a change to the anchor matrix.
GINT=10**220
class IV:
    def __init__(self,l,u):self.l,self.u=l,u
    def __mul__(self,c):
        c=F(c);a,b=F(self.l,GINT)*c,F(self.u,GINT)*c
        return min(a,b),max(a,b)
    __rmul__=__mul__
def integ(k,half,degree):
    p0=p1=GINT;v0=2*GINT//(half+2);v1=-(-2*GINT//(half+2))
    for j in range(1,k+1):
        p0=35*p0//36;p1=-(-35*p1//36);den=half+2*j+2
        v0=2*(j*v0+p0)//den;v1=-(-2*(j*v1+p1)//den)
    edge0=35*p0//36;edge1=-(-35*p1//36);vals=[IV(v0,v1)]
    for n in range(degree):
        t=half+2*n;den=t+2*k+4
        v0=36*((t+2)*v0-2*edge1)//den
        v1=-(-36*((t+2)*v1-2*edge0)//den)
        assert 0<v0<=v1
        vals.append(IV(v0,v1))
    return vals
def down100(x):
    H=10**100
    if isinstance(x,IV):x=x*1
    if isinstance(x,tuple):
        a,b=x;v=(a*H).__floor__()
        assert v==(b*H).__floor__()
        return F(v,H)
    return F((x*H).__floor__(),H)
name="2026-11-26_r6_prefix1100_centered_beta_dual.py"
src=pinned(name)
old="H=10**100; down=lambda x:Q(x.numerator*H//x.denominator,H)"
assert src.count(old)==1
src=src.replace(old,"H=10**100; down=down100")
env={"__name__":"prefix1111_replay","__file__":str(HERE/name),"down100":down100}
exec(compile(src,str(HERE/name),"exec"),env)
env["integ"]=integ
anchor=env["anchor_dual"];make=env["make_oracle"]
cases=[(10**21,21440036720404643983373),(10**21,21440036720404643983374),(10**22,214400367204046439832847),(10**22,214400367204046439832848)]
displays=["-6.637907832856747e-12","4.878091008086301e-13","-3.301386868029895e-14","6.795578246862388e-13"]
def compact(a,m,k,p):
    return dict(m=str(m),k=str(k),grid=str(p),center_lo=str((a[0]*p).__floor__()),center_hi=str((a[0]*p).__ceil__()),radius_hi=str((a[1]*p).__ceil__()),parts_hi=[str((v*p).__ceil__()) for v in a[2:]])
oracle,loc,deg=make(anchor([3200,3600,4000,4400]),80,7,55,F(160427545,10**8));assert deg==218
raw=[]
for (m,k),display in zip(cases,displays):
    a=oracle(m,k)
    assert abs(a[0]-F(display))<=F(1,10**26) and a[1]<=F(2,10**17) and a[6]<F(1,10**100) and abs(a[0])>a[1]
    raw.append(compact(a,m,k,10**50))
print("REPLAY",json.dumps(raw))
# New tighter anchor, higher numerator cut; same observer and frozen basis.
oracle,loc,deg=make(anchor([4000,4400,4800,5200]),120,7,75,F(160427545,10**8));assert deg==298
ref=[]
for m,k in cases:
    a=oracle(m,k);assert abs(a[0])>a[1] and a[6]<F(1,10**100)
    ref.append(compact(a,m,k,10**70))
print("REFINED",json.dumps(ref))
# Reuse the exact prior sieve and its verified conditional input. The raw
# replay above now discharges the display-enclosure assumption.
prior=pinned("2026-11-26_r6_prefix1110_amplitude_reverse_strip.md")
priorcode=prior.split("\x60\x60\x60python\n",1)[1].split("\x60\x60\x60",1)[0]
ss={}
exec(compile(priorcode,"PREFIX-1110 exact sieve","exec"),ss)
R1110=ss["R"][:];C=ss["C"];T=ss["T"];E=ss["E"];isolate=ss["isolate"];oldpts=ss["new"]
assert len(oldpts)==13
def reverse(R,data):
    for A,B in zip(data[::2],data[1::2]):
        m,k=int(A["m"]),int(A["k"]);assert int(B["k"])==k+1 and int(B["m"])==m
        def box(a):
            p=int(a["grid"])
            return F(int(a["center_lo"])-int(a["radius_hi"]),p),F(int(a["center_hi"])+int(a["radius_hi"]),p)
        al,au=box(A);bl,bu=box(B);al,au=-au,-al;assert al>0 and bl>0
        rl=al/(al+bu);ru=au/(au+bl);eps=(F(2000,m)+F(620,m*m))/F("0.044")**2
        R=[max(R[0],(k+rl-eps-C[1]-T[1]/m)/m),min(R[1],(k+ru+eps-C[0]-T[0]/m)/m)]
        assert R[0]<=R[1]
    return R
Rraw=reverse(R1110,raw);Rnew=reverse(Rraw,ref)
assert Rnew[1]-Rnew[0]<F(278,10**38)
ss["R"]=Rnew
def band(m):return Rnew[0]*m+C[0]+T[0]/m-F(E,m*m),Rnew[1]*m+C[1]+T[1]/m+F(E,m*m)
for m,j in oldpts:
    lo,hi=band(m);assert not lo<=j<=hi
new=[];windows=[];l=65536*10**9
while l<10**18:
    h=2*l-1;assert (Rnew[1]-Rnew[0])*h+C[1]-C[0]+(T[1]-T[0])/l+F(2*E,l*l)<1
    _,n,_,pts=isolate(l,h);new+=pts;windows.append((l,h,n,len(pts)));l*=2
assert len(new)==9 and sum(w[2] for w in windows)==1068
assert hashlib.sha256(json.dumps(new,separators=(",",":")).encode()).hexdigest()=="8ecd79980293bda22f6750ae91b58c9933d2a39cbe1f3c71f38a3d0d4641aa9e"
print("RNEW",*[str(x) for x in Rnew]);print("WINDOWS",windows)
def certify(oracle,points):
    out=[]
    for m,j in points:
        a=oracle(m,j);s=int(a[0]>a[1])-int(a[0]<-a[1])
        d=compact(a,m,j,10**70);d["sign"]=s
        out.append(d)
    return out
closed=certify(oracle,new)
remaining=[(int(x["m"]),int(x["k"])) for x in closed if not x["sign"]];assert len(remaining)==2
oracle,loc,deg=make(anchor([4400,4800,5200,5600]),120,7,75,F(160427545,10**8));assert deg==298
last=certify(oracle,remaining);assert all(x["sign"] for x in last)
print("CLOSE",json.dumps(closed));print("FINAL",json.dumps(last))
by_m={int(x["m"]):x for x in closed};by_m.update({int(x["m"]):x for x in last})
rm=(sum(Rnew)*10**42/2).__floor__()
assert rm==21440036720404643983274790532018959153833541
for m,j in new:
    sign=by_m[m]["sign"];assert sign
    assert (F(rm,10**42)*m+sum(C)/2+sum(T)/(2*m)).__floor__()==j-(sign>0)
assert l-10**8==1073741823900000000
print("CERTIFIED",l-10**8,"NO EXCEPTIONS")

#!/usr/bin/env python3
"""Stage382-B exact Fraction certificate: original 16 cost labels and 4 residuals."""
from fractions import Fraction as F
from hashlib import sha256
from math import comb
import json,sys

f=lambda s:F(str(s))
PBOX=(f("0.2308"),f("0.2345"),f("0.55"),f("0.56"))
QBOX=(f("0.2365"),f("0.239"),f("0.57566"),f("0.57574"))
W=(1,3,3,1); M=(61,21,9,9); EPS=F(11,5000)
A1=F(1,4); A3=F(3,4)
def B(k,z):return z**k*(1-z)**(3-k)
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def r1(x,y):return 4*B(1,x)+B(1,y)-F(21,32)
def r0(x,y):return 4*B(0,x)+B(0,y)-F(61,32)
def budget(x,y):return sum(F(5,32)*W[k]*abs(r(k,x,y)) for k in range(4))
def bpoly(x,y):return F(3,16)*(4*x*(1-x)+y*(1-y))-F(45,256)
def D(a,z):return sum(F(1,2)*W[k]*abs(B(k,a)-B(k,z)) for k in range(4))
def cost(x,y):return (63*D(A1,x)+D(A3,x)+9*D(A1,y)+7*D(A3,y))/256
def delta(y):return F(9,64)-y*y*(1-y)
def C0(x,y):return F(5157,32768)-F(189,256)*x+F(93,128)*x*x-F(61,256)*x**3+F(33,512)*y*y-F(29,512)*y**3
def cp(x,y):return C0(x,y)+F(21,512)*abs(delta(y))

def root(fun,lo,hi,n,increasing):
    assert (fun(lo)<0<fun(hi)) if increasing else (fun(lo)>0>fun(hi))
    for _ in range(n):
        m=(lo+hi)/2;v=fun(m)
        if v==0:return m,m
        if (v<0)==increasing:lo=m
        else:hi=m
    return lo,hi
def face_y(x):return root(lambda y:r1(x,y),PBOX[2],QBOX[3],115,False)
def beta():
    def s(x):
        yl,yu=face_y(x);a=r0(x,yu);b=r0(x,yl)
        assert a>0 or b<0
        return 1 if a>0 else -1
    lo,hi=PBOX[:2];assert s(lo)==1 and s(hi)==-1
    for _ in range(68):
        m=(lo+hi)/2
        if s(m)==1:lo=m
        else:hi=m
    yl=face_y(lo)[0];yu=face_y(hi)[1]
    return lo,hi,yl,yu,bpoly(lo,yu),bpoly(hi,yl)
def alpha():return root(lambda y:16*y*y-4*y-3,QBOX[2],QBOX[3],90,True)
def qx(a,b):
    lo,hi=QBOX[:2];assert r1(lo,b)<0 and r1(hi,a)>0
    for _ in range(85):
        m=(lo+hi)/2
        if r1(m,a)>0:hi=m
        elif r1(m,b)<0:lo=m
        else:raise ValueError("alpha enclosure needs refining")
    return lo,hi
def binterval(xlo,xhi,ylo,yhi):
    assert xlo>=0 and xhi<F(1,2) and ylo>F(1,2) and yhi<1
    return bpoly(xlo,yhi),bpoly(xhi,ylo)
def px(targetlo,targethi):
    def s(x):
        yl,yu=face_y(x);lo,hi=binterval(x,x,yl,yu)
        if hi<targetlo:return -1
        if lo>targethi:return 1
        raise ValueError("target interval ambiguous")
    lo,hi=f("0.23113"),f("0.23115")
    assert s(lo)==-1 and s(hi)==1
    for _ in range(35):
        m=(lo+hi)/2
        if s(m)==-1:lo=m
        else:hi=m
    return lo,hi,face_y(lo)[0],face_y(hi)[1]
def C0range(xl,xu,yl,yu):
    return (F(5157,32768)-F(189,256)*xu+F(93,128)*xl**2-F(61,256)*xu**3+F(33,512)*yl**2-F(29,512)*yu**3,
            F(5157,32768)-F(189,256)*xl+F(93,128)*xu**2-F(61,256)*xl**3+F(33,512)*yu**2-F(29,512)*yl**3)
def costrange(xl,xu,yl,yu):
    lo,hi=C0range(xl,xu,yl,yu)
    dl=F(9,64)-yu**2*(1-yu);du=F(9,64)-yl**2*(1-yl)
    if dl>0:al,au=dl,du
    elif du<0:al,au=-du,-dl
    else:al,au=F(0),max(-dl,du)
    return lo+F(21,512)*al,hi+F(21,512)*au
def floorq(q):return q.numerator//q.denominator
def dec(q,upper=False):
    n=-floorq(-q*10**12) if upper else floorq(q*10**12)
    return str(n//10**12)+"."+str(n%10**12).zfill(12)
def dec18(q,upper=False):
    n=-floorq(-q*10**18) if upper else floorq(q*10**18)
    return str(n//10**18)+"."+str(n%10**18).zfill(18)
def sign_controls(k,a,lo,hi):
    def mul(p,q):
        z=[F(0)]*(len(p)+len(q)-1)
        for i,x in enumerate(p):
            for j,y in enumerate(q):z[i+j]+=x*y
        return z
    p=[F(1)]
    for _ in range(k):p=mul(p,[F(0),F(1)])
    for _ in range(3-k):p=mul(p,[F(1),F(-1)])
    h=[B(k,a)-p[0]]+[-z for z in p[1:]]
    power=[sum(h[j]*comb(j,i)*lo**(j-i)*(hi-lo)**i for j in range(i,4)) for i in range(4)]
    return [sum(power[j]*F(comb(i,j),comb(3,j)) for j in range(i+1)) for i in range(4)]
def run():
    audit=[]
    for tag,(xl,xu,yl,yu) in {"P":PBOX,"Q":QBOX}.items():
        for var,lo,hi in [("x",xl,xu),("y",yl,yu)]:
            for a in [A1,A3]:
                for k in range(4):
                    controls=sign_controls(k,a,lo,hi)
                    sign="+" if min(controls)>0 else "-" if max(controls)<0 else "MIXED"
                    audit.append({"box":tag,"coordinate":var,"anchor":str(a),"label":k,"sign":sign,"bernstein_controls":[str(v) for v in controls]})
    uncertain=[(t["box"],t["coordinate"],t["anchor"],t["label"]) for t in audit if t["sign"]=="MIXED"]
    assert uncertain==[("Q","y","3/4",2)]
    xs=list(map(f,["0.2308","0.231","0.232","0.2345","0.2365","0.237","0.238","0.239"]))
    ys=list(map(f,["0.55","0.553","0.556","0.56","0.57566","0.57567","0.57568","0.57569","0.57570","0.57571","0.57572","0.57574"]))
    for x in xs:
        for y in ys:assert cost(x,y)==cp(x,y)
    xbL,xbU,ybL,ybU,bL,bU=beta()
    aL,aU=alpha();xqL,xqU=qx(aL,aU)
    bqL,bqU=binterval(xqL,xqU,aL,aU)
    xpL,xpU,ypL,ypU=px(2*bL+EPS-bqU,2*bU+EPS-bqL)
    for xa,xb,ya,yb in [(xpL,xpU,ypL,ypU),(xqL,xqU,aL,aU)]:
        x=(xa+xb)/2;y=(ya+yb)/2
        assert abs(budget(x,y)-bpoly(x,y))<F(1,10**16)
        assert cost(x,y)==cp(x,y)
    cpl,cpu=costrange(xpL,xpU,ypL,ypU)
    cql,cqu=costrange(xqL,xqU,aL,aU)
    TL=F(33,1024)+cpl+cql;TU=F(33,1024)+cpu+cqu
    assert TU-TL<F(1,10**8)
    Pw=(f("0.2311391166"),f("0.5556844758"))
    Qw=(f("0.2378069027"),f("0.5756939095"))
    bw=budget(*Pw)+budget(*Qw);cw=F(33,1024)+cost(*Pw)+cost(*Qw)
    assert bw<2*bL+EPS and cw<TU+F(1,10**8)
    manifest={"status":"CONDITIONAL_ON_STAGE379_380_381_GLOBAL_MINIMIZER_LEMMAS",
      "model":"16 labeled audit comparisons; 4 independent residual channels per source",
      "frozen_science":{"global":"bf84bd7c61a2444b59b1da96be57df0e9ae47e53",
       "em":"2af3fc484eb11060b69e0afc1b562bcaf5ad1419",
       "p000_blob":"bcc2590d3168a28f72e8b9f0f9b1f76faadcd488"},
      "beta_brackets":[str(x) for x in (xbL,xbU,ybL,ybU,bL,bU)],
      "Q_brackets":[str(x) for x in (aL,aU,xqL,xqU,bqL,bqU)],
      "P_brackets":[str(x) for x in (xpL,xpU,ypL,ypU)],
      "T_brackets_exact":[str(TL),str(TU)],
      "T_decimal_outward":[dec(TL),dec(TU,True)],
      "unknown_audit_labels":uncertain,"audit_sign_controls":audit,
      "exact_rational_feasible_witness":{"P":[str(z) for z in Pw],"Q":[str(z) for z in Qw],
       "original_budget":str(bw),"original_cost":str(cw)}}
    data=json.dumps(manifest,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
    output=sys.argv[1] if len(sys.argv)>1 else "CERTIFICATE_STAGE382B_EXACT.json"
    with open(output,"w",encoding="utf-8") as fp:fp.write(data)
    print("SIGN_UNKNOWN_LABELS",uncertain)
    print("COST_IDENTITY_EXACT_GRID_96_PASS",len(xs)*len(ys))
    print("BETA_BRACKETS",*[dec18(v,i%2==1) for i,v in enumerate((xbL,xbU,ybL,ybU,bL,bU))])
    print("ALPHA_AND_XQ_BRACKETS",*[dec18(v,i%2==1) for i,v in enumerate((aL,aU,xqL,xqU,bqL,bqU))])
    print("P_BRACKETS",*[dec18(v,i%2==1) for i,v in enumerate((xpL,xpU,ypL,ypU))])
    print("CERTIFIED_T_BRACKET",dec(TL),dec(TU,True))
    print("WITNESS_BUDGET_LT_BETA_LOWER",bw<2*bL+EPS)
    print("WITNESS_COST_BRACKET",dec(cw),dec(cw,True))
    print("STAGE382B_EXACT_OBJECTIVE_BRACKET_PASS",len(data.encode()),sha256(data.encode()).hexdigest())
if __name__=="__main__":run()

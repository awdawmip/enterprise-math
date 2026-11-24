from fractions import Fraction as F
from math import factorial, prod, lcm, comb
import sympy as S
Y,x,n=S.symbols('Y x n')
a=[-Y**2*(Y-6),-Y**2*(31*Y**2-516*Y+1020),-6*Y**2*(15*Y**3-406*Y**2+2078*Y-1152),-Y**3*(65*Y**3-2408*Y**2+19836*Y-27648),-5*Y**4*(3*Y**3-140*Y**2+1568*Y-3456),-Y**5*(Y-36)*(Y-16)*(Y-4)]
A=[S.Poly((-1)**j*p.subs(Y,4-x),x) for j,p in enumerate(a)]
D=100; R=F(5,2); T=F(1,10**18) # conservative inherited tail bound from PREFIX1056
W=10**70

def down(z): return z.numerator//z.denominator

def up(z): return -down(-z)

def box(l,h=None):
    if h is None: h=l
    return down(F(l)*W),up(F(h)*W)

def add(*a):return sum(i[0] for i in a),sum(i[1] for i in a)

def sc(a,c):
    l,h=sorted((F(a[0])*c,F(a[1])*c));return down(l),up(h)

def mul(a,b):
    v=[i*j for i in a for j in b];return min(v)//W,-((-max(v))//W)

def widen(a,e):
    b=up(e*W);return a[0]-b,a[1]+b

def mag(a):return F(max(map(abs,a)),W)

def falling(z,j):return prod(z-i for i in range(j))

def initial(alpha,j0,y):
    b=[F(int(i==j0)*(-1)**i) for i in range(4)] if alpha==0 else [F(1)]
    w=[S.Poly(S.expand(sum(A[j].nth(k-4+j)*prod(n+alpha-k-i for i in range(j)) for j in range(6) if k-4+j>=0)),n) for k in range(8)]
    wi=[[F(p.nth(i)) for i in range(6)] for p in w]
    def ev(p,i):return sum(c*i**j for j,c in enumerate(p))
    for i in range(len(b),D+1):
        v=[ev(p,i) for p in wi];assert v[0]
        b.append(-sum(v[k]*b[i-k] for k in range(1,min(7,i)+1))/v[0])
    X=4-y; s=F(5,4) # y=39/16
    assert s*s==X
    xa=1 if alpha==0 else s**3
    q=X/R
    err=[T*xa/X**j*q**(D+1)*F(D+3)**j*factorial(j)/(1-q)**(j+1) for j in range(5)]
    z=[]
    for j in range(5):
        val=sum(bi*falling(i+alpha,j)*X**i*xa/X**j*(-1)**j for i,bi in enumerate(b))
        z.append(widen(box(F(val)),err[j]))
    val=sum(bi*xa*(2*X**(i+1)/(i+alpha+1)+X**(i+2)/(i+alpha+2)) for i,bi in enumerate(b))
    z.append(widen(box(F(val)),6*X*err[0]))
    return z

AP=[tuple(int(S.Poly(p,Y).nth(k)) for k in range(S.Poly(p,Y).degree()+1)) for p in a]
L0=max(5-j+len(p)-1 for j,p in enumerate(AP))
FALL={}
for l in range(L0+1):
    for j in range(6):
        f=[1]
        for k in range(j):
            g=[0]*(len(f)+1)
            for i,v in enumerate(f):g[i]-=(l+k)*v;g[i+1]+=v
            f=g
        FALL[l,j]=f

def recurrence(y,r,N):
    L=L0; w=[[F(0)]*6 for _ in range(L+1)]
    for j,p in enumerate(AP):
        for k in range(len(p)):
            v=sum(F(p[i]*comb(i,k))*y**(i-k) for i in range(k,len(p)))*(-r)**k/(-r)**j
            l=5-j+k
            for i,f in enumerate(FALL[l,j]):w[l][i]+=v*f
    den=lcm(*(c.denominator for p in w for c in p));ws=[[int(c*den) for c in p] for p in w]
    def sh(p):return [sum(p[k]*comb(k,i)*N**(k-i) for k in range(i,6)) for i in range(6)]
    z=[sh(p) for p in ws]; sign=1 if z[0][-1]>0 else -1
    assert all(sign*z[0][i]>0 for i in range(6))
    ratio=max(F(sum(abs(p[i]) for p in z[1:]),sign*z[0][i]) for i in range(6))
    assert ratio<1,(y,r,N,float(ratio))
    def ev(p,i):
        v=0
        for a in reversed(p):v=v*i+a
        return v
    rec=[]
    for i in range(5,N):
        v=[ev(p,i) for p in ws];assert v[0]
        rec.append([F(-v[k],v[0]) for k in range(1,min(L,i)+1)])
    return rec,L,ratio

def horner(c,t):
    b=(0,0)
    for v in reversed(c):b=add(mul(b,t),v)
    return b

def expand(z,y,r,N,rec,L):
    c=[sc(z[j],(-r)**j/F(factorial(j))) for j in range(5)]
    for i,row in enumerate(rec,5):c.append(add(*(sc(c[i-k],v) for k,v in enumerate(row,1))))
    B=max(map(mag,c[-L:]))
    return c,B

def evalstate(c,B,z,y,r,N,t,q,full=True):
    # t interval, 0<=t<=q<1; derivative tails and integrated primitive
    out=[]
    for j in range(5 if full else 2):
        p=[sc(c[i],F(falling(i,j))/(-r)**j) for i in range(j,N)]
        err=B*F(N)**j*factorial(j)*q**(N-j)/(r**j*(1-q)**(j+1))
        out.append(widen(horner(p,t),err))
    if not full:out.extend([(0,0)]*3)
    # v_t=-r*(y-6-r*t)*u
    p=[z[5]]
    for i in range(N+1):
        terms=[]
        if i<N:terms.append(sc(c[i],-r*(y-6)/F(i+1)))
        if i>0:terms.append(sc(c[i-1],r*r/F(i+1)))
        p.append(add(*terms))
    e0=B*q**N/(1-q)
    out.append(widen(horner(p,t),6*r*q*e0))
    return out

def contrast(z,Y):
    # Y interval, 0<Y<4
    Z=add(box(36),sc(Y,-1)); H=mul(mul(Y,Y),mul(Z,Z)); Hp=sc(mul(mul(Y,Z),add(box(36),sc(Y,-2))),2)
    P=mul(mul(Y,sc(Z,-1)),add(sc(Y,17),box(-91)))
    return add(sc(mul(Hp,z[0]),4),sc(mul(H,z[1]),4),sc(mul(P,z[0]),-2),sc(mul(add(box(11),Y),z[5]),12))

def go():
    y=F(39,16)
    states=[initial(F(0),j,y) for j in range(4)]+[initial(F(3,2),0,y)]
    states.append([(0,0)]*5+[box(1)])
    weights=[box(F(235698,100),F(235702,100)),box(F(-44062,100),F(-44059,100)),box(F(6845,100),F(6848,100)),box(F(-1244,100),F(-1242,100)),box(-135),box(F(-5241077,100),F(-5241068,100))]
    N=120; q=F(1,2); overall=None
    for step in range(100):
        r=min(y,4-y)/8; h=r*q
        rec,L,ratio=recurrence(y,r,N)
        cs=[expand(z,y,r,N,rec,L) for z in states]
        low=None
        for j in range(8):
            t=box(q*j/8,q*(j+1)/8); yy=box(y-r*q*(j+1)/8,y-r*q*j/8)
            combined=add(*(mul(w,contrast(evalstate(c,B,z,y,r,N,t,q*(j+1)/8,False),yy)) for (c,B),z,w in zip(cs,states,weights)))
            low=combined[0] if low is None else min(low,combined[0])
        if low<=0:
            print('STOP',step,float(y),float(F(low,W)),flush=True);break
        overall=low if overall is None else min(overall,low)
        states=[evalstate(c,B,z,y,r,N,box(q),q) for (c,B),z in zip(cs,states)]
        y-=h
        print(step+1, 'y',float(y),'lower',float(F(low,W)),'ratio',float(ratio),'width',max(float(F(z[0][1]-z[0][0],W)) for z in states),flush=True)
        if y<F(1,240):break
    assert y<F(1,240) and overall>400*W
    print("PREFIX1057_RECENTERED_LOWER_CERTIFICATE_PASSED")
    print('FINAL',y,'lower',float(F(overall,W)))
if __name__=='__main__':go()

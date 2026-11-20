"""R5: exact Gaussian-integer DP for the q=±i N^21 coefficient."""
from fractions import Fraction
from itertools import product

S0=(214,215,216,217,218)
S1=(214,216,217,218,219,220,221)
S2=(215,216,217,218,219,220,221)
SETS=(set(S0),set(S1),set(S2))
E0=range(219,315)
E1=(215,)+tuple(range(222,315))
E2=(214,)+tuple(range(222,315))
EH=range(222,315)

def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(a,x):return x*a[0],x*a[1]
def rotate(a,k):
    x,y=a
    return ((x,y),(-y,x),(-x,-y),(y,-x))[k%4]

def bfree(E):
    re,im=Fraction(0),Fraction(0)
    for p in E:
        if p%4==0: re+=Fraction(p-1,2)
        elif p%4==2: re+=Fraction(p,2)
        elif p%4==1: re+=Fraction(p,2); im-=Fraction(p,2)
        else: re+=Fraction(p,2); im+=Fraction(p,2)
    return re,im
B0,B1,B2,BH=map(bfree,(E0,E1,E2,EH))
assert (B0,B1,B2,BH)==((12780,-24),(12558,Fraction(169,2)),(Fraction(25115,2),-23),(Fraction(24901,2),-23))

def moments(S,m):
    # H=Σ i^cost; D=-Σcost*i^cost; V=Σcost(cost-1)*i^cost.
    dp={0:((1,0),(0,0),(0,0))}
    for p in S:
        new={}
        for count,(H,D,V) in dp.items():
            for n in range(m-count):
                c=p*n
                h=rotate(H,c)
                d=add(rotate(D,c),scale(h,-c))
                v=add(rotate(V,c),add(scale(rotate(D,c),-2*c),scale(h,c*(c-1))))
                old=new.get(count+n,((0,0),(0,0),(0,0)))
                new[count+n]=(add(old[0],h),add(old[1],d),add(old[2],v))
        dp=new
    H,D,V=(0,0),(0,0),(0,0)
    for h,d,v in dp.values():H=add(H,h);D=add(D,d);V=add(V,v)
    return H,D,V

def overlap(m):
    dp={(0,0,0):((1,0),(0,0))}
    for p in range(214,222):
        membership=tuple(int(p in Sj) for Sj in SETS)
        new={}
        for counts,(H,D) in dp.items():
            for n in range(m):
                next_counts=tuple(min(m,counts[j]+membership[j]*n) for j in range(3))
                if sum(x<m for x in next_counts)<2: continue
                c=p*n;h=rotate(H,c);d=add(rotate(D,c),scale(h,-c))
                prev=new.get(next_counts,((0,0),(0,0)))
                new[next_counts]=(add(prev[0],h),add(prev[1],d))
        dp=new
    H,D=(0,0),(0,0)
    for counts,(h,d) in dp.items():
        mult=max(sum(x<m for x in counts)-1,0)
        H=add(H,scale(h,mult));D=add(D,scale(d,mult))
    return H,D

def coefficients(m):
    assert m>=2 and m%2==0
    u0,d0,v0=moments(S0,m)
    u1,d1,_=moments(S1,m)
    u2,d2,_=moments(S2,m)
    uh,dh=overlap(m)
    assert u0==(0,0)
    D=add(add(d0,mul((220,-220),u1)),add(scale(u2,220),scale(uh,-440)))
    shift=lambda b:(b[0]+Fraction(23,2),b[1])
    E=add(scale(v0,Fraction(1,2)),mul(shift(B0),d0))
    E=add(E,mul((220,-220),add(mul(shift(B1),u1),d1)))
    E=add(E,scale(add(mul(shift(B2),u2),d2),220))
    E=add(E,scale(add(mul(shift(BH),uh),dh),-440))
    return D,E

def previous_D(m):
    if m%4==2:
        t=(m-2)//4
        return (t+1)*(436*t+656),-2*(t+1)
    t=(m-4)//4
    return 436*(t+1)*(t+2),220*(t+1)*(t+2)

# Independent complete tuple enumeration: deliberately avoids the state DP.
def brute_event(S,m):
    H,D,V=(0,0),(0,0),(0,0)
    for ns in product(range(m),repeat=len(S)):
        if sum(ns)>=m:continue
        c=sum(p*n for p,n in zip(S,ns));w=rotate((1,0),c)
        H=add(H,w);D=add(D,scale(w,-c));V=add(V,scale(w,c*(c-1)))
    return H,D,V

def brute_overlap(m):
    H,D=(0,0),(0,0)
    for ns in product(range(m),repeat=8):
        counts=[sum(ns[p-214] for p in Sj) for Sj in SETS]
        k=max(sum(x<m for x in counts)-1,0)
        if not k:continue
        c=sum((p+214)*n for p,n in enumerate(ns)); w=rotate((1,0),c)
        H=add(H,scale(w,k));D=add(D,scale(w,-c*k))
    return H,D

if __name__=="__main__":
    for m in range(2,21,2):
        D,E=coefficients(m)
        assert D==previous_D(m),(m,D)
        print(m,D,E)
    for m in (2,4):
        for Sj in (S0,S1,S2):
            assert brute_event(Sj,m)==moments(Sj,m)
        assert brute_overlap(m)==overlap(m)
        print("independent exhaustive PASS",m)
    print("PASS: ten exact DP cases, ten prior-regression cases, two independent complete enumerations")

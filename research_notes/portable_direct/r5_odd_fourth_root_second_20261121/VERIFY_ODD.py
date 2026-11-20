"""R5: exact symbolic certificate + independent Z[i] DP for odd-m fourth-root N^22 term."""
from collections import defaultdict
import sympy as sp

S0=(214,215,216,217,218)
S1=(214,216,217,218,219,220,221)
S2=(215,216,217,218,219,220,221)
SETS=tuple(map(set,(S0,S1,S2)))
I=sp.I
z=sp.symbols("z")

# Direct expansion of the free denominator at q=i(1-s)
E0=range(219,315)
b0=sp.simplify(sum(sp.Rational(p-1,2) if p%4==0
                    else -p*I**p/(1-I**p) for p in E0))
assert b0 == 12780-24*I

def H(S):
    v=z/(1-z)
    for p in S: v/=1-z*I**p
    return v

def M(a,b):
    return (1-a*b*z*z)/((1-a*z)*(1-b*z)*(1-a*b*z))

def overlap3(a,b,c):
    tri=(1-a*b*c*z**3)/((1-a*b*c*z*z)*(1-a*z)*(1-b*z)*(1-c*z))
    return M(b,c)/(1-a*z)+M(a,c)/(1-b*z)+M(a,b)/(1-c*z)-tri

# Weighted overlap of three short bad events, proven from max/min composition.
h=z/((1-z)*(1-z*z)*(1-I*z))*(
    sp.Rational(1,2)*overlap3(-1,-I,1)
    +(1-I)/4*overlap3(-1,-I,I)
    +(1+I)/4*overlap3(-1,-I,-I))
h0,h1,h2=map(H,(S0,S1,S2))
D= -h0*sum(p*z*I**p/(1-z*I**p) for p in S0)
D+=220*(1-I)*h1+220*h2-440*h
odd=lambda v: sp.cancel((v-v.subs(z,-z))/2)
K=sp.cancel(odd(D)+(b0+12)*odd(h0))
P=sp.expand(sp.cancel(K*(1-z**4)**3*(1-I*z*z)/z))
expected=((12352-244*I)+(12332-12376*I)*z**2
          +(-14552-12332*I)*z**4+(-14068+14112*I)*z**6
          +(24+13872*I)*z**8)
assert sp.simplify(P-expected)==0
w=sp.symbols("w")
Pw=((12352-244*I)+(12332-12376*I)*w+(-14552-12332*I)*w**2
    +(-14068+14112*I)*w**3+(24+13872*I)*w**4)
assert sp.expand(Pw.subs(w,-I))==440-440*I

# Separately implement weighted bounded-state DP in ordinary integer pairs.
def add(a,b): return a[0]+b[0],a[1]+b[1]
def rot(x,k):
    a,b=x
    return ((a,b),(-b,a),(-a,-b),(b,-a))[k%4]

def moments(S,m):
    states={0:((1,0),(0,0))}
    for p in S:
        nxt={}
        for cost,(w,d) in states.items():
            for n in range(m-cost):
                ww=rot(w,p*n)
                dd=add(rot(d,p*n),(-p*n*ww[0],-p*n*ww[1]))
                oldw,oldd=nxt.get(cost+n,((0,0),(0,0)))
                nxt[cost+n]=(add(oldw,ww),add(oldd,dd))
        states=nxt
    totalw,totald=(0,0),(0,0)
    for ww,dd in states.values():
        totalw=add(totalw,ww)
        totald=add(totald,dd)
    return totalw,totald

def overlap(m):
    states={(0,0,0):(1,0)}
    for p in range(214,222):
        member=tuple(int(p in S) for S in SETS)
        nxt={}
        for key,weight in states.items():
            for n in range(m):
                key2=tuple(min(m,key[j]+member[j]*n) for j in range(3))
                nxt[key2]=add(nxt.get(key2,(0,0)),rot(weight,p*n))
        states=nxt
    total=(0,0)
    for key,weight in states.items():
        mult=max(sum(k<m for k in key)-1,0)
        total=add(total,(mult*weight[0],mult*weight[1]))
    return total

def K_independent(m):
    a,der=moments(S0,m)
    b,_=moments(S1,m)
    c,_=moments(S2,m)
    h=overlap(m)
    D=add(der,(220*(b[0]+b[1])+220*c[0]-440*h[0],
               220*(b[1]-b[0])+220*c[1]-440*h[1]))
    K=add(D,(12792*a[0]+24*a[1],12792*a[1]-24*a[0]))
    return D,K,a

def K_poly(m):
    pol={1:(12352,-244),3:(12332,-12376),5:(-14552,-12332),
         7:(-14068,14112),9:(24,13872)}
    total=(0,0)
    for j,pair in pol.items():
        if j>m: continue
        for t in range((m-j)//4+1):
            rest=m-j-4*t
            if rest%2: continue
            term=rot(pair,rest//2)
            mult=(t+1)*(t+2)//2
            total=add(total,(mult*term[0],mult*term[1]))
    return total

if __name__=="__main__":
    print("b0",b0)
    print("P",P)
    for m in range(1,20,2):
        d,k,h0val=K_independent(m)
        assert h0val==((m-1)//4+1,0),(m,h0val)
        assert k==K_poly(m),(m,k,K_poly(m))
        print(m,d,k)
    print("PASS: exact rational identity for all odd m; independent Z[i] DP for m=1,3,...,19")

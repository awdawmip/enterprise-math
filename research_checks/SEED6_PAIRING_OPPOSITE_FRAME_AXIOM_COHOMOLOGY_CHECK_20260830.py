#!/usr/bin/env python3
"""Exact finite checker for RS-SEED6-PAIRING-OPPOSITE-FRAME-AXIOM-COHOMOLOGY."""
from itertools import combinations, permutations
from math import comb, gcd

N = 0
def ck(x, m=""):
    global N
    N += 1
    if not x:
        raise AssertionError(m or f"check {N} failed")

def rank(rows):
    B = {}
    for x0 in rows:
        x = x0
        while x:
            p = x.bit_length()-1
            if p in B: x ^= B[p]
            else: B[p] = x; break
    return len(B)

def par(x): return x.bit_count() & 1

class DSU:
    def __init__(self,n): self.p=list(range(n))
    def f(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]; x=self.p[x]
        return x
    def u(self,a,b):
        a,b=self.f(a),self.f(b)
        if a==b: return False
        self.p[b]=a; return True

def red(a,b):
    d=gcd(a,b); return a//d,b//d

def pins(a,b,R):
    A,B=red(a,b)
    if A==B: return ()
    S=set(R); M=max(R)
    return tuple((A*t,B*t,t) for t in range(1,M//min(A,B)+1) if A*t in S and B*t in S)

def cx(a,b,R0):
    R=tuple(sorted(set(R0))); A,B=red(a,b); k=len(R)
    if A==B:
        E=[("ha",r,s) for i,r in enumerate(R) for s in R[i+1:]]
        b1=[(1<<R.index(r))^(1<<R.index(s)) for _,r,s in E]
        return dict(a=a,b=b,R=R,A=A,B=B,p=(),V=k,E=E,F=[],b1=b1,b2=[],eq=True)
    V0=[("a",r) for r in R]+[("b",r) for r in R]; vi={v:i for i,v in enumerate(V0)}
    d=DSU(2*k); P=pins(a,b,R); touched=set()
    for At,Bt,t in P:
        x,y=vi[("b",At)],vi[("a",Bt)]
        ck(x not in touched and y not in touched,"pinches must be typed matching")
        touched|={x,y}; ck(d.u(x,y))
    roots={}; q=[]
    for i in range(2*k):
        z=d.f(i)
        if z not in roots: roots[z]=len(roots)
        q.append(roots[z])
    E=[]; em={}
    for row in "ab":
        for i,r in enumerate(R):
            for s in R[i+1:]:
                em[(row,r,s)]=len(E); E.append(("h"+row,r,s))
    for r in R: em[("v",r,r)]=len(E); E.append(("v",r,r))
    b1=[]
    for typ,r,s in E:
        if typ=="ha": u,v=vi[("a",r)],vi[("a",s)]
        elif typ=="hb": u,v=vi[("b",r)],vi[("b",s)]
        else: u,v=vi[("a",r)],vi[("b",r)]
        b1.append((1<<q[u])^(1<<q[v]))
    F=[]; b2=[]
    for i,r in enumerate(R):
        for s in R[i+1:]:
            es=(em[("a",r,s)],em[("v",s,s)],em[("b",r,s)],em[("v",r,r)])
            F.append(es); z=0
            for e in es: z ^= 1<<e
            b2.append(z)
    return dict(a=a,b=b,R=R,A=A,B=B,p=P,V=len(roots),E=E,F=F,b1=b1,b2=b2,eq=False)

def ei(X,typ,r,s=None):
    target={r} if s is None else {r,s}
    for i,(t,u,v) in enumerate(X["E"]):
        if t==typ and ({u} if t=="v" else {u,v})==target: return i
    raise KeyError((typ,r,s))

def closed(X,c): return all(par(c&f)==0 for f in X["b2"])
def db(X,l):
    z=0
    for e,b in enumerate(X["b1"]):
        if par(l&b): z|=1<<e
    return z
def exact(X,c):
    G=[db(X,1<<v) for v in range(X["V"])]
    return rank(G+[c])==rank(G)
def alpha(X):
    if X["eq"]: return 0
    return sum(1<<i for i,e in enumerate(X["E"]) if e[0]=="v")
def gamma(X,At,Bt): return (1<<ei(X,"v",At))^(1<<ei(X,"ha",At,Bt))

def formulas(X):
    k=len(X["R"]); r1=rank(X["b1"]); r2=rank(X["b2"]); beta=len(X["E"])-r1-r2
    if X["eq"]:
        b0=(k-1)*(k-2)//2
        ck((X["V"],len(X["E"]),len(X["F"]))==(k,comb(k,2),0))
        ck((r1,r2,beta)==(k-1,0,b0)); ck(alpha(X)==0 and exact(X,0))
        return
    m=len(X["p"]); b0=(k-1)*(k-2)//2
    ck((X["V"],len(X["E"]),len(X["F"]))==(2*k-m,k*k,comb(k,2)))
    ck((r1,r2,beta)==(2*k-m-1,comb(k,2),b0+m))
    ck(len(X["E"])-r2==k*(k+1)//2)
    h=alpha(X); ck(closed(X,h)); ck(exact(X,h)==(m==0))
    for At,Bt,t in X["p"]: ck(par(h&gamma(X,At,Bt))==1)

def orbit_checks():
    for X in (cx(2,3,[2,3]),cx(2,3,[2,3,5]),cx(2,3,[5,7,11]),cx(5,5,[1,2,3])):
        flats={c for c in range(1<<len(X["E"])) if closed(X,c)}
        G={db(X,l) for l in range(1<<X["V"])}
        beta=len(X["E"])-rank(X["b1"])-rank(X["b2"]); n=0
        while flats:
            c=min(flats); O={c^g for g in G}; ck(O<=flats); flats-=O; n+=1
        ck(n==1<<beta); ck(len(G)==1<<(X["V"]-1))

def independence():
    X=cx(2,3,[2,3,5]); h=alpha(X)
    c=(1<<ei(X,"ha",2,5))|(1<<ei(X,"hb",2,5))
    tri=(1<<ei(X,"ha",2,3))|(1<<ei(X,"ha",3,5))|(1<<ei(X,"ha",2,5))
    g=gamma(X,2,3)
    ck(closed(X,c) and not exact(X,c) and not exact(X,h^c))
    ck((par(h&g),par(h&tri),par(c&g),par(c&tri))==(1,0,0,1))

def resonance_checks():
    for a in range(2,17):
      for b in range(2,17):
        A,B=red(a,b)
        for r in range(1,31):
          for s in range(1,31):
            x=b*r==a*s; y=a*r==b*s
            ck(x==(r%A==0 and s%B==0 and r//A==s//B))
            ck(y==(r%B==0 and s%A==0 and r//B==s//A))
            ck((not(x and y)) if A!=B else (A==B==1 and x==(r==s) and y==(r==s)))

def census():
    U=range(1,9); sets=[S for q in range(2,6) for S in combinations(U,q)]
    for a in range(2,13):
      for b in range(2,13):
        for R in sets:
            X=cx(a,b,R); formulas(X); ck(X["p"]==pins(a,b,tuple(R)))
    named=[
      ("none",2,3,[5,7,11],0),("one",2,3,[2,3],1),("many",2,3,[2,3,4,6],2),
      ("C1",8,18,[4,8,9,18],2),("C2",6,35,[6,12,35,70],2),
      ("O1",6,10,[3,5,6,9,10,15],3),("O2",12,18,[2,3,4,6,8,12],3),
      ("eq",5,5,[1,2,3,4],0)]
    for name,a,b,R,m in named:
        X=cx(a,b,R); ck(len(X["p"])==m,name); formulas(X)

PM=(
 frozenset((frozenset((0,1)),frozenset((2,3)))),
 frozenset((frozenset((0,2)),frozenset((1,3)))),
 frozenset((frozenset((0,3)),frozenset((1,2)))))
S4=tuple(permutations(range(4))); S3=tuple(permutations(range(3)))
I4=(0,1,2,3); I3=(0,1,2)
def mul(p,q): return tuple(p[q[i]] for i in range(len(q)))
def inv(p):
    z=[0]*len(p)
    for i,j in enumerate(p): z[j]=i
    return tuple(z)
def typ(p):
    seen=set(); L=[]
    for i in range(len(p)):
        if i in seen: continue
        j=i;n=0
        while j not in seen: seen.add(j);n+=1;j=p[j]
        if n>1:L.append(n)
    return tuple(sorted(L,reverse=True))
def phi(p):
    out=[]
    for M in PM:
        Q=frozenset(frozenset(p[x] for x in pair) for pair in M)
        out.append(PM.index(Q))
    return tuple(out)
def s4():
    K={p for p in S4 if phi(p)==I3}; ck(len(K)==4); ck({typ(p) for p in K}=={(),(2,2)})
    for q in S3: ck(sum(phi(p)==q for p in S4)==4)
    tau=(0,2,1); F=[p for p in S4 if phi(p)==tau]
    ck(len(F)==4 and sum(typ(p)==(2,) for p in F)==2)
    C=[]
    for T in combinations(S4,6):
        H=set(T)
        if I4 in H and all(mul(x,y) in H for x in H for y in H) and {phi(x) for x in H}==set(S3):
            C.append(frozenset(H))
    C=list(dict.fromkeys(C)); ck(len(C)==4)
    O={frozenset(mul(mul(v,h),inv(v)) for h in C[0]) for v in K}; ck(O==set(C))
    for H in C:
        sec={phi(h):h for h in H}; ck(len(sec)==6)
        for x in S3:
          for y in S3: ck(mul(sec[x],sec[y])==sec[mul(x,y)])

def main():
    resonance_checks(); census(); orbit_checks(); independence(); s4()
    print(f"PASS checks={N}; C2_flat=Z1; gauge=H1; pinch_plus_one_H1_bit=PASS; height_periods=1; operator_height_independence=PASS; S4_kernel_V4=4; sections=4; marked_tau_lifts=4_two_atom_transpositions")

if __name__=="__main__": main()

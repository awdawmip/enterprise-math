#!/usr/bin/env python3
"""Exact finite checker for RS-DECORATED-CARRIER-MINIMAL-AUGMENTATION-ATOM-TRANSPORT."""
from itertools import product, permutations, combinations

N=0
def ck(x,m=""):
    global N
    N+=1
    if not x: raise AssertionError(m or f"check {N} failed")

def mul(p,q): return tuple(p[q[i]] for i in range(len(q)))
def inv(p):
    z=[0]*len(p)
    for i,j in enumerate(p): z[j]=i
    return tuple(z)
def compose_many(xs,I):
    z=I
    for x in xs: z=mul(z,x)
    return z

def parity(p):
    invs=0
    for i in range(len(p)):
      for j in range(i+1,len(p)): invs += p[i]>p[j]
    return invs&1

S3=tuple(permutations(range(3))); I3=(0,1,2)
C3=tuple(p for p in S3 if parity(p)==0)
MARK=0
H0=tuple(p for p in S3 if p[MARK]==MARK)

def p3pow(a,n):
    z=I3
    for _ in range(a%3): z=mul(n,z)
    return z

g3=next(p for p in C3 if p!=I3)
# additive C3 coordinate with chosen generator; residual C2 will invert it.
def c3el(a): return p3pow(a,g3)
def c3coord(p):
    return next(a for a in range(3) if c3el(a)==p)

def s3_split_checks():
    ck(len(C3)==3 and all(mul(x,y) in C3 for x in C3 for y in C3))
    ck(len(H0)==2 and {parity(p) for p in H0}=={0,1})
    marked={parity(p):p for p in H0}; ck(len(marked)==2)
    # unique A3 * marked-C2 decomposition
    for p in S3:
        e=parity(p); h=marked[e]
        a=mul(p,inv(h)); ck(a in C3); ck(mul(a,h)==p)
        ck(sum(mul(c3el(t),h)==p for t in range(3))==1)
    tau=marked[1]
    for a in range(3):
        q=mul(mul(tau,c3el(a)),inv(tau))
        ck(c3coord(q)==(-a)%3)
    # abstract sign splittings are exactly the three transposition complements;
    # the marked state selects the unique one fixing MARK.
    spl=[]
    for t in S3:
        if parity(t)==1 and mul(t,t)==I3: spl.append(t)
    ck(len(spl)==3 and sum(t[MARK]==MARK for t in spl)==1)
    return marked

PM=(
 frozenset((frozenset((0,1)),frozenset((2,3)))),
 frozenset((frozenset((0,2)),frozenset((1,3)))),
 frozenset((frozenset((0,3)),frozenset((1,2)))))
S4=tuple(permutations(range(4))); I4=(0,1,2,3)
def phi(p):
    out=[]
    for M in PM:
        Q=frozenset(frozenset(p[x] for x in pair) for pair in M)
        out.append(PM.index(Q))
    return tuple(out)
K=tuple(p for p in S4 if phi(p)==I3)

def addv(x,y): return mul(x,y) # V4 is elementary abelian

def act3_on_v4(q,v,section):
    s=section[q]
    return mul(mul(s,v),inv(s))

def all_sections():
    comps=[]
    for T in combinations(S4,6):
        H=set(T)
        if I4 not in H: continue
        if any(mul(x,y) not in H for x in H for y in H): continue
        if {phi(x) for x in H}!=set(S3): continue
        sec={phi(x):x for x in H}
        if all(mul(sec[x],sec[y])==sec[mul(x,y)] for x in S3 for y in S3):
            comps.append(sec)
    # dedup by ordered images
    uniq={tuple(sec[q] for q in S3):sec for sec in comps}
    return list(uniq.values())

def s4_section_checks():
    ck(len(K)==4 and all(mul(x,y) in K for x in K for y in K))
    ck(all(sum(phi(p)==q for p in S4)==4 for q in S3))
    secs=all_sections(); ck(len(secs)==4)
    base=secs[0]
    keys={tuple(sec[q] for q in S3) for sec in secs}
    conj={tuple(mul(mul(w,base[q]),inv(w)) for q in S3) for w in K}
    ck(conj==keys)
    # V4 acts freely/transitively on sections, and the coordinate difference is a coboundary.
    for w in K:
        sw={q:mul(mul(w,base[q]),inv(w)) for q in S3}
        for q in S3:
            d=mul(sw[q],inv(base[q]))
            expected=mul(w,act3_on_v4(q,w,base)) # w^{-1}=w in V4
            ck(d==expected and d in K)
    # Action on three nonzero V4 vectors is faithful S3 = GL(2,2).
    nz=[v for v in K if v!=I4]
    action=[]
    for q in S3:
        perm=tuple(nz.index(act3_on_v4(q,v,base)) for v in nz)
        action.append(perm)
    ck(len(set(action))==6 and set(action)==set(S3))
    return base,nz

# C3 twisted H1 on a bouquet of beta loops with C2 holonomy vector h.
def c3_delta(beta,h,b):
    return tuple(((1-(-1 if h[i] else 1))*b)%3 for i in range(beta))
def c3_orbits(beta,h):
    C=list(product(range(3),repeat=beta))
    B={c3_delta(beta,h,b) for b in range(3)}
    unseen=set(C); orbits=[]
    while unseen:
        a=min(unseen); O={tuple((a[i]+d[i])%3 for i in range(beta)) for d in B}
        ck(O<=unseen); unseen-=O; orbits.append(O)
    return orbits

def c3_checks():
    for beta in range(0,6):
      for h in product(range(2),repeat=beta):
        O=c3_orbits(beta,h)
        d=0 if beta==0 else (beta if not any(h) else beta-1)
        ck(len(O)==3**d)
        # inversion descends to quotient; full-gauge orbit count after residual C2.
        reps=[min(o) for o in O]; idx={a:i for i,o in enumerate(O) for a in o}
        seen=set(); full=0
        for i,r in enumerate(reps):
            if i in seen: continue
            neg=tuple((-x)%3 for x in r); j=idx[neg]
            seen|={i,j}; full+=1
        expected=1 if d==0 else 1+(3**d-1)//2
        ck(full==expected)
    # minimal same-L1/different-L2: beta=1,h=0 has zero and nonzero classes.
    O=c3_orbits(1,(0,)); ck(len(O)==3)
    zero=next(i for i,o in enumerate(O) if (0,) in o)
    nonzero=[i for i,o in enumerate(O) if (1,) in o or (2,) in o]
    ck(len(nonzero)==2 and zero not in nonzero)

# V4 as F2^2. Encode I4 and the three nonzero kernel elements by 0..3;
# addition is group multiplication in K.
def v_index(v,nz): return 0 if v==I4 else 1+nz.index(v)
def v_el(i,nz): return I4 if i==0 else nz[i-1]
def v_add(i,j,nz): return v_index(mul(v_el(i,nz),v_el(j,nz)),nz)
def v_act(q,i,sec,nz): return v_index(act3_on_v4(q,v_el(i,nz),sec),nz)
def v_delta(gs,b,sec,nz):
    # In characteristic 2, b - g.b = b + g.b.
    return tuple(v_add(b,v_act(g,b,sec,nz),nz) for g in gs)
def v_orbits(gs,sec,nz):
    beta=len(gs); C=list(product(range(4),repeat=beta)); B={v_delta(gs,b,sec,nz) for b in range(4)}
    unseen=set(C); orbits=[]
    while unseen:
        a=min(unseen); O={tuple(v_add(a[i],d[i],nz) for i in range(beta)) for d in B}
        ck(O<=unseen); unseen-=O; orbits.append(O)
    return orbits,B

def fixed_dim(gs,sec,nz):
    fixed=[i for i in range(4) if all(v_act(g,i,sec,nz)==i for g in gs)]
    # fixed set is a vector subspace of size 1,2,4.
    return {1:0,2:1,4:2}[len(fixed)]

def v4_checks(sec,nz):
    for beta in range(0,4):
      for gs in product(S3,repeat=beta):
        O,B=v_orbits(gs,sec,nz)
        if beta==0: d=0
        else: d=2*beta-2+fixed_dim(gs,sec,nz)
        ck(len(O)==2**d)
        ck(len(B)==2**(0 if beta==0 else 2-fixed_dim(gs,sec,nz)))
    # one-loop exact 2/1/0 dimensions
    ident=I3
    trans=next(q for q in S3 if parity(q)==1)
    cyc=next(q for q in S3 if q!=I3 and parity(q)==0)
    dims=[]
    for g in (ident,trans,cyc):
        O,_=v_orbits((g,),sec,nz); dims.append((len(O)).bit_length()-1)
    ck(tuple(dims)==(2,1,0))
    # minimal same-L2/different-L3 with rho=identity.
    O,_=v_orbits((I3,),sec,nz); ck(len(O)==4)
    ck(any((0,) in o for o in O) and any((1,) in o for o in O))
    return dims

def carrier_regressions():
    # beta=(k-1)(k-2)/2+m for a!=b; equality has m=0.
    cases={
      "clean":(3,0,1),
      "single_pinch":(2,1,1),
      "multi_pinch":(3,2,3),
      "equality_beta0":(2,0,0),
      "equality_beta1":(3,0,1),
      "beta2":(3,1,2),
    }
    for name,(k,m,beta) in cases.items():
        ck((k-1)*(k-2)//2+m==beta,name)
        # C3 lift dimension checks for h=0/nonzero where possible.
        if beta==0:
            ck(len(c3_orbits(0,()))==1)
        else:
            ck(len(c3_orbits(beta,(0,)*beta))==3**beta)
            h=(1,)+(0,)*(beta-1)
            ck(len(c3_orbits(beta,h))==3**(beta-1))

def main():
    marked=s3_split_checks(); sec,nz=s4_section_checks(); c3_checks(); dims=v4_checks(sec,nz); carrier_regressions()
    print(
      f"PASS checks={N}; L1_to_L2=C3_twisted_H1; S3_sign_kernel=3; marked_split=canonical; "
      f"L2_to_L3=V4_twisted_H1; S4_kernel=4; sections=4_all_V4_gauge; "
      f"L3_one_loop_dims=id:{dims[0]},transposition:{dims[1]},3cycle:{dims[2]}; "
      "clean_single_multi_equality=PASS"
    )

if __name__=="__main__": main()

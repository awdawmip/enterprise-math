#!/usr/bin/env python3
from itertools import product, combinations
L=(0,1); P=tuple(product(L,repeat=2)); ORDER=("SYM","DOWN","UP","UNIT","XOR_REF")
checks=0
def ck(x,m):
    global checks; checks+=1
    if not x: raise AssertionError(m)
def sw(s): return s[1],s[0]
def mu(s): return s[0]^s[1]
for s in P:
    ck(sw(sw(s))==s,"sw2"); ck(mu(sw(s))==mu(s),"mu symmetry")
for h in L:
    ck(mu((h,0))==h and mu((0,h))==h,"unit compose")
def fams():
    for a in product((0,1),repeat=2):
        e=dict(zip(L,a))
        for b in product((0,1),repeat=4): yield e,dict(zip(P,b))
def laws(e,f):
    return {
      "SYM":all(f[s]==f[sw(s)] for s in P),
      "DOWN":all((not f[x,y]) or (e[x] and e[y]) for x,y in P),
      "UP":all((not(e[x] and e[y])) or f[x,y] for x,y in P),
      "UNIT":all(f[h,0]==e[h]==f[0,h] for h in L),
      "XOR_REF":all(f[s]==e[mu(s)] for s in P)}
def model(names):
    out=[]
    for e,f in fams():
        q=laws(e,f)
        if all(q[n] for n in names):
            out.append(((e[0],e[1]),tuple(f[s] for s in P)))
    return out
def local(names): return tuple(sorted({a for a,_ in model(names)}))
base=((0,0),(0,1),(1,0),(1,1))
expected={
 (): (64,base), ("SYM",):(32,base), ("DOWN",):(21,base), ("UP",):(33,base),
 ("UNIT",):(8,base), ("XOR_REF",):(4,base), ("DOWN","UP"):(4,base),
 ("DOWN","UNIT"):(4,((0,0),(1,0),(1,1))),
 ("UP","XOR_REF"):(3,((0,0),(1,0),(1,1))),
 ("DOWN","XOR_REF"):(2,((0,0),(1,1))),
 ORDER:(2,((0,0),(1,1)))}
for n,(c,l) in expected.items(): ck(len(model(n))==c,n); ck(local(n)==l,n)
table=[]
for r in range(6):
    for n in combinations(ORDER,r): table.append((n,len(model(n)),local(n)))
ck(len(table)==32,"32 packages")
for e,f in fams():
    q=laws(e,f); ind=all(f[x,y]==(e[x] and e[y]) for x,y in P)
    ck(ind==(q["DOWN"] and q["UP"]),"IND")
    if q["XOR_REF"]: ck(q["UNIT"] and q["SYM"],"xor implications")
    if ind: ck(q["SYM"],"ind symmetry")
for n in ORDER:
    vals=[laws(e,f)[n] for e,f in fams()]
    ck(any(vals) and not all(vals),n+" +/-")
ck(local(("DOWN","UNIT"))==((0,0),(1,0),(1,1)),"3 contracts")
ck(local(("DOWN","XOR_REF"))==((0,0),(1,1)),"constant")
ck(local(("DOWN",))==base and local(("XOR_REF",))==base,"minimal pair")
full=set(model(ORDER)); AF=((0,0),(0,0,0,0)); AT=((1,1),(1,1,1,1))
ck(full=={AF,AT},"residual pair")
ck([m for m in model(ORDER) if m[0][0]==1]==[AT],"normalization diagnostic")
print("PASS P000_EFFECTIVITY_COMPOSITION_CONSTRAINT_SPACE_EXACTLY_CLASSIFIED; "
      f"checks={checks}; baseline_families=64; q14_local_contracts=4; "
      "single_candidate_laws_reduce_q14_local_contracts=FALSE; "
      "DOWN_PLUS_UNIT_local_contracts=3; DOWN_PLUS_XOR_REF_local_contracts=2; "
      "full_structural_package_models=2; residual_models=ALL_FALSE|ALL_TRUE; "
      "residual_effectivity_information_bits=1; unique_rule_without_normalization=FALSE; "
      "normalization_E0_true_forces=ALL_TRUE")

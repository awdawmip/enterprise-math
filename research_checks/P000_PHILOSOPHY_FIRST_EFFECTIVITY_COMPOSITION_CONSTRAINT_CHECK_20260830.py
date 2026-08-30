#!/usr/bin/env python3
from itertools import product

CHECKS = 0

def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

OBJECTS = {"U": [()], "L": [0,1], "P": [(0,0),(0,1),(1,0),(1,1)]}
INDEX = {o:{x:i for i,x in enumerate(xs)} for o,xs in OBJECTS.items()}
def fn(src,dst,f): return (src,dst,tuple(INDEX[dst][f(x)] for x in OBJECTS[src]))
generators=set((o,o,tuple(range(len(xs)))) for o,xs in OBJECTS.items())
generators |= {
    fn("P","P",lambda x:(x[1],x[0])), fn("L","P",lambda h:(h,0)), fn("L","P",lambda h:(0,h)),
    fn("P","L",lambda x:x[0]), fn("P","L",lambda x:x[1]), fn("P","L",lambda x:x[0]^x[1]),
    fn("U","L",lambda _:0), fn("L","U",lambda _:()), fn("P","U",lambda _:())}
def compose(f,g):
    s,m,mf=f; m2,d,mg=g
    return None if m!=m2 else (s,d,tuple(mg[j] for j in mf))
morphisms=set(generators)
changed=True
while changed:
    changed=False
    cur=list(morphisms)
    for f in cur:
        for g in cur:
            h=compose(f,g)
            if h is not None and h not in morphisms:
                morphisms.add(h); changed=True
expected_hom={
    ("U","U"):1,("U","L"):1,("U","P"):1,("L","U"):1,("L","L"):2,("L","P"):3,
    ("P","U"):1,("P","L"):4,("P","P"):9}
check(len(morphisms)==23,"category size")
for pair,n in expected_hom.items(): check(sum(1 for f in morphisms if f[:2]==pair)==n,f"hom {pair}")

L=(0,1); P=((0,0),(0,1),(1,0),(1,1)); PIDX={p:i for i,p in enumerate(P)}
def law_flags(u,e1,e2):
    E1=lambda h:bool(e1[h]); E2=lambda p:bool(e2[PIDX[p]])
    return {
      "ROT_SWAP":all(E2((a,b))==E2((b,a)) for a,b in P),
      "RESTRICTION":all((not E2((a,b))) or (E1(a) and E1(b)) for a,b in P),
      "GLUE":all((not(E1(a) and E1(b))) or E2((a,b)) for a,b in P),
      "NEUTRAL_REFINEMENT":all(E2((h,0))==E1(h)==E2((0,h)) for h in L),
      "FUSION_FORWARD":all((not E2((a,b))) or E1(a^b) for a,b in P),
      "FUSION_BACKWARD":all((not E1(a^b)) or E2((a,b)) for a,b in P),
      "UNIT_NATURALITY":bool(u)==E1(0), "UNIT_TRUE":bool(u)}
assignments=[(u,e1,e2,law_flags(u,e1,e2)) for u in (0,1) for e1 in product((0,1),repeat=2) for e2 in product((0,1),repeat=4)]
check(len(assignments)==128,"assignment universe")

bundles={
 "NO_LAWS":(),
 "ROTATION_ONLY":("ROT_SWAP",),
 "INDEPENDENT_PRODUCT":("ROT_SWAP","RESTRICTION","GLUE"),
 "PRODUCT_PLUS_NEUTRAL_REFINEMENT":("ROT_SWAP","RESTRICTION","GLUE","NEUTRAL_REFINEMENT"),
 "PRODUCT_NEUTRAL_PLUS_FUSION_FORWARD":("ROT_SWAP","RESTRICTION","GLUE","NEUTRAL_REFINEMENT","FUSION_FORWARD"),
 "LOWER_NATURALITY_PLUS_EFFECTIVE_UNIT":("ROT_SWAP","RESTRICTION","GLUE","NEUTRAL_REFINEMENT","FUSION_FORWARD","UNIT_NATURALITY","UNIT_TRUE"),
 "FULL_TWO_SIDED_REFINEMENT":("ROT_SWAP","RESTRICTION","GLUE","NEUTRAL_REFINEMENT","FUSION_FORWARD","FUSION_BACKWARD"),
 "FULL_TWO_SIDED_PLUS_EFFECTIVE_UNIT":("ROT_SWAP","RESTRICTION","GLUE","NEUTRAL_REFINEMENT","FUSION_FORWARD","FUSION_BACKWARD","UNIT_NATURALITY","UNIT_TRUE"),
 "MIN_UNIQUE_CORE":("RESTRICTION","FUSION_BACKWARD","UNIT_NATURALITY","UNIT_TRUE")}
expected={
 "NO_LAWS":(128,((0,0),(0,1),(1,0),(1,1))), "ROTATION_ONLY":(64,((0,0),(0,1),(1,0),(1,1))),
 "INDEPENDENT_PRODUCT":(8,((0,0),(0,1),(1,0),(1,1))), "PRODUCT_PLUS_NEUTRAL_REFINEMENT":(6,((0,0),(1,0),(1,1))),
 "PRODUCT_NEUTRAL_PLUS_FUSION_FORWARD":(6,((0,0),(1,0),(1,1))), "LOWER_NATURALITY_PLUS_EFFECTIVE_UNIT":(2,((1,0),(1,1))),
 "FULL_TWO_SIDED_REFINEMENT":(4,((0,0),(1,1))), "FULL_TWO_SIDED_PLUS_EFFECTIVE_UNIT":(1,((1,1),)), "MIN_UNIQUE_CORE":(1,((1,1),))}
for name,req in bundles.items():
    good=[a for a in assignments if all(a[3][x] for x in req)]; loc=tuple(sorted({a[1] for a in good}))
    check((len(good),loc)==expected[name],f"bundle {name}")

law_names=("ROT_SWAP","RESTRICTION","GLUE","NEUTRAL_REFINEMENT","FUSION_FORWARD","FUSION_BACKWARD","UNIT_NATURALITY","UNIT_TRUE")
spectrum={}; unique_masks=[]
for mask in range(256):
    req=tuple(law_names[i] for i in range(8) if (mask>>i)&1)
    good=[a for a in assignments if all(a[3][x] for x in req)]; loc=tuple(sorted({a[1] for a in good}))
    spectrum[loc]=spectrum.get(loc,0)+1
    if loc==((1,1),): unique_masks.append(mask)
check(spectrum=={((1,1),):16,((0,0),(1,1)):48,((1,0),(1,1)):48,((0,0),(1,0),(1,1)):54,((0,0),(0,1),(1,0),(1,1)):90},"law lattice spectrum")
minimal=[m for m in unique_masks if not any(n!=m and (n&m)==n for n in unique_masks)]
check(len(minimal)==1,"unique minimal forcing bundle")
check(tuple(law_names[i] for i in range(8) if (minimal[0]>>i)&1)==("RESTRICTION","FUSION_BACKWARD","UNIT_NATURALITY","UNIT_TRUE"),"minimal core")

A=(1,(1,0),(1,0,0,0)); B=(1,(1,1),(1,1,1,1)); lower=bundles["LOWER_NATURALITY_PLUS_EFFECTIVE_UNIT"]
for label,x in (("A",A),("B",B)): check(all(law_flags(*x)[z] for z in lower),f"matched {label}")
check(A[1][1]!=B[1][1],"matched systems disagree at H=1")
check(not law_flags(*A)["FUSION_BACKWARD"] and law_flags(*B)["FUSION_BACKWARD"],"strong law discriminator")

w=(1,(1,0),(1,0,0,1)); f=law_flags(*w); check(f["FUSION_BACKWARD"] and f["UNIT_NATURALITY"] and f["UNIT_TRUE"] and not f["RESTRICTION"],"drop restriction")
f=law_flags(*A); check(f["RESTRICTION"] and f["UNIT_NATURALITY"] and f["UNIT_TRUE"] and not f["FUSION_BACKWARD"],"drop backward")
w=(0,(0,0),(0,0,0,0)); f=law_flags(*w); check(f["RESTRICTION"] and f["FUSION_BACKWARD"] and not(f["UNIT_NATURALITY"] and f["UNIT_TRUE"]),"drop unit")

print(f"PASS P000_Q17_EFFECTIVITY_COMPOSITION; checks={CHECKS}; category_morphisms=23; assignments=128; lower_local_selectors=10,11; full_two_sided_no_unit=00,11; full_two_sided_plus_unit=11; minimal_unique_core=restriction+fusion_backward+effective_unit; matched_lower_systems=trivial_only_vs_all_effective; law_lattice_families=5")

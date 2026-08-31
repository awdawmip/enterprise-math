#!/usr/bin/env python3
import json
from itertools import permutations, product

TRI=((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))
FCC_DIRS=[]
for zero in range(3):
    nz=[i for i in range(3) if i!=zero]
    for a in (-1,1):
        for b in (-1,1):
            v=[0,0,0]; v[nz[0]]=a; v[nz[1]]=b; FCC_DIRS.append(tuple(v))
FCC_DIRS=tuple(sorted(set(FCC_DIRS)))

FCC_R={(-1,-1,0),(-1,0,-1),(-1,0,1),(-1,1,0),(0,-2,-2),(0,-1,-1),(0,-1,1),(0,0,0),(0,1,-1),(0,1,1),(0,2,0),(1,-1,0),(1,0,-1),(1,0,1),(1,1,0),(1,2,-1),(1,2,1),(2,0,0),(2,1,-1),(2,1,1),(2,2,0)}
HCP_R={(-1,0,-1),(-1,0,0),(-1,0,1),(-1,1,0),(0,-2,-1),(0,-1,-1),(0,-1,0),(0,-1,1),(0,0,-1),(0,0,0),(0,0,1),(0,1,0),(1,-1,-1),(1,-1,0),(1,-1,1),(1,0,-1),(1,0,0),(1,0,1),(1,1,0),(2,-1,0),(2,0,0)}


def fcc_n(p):
    x,y,z=p
    return tuple((x+a,y+b,z+c) for a,b,c in FCC_DIRS)


def hcp_n(p):
    i,j,k=p
    out=[(i+a,j+b,k) for a,b in TRI]
    off=((0,0),(-1,0),(0,-1)) if k%2==0 else ((0,0),(1,0),(0,1))
    for dk in (-1,1): out += [(i+a,j+b,k+dk) for a,b in off]
    return tuple(out)


def frontier(C,nbr):
    C=set(C); F=set()
    for p in C: F.update(nbr(p))
    return F-C


def weight(C,x,nbr):
    C=set(C); return sum(q in C for q in nbr(x))


def connected(C,nbr):
    C=set(C); seen={next(iter(C))}; stack=list(seen)
    while stack:
        p=stack.pop()
        for q in nbr(p):
            if q in C and q not in seen: seen.add(q); stack.append(q)
    return seen==C


def g0(C,nbr):
    F=frontier(C,nbr); W={x:weight(C,x,nbr) for x in F}; E=set()
    for x in F:
        for y in nbr(x):
            if y in F and x<y: E.add((x,y))
    return F,W,E


def same_g0(C1,C2,h1,h2,nbr):
    F1,W1,E1=g0(C1,nbr); F2,W2,E2=g0(C2,nbr)
    if F1-{h1} != F2-{h2}: return False
    mp=lambda x: h2 if x==h1 else x
    if any(W1[x]!=W2[mp(x)] for x in F1): return False
    return {tuple(sorted((mp(a),mp(b)))) for a,b in E1}==E2


FCC_OPS=tuple((p,s) for p in permutations(range(3)) for s in product((-1,1),repeat=3))
def fcc_apply(x,op):
    p,s=op; return tuple(s[i]*x[p[i]] for i in range(3))
def fcc_canon(S):
    best=None
    for op in FCC_OPS:
        pts=sorted(fcc_apply(x,op) for x in S); a=pts[0]
        key=tuple(sorted((x-a[0],y-a[1],z-a[2]) for x,y,z in pts))
        best=key if best is None or key<best else best
    return best


def r120(p):
    i,j,k=p; return (-i-j-(k&1),i,k)
def hcp_apply(p,op):
    r,swap,href,phase=op
    for _ in range(r): p=r120(p)
    i,j,k=p
    if swap: i,j=j,i
    if href: k=-k
    if phase: i,j,k=-i,-j,k+1
    return (i,j,k)
HCP_OPS=tuple(product(range(3),(0,1),(0,1),(0,1)))
def hcp_canon(S):
    best=None
    for op in HCP_OPS:
        pts=[hcp_apply(x,op) for x in S]
        mi=min(x for x,_,_ in pts); mj=min(y for _,y,_ in pts); mk=min(z for _,_,z in pts)
        tz=mk if mk%2==0 else mk-1
        key=tuple(sorted((x-mi,y-mj,z-tz) for x,y,z in pts))
        best=key if best is None or key<best else best
    return best


def check(world,R,h1,h2,nbr,canon):
    C1=R-{h1}; C2=R-{h2}; FR=frontier(R,nbr)
    F1,W1,E1=g0(C1,nbr); F2,W2,E2=g0(C2,nbr)
    assert len(R)==21 and len(C1)==len(C2)==20
    assert len(nbr(h1))==len(nbr(h2))==12
    assert set(nbr(h1))<=R and set(nbr(h2))<=R
    assert connected(C1,nbr) and connected(C2,nbr)
    assert F1-{h1}==FR and F2-{h2}==FR
    assert W1[h1]==W2[h2]==12
    assert all(h1 not in e for e in E1) and all(h2 not in e for e in E2)
    assert same_g0(C1,C2,h1,h2,nbr)
    assert canon(F1)!=canon(F2) and canon(C1)!=canon(C2)
    for x in FR: assert same_g0(C1|{x},C2|{x},h1,h2,nbr)
    assert g0(C1|{h1},nbr)==g0(R,nbr)
    assert g0(C2|{h2},nbr)==g0(R,nbr)
    return {
      "world":world,"base_R_size":21,"cluster_size":20,"outer_frontier_size":len(FR),
      "G0_vertices":len(F1),"G0_edges":len(E1),"surface_weight_sum":sum(W1.values()),
      "hole_weight":12,"hole_frontier_degree":0,"same_G0":True,
      "native_frontier_equivalent":False,"native_cluster_equivalent":False,
      "matched_outer_action_checks":len(FR),"matched_cavity_action_check":True,
      "one_step_G0_bisimulation":True
    }


def main():
    out={"schema":"ENTERPRISE_MATH_R043C1_CAVITY_COLLISION_CERT_V1","task_id":"RS-R043C1-NATIVE-SLOT-COMPLETION-G0-INJECTIVITY","researcher_id":"EM-R043C1-7D91A4","worlds":[check("FCC",FCC_R,(0,0,0),(1,1,0),fcc_n,fcc_canon),check("HCP",HCP_R,(0,0,0),(1,0,0),hcp_n,hcp_canon)],"theorem_boundary":{"pi_raw_native_slot_injectivity":"KILLED_BY_REALIZABLE_COLLISION","constructed_collision_future":"ALL_HORIZON_G0_TRANSITION_EQUIVALENT_BY_SHIELDED_CAVITY_INDUCTION","global_G0_stationary_sufficiency":"NOT_PROVED_OR_KILLED_BY_THIS_CERTIFICATE"}}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__": main()

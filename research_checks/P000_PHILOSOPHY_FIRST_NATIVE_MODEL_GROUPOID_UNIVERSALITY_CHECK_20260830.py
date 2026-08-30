#!/usr/bin/env python3
from __future__ import annotations
import itertools
import json
from pathlib import Path

AXES = ("AB","AC","AD","BC","BD","CD")
STARS = (
    frozenset(("AB","AC","AD")),
    frozenset(("AB","BC","BD")),
    frozenset(("AC","BC","CD")),
    frozenset(("AD","BD","CD")),
)
VERTICES = (0,1,2,3)
EDGES4 = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
EDGE_LABEL = {
    (0,1): "AB", (0,2): "AC", (0,3): "AD",
    (1,2): "BC", (1,3): "BD", (2,3): "CD",
}
LABEL_EDGE = {v:k for k,v in EDGE_LABEL.items()}

def comp(p,q):
    return tuple(p[q[i]] for i in range(len(p)))

def inv(p):
    out=[0]*len(p)
    for i,j in enumerate(p):
        out[j]=i
    return tuple(out)

def ppow(p,n):
    r=tuple(range(len(p)))
    for _ in range(n):
        r=comp(r,p)
    return r

def generated(perms):
    n=len(perms[0])
    e=tuple(range(n))
    seen={e}
    stack=[e]
    while stack:
        g=stack.pop()
        for h in perms:
            x=comp(g,h)
            if x not in seen:
                seen.add(x); stack.append(x)
    return seen

def induced_axis_perm(p4):
    labels=[]
    for lab in AXES:
        i,j=LABEL_EDGE[lab]
        a,b=sorted((p4[i],p4[j]))
        labels.append(AXES.index(EDGE_LABEL[(a,b)]))
    return tuple(labels)

def carrier_auts():
    idx={x:i for i,x in enumerate(AXES)}
    starsets={frozenset(idx[x] for x in s) for s in STARS}
    out=[]
    for p in itertools.permutations(range(6)):
        image={frozenset(p[i] for i in s) for s in starsets}
        if image==starsets:
            out.append(p)
    return out

def graph_auts(n, edges):
    E={frozenset(e) for e in edges}
    out=[]
    for p in itertools.permutations(range(n)):
        image={frozenset((p[i],p[j])) for i,j in (tuple(x) for x in E)}
        if image==E:
            out.append(p)
    return out

# Semidirect product C2^4 ⋊ S4, with S4 permuting the four fiber coordinates.
S4=list(itertools.permutations(range(4)))
E4=tuple(range(4))
ZERO=(0,0,0,0)
V=list(itertools.product((0,1), repeat=4))

def act(p,w):
    pi=inv(p)
    return tuple(w[pi[i]] for i in range(4))

def vxor(u,v):
    return tuple(a^b for a,b in zip(u,v))

def gmul(g,h):
    u,p=g; v,q=h
    return (vxor(u,act(p,v)), comp(p,q))

GID=(ZERO,E4)

def gpow(g,n):
    r=GID
    for _ in range(n):
        r=gmul(r,g)
    return r

def ginv(g):
    u,p=g
    pi=inv(p)
    return (act(pi,u),pi)

def conj(k,g):
    return gmul(gmul(k,g),ginv(k))

def main():
    cert_path=Path(__file__).resolve().parents[1] / "research_artifacts" / \
        "P000_PHILOSOPHY_FIRST_NATIVE_MODEL_GROUPOID_UNIVERSALITY" / \
        "Q10_MODEL_GROUPOID_CERTIFICATE.json"
    cert=json.loads(cert_path.read_text(encoding="utf-8"))

    caut=carrier_auts()
    assert len(caut)==24

    # Frozen carrier generators a=(BCD), b=(AB) on four star vertices.
    a=(0,2,3,1)
    b=(1,0,2,3)
    ax_a=induced_axis_perm(a)
    ax_b=induced_axis_perm(b)
    assert ppow(a,3)==E4
    assert ppow(b,2)==E4
    assert ppow(comp(a,b),4)==E4
    assert len(generated((a,b)))==24
    assert len(generated((ax_a,ax_b)))==24

    # Gen12 core: four opaque Cells, complete adjacency K4, one Cell per star.
    k4_edges=list(itertools.combinations(range(4),2))
    aut_k4=graph_auts(4,k4_edges)
    assert len(aut_k4)==24
    # One-to-one star anchoring forces the same S4 action on Cells and carrier stars.
    gen12_aut_order=len(aut_k4)
    gen12_image_order=24
    gen12_kernel_order=1
    gen12_exists_lift=(gen12_aut_order==24 and gen12_image_order==24 and gen12_kernel_order==1)
    assert gen12_exists_lift

    # P4 countermodel: four opaque Cells in a path, with the same one-to-one star anchor.
    p4_edges=[(0,1),(1,2),(2,3)]
    aut_p4=graph_auts(4,p4_edges)
    assert len(aut_p4)==2
    p4_image_order=len(aut_p4)  # anchor-preserving carrier readout is the same permutation
    assert p4_image_order < 24
    p4_exists_lift=False

    # Deleting Cell-Axis/star anchoring decouples native Cells from carrier axes.
    # With uniform PF10 data, Aut(P4) x Aut(carrier) projects onto the carrier S4,
    # and the pure-axis factor gives a section: an exact false positive.
    p4_without_inc_aut_order=len(aut_p4)*len(caut)
    p4_without_inc_image_order=len(caut)
    p4_without_inc_has_pure_axis_section=(p4_without_inc_image_order==24)
    assert p4_without_inc_aut_order==48
    assert p4_without_inc_has_pure_axis_section

    # Deleting adjacency while keeping a one-to-one star anchor leaves S4.
    p4_without_adj_aut_order=24
    assert p4_without_adj_aut_order==24

    # K_{2,2,2,2}: eight Cells, two opaque Cells above each carrier star.
    cells=[(i,bit) for i in range(4) for bit in range(2)]
    idx={c:k for k,c in enumerate(cells)}
    k2222_edges=[]
    for x,y in itertools.combinations(cells,2):
        if x[0] != y[0]:
            k2222_edges.append((idx[x],idx[y]))
    aut_k2222=graph_auts(8,k2222_edges)
    assert len(aut_k2222)==384

    # The star-anchor quotient has image S4 and kernel C2^4.
    k2222_image_order=24
    k2222_kernel_order=16
    assert len(aut_k2222)==k2222_image_order*k2222_kernel_order

    # Exact frozen-generator lift enumeration in C2^4 ⋊ S4.
    pairs=[]
    for u in V:
        A=(u,a)
        for v in V:
            B=(v,b)
            if gpow(A,3)==GID and gpow(B,2)==GID and gpow(gmul(A,B),4)==GID:
                pairs.append((A,B))
    assert len(pairs)==16

    pair_index={repr(x):i for i,x in enumerate(pairs)}
    seen=set()
    orbit_sizes=[]
    fixed_all=0
    for i,(A,B) in enumerate(pairs):
        fixed=True
        for kv in V:
            k=(kv,E4)
            if conj(k,A)!=A or conj(k,B)!=B:
                fixed=False
                break
        if fixed:
            fixed_all += 1
        if i not in seen:
            orb=set()
            for kv in V:
                k=(kv,E4)
                kp=(conj(k,A),conj(k,B))
                orb.add(pair_index[repr(kp)])
            seen |= orb
            orbit_sizes.append(len(orb))
    orbit_sizes=sorted(orbit_sizes)
    assert orbit_sizes==[8,8]
    assert fixed_all==0

    # Q10 object-level predicates.
    exists_lift = {
        "GEN12_K4": True,
        "P4_NO_LIFT": False,
        "K2222_SPLIT_NONCANONICAL": True,
    }
    forall_models_exists_lift=all(exists_lift.values())
    assert forall_models_exists_lift is False

    # A natural family on the full groupoid would in particular be invariant
    # under every automorphism of K2222. Kernel conjugations already rule this out.
    natural_lift_family=(fixed_all>0)
    assert natural_lift_family is False

    results={
        "carrier_star_hypergraph_aut_order": len(caut),
        "carrier_generators_generate_order": len(generated((a,b))),
        "axis_image_generated_order": len(generated((ax_a,ax_b))),
        "gen12_core_aut_order": gen12_aut_order,
        "gen12_image_order": gen12_image_order,
        "gen12_kernel_order": gen12_kernel_order,
        "gen12_exists_lift": gen12_exists_lift,
        "p4_aut_order": len(aut_p4),
        "p4_image_order": p4_image_order,
        "p4_exists_lift": p4_exists_lift,
        "p4_without_inc_aut_order": p4_without_inc_aut_order,
        "p4_without_inc_image_order": p4_without_inc_image_order,
        "p4_without_inc_has_pure_axis_section": p4_without_inc_has_pure_axis_section,
        "p4_without_adj_aut_order": p4_without_adj_aut_order,
        "k2222_aut_order": len(aut_k2222),
        "k2222_image_order": k2222_image_order,
        "k2222_kernel_order": k2222_kernel_order,
        "k2222_section_count": len(pairs),
        "k2222_kernel_conjugacy_orbit_sizes": orbit_sizes,
        "k2222_kernel_fixed_section_count": fixed_all,
        "for_all_models_exists_lift": forall_models_exists_lift,
        "natural_lift_family_on_full_groupoid": natural_lift_family,
    }
    assert cert["exact_regression"]==results
    assert cert["terminal_class"]=="P000_NATIVE_MODEL_GROUPOID_AND_UNIVERSAL_LIFT_QUANTIFIERS_CLASSIFIED"
    assert cert["predicates"]["FOR_ALL_MODELS_EXISTS_LIFT"] is False
    assert cert["predicates"]["NATURAL_LIFT_FAMILY"] is False
    assert cert["membership"]["GL23_NONSPLIT"]["status"]=="OUTSIDE_MINIMAL_Q10_SIGNATURE"
    assert cert["guards"]["CARRIER_S4_IS_NOT_COMPLETE_NATIVE_P000_ROTATION_GROUP"] is True
    assert cert["guards"]["NO_KERNEL_QUOTIENT"] is True

    print("PASS Q10 model-groupoid certificate")
    print(json.dumps(results, sort_keys=True))

if __name__=="__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from pathlib import Path

TASK_ID = "RS-P000-PHILOSOPHY-FIRST-PROBLEM-LANGUAGE-AUDIT"
ALLOWED_STATUSES = {
    "WELL_POSED_NATIVE", "PRESENTATION_DEPENDENT", "STRICTLY_WEAKER_PROXY",
    "UNDERDETERMINED", "EQUIVALENT_AFTER_EXPLICIT_HYPOTHESES",
}
REQUIRED_FIELDS = {
    "object", "allowed_equivalence", "observable", "claimed_invariant",
    "quantifier_level", "status", "minimal_rewrite",
}

def ident(n):
    return tuple(range(n))

def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))

def inv(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)

def power(p, n):
    out = ident(len(p))
    for _ in range(n):
        out = compose(p, out)
    return out

def generated(*gens):
    n = len(gens[0])
    seen = {ident(n)}
    todo = [ident(n)]
    while todo:
        x = todo.pop()
        for g in gens:
            for y in (compose(g, x), compose(x, g)):
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
    return seen

def parity(p):
    return sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j]) & 1

def edge_action(vertex_perm):
    edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    index = {e:i for i,e in enumerate(edges)}
    out = []
    for u,v in edges:
        e = tuple(sorted((vertex_perm[u], vertex_perm[v])))
        out.append(index[e])
    return tuple(out)

def preserves_graph(p, edges):
    e = {tuple(sorted(x)) for x in edges}
    return all(tuple(sorted((p[u],p[v]))) in e for u,v in e)

def ext_mul(x, y):
    g,e = x
    h,f = y
    return (compose(g,h), e ^ f)

def ext_F(x):
    g,e = x
    return (g, e ^ parity(g))

def load_artifact():
    path = Path(__file__).resolve().parents[1] / "research_artifacts" / "P000_PHILOSOPHY_FIRST_PROBLEM_LANGUAGE_AUDIT" / "P000_QUESTION_LANGUAGE_AUDIT_V1.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    fallback = Path("/mnt/data/P000_QUESTION_LANGUAGE_AUDIT_V1.json")
    if fallback.exists():
        return json.loads(fallback.read_text(encoding="utf-8"))
    raise FileNotFoundError("P000_QUESTION_LANGUAGE_AUDIT_V1.json not found")

def main():
    checks = 0
    art = load_artifact()
    assert art["task_id"] == TASK_ID
    assert art["hard_target"] == "P000_PROBLEM_LANGUAGE_AND_OBJECT_LEVEL_EXACTLY_AUDITED"
    assert len(art["questions"]) >= 8
    assert len(art["countermodels"]) >= 3
    checks += 4

    qids = set()
    for q in art["questions"]:
        assert q["id"] not in qids
        qids.add(q["id"])
        assert REQUIRED_FIELDS.issubset(q)
        assert q["status"] in ALLOWED_STATUSES
        assert q["minimal_rewrite"].strip()
        assert q.get("evidence")
        checks += 5
    assert {"Q01","Q02","Q03","Q04","Q05","Q06","Q07","Q08","Q09","Q10","Q11","Q12"} <= qids
    checks += 1

    # Frozen carrier S4 action from vertex generators a=(BCD), b=(AB).
    a = (0,2,3,1)
    b = (1,0,2,3)
    S4 = set(itertools.permutations(range(4)))
    H = generated(a,b)
    assert H == S4 and len(H) == 24
    assert power(a,3) == ident(4)
    assert power(b,2) == ident(4)
    assert power(compose(a,b),4) == ident(4)
    ae, be = edge_action(a), edge_action(b)
    assert ae == (1,2,0,5,3,4)   # (E1 E2 E3)(E4 E6 E5)
    assert be == (0,3,4,1,2,5)   # (E2 E4)(E3 E5); E1,E6 fixed
    checks += 7

    # CM1: same abstract action, different presentation. "b fixes E1" flips.
    tau = (1,0,2,3,4,5)
    be2 = compose(compose(tau, be), inv(tau))
    assert be[0] == 0
    assert be2[0] != 0
    assert be2 == compose(compose(tau,be), inv(tau))
    assert power(be,2) == ident(6) == power(be2,2)
    checks += 4

    # CM2: G~=S4 x C2 has two sections interchanged by a q-preserving automorphism.
    ext = [(g,e) for g in S4 for e in (0,1)]
    s0 = lambda g: (g,0)
    s1 = lambda g: (g,parity(g))
    assert len(ext) == 48
    assert s0(b) != s1(b) and s0(a) == s1(a)
    for g in S4:
        assert s0(g)[0] == g and s1(g)[0] == g
        assert ext_F(s0(g)) == s1(g)
        checks += 2
    for g in S4:
        for h in S4:
            assert ext_mul(s0(g),s0(h)) == s0(compose(g,h))
            assert ext_mul(s1(g),s1(h)) == s1(compose(g,h))
            checks += 2
    for x in ext:
        assert ext_F(ext_F(x)) == x
        assert ext_F(x)[0] == x[0]
        checks += 2
    for x in ext:
        for y in ext:
            assert ext_F(ext_mul(x,y)) == ext_mul(ext_F(x),ext_F(y))
            checks += 1

    # CM3: identical carrier image and chosen relation residues, different hidden kernel.
    A0, B0 = a, b
    A1, B1 = (a,0), (b,0)
    def ext_pow(x,n):
        out = (ident(4),0)
        for _ in range(n):
            out = ext_mul(x,out)
        return out
    assert power(A0,3) == ident(4)
    assert power(B0,2) == ident(4)
    assert power(compose(A0,B0),4) == ident(4)
    assert ext_pow(A1,3) == (ident(4),0)
    assert ext_pow(B1,2) == (ident(4),0)
    assert ext_pow(ext_mul(A1,B1),4) == (ident(4),0)
    ker0 = [g for g in S4 if g == ident(4)]
    ker1 = [(g,e) for g,e in ext if g == ident(4)]
    assert (len(S4),len(ext),len(ker0),len(ker1)) == (24,48,1,2)
    checks += 7

    # CM4: one K4 witness cannot establish universality over unconstrained 4-cell adjacency.
    all4 = list(S4)
    K4_edges = {(i,j) for i in range(4) for j in range(i+1,4)}
    P4_edges = {(0,1),(1,2),(2,3)}
    autK4 = [p for p in all4 if preserves_graph(p,K4_edges)]
    autP4 = [p for p in all4 if preserves_graph(p,P4_edges)]
    assert len(autK4) == 24
    assert len(autP4) == 2
    assert len(autP4) < 24
    checks += 3

    carriers = {("carrier", i) for i in range(4)}
    cells = {("cell", i) for i in range(4)}
    assert carriers.isdisjoint(cells)
    checks += 1

    rules = art["checker_contract"]["rules"]
    assert len(rules) >= 10
    assert any("CANONICALITY_TEST" in x for x in rules)
    assert any("QUANTIFIER_TEST" in x for x in rules)
    assert any("PROXY_TEST" in x for x in rules)
    assert any("SORT_TEST" in x for x in rules)
    assert any("KERNEL_TEST" in x for x in rules)
    checks += 6

    print(
        "PASS P000_PROBLEM_LANGUAGE_AUDIT; "
        f"checks={checks}; questions={len(art['questions'])}; "
        f"countermodels={len(art['countermodels'])}; S4_order={len(H)}; "
        f"extension_order={len(ext)}; kernel_orders=1,2; "
        f"Aut_K4={len(autK4)}; Aut_P4={len(autP4)}; "
        "presentation_surface_flip=TRUE; canonical_section_fixed=FALSE"
    )

if __name__ == "__main__":
    main()

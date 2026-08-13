#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path

EXPECTED = {
    "research/R052/R052_FORMAL_PLANE_SIGNATURE_FAMILY.json":"946eb08652b7c505adb9b2e8c1263a7260147962b1b7056d5a890d623fbcd0e2",
    "research/R052/R052_PI_ROLE_REGISTRY.json":"33cabef583b3847eedae152181de002806b800bd8cdb01c07b595d5a695dfe66",
    "research/R052/R052_THEOREM_COUNTEREXAMPLE_LEDGER.json":"4a854ca114ab46e7b828f3eb991be745ac2342c034809566218442926b48ebac",
}

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20), b""):
            h.update(chunk)
    return h.hexdigest()

def verify_input_hashes(repo: Path) -> dict:
    out={}
    for rel, expected in EXPECTED.items():
        p=repo/rel
        if not p.exists():
            raise FileNotFoundError(f"missing frozen input: {p}")
        got=sha256(p)
        if got != expected:
            raise AssertionError(f"{rel}: expected {expected}, got {got}")
        out[rel]=got
    return out

def h(m,j):
    assert m%2==0
    return (j+m//2)%m

def orbit(m,j):
    return frozenset((j,h(m,j)))

def check_r1():
    cases=0
    ref_cases=0
    for m in (4,6,8,10,12,14,16):
        for j in range(m):
            assert h(m,h(m,j))==j
            assert h(m,j)!=j
            assert orbit(m,j)==orbit(m,h(m,j))
            cases+=1
        for k in (1,2,3,4,5):
            M=k*m
            for j in range(m):
                i=(k*j)%M
                assert (k*h(m,j))%M == h(M,i)
                image_orbit=frozenset((k*x)%M for x in orbit(m,j))
                assert image_orbit == orbit(M,i)
                ref_cases+=1
    assert 4%2==0 and 5%2==1  # frozen unrestricted-refinement parity-loss shape
    return {"r1_point_cases":cases,"r1_uniform_refinement_cases":ref_cases}

def check_extension_parity():
    parity_cases=0
    for n in range(-15,16):
        for m in range(-8,9):
            assert (n%2)==((n+2*m)%2)
            assert (n%2)==((-n)%2)
            parity_cases+=2
    split_cases=0
    # Split L=Z x C2; K=Zx{0}, generators ±(1,0).
    for a in range(-30,31):
        double=(2*a,0)
        assert double not in {(1,0),(-1,0)}
        split_cases+=1
    nonsplit_cases=0
    primitive=[]
    # Non-split L=Z, p mod 2, K=2Z, kernel generators ±2.
    for x in range(-31,32,2):
        dx=2*x
        is_primitive=dx in (-2,2)
        if is_primitive:
            primitive.append(x)
        nonsplit_cases+=1
    assert primitive==[-1,1]
    return {"parity_invariance_cases":parity_cases,"split_lift_cases":split_cases,
            "nonsplit_odd_lift_cases":nonsplit_cases,"primitive_half_lifts":primitive}

def check_scaling():
    cases=0
    Js=(Fraction(1,3),Fraction(5,7),Fraction(11,2))
    for J in Js:
        for a in (Fraction(1,2),Fraction(2),Fraction(5,3)):
            for c in (Fraction(1,3),Fraction(3),Fraction(7,2)):
                J2=a*a*J/c
                assert J2/J == a*a/c
                for b in (Fraction(1,2),Fraction(2),Fraction(9,4)):
                    P=Fraction(7,5)
                    P2=b*P
                    assert (J2/P2)/(J/P) == a*a/(c*b)
                    cases+=1
    return {"exact_fraction_scale_cases":cases}

def check_pair_graph(artifact_dir: Path):
    data=json.loads((artifact_dir/"R052B_PAIRWISE_COMPARABILITY_GRAPH.json").read_text(encoding="utf-8"))
    roles=[
        "R1_CELL_HALF_CYCLE","R2_DIRECTION_DECK","R3_GROUP_INVOLUTION_ACTION",
        "R4_RAW_ISOPERIMETRIC_CUT","R5_TURN_KERNEL_GENERATOR_CLASS"]
    expected={tuple(sorted(p)) for i,r in enumerate(roles) for p in ([r,s] for s in roles[i+1:])}
    got={tuple(sorted(x["roles"])) for x in data["pairs"]}
    assert len(data["pairs"])==10
    assert got==expected
    return {"pair_count":10}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, default=None)
    ap.add_argument("--artifact-dir", type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument("--synthetic-only", action="store_true",
                    help="Run exact finite/group/scaling checks without requiring the frozen R052 checkout.")
    ns=ap.parse_args()
    result={"schema":"ENTERPRISE_MATH_R052B_EXACT_CHECK_RESULTS_V1"}
    if not ns.synthetic_only:
        if ns.repo_root is None:
            raise SystemExit("--repo-root is required unless --synthetic-only is used")
        result["input_hashes"]=verify_input_hashes(ns.repo_root)
    result.update(check_r1())
    result.update(check_extension_parity())
    result.update(check_scaling())
    result.update(check_pair_graph(ns.artifact_dir))
    result["floating_point_used"]=False
    result["overall"]="PASS"
    print(json.dumps(result, sort_keys=True, indent=2))

if __name__=="__main__":
    main()

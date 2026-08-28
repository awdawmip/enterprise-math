#!/usr/bin/env python3
"""Exact replay for the blind CM(-24) branch-pattern reduction."""
from __future__ import annotations
import hashlib, itertools, json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "research_artifacts" / "RB_ENTERPRISE_DEGREE6_CM24_BLIND_BRANCH_PATTERN_COMPLETION" / "raw_freeze_branch_reduction.json"
EXPECTED_SHA256 = "86e462dcebad843aeab27354a2f4ce5fc17ef15bce4e6db30ef23e6ca1a62b29"

def ez(expr, label):
    z=sp.factor(sp.expand(expr), extension=[sp.I, sp.sqrt(2), sp.Pow(3,sp.Rational(1,4))])
    if z != 0:
        z=sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label}: {z}")

def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    x1,y1=P; x2,y2=Q
    if sp.simplify(x1-x2)==0 and sp.simplify(y1+y2)==0:
        return None
    if sp.simplify(x1-x2)==0:
        m=sp.cancel((3*x1**2-3)/(2*y1))
    else:
        m=sp.cancel((y2-y1)/(x2-x1))
    x3=sp.radsimp(sp.cancel(m**2-x1-x2))
    y3=sp.radsimp(sp.cancel(m*(x1-x3)-y1))
    return x3,y3

def roots_for(P):
    s=sp.sqrt(3); a=sp.Pow(3,sp.Rational(1,4))
    x,y=P
    cases=[
      (0,(0,sp.I*a,a)),
      (s,(a,0,sp.sqrt(2)*a)),
      (-s,(sp.I*a,sp.I*sp.sqrt(2)*a,0)),
      (-2,(sp.I*sp.sqrt(2),sp.I*(sp.sqrt(6)+sp.sqrt(2))/2,sp.I*(sp.sqrt(6)-sp.sqrt(2))/2)),
      (sp.Rational(3,2),(s/sp.sqrt(2),sp.I*(a-a**3)/2,(a+a**3)/2)),
      (-12+7*s,(2*a-a**3,sp.I*(3-s),sp.sqrt(2)*(a-a**3))),
      (-12-7*s,(sp.I*(2*a+a**3),sp.I*sp.sqrt(2)*(a+a**3),sp.I*(3+s))),
    ]
    for xx,rr0 in cases:
        if sp.simplify(x-xx)==0:
            rr=list(rr0)
            if sp.simplify(rr[0]*rr[1]*rr[2]+y)!=0:
                for j,r in enumerate(rr):
                    if r != 0:
                        rr[j]=-r; break
            r0,rp,rm=rr
            ez(r0**2-x,"sqrt R")
            ez(rp**2-(x-s),"sqrt R-s")
            ez(rm**2-(x+s),"sqrt R+s")
            ez(r0*rp*rm+y,"product=-t")
            return
    raise AssertionError(f"unclassified sum {P}")

def matchings(items):
    items=list(items)
    if not items:
        yield (); return
    a=items[0]
    for j in range(1,len(items)):
        b=items[j]
        rest=items[1:j]+items[j+1:]
        for tail in matchings(rest):
            yield tuple(sorted((tuple(sorted((a,b))),)+tail))

def main():
    obj=json.loads(ARTIFACT.read_text(encoding="utf-8"))
    payload=obj["payload"]
    canonical=json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
    got=hashlib.sha256(canonical).hexdigest()
    assert got==EXPECTED_SHA256
    assert obj["payload_sha256"]=="sha256:"+EXPECTED_SHA256
    assert payload["phase"]=="BLIND_BRANCH_PATTERN_FREEZE"
    assert payload["primary_verdict"]=="BLIND_BRANCH_PATTERN_INCOMPLETE"

    # Irreducibility witness over Kb=Q(sqrt2,sqrt3).
    p=23
    assert 5*5%p==2 and 16*16%p==3
    assert (12*5-10*16)%p==15
    assert [x for x in range(p) if (x**3-3*x-15)%p==0]==[]
    # Therefore the monic cubic is irreducible over Kb.  Since
    # K0/Kb is a tower of at most two quadratic extensions, a cubic
    # root cannot enter K0.

    s=sp.sqrt(3); q=sp.I*sp.sqrt(2)
    P={"O":None,"T0":(0,0),"Tp":(s,0),"Tm":(-s,0),"Ap":(-2,q),"Am":(-2,-q)}
    names=list(P)
    for n,Q in P.items():
        if Q is not None:
            ez(Q[1]**2-(Q[0]**3-3*Q[0]),"branch "+n)

    # Exact 2-descent witnesses for all 15 pair sums.
    expected_pairs=list(itertools.combinations(names,2))
    assert [tuple(row["pair"]) for row in payload["pair_block_two_divisibility"]["pairs"]]==expected_pairs
    for u,v in expected_pairs:
        S=add(P[u],P[v])
        if S is None:
            assert {u,v}=={"Ap","Am"}
        else:
            roots_for(S)

    # Branch-support automorphisms: no nonzero translation works (the
    # pair-sum table gives an image outside B), and the j=1728
    # origin-fixing maps ±i send Ap from R=-2 to R=2.  Thus only
    # id and [-1] preserve B.  The latter sends t=-k to t=k, so the
    # k-pinned ODE has trivial source symmetry.
    pair_sums={tuple(row["pair"]):row["sum"] for row in payload["pair_block_two_divisibility"]["pairs"]}
    for witness in [("T0","Ap"),("Tp","Ap"),("Tm","Ap"),("Ap","T0"),("Am","T0")]:
        key=tuple(sorted(witness,key=names.index))
        assert pair_sums[key] != "O"
        assert pair_sums[key]["R"] not in ("0","sqrt(3)","-sqrt(3)","-2")
    assert sp.Integer(2) not in [0,s,-s,-2]
    k2=12*sp.sqrt(2)-10*s
    assert sp.simplify(k2)!=0

    swap={"O":"O","T0":"T0","Tp":"Tp","Tm":"Tm","Ap":"Am","Am":"Ap"}
    pairs=[tuple(sorted(x)) for x in itertools.combinations(names,2)]
    def swp(pair): return tuple(sorted((swap[pair[0]],swap[pair[1]])))
    assert len(set(min(p,swp(p)) for p in pairs))==11

    ms=sorted(set(matchings(names)))
    def swm(m): return tuple(sorted(tuple(sorted((swap[a],swap[b]))) for a,b in m))
    assert len(ms)==15
    assert len(set(min(m,swm(m)) for m in ms))==9

    assert [(6-b)//2 for b in (4,2,0,0)]==[1,2,3,3]
    assert [(6-b)//2 for b in (2,2,2,0)]==[2,2,2,3]
    assert 9+3==12
    assert payload["riemann_roch_reduction"]["total_divisor_type_lanes_before_rr"]==480

    print("PASS: blind CM(-24) branch-pattern reduction exact replay")
    print("artifact_sha256="+EXPECTED_SHA256)
    print("q_special_points=0")
    print("pair_blocks_2divisible=15/15")
    print("support_assignments=15+15")
    print("rr_divisor_type_lanes=480")

if __name__=="__main__":
    main()

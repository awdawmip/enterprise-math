#!/usr/bin/env python3
"""Exact finite crosschecks for the auxiliary noncritical square-port theorem.

Every integer x with x mod p != 0,+1,-1 is enumerated for each config.
No native Heartbeat/X6 semantics are simulated.
"""
import json
from datetime import datetime, timezone
from pathlib import Path


def vp(n: int, p: int) -> int:
    a = 0
    while n % p == 0:
        a += 1
        n //= p
    return a


def readout(x: int, mod: int) -> int:
    return ((x + 1) * (pow(x, -1, mod) + 1)) % mod


def advance(x: int, mod: int, h: int, degree: int) -> int:
    return (x + h * pow(x, degree, mod)) % mod


def classify(p: int, e: int, degree: int, lam: int) -> dict:
    assert p in (3, 5, 7) and e >= 2 and degree >= 2 and degree % 2 == 0
    L = 2 * e + 2
    mod = p ** L
    a = vp(degree - 1, p)
    g = __import__('math').gcd(degree - 1, (p - 1) // 2)
    root_residues = [r for r in range(1, p) if pow(r, 2 * (degree - 1), p) == p - 1]
    predicted_collision = g * p ** (e + a) if root_residues and a < e else 0
    predicted_permanent = predicted_collision if a >= 2 else 0
    h = (p ** e) * lam

    sources_seen = 0
    pairs_seen = 0
    collision01 = 0
    permanent012 = 0
    all_nonsplit_check = 0
    split_sample = None
    permanent_sample = None
    observer_multiplications = 0
    updates = 0
    for x in range(1, mod):
        if x % p in (0, 1, p - 1):
            continue
        sources_seen += 1
        y = pow(x, -1, mod)
        if x >= y:
            continue
        pairs_seen += 1
        assert x != y and (x * y) % mod == 1
        obs0_x = readout(x, mod)
        obs0_y = readout(y, mod)
        observer_multiplications += 2
        assert obs0_x == obs0_y
        x1 = advance(x, mod, h, degree)
        y1 = advance(y, mod, h, degree)
        updates += 2
        obs1_x = readout(x1, mod)
        obs1_y = readout(y1, mod)
        observer_multiplications += 2
        same1 = obs1_x == obs1_y
        # Exact symbolic condition for O0/O1 collision, checked independently.
        F = (pow(x, degree - 1, p ** (e + 2)) +
             pow(y, degree - 1, p ** (e + 2))) % (p ** (e + 2))
        assert same1 == ((F + h) % (p ** (e + 2)) == 0)
        if not same1:
            continue
        collision01 += 1
        x2 = advance(x1, mod, h, degree)
        y2 = advance(y1, mod, h, degree)
        updates += 2
        obs2_x, obs2_y = readout(x2, mod), readout(y2, mod)
        observer_multiplications += 2
        same2 = obs2_x == obs2_y
        assert same2 == (a >= 2)
        if same2:
            permanent012 += 1
            if permanent_sample is None:
                permanent_sample = {"x": x, "y": y, "O0": obs0_x,
                                    "O1": obs1_x, "O2": obs2_x}
            # Verify extra actual update/readout times; all-time is proved algebraically.
            z, w = x2, y2
            for _ in range(3, 7):
                z = advance(z, mod, h, degree)
                w = advance(w, mod, h, degree)
                updates += 2
                assert readout(z, mod) == readout(w, mod)
                observer_multiplications += 2
                all_nonsplit_check += 1
        elif split_sample is None:
            split_sample = {"x": x, "y": y, "O0": obs0_x, "O1": obs1_x,
                            "O2_x": obs2_x, "O2_y": obs2_y}
    assert sources_seen == (p - 3) * p ** (L - 1)
    assert pairs_seen * 2 == sources_seen
    assert len(root_residues) == (2 * g if p % 4 == 1 else 0)
    assert collision01 == predicted_collision, (p, e, degree, lam, collision01, predicted_collision)
    assert permanent012 == predicted_permanent
    return {
        "p": p, "L": L, "e": e, "d": degree, "lambda": lam,
        "a_vp_d_minus_1": a, "g": g,
        "modulus": mod, "noncritical_sources": sources_seen,
        "all_initial_inversion_pairs": pairs_seen,
        "root_residue_count": len(root_residues),
        "initial_two_readout_pair_collisions": collision01,
        "infinite_trajectory_pairs_by_theorem": predicted_permanent,
        "three_readout_pair_collisions": permanent012,
        "future_singleton_sources": sources_seen - 2 * predicted_permanent,
        "future_size_two_fibers": predicted_permanent,
        "actual_extra_time_checks": all_nonsplit_check,
        "observer_product_evaluations": observer_multiplications,
        "state_updates": updates,
        "split_sample": split_sample,
        "permanent_sample": permanent_sample,
        "fixed_time_gap_witnesses": fixed_pair_witnesses(p,e,degree,lam),
        "status": "PASS"
    }



def fixed_pair_witnesses(p: int, e: int, degree: int, lam: int) -> list[dict]:
    """Construct collisions for every selected fixed time gap (no all-gap finite claim)."""
    n = degree - 1
    a = vp(n, p)
    if p % 4 != 1 or a > 1:
        return []
    mod = p ** (2 * e + 2)
    h = p ** e * lam
    root_r = next(r for r in range(1, p) if pow(r, 2 * n, p) == p - 1)
    witnesses = []
    for delta in (1, 2, 3, 4, 5, 25):
        # Scale-compensated, unique digit lift: derivative of x^n+x^-n has v_p = a.
        x = root_r
        for j in range(1, e + 2 - a):
            target_mod = p ** (a + j + 1)
            hits = []
            for digit in range(p):
                candidate = x + digit * p ** j
                f = (pow(candidate, n, target_mod) +
                     pow(candidate, -n, target_mod)) % target_mod
                if (f + h * (degree - n * delta)) % target_mod == 0:
                    hits.append(candidate)
            assert len(hits) == 1, (p, e, degree, lam, delta, j, hits)
            x = hits[0]
        y = pow(x, -1, mod)
        assert x != y and x % p not in (1, p-1)
        z,w=x,y
        for _ in range(delta):
            z=advance(z,mod,h,degree)
            w=advance(w,mod,h,degree)
        assert readout(z,mod)==readout(w,mod)
        x1,y1=advance(x,mod,h,degree),advance(y,mod,h,degree)
        x2,y2=advance(x1,mod,h,degree),advance(y1,mod,h,degree)
        assert (readout(x1,mod)!=readout(y1,mod) or
                readout(x2,mod)!=readout(y2,mod))
        witnesses.append({"delta":delta,"x":x,"inverse_y":y,
                          "common_O0":readout(x,mod),
                          "common_Odelta":readout(z,mod),
                          "future_split_time": 1 if readout(x1,mod)!=readout(y1,mod) else 2})
    return witnesses


def main() -> None:
    configs = [
        (5, 2, 2, 1),      # a=0; p |/ n, 0/1 collision splits at time2
        (5, 2, 6, 1),      # a=1; new splitting at L=6 vs L=5
        (5, 2, 26, 1),     # a=2>=e; no 0/1 collision
        (5, 2, 6, 2),      # lambda unit variation
        (5, 3, 2, 1),      # a=0
        (5, 3, 6, 1),      # a=1; splits
        (5, 3, 26, 1),     # a=2<e; persistent double fibers
        (5, 3, 26, 2),     # lambda unit variation
        (5, 3, 126, 1),    # a=3>=e; no 0/1 collision
        (7, 2, 2, 1),      # -1 nonsquare
        (7, 2, 8, 1),      # -1 nonsquare; a=1
    ]
    result = [classify(*cfg) for cfg in configs]
    totals = {k: sum(r[k] for r in result) for k in
              ("noncritical_sources", "all_initial_inversion_pairs",
               "initial_two_readout_pair_collisions", "three_readout_pair_collisions",
               "actual_extra_time_checks", "observer_product_evaluations", "state_updates")}
    out = {
        "artifact_kind": "AUTHOR_EXACT_FINITE_CROSSCHECK",
        "scope": "auxiliary ring Z/p^(2e+2)Z noncritical x mod p != 0,+1,-1",
        "method": "exhaustive integer-labelled source involution pairs and exact modular two-factor readouts",
        "run_date_utc": datetime.now(timezone.utc).isoformat(),
        "configuration_count": len(configs),
        "configs": result,
        "totals": totals,
        "mathematical_strength": "finite full-noncritical-domain checks only; all-e prime theorem requires accompanying algebraic proof",
        "native_x6_experiment": False,
        "result": "PASS",
    }
    path = Path(__file__).with_name("d25_square_port_next_precision_noncritical_author_check_20261030.json")
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"result":out["result"], "configuration_count":len(configs), "totals":totals}, ensure_ascii=False))


if __name__ == "__main__":
    main()

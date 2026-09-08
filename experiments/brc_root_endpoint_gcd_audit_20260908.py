"""Bounded endpoint-gcd observations on three pinned mathematical puzzles.

This audit also keeps separate D/U constructive families and compares root
and residual representations. It has no arbitrary-target or search interface.
"""
from __future__ import annotations

import argparse
from hashlib import sha1, sha256
from math import gcd
from pathlib import Path
from statistics import median
from time import perf_counter_ns
import json
import platform
import sys


INPUT_BLOB = "e56cfc8457e2398b5de3c90182c2b37824580ef3"
CORE_BLOB = "2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07"
SMALL_PRIME_HELPER_BLOB = "65f06c03038b2c95a875436c099f50f008700af3"
ROUNDS = 9
REPEATS = 8


def checked_text(path, blob):
    raw = path.read_bytes().replace(b"\r\n",b"\n").rstrip(b"\n")+b"\n"
    assert sha1(f"blob {len(raw)}\0".encode("ascii")+raw).hexdigest() == blob
    return raw.decode("utf-8")


def audit_residue_pair_cost(result, enterprise_root):
    """Verify the exact half-width identity on saved inputs, then time it."""
    checked_text(enterprise_root/"src"/"enterprise_math"/"core.py",CORE_BLOB)
    sys.path.insert(0,str(enterprise_root/"src"))
    from enterprise_math.core import integer_nth_root
    here = Path(__file__).resolve().parent
    original = json.loads(checked_text(here/"brc_public_rsa_fixed_predicates_20260908.json",INPUT_BLOB))

    def validate(n,values):
        for value in values:
            assert 1 <= value < n
            if value > 1:
                other,remainder = divmod(n,value)
                assert remainder == 0 and value*other == n
        return values

    def from_pair(r,gap):
        # This checks the exact domain without reconstructing the root or N.
        if r <= 0 or gap <= 0 or ((gap-r) & 3) != 3:
            raise ValueError("an odd nonsquare BRC residual pair is required")
        lower = gcd(r,gap-1) >> (1-(r & 1))
        upper = gcd(gap,r+1) >> (1-(gap & 1))
        return lower,upper

    def complete_root(case):
        n = case["n"]
        j = integer_nth_root(n,2)
        return validate(n,(gcd(n,j),gcd(n,j+1)))

    def prepared_root(case):
        return validate(case["n"],(gcd(case["n"],case["j"]),gcd(case["n"],case["j"]+1)))

    def complete_pair(case):
        n = case["n"]
        j = integer_nth_root(n,2)
        r = n-j*j
        gap = 2*j+1-r
        return validate(n,from_pair(r,gap))

    def prepared_pair(case):
        # Candidate computation reads only R,A; N is used for final certificate verification.
        return validate(case["n"],from_pair(case["r"],case["gap"]))

    cases = []
    for row,observed in zip(original["records"],result["public_observations"],strict=True):
        assert row["label"] == observed["label"] and row["decimal_sha256"] == observed["decimal_sha256"]
        state = row["state_annotation"]
        cases.append({"name":row["label"],"kind":"public_fixed_input","bits":row["bits"],
            "direction":state["direction"],"n":int(row["N"]),"j":int(state["J"]),
            "r":int(state["R"]),"gap":int(state["next_square_gap"]),
            "expected":(int(observed["lower_gcd"]),int(observed["upper_gcd"]))})
    for row in result["positive_controls"]:
        state = row["state"]
        cases.append({"name":row["name"],"kind":"prescribed_positive","bits":row["bits"],
            "direction":row["direction"],
            "n":int(row["factor_pair"][0])*int(row["factor_pair"][1]),
            "j":int(state["J"]),"r":int(state["R"]),"gap":int(state["A"]),
            "expected":tuple(map(int,row["gcd_pair"]))})
    assert len(cases) == 19
    identity_checks = []
    for case in cases:
        n,j,r,gap = (case[k] for k in ("n","j","r","gap"))
        assert n % 2 and j*j < n < (j+1)**2 and r+gap == 2*j+1
        assert r == n-j*j and gap == (j+1)**2-n
        observed = from_pair(r,gap)
        expected = (gcd(n,j),gcd(n,j+1))
        assert observed == expected == case["expected"]
        identity_checks.append({"name":case["name"],"kind":case["kind"],
            "lower_equal":True,"upper_equal":True,
            "max_residual_bits":max(r.bit_length(),gap.bit_length()),
            "N_bits":n.bit_length(),"parity_domain_valid":True})
    methods = {"complete_root":complete_root,"prepared_root":prepared_root,
               "complete_residue_pair":complete_pair,"prepared_residue_pair":prepared_pair}
    names = tuple(methods)
    measurements = []
    for case_index,case in enumerate(cases):
        for method in methods.values():
            assert method(case) == case["expected"]
        raw = {name:[] for name in methods}
        for round_index in range(ROUNDS):
            offset = (round_index+case_index) % len(names)
            order = names[offset:]+names[:offset]
            for name in order:
                started = perf_counter_ns()
                for _ in range(REPEATS):
                    assert methods[name](case) == case["expected"]
                elapsed = perf_counter_ns()-started
                raw[name].append({"round":round_index,"order_slot":order.index(name)+1,
                    "repeats":REPEATS,"total_ns":elapsed,"ns_per_call":elapsed/REPEATS})
        medians = {name:median(row["ns_per_call"] for row in rows) for name,rows in raw.items()}
        measurements.append({"name":case["name"],"kind":case["kind"],
            "bits":case["bits"],"direction":case["direction"],"median_ns_per_call":medians,
            "raw_rounds":raw,
            "complete_pair_speedup":medians["complete_root"]/medians["complete_residue_pair"],
            "prepared_pair_speedup":medians["prepared_root"]/medians["prepared_residue_pair"],
            "complete_pair_faster_rounds":sum(pair["total_ns"] < root["total_ns"]
                for root,pair in zip(raw["complete_root"],raw["complete_residue_pair"],strict=True)),
            "prepared_pair_faster_rounds":sum(pair["total_ns"] < root["total_ns"]
                for root,pair in zip(raw["prepared_root"],raw["prepared_residue_pair"],strict=True))})
    return {"status":"VERIFIED_EXACT_RESIDUE_PAIR_ENDPOINT_GCD",
        "formula_lower":"gcd(N,J)=gcd(R,A-1)/gcd(R,2)",
        "formula_upper":"gcd(N,J+1)=gcd(A,R+1)/gcd(A,2)",
        "domain":"N is odd and nonsquare, N>2; R=N-J^2, A=(J+1)^2-N. A prepared positive pair satisfies A-R=3 mod 4.",
        "scope":"Exact gcd values, including nonsquare composites with repeated prime factors; no squarefree premise is needed.",
        "information_scope":"Both residuals are retained. They encode J=(R+A-1)/2, so avoiding the root coordinate in the gcd is not an information-loss claim.",
        "identity_checks":identity_checks,"measurements":measurements,
        "candidate_operands":"Only R,A and their neighboring integers; approximately half the bit length of N.",
        "cost_contract":{
            "timed":"Domain checks, gcds, parity correction, factor divmod/product verification and equality checks. Complete pair calls include target root and residual construction.",
            "excluded":"Imports, source/input checks, fixture restoration, warmups and serialization.",
            "comparison":"New paired same-process run; compare to its own baseline, not prior-run timing.",
            "rounds":ROUNDS,"repeats":REPEATS},
        "coverage":{"fixed_inputs":19,"public_inputs_reused":3,"positive_fixtures_reused":16,
            "new_public_endpoint_observations":0,"new_public_multiplier_positions":0,
            "timed_public_gcd_calls_per_variant":3*ROUNDS*REPEATS*2,
            "timed_constructive_gcd_calls_per_variant":16*ROUNDS*REPEATS*2,
            "identity_check_gcd_calls":19*4,"warmup_gcd_calls":19*4*2},
        "extension_scope":"A separate exact-identity and cost extension on the saved corpus. Original endpoint observations and timings are unchanged."}


def audit_centered_union_cost(result, enterprise_root):
    """Audit one centered gcd and its exact union of the two endpoints."""
    checked_text(enterprise_root/"src"/"enterprise_math"/"core.py",CORE_BLOB)
    sys.path.insert(0,str(enterprise_root/"src"))
    from enterprise_math.core import integer_nth_root
    original = json.loads(checked_text(Path(__file__).resolve().parent/
        "brc_public_rsa_fixed_predicates_20260908.json",INPUT_BLOB))
    cases = []
    for row,observed in zip(original["records"],result["public_observations"],strict=True):
        state = row["state_annotation"]
        cases.append({"name":row["label"],"kind":"public_fixed_input","bits":row["bits"],
            "direction":state["direction"],"n":int(row["N"]),"j":int(state["J"]),
            "r":int(state["R"]),"gap":int(state["next_square_gap"]),
            "expected":int(observed["lower_gcd"])*int(observed["upper_gcd"])})
    for row in result["positive_controls"]:
        state = row["state"]
        cases.append({"name":row["name"],"kind":"prescribed_positive","bits":row["bits"],
            "direction":row["direction"],
            "n":int(row["factor_pair"][0])*int(row["factor_pair"][1]),
            "j":int(state["J"]),"r":int(state["R"]),"gap":int(state["A"]),
            "expected":int(row["gcd_pair"][0])*int(row["gcd_pair"][1])})
    for case in cases:
        n,j,r,gap = (case[k] for k in ("n","j","r","gap"))
        assert n > 2 and n % 2 and j*j < n < (j+1)**2
        assert r == n-j*j and gap == 2*j+1-r
        delta = j-r
        assert delta == (gap-r-1)//2 and 0 < abs(delta) <= j and delta % 2
        assert (delta > 0) == (case["direction"] == "D")
        case["delta"] = delta

    def verify(n,factor):
        assert 1 <= factor < n
        if factor > 1:
            other,remainder = divmod(n,factor)
            assert remainder == 0 and factor*other == n
        return factor

    def complete_endpoints(case):
        n = case["n"]
        j = integer_nth_root(n,2)
        return verify(n,gcd(n,j)*gcd(n,j+1))

    def prepared_endpoints(case):
        n,j = case["n"],case["j"]
        return verify(n,gcd(n,j)*gcd(n,j+1))

    def complete_center(case):
        n = case["n"]
        j = integer_nth_root(n,2)
        delta = j*(j+1)-n
        return verify(n,gcd(n,delta))

    def prepared_center(case):
        return verify(case["n"],gcd(case["n"],case["delta"]))

    def pair_value(r,gap):
        delta = (gap-r-1)//2
        return gcd(r,delta)*gcd(r+1,delta)

    def complete_pair(case):
        n = case["n"]
        j = integer_nth_root(n,2)
        r = n-j*j
        gap = 2*j+1-r
        return verify(n,pair_value(r,gap))

    def prepared_pair(case):
        return verify(case["n"],pair_value(case["r"],case["gap"]))

    methods = {"complete_endpoints":complete_endpoints,"prepared_endpoints":prepared_endpoints,
        "complete_center":complete_center,"prepared_center":prepared_center,
        "complete_pair":complete_pair,"prepared_pair":prepared_pair}
    names = tuple(methods)
    checks = []
    measurements = []
    for case_index,case in enumerate(cases):
        assert all(method(case) == case["expected"] for method in methods.values())
        checks.append({"name":case["name"],"kind":case["kind"],"direction":case["direction"],
            "delta_sign":1 if case["delta"] > 0 else -1,"delta_bits":abs(case["delta"]).bit_length(),
            "all_six_variants_equal":True,"proper_factor_preserved":case["expected"] > 1})
        raw = {name:[] for name in methods}
        for round_index in range(ROUNDS):
            offset = (case_index+round_index) % len(names)
            order = names[offset:]+names[:offset]
            for name in order:
                started = perf_counter_ns()
                for _ in range(REPEATS):
                    assert methods[name](case) == case["expected"]
                raw[name].append(perf_counter_ns()-started)
        medians = {name:median(values)/REPEATS for name,values in raw.items()}
        measurements.append({"name":case["name"],"case_index":case_index,"kind":case["kind"],
            "bits":case["bits"],"direction":case["direction"],"median_ns_per_call":medians,
            "raw_total_ns_by_round":raw,
            "complete_center_speedup":medians["complete_endpoints"]/medians["complete_center"],
            "complete_pair_speedup":medians["complete_endpoints"]/medians["complete_pair"],
            "prepared_center_speedup":medians["prepared_endpoints"]/medians["prepared_center"],
            "prepared_pair_speedup":medians["prepared_endpoints"]/medians["prepared_pair"],
            "complete_center_faster_rounds":sum(b<a for a,b in zip(raw["complete_endpoints"],raw["complete_center"],strict=True)),
            "complete_pair_faster_rounds":sum(b<a for a,b in zip(raw["complete_endpoints"],raw["complete_pair"],strict=True))})
    return {"status":"VERIFIED_CENTERED_GCD_ENDPOINT_UNION",
        "delta":"J-R = J*(J+1)-N = (A-R-1)/2",
        "sign":"D gives positive delta; U gives negative delta; odd N excludes delta=0.",
        "union_identity":"gcd(N,delta)=gcd(N,J)*gcd(N,J+1), because consecutive roots are coprime.",
        "pair_identities":"gcd(N,J)=gcd(R,delta); gcd(N,J+1)=gcd(R+1,delta).",
        "properness":"For odd nonsquare N>2, 0<abs(delta)<=J<N, so a union value greater than one is a proper factor.",
        "input_scope":"Fixed verified odd nonsquare inputs. Complete paths include their own native root and necessary coordinate construction.",
        "checks":checks,"measurements":measurements,
        "cost_contract":{"rounds":ROUNDS,"repeats":REPEATS,
            "variant_order":names,"round_order":"rotate variant_order left by (case_index+round_index) modulo 6",
            "raw_unit":"Total nanoseconds for all repeats of one variant in that round.",
            "timed":"Candidate calculation, proper-factor divmod/product verification and equality assertion; complete paths include root/coordinate preparation.",
            "excluded":"Imports, source/input/domain verification, case restoration, initial identity/warmup calls and serialization.",
            "comparison":"One scalar endpoint-union output for every variant, in a new paired run; earlier timing records are unchanged.",
            "prepared_inputs":"J, delta or (R,A) is already materialized as specified. Prepared costs are not full N-only costs."},
        "coverage":{"fixed_inputs":19,"public_inputs_reused":3,"positive_fixtures_reused":16,
            "new_public_endpoint_observations":0,"new_public_multiplier_positions":0,
            "timed_public_calls_per_variant":3*ROUNDS*REPEATS,
            "timed_constructive_calls_per_variant":16*ROUNDS*REPEATS,
            "gcds_per_call":{"complete_endpoints":2,"prepared_endpoints":2,
                "complete_center":1,"prepared_center":1,"complete_pair":2,"prepared_pair":2},
            "initial_identity_and_warmup_gcd_calls":190},
        "extension_scope":"New algebraic composition and cost comparison on existing fixed observations; no new public search."}


def audit_center_candidate_cost(result, enterprise_root):
    """Try the center difference itself as a factor using one short remainder."""
    checked_text(enterprise_root/"src"/"enterprise_math"/"core.py",CORE_BLOB)
    sys.path.insert(0,str(enterprise_root/"src"))
    from enterprise_math.core import integer_nth_root
    original = json.loads(checked_text(Path(__file__).resolve().parent/
        "brc_public_rsa_fixed_predicates_20260908.json",INPUT_BLOB))
    cases = []
    for row,observed in zip(original["records"],result["public_observations"],strict=True):
        state = row["state_annotation"]
        cases.append({"name":row["label"],"kind":"public_fixed_input","bits":row["bits"],
            "direction":state["direction"],"n":int(row["N"]),"j":int(state["J"]),
            "r":int(state["R"]),"gap":int(state["next_square_gap"]),
            "expected":int(observed["lower_gcd"])*int(observed["upper_gcd"])})
    for row in result["positive_controls"]:
        state = row["state"]
        cases.append({"name":row["name"],"kind":"prescribed_positive","bits":row["bits"],
            "direction":row["direction"],
            "n":int(row["factor_pair"][0])*int(row["factor_pair"][1]),
            "j":int(state["J"]),"r":int(state["R"]),"gap":int(state["A"]),
            "expected":int(row["gcd_pair"][0])*int(row["gcd_pair"][1])})
    for case in cases:
        n,j,r,gap = (case[k] for k in ("n","j","r","gap"))
        assert n % 2 and j*j < n < (j+1)**2 and r == n-j*j and gap == 2*j+1-r
        case["h"] = abs(j*(j+1)-n)
        assert 0 < case["h"] <= j and case["h"] == abs(gap-r-1)//2
        assert j % case["h"] == r % case["h"]

    def verify(n,factor):
        assert 1 <= factor < n
        if factor > 1:
            other,remainder = divmod(n,factor)
            assert remainder == 0 and factor*other == n
        return factor

    def short_gate(value,h):
        if h <= 1:
            return 1
        residue = value % h
        return h if residue == 0 or residue == h-1 else 1

    def complete_center_gcd(case):
        n = case["n"]
        j = integer_nth_root(n,2)
        return verify(n,gcd(n,j*(j+1)-n))

    def complete_candidate(case):
        n = case["n"]
        j = integer_nth_root(n,2)
        h = abs(j*(j+1)-n)
        return verify(n,short_gate(j,h))

    def prepared_center_gcd(case):
        return verify(case["n"],gcd(case["n"],case["h"]))

    def prepared_root_candidate(case):
        n,j = case["n"],case["j"]
        h = abs(j*(j+1)-n)
        return verify(n,short_gate(j,h))

    def prepared_residual_candidate(case):
        r,gap = case["r"],case["gap"]
        h = abs(gap-r-1)//2
        return verify(case["n"],short_gate(r,h))

    methods = {"complete_center_gcd":complete_center_gcd,"complete_candidate":complete_candidate,
        "prepared_center_gcd":prepared_center_gcd,"prepared_root_candidate":prepared_root_candidate,
        "prepared_residual_candidate":prepared_residual_candidate}
    checks = []
    measurements = []
    names = tuple(methods)
    for case_index,case in enumerate(cases):
        assert all(method(case) == case["expected"] for method in methods.values())
        residue = case["j"] % case["h"]
        checks.append({"name":case["name"],"kind":case["kind"],"direction":case["direction"],
            "h_bits":case["h"].bit_length(),"short_remainder_is_0_or_minus1":residue in (0,case["h"]-1),
            "candidate_is_proper_factor":case["expected"] > 1,
            "equality_with_union_observed_on_this_input":True})
        raw = {name:[] for name in methods}
        for round_index in range(ROUNDS):
            offset = (case_index+round_index) % len(names)
            order = names[offset:]+names[:offset]
            for name in order:
                started = perf_counter_ns()
                for _ in range(REPEATS):
                    assert methods[name](case) == case["expected"]
                raw[name].append(perf_counter_ns()-started)
        medians = {name:median(values)/REPEATS for name,values in raw.items()}
        measurements.append({"name":case["name"],"case_index":case_index,"kind":case["kind"],
            "bits":case["bits"],"direction":case["direction"],"median_ns_per_call":medians,
            "raw_total_ns_by_round":raw,
            "complete_candidate_speedup":medians["complete_center_gcd"]/medians["complete_candidate"],
            "complete_candidate_faster_rounds":sum(b<a for a,b in zip(raw["complete_center_gcd"],raw["complete_candidate"],strict=True))})
    generalization = []
    p = 127
    for a in (3,5,8):
        for label,offset in (("lower_D",a-1),("lower_U",a+1),
                             ("upper_U",-(a-1)),("upper_D",-(a+1))):
            q = a*a*p+offset
            n = p*q
            j = a*p if offset > 0 else a*p-1
            r = n-j*j
            gap = (j+1)**2-n
            case = {"n":n,"j":j,"r":r,"gap":gap,"h":p}
            assert n % 2 and j*j < n < (j+1)**2
            assert abs(j-r) == p
            direction = "D" if r <= j else "U"
            assert direction == label.rsplit("_",1)[1]
            assert all(method(case) == p for method in methods.values())
            generalization.append({"a":a,"branch":label,"N":str(n),"factor_pair":[str(p),str(q)],
                "direction":direction,"delta":str(j-r),"complete_candidate_verified":True,
                "prime_pair_claimed":False})
    return {"status":"VERIFIED_PROPER_CENTER_CANDIDATE_SUBSET",
        "candidate":"h=abs(J*(J+1)-N)>1; accept h if J mod h is 0 or h-1.",
        "proof":"h divides J*(J+1)-N. The short remainder condition makes h divide J or J+1, hence h divides N. Also h<=J<N.",
        "residual_form":"h=abs(A-R-1)/2 and R mod h equals J mod h; the same gate uses only the two residuals.",
        "scope":"A sufficient subset of the centered-gcd route, not an equivalent replacement. Sentinel 1 means this candidate was not admitted; it does not assert gcd(N,h)=1 on arbitrary inputs.",
        "general_positive_family":"For any odd p>1 and integer a>=2, q=a^2*p plus or minus (a-1) or (a+1) gives the four separated branches, abs(delta)=p and a passing short remainder.",
        "checks":checks,"measurements":measurements,"generalization_controls":generalization,
        "cost_contract":{"rounds":ROUNDS,"repeats":REPEATS,"variant_order":names,
            "round_order":"rotate variant_order left by (case_index+round_index) modulo 5",
            "raw_unit":"Total nanoseconds for all repeats in a round.",
            "timed":"Coordinate construction required by the named input form, short remainder or gcd, candidate divmod/product verification and equality assertion; complete paths include the root.",
            "excluded":"Imports, source/input/domain checks, case restoration, initial identity/warmup calls, generalization controls and serialization.",
            "comparison":"New paired run on the same fixed corpus; candidate and centered-gcd outcomes coincide on this corpus only.",
            "prepared_inputs":"prepared_center_gcd receives h; prepared_root_candidate receives J and constructs h inside the timer; prepared_residual_candidate receives R,A and constructs h inside the timer."},
        "coverage":{"public_inputs_reused":3,"positive_fixtures_reused":16,"new_small_constructive_cases":12,
            "new_public_endpoint_observations":0,"new_public_multiplier_positions":0,
            "timed_public_calls_per_variant":3*ROUNDS*REPEATS,
            "timed_constructive_calls_per_variant":16*ROUNDS*REPEATS,
            "candidate_path_gcd_calls":0,"candidate_path_search_extensions":0,
            "new_primality_checks":0},
        "extension_scope":"One sufficient arithmetic branch and prescribed positive generalization; no new public search or success-rate estimate."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root",type=Path,required=True)
    parser.add_argument("--output-dir",type=Path,default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    checked_text(args.enterprise_root/"src"/"enterprise_math"/"core.py",CORE_BLOB)
    checked_text(here/"brc_kernel13_state_pairs_20260908.py",SMALL_PRIME_HELPER_BLOB)
    from brc_kernel13_state_pairs_20260908 import small_prime
    sys.path.insert(0,str(args.enterprise_root/"src"))
    from enterprise_math.core import integer_nth_root
    document = json.loads(checked_text(here/"brc_public_rsa_fixed_predicates_20260908.json",INPUT_BLOB))
    assert [r["label"] for r in document["records"]] == ["RSA-270","RSA-896","RSA-2048"]

    def verify_factors(n, values):
        for value in values:
            assert 1 <= value < n
            if value > 1:
                other,remainder = divmod(n,value)
                assert remainder == 0 and value*other == n
        return values

    def complete_root(case):
        n = case["n"]
        j = integer_nth_root(n,2)
        return verify_factors(n,(gcd(n,j),gcd(n,j+1)))

    def prepared_root(case):
        n,j = case["n"],case["j"]
        return verify_factors(n,(gcd(n,j),gcd(n,j+1)))

    def complete_residual(case):
        n = case["n"]
        j = integer_nth_root(n,2)
        remainder = n-j*j
        gap = 2*j+1-remainder
        return verify_factors(n,(gcd(n,remainder),gcd(n,gap)))

    def prepared_residual(case):
        # The evaluated representation reads N,R,A and does not read J.
        n = case["n"]
        return verify_factors(n,(gcd(n,case["r"]),gcd(n,case["gap"])))

    methods = {"complete_root":complete_root,"prepared_root":prepared_root,
               "complete_residual":complete_residual,"prepared_residual":prepared_residual}
    public = []
    cases = []
    for row in document["records"]:
        n = int(row["N"])
        state = row["state_annotation"]
        j,r,gap = int(state["J"]),int(state["R"]),int(state["next_square_gap"])
        assert n > 2 and n % 2 and j*j < n < (j+1)**2
        assert r == n-j*j and gap == (j+1)**2-n
        assert sha256(row["N"].encode("ascii")).hexdigest() == row["decimal_sha256"]
        # Exactly the two newly declared endpoint observations.
        started = perf_counter_ns()
        lower = gcd(n,j)
        lower_ns = perf_counter_ns()-started
        started = perf_counter_ns()
        upper = gcd(n,j+1)
        upper_ns = perf_counter_ns()-started
        expected = verify_factors(n,(lower,upper))
        case = {"name":row["label"],"kind":"public_fixed_input","n":n,"j":j,"r":r,"gap":gap,
                "direction":state["direction"],"expected":expected,"bits":n.bit_length()}
        candidates = []
        for endpoint,value in zip(("J","J+1"),expected,strict=True):
            if value > 1:
                candidates.append({"endpoint":endpoint,"factor":str(value),"cofactor":str(n//value)})
        public.append({"label":row["label"],"bits":n.bit_length(),"direction":state["direction"],
            "decimal_sha256":row["decimal_sha256"],"source_pdf":row["source_pdf"],
            "reused_state":True,"primary_endpoint_gcd_calls":2,
            "lower_gcd":str(lower),"upper_gcd":str(upper),
            "lower_call_ns":lower_ns,"upper_call_ns":upper_ns,
            "proper_factor_certificates":candidates})
        cases.append(case)

    # Four prescribed semiprimes show each state/endpoint branch.
    # Further sizes are algebraic composites, without prime-factor claims.
    small_p = {"lower_D":127,"lower_U":107,"upper_U":131,"upper_D":101}
    branches = (("lower_D",1,"D","J"),("lower_U",3,"U","J"),
                ("upper_U",-1,"U","J+1"),("upper_D",-3,"D","J+1"))
    controls = []
    for branch,delta,direction,endpoint in branches:
        for size in ("small",896,2048,8192):
            p = small_p[branch] if size == "small" else (1 << (size//2-1))-(21 if delta == -1 else 19)
            q = 4*p+delta
            n = p*q
            j = 2*p if delta > 0 else 2*p-1
            r = n-j*j
            gap = (j+1)**2-n
            assert p > 2 and q > 2 and n % 2 and j*j < n < (j+1)**2
            assert (r <= j) == (direction == "D")
            assert (gap == (4-delta)*p+1) if delta > 0 else (gap == -delta*p)
            expected = (p,1) if delta > 0 else (1,p)
            if size == "small":
                assert small_prime(p) and small_prime(q)
            else:
                assert n.bit_length() == size
            case = {"name":f"{branch}_{size}","kind":"prescribed_positive","n":n,"j":j,"r":r,"gap":gap,
                "direction":direction,"expected":expected,"bits":n.bit_length()}
            assert all(method(case) == expected for method in methods.values())
            controls.append({"name":case["name"],"direction":direction,"endpoint":endpoint,
                "ratio_parameter":2,"signed_offset":delta,"bits":n.bit_length(),
                "N_sha256":sha256(str(n).encode("ascii")).hexdigest(),
                "factor_pair":[str(p),str(q)],"state":{"J":str(j),"R":str(r),"A":str(gap)},
                "gcd_pair":[str(x) for x in expected],"four_variants_agree":True,
                "known_prime_pair":True if size == "small" else None})
            cases.append(case)
    assert len(controls) == 16 and sum(row["known_prime_pair"] is True for row in controls) == 4

    # Residual equality is verified on this fixed corpus, not presumed for
    # arbitrary nonsquare composites. The general theorem is equality of
    # shared-prime supports, with equality of gcd values for squarefree N.
    representation_checks = []
    for case in cases[:3]:
        assert all(method(case) == case["expected"] for method in methods.values())
        representation_checks.append({"label":case["name"],"actual_gcd_values_agree":True,
            "scope":"fixed-corpus verification; these calls are replays of the endpoint information"})

    measurements = []
    names = tuple(methods)
    for case_index,case in enumerate(cases):
        for method in methods.values():
            assert method(case) == case["expected"]
        raw = {name:[] for name in methods}
        for round_index in range(ROUNDS):
            offset = (case_index+round_index) % len(names)
            order = names[offset:]+names[:offset]
            for name in order:
                started = perf_counter_ns()
                for _ in range(REPEATS):
                    assert methods[name](case) == case["expected"]
                elapsed = perf_counter_ns()-started
                raw[name].append({"round":round_index,"order_slot":order.index(name)+1,
                    "repeats":REPEATS,"total_ns":elapsed,"ns_per_call":elapsed/REPEATS})
        medians = {name:median(row["ns_per_call"] for row in rows) for name,rows in raw.items()}
        measurements.append({"name":case["name"],"kind":case["kind"],"bits":case["bits"],
            "direction":case["direction"],"median_ns_per_call":medians,"raw_rounds":raw,
            "speedup_relative_to_complete_root":{name:medians["complete_root"]/value for name,value in medians.items()}})

    result = {
        "status":"VERIFIED_FIXED_ROOT_ENDPOINT_GCD_OBSERVATIONS",
        "researcher":"EM-HME-0CE4FD / TASK_RESEARCH",
        "global_snapshot":"91cd38de772d892c0707ba356d7bbcecb44996bb",
        "project_parent":"ecf1ee1347804cb2fc2bec1f9d56fe96a21e2623",
        "input_blob":INPUT_BLOB,"core_blob":CORE_BLOB,"small_prime_helper_blob":SMALL_PRIME_HELPER_BLOB,
        "python":sys.version,"platform":platform.platform(),
        "contracts":{
            "inputs":"Fixed published mathematical puzzles and prescribed positive composites, all odd nonsquares greater than two.",
            "root_only":"gcd(N,J), gcd(N,J+1), J=floor(sqrt(N)); no residual is read.",
            "residual_only":"gcd(N,R), gcd(N,A) given their materialized values; no root coordinate is read.",
            "complete_residual":"Computing those residuals from N incurs the target root and exact squares, included in its timer.",
            "prime_support_equivalence":"gcd(N,R)=gcd(N,J^2) and gcd(N,A)=gcd(N,(J+1)^2); shared-prime supports agree with the corresponding root gcd. For squarefree N the gcd values also agree.",
            "fixed_gap_U":"For b>=1 and a^2=mN+b^2, the condition a>b^2 puts the witness in U. No new fixed-gap public witness call was made.",
            "lower_family":"q=a^2*p+delta, 1<=delta<=2a gives J=ap,R=delta*p; D for delta<=a, U otherwise.",
            "upper_family":"q=a^2*p-delta, 1<=delta<=2a-1 gives ceil root ap,A=delta*p; U for delta<a, D otherwise.",
            "family_factor_condition":"p>1 and q>a give 1<gcd(N,ap)<N; for prime q>a this gcd equals p.",
            "novelty":"Composition of classical gcd/root identities with the separated BRC state records; no general new factoring theorem claimed."},
        "public_observations":public,"positive_controls":controls,
        "public_representation_replays":representation_checks,"measurements":measurements,
        "cost_contract":{
            "timed":"Both gcds and verification of every returned proper factor by divmod and exact product; complete paths also pay for their root/state preparation.",
            "prepared_scope":"Previously materialized J or R,A is supplied; preparation is not free for an N-only caller.",
            "excluded":"Imports, source/input checks, fixture construction, annotation, warmup and serialization.",
            "rounds":ROUNDS,"repeats":REPEATS,
            "sampling":"Same-process paired cost replays; not independent factoring observations.",
            "positive_scope":"All large fixtures are constructed composites with no prime-factor claim; four specified small pairs receive exact bounded primality checks."},
        "coverage":{
            "public_inputs":3,"primary_public_endpoint_gcd_calls":6,
            "new_public_multiplier_positions":0,"public_unique_multiplier_positions_remain":312,
            "public_square_completion_witness_calls":0,"positive_fixtures":16,"known_small_prime_pairs":4,
            "public_timed_gcd_calls_per_variant":3*ROUNDS*REPEATS*2,
            "constructive_timed_gcd_calls_per_variant":16*ROUNDS*REPEATS*2,
            "public_validation_and_warmup_gcd_calls":48,
            "constructive_validation_and_warmup_gcd_calls":256,
            "search_fallbacks":0,"adaptive_range_extensions":0},
        "reuse_resolution":"COMPOSE_APPLIED: pinned native floor-root source, saved BRC states, standard-library gcd, and the earlier bounded small-prime checker.",
        "goal_status":"ACTIVE",
    }
    result["residue_pair_extension"] = audit_residue_pair_cost(result,args.enterprise_root)
    result["centered_union_extension"] = audit_centered_union_cost(result,args.enterprise_root)
    result["center_candidate_extension"] = audit_center_candidate_cost(result,args.enterprise_root)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    destination = args.output_dir/"brc_root_endpoint_gcd_audit_20260908.json"
    destination.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(destination),"public":public,
        "residue_pair_measurements":[{k:v for k,v in r.items() if k != "raw_rounds"}
            for r in result["residue_pair_extension"]["measurements"]],
        "centered_union_measurements":[{k:v for k,v in r.items() if k != "raw_total_ns_by_round"}
            for r in result["centered_union_extension"]["measurements"]],
        "center_candidate_measurements":[{k:v for k,v in r.items() if k != "raw_total_ns_by_round"}
            for r in result["center_candidate_extension"]["measurements"]],
        "small_prime_pairs":[r["factor_pair"] for r in controls if r["known_prime_pair"]],
        "measurements":[{k:v for k,v in r.items() if k != "raw_rounds"} for r in measurements],
        "coverage":result["coverage"]},ensure_ascii=True))


if __name__ == "__main__":
    main()

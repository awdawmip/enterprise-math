"""Short, reproducible read-only audit of POWER 87/89 at pinned commit.
Original source files are imported unchanged. No repository mutation or remote write.
"""
from __future__ import annotations
import dataclasses
import json
import math
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from power.weapons.dyadic_hensel_branch_rigidity_filter import DyadicHenselBranchRigidityFilterEngine as H
from power.weapons.vectorized_bitmask_dyadic_sieve import VectorizedBitmaskDyadicSieveEngine as V
from power.rsa280_spec import RSA_280_INT

report = {
    "repository": "awdawmip/power",
    "source_ref": "74b386de5f1ca8dcc662935f563c438e1cfeee7e",
    "scope": "Native engine calls, short mathematical checks, and Python trace observations; not a general factoring benchmark.",
}

# Native scalar mask sieve: it contains every quadratic residue, including zero.
v = V(primes_count=64)
report["qr_masks"] = {
    "primes_count": len(v.primes),
    "max_mask_bits": max(x.bit_length() for x in v._qr_masks.values()),
    "table_exact_for_all_64_primes": all(
        {r for r in range(p) if (v._qr_masks[p] >> r) & 1}
        == {r*r % p for r in range(p)}
        for p in v.primes
    ),
    "all_squares_0_through_4095_preserved": all(v.simd_quadratic_filter(x*x) for x in range(4096)),
}

# Every stored successful vectorized-scan example is a one-candidate Fermat example.
stored = json.loads((ROOT/"docs/vectorized_bitmask_dyadic_sieve_results.json").read_text())
toy_rows = []
for item in stored["small_semiprime_solves"]:
    n = item["n"]
    p, q = item["factors"]
    center = math.isqrt(n)
    parity = 1 if n % 4 == 1 else 0
    if center % 2 != parity:
        center += 1
    delta = center*center-n
    radius = math.isqrt(delta) if delta >= 0 else -1
    native = v.scan_simd_horizon(n, math.isqrt(n), count=1)
    toy_rows.append({
        "n": n, "n_bits": n.bit_length(), "p": p, "q": q,
        "factor_product_correct": p*q == n,
        "factor_gap": q-p,
        "first_center_is_true_center": center == (p+q)//2,
        "plain_fermat_first_candidate_factors": delta >= 0 and radius*radius == delta and center-radius == p and center+radius == q,
        "native_success": native.is_success,
        "native_candidates": native.candidates_tested,
    })
report["stored_success_family"] = toy_rows

# Native 87 beam truncation can remove both true orientations even within its radius bound.
p, q = 1009, 2003
n = p*q
trace_rows = []
def bit_trace(frame, event, arg):
    if frame.f_code.co_name == "solve_or_filter" and event == "line" and frame.f_lineno == 125:
        d = frame.f_locals
        depth = d["k"] + 1
        mask = (1 << depth)-1
        truths = {(p & mask, q & mask), (q & mask, p & mask)}
        beam = d["next_beam"]
        width = d["self"].max_beam_width
        present = [i for i,x in enumerate(beam) if x in truths]
        retained = [i for i,x in enumerate(beam[:width]) if x in truths]
        trace_rows.append({
            "depth": depth, "before_width": len(beam), "after_width": min(width,len(beam)),
            "true_pairs": sorted(truths), "true_pair_sorted_positions_zero_based": present,
            "true_pair_retained_positions_zero_based": retained,
        })
    return bit_trace
sys.settrace(bit_trace)
try:
    hres = H(max_beam_width=128).solve_or_filter(n)
finally:
    sys.settrace(None)
report["bit_beam_counterexample"] = {
    "p":p, "q":q, "n":n, "true_radius":(q-p)//2,
    "native":dataclasses.asdict(hres),
    "beam_truncations":trace_rows,
}

# Native 89 byte initialization and 16/256 byte sampling lose true paths.
byte_rows=[]
for p,q in [(7,11),(17,19),(503,509),(257,263),(1000003,1000033)]:
    stage_zero=[]
    def byte_trace(frame,event,arg):
        if frame.f_code.co_name == "byte_dyadic_hensel_lift" and event == "line" and frame.f_lineno == 133:
            d=frame.f_locals
            if d["byte_idx"] == 0:
                stage_zero.extend(d["next_beam"])
        return byte_trace
    sys.settrace(byte_trace)
    try:
        native=v.byte_dyadic_hensel_lift(p*q,target_depth_bytes=4,max_beam=64)
    finally:
        sys.settrace(None)
    truths={(p%256,q%256),(q%256,p%256)}
    byte_rows.append({
        "p":p,"q":q,"n":p*q,"native_factors":native[0],
        "nodes":native[1],"pruned":native[2],"active":native[3],
        "first_byte_native_candidates":stage_zero,
        "true_first_byte_pairs":sorted(truths),
        "true_first_byte_pair_retained":any(x in truths for x in stage_zero),
        "all_native_first_byte_pairs_satisfy_product_congruence":all((a*b-p*q)%256 == 0 for a,b in stage_zero),
    })
report["byte_counterexamples_and_control"]=byte_rows

report["byte_trivial_factor_return"] = [
    {"n": n, "native_result": v.byte_dyadic_hensel_lift(n, target_depth_bytes=2)}
    for n in (9, 15)
]

# RSA 87 probe's radius hypothesis is ruled out even before factoring.
n=RSA_280_INT
s0=math.isqrt(n)
ceil_sqrt=s0+(s0*s0<n)
min_defect=ceil_sqrt*ceil_sqrt-n
report["rsa_radius_assumption"]={
    "n_bits":n.bit_length(),
    "probe_radius_bound":1<<24,
    "bound_squared":1<<48,
    "minimum_integer_center_defect":min_defect,
    "minimum_defect_bits":min_defect.bit_length(),
    "minimum_defect_exceeds_bound_squared":min_defect > (1<<48),
    "minimum_radius_floor":math.isqrt(min_defect),
    "minimum_radius_floor_bits":math.isqrt(min_defect).bit_length(),
    "logic":"Any positive integer factor pair has S=(p+q)/2 >= ceil(sqrt(N)), so R^2=S^2-N >= minimum_integer_center_defect.",
}
rsa_h=[]
for bound_name,bound in [("probe_2pow24",1<<24),("native_default",None)]:
    result=H(max_beam_width=64).solve_or_filter(n,target_depth_bits=64,max_fermat_radius=bound)
    rsa_h.append({
        "bound_name":bound_name,"radius_bound_bits":result.metadata["max_fermat_radius"].bit_length(),
        "nodes":result.total_nodes_visited,"parity_pruned":result.pruned_parity_nodes,
        "archimedean_pruned":result.pruned_archimedean_nodes,"active":result.beam_width,
        "success":result.is_success,"factors":result.factors,"elapsed_ms_local":result.elapsed_ms,
    })
report["rsa87_replay"]=rsa_h

# Short native replay of the 89 finite horizon, separate from byte routine.
res=v.scan_simd_horizon(n,start_center=s0,count=50000,step=2)
report["rsa89_horizon_replay"]={k:val for k,val in dataclasses.asdict(res).items() if k!="n"}
report["rsa89_byte_replay"]=[]
for depth in (2,4,8):
    t=time.perf_counter()
    result=v.byte_dyadic_hensel_lift(n,target_depth_bytes=depth,max_beam=64)
    report["rsa89_byte_replay"].append({
        "depth_bytes":depth,"factors":result[0],"nodes":result[1],"pruned":result[2],"active":result[3],
        "elapsed_ms_local":1000*(time.perf_counter()-t),
    })

out=ROOT/"audit_checks_results.json"
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({
    "saved":str(out),"qr_masks":report["qr_masks"],
    "all_six_toys_are_one_candidate_plain_fermat":all(x["plain_fermat_first_candidate_factors"] for x in toy_rows),
    "bit_counterexample_success":hres.is_success,"bit_trace":trace_rows,
    "byte_counterexamples":byte_rows,
    "rsa_radius_assumption":report["rsa_radius_assumption"],
    "rsa87_replay":rsa_h,"rsa89_horizon_replay":report["rsa89_horizon_replay"],
    "rsa89_byte_replay":report["rsa89_byte_replay"],
},ensure_ascii=False,indent=2))


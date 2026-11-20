"""Unit195 exact non-shortest signed-X6 / lazy-A5 / nonlazy-A5 bridge check.

Source at experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py,
immutable fd2bcff10ca6e147348b6c1236027fc0d2877df3,
Git blob SHA-1 300a96e3dc24bf6fff73743037a0347a8bc83176.
Copy is supplied alongside this checker under its original bytes and must match.
"""
import hashlib
import importlib.util
import json
from collections import defaultdict
from math import comb
from pathlib import Path

PIN = "300a96e3dc24bf6fff73743037a0347a8bc83176"
ROOT = Path(__file__).resolve().parent
source = ROOT / "signed_brc.py"
raw = source.read_bytes()
blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()
if blob != PIN:
    raise RuntimeError(f"frozen source blob mismatch: {blob}")
spec = importlib.util.spec_from_file_location("frozen_signed_brc", source)
frozen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frozen)
zero = (0,) * 6


def move(z, i, j):
    w = list(z)
    w[i] += 1
    w[j] -= 1
    return tuple(w)


def next_layer(dp, include_self):
    ans = defaultdict(int)
    for z, value in dp.items():
        for i in range(6):
            for j in range(6):
                if include_self or i != j:
                    ans[move(z, i, j)] += value
    return dict(ans)


lazy = [{zero: 1}]
root = [{zero: 1}]
for n in range(1, 6):
    lazy.append(next_layer(lazy[-1], True))
    root.append(next_layer(root[-1], False))

checks = 0
nonshortest = 0
shortest = 0
violations = 0
layers = []
examples = {}
for n in range(6):
    L = lazy[n]
    A = root[n]
    if not set(A).issubset(set(L)):
        raise RuntimeError("nonlazy endpoint absent from lazy A5")
    if sum(L.values()) != 36**n or sum(A.values()) != 30**n:
        raise RuntimeError("DP mass conservation mismatch")
    e_sum = 0
    for z, n_lazy in L.items():
        r = sum(max(v, 0) for v in z)
        e = frozen.endpoint_multiplicity(2*n, z)
        e_sum += e
        checks += 1
        if n > r:
            nonshortest += 1
        else:
            shortest += 1
        if e != comb(2*n, n) * n_lazy:
            violations += 1
        # Full k <= n binomial inversion of frozen native counts.
        inverse = 0
        for k in range(n+1):
            e_k = frozen.endpoint_multiplicity(2*k,z)
            ratio, remainder = divmod(e_k, comb(2*k,k))
            if remainder:
                raise RuntimeError("native-to-lazy fiber nonintegral")
            inverse += comb(n,k) * (-6)**(n-k) * ratio
        if inverse != A.get(z, 0):
            violations += 1
    if e_sum != comb(2*n,n)*36**n:
        raise RuntimeError("balanced native mass mismatch")
    layers.append({"n":n,"reachable_balanced_endpoints":len(L),"lazy_A5_count":sum(L.values()),"nonlazy_A5_count":sum(A.values()),"native_X6_count":e_sum,"shuffle_fiber":comb(2*n,n)})

for z,n in [((0,0,0,0,0,0),2),((1,-1,0,0,0,0),2),((2,-2,0,0,0,0),3)]:
    e=frozen.endpoint_multiplicity(2*n,z)
    examples["n=%s;z=%s"%(n,z)]={"native":e,"lazy":lazy[n].get(z,0),"nonlazy":root[n].get(z,0),"shuffles":comb(2*n,n)}

out = {
  "schema":"X6_UNIT195_EXACT_LAZY_A5_PINNED_NATIVE_BRIDGE_V1",
  "frozen_scientific_comparison_commit":"fd2bcff10ca6e147348b6c1236027fc0d2877df3",
  "source":"experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py",
  "source_git_blob_sha1":blob,
  "max_paired_length_n":5,
  "examined_endpoint_layer_pairs":checks,
  "nonshortest_endpoint_layer_pairs":nonshortest,
  "shortest_endpoint_layer_pairs":shortest,
  "mismatches":violations,
  "tested_equalities":["E_2n(z)=C(2n,n)*L_n(z)","A_n(z)=sum_k C(n,k)*(-6)^(n-k)*E_2k(z)/C(2k,k)"],
  "layers":layers,
  "examples":examples,
  "native_R063_benchmark_rerun":False,
  "p022_A5_original_module_executed":False,
  "exact_frozen_signed_brc_module_executed":True,
  "independent_algorithms":"36-event lazy A5 and 30-event nonlazy A5 endpoint DP, versus frozen signed_brc.endpoint_multiplicity combinatorial kernel",
  "author_status":"EXACT_FINITE_CHECK / UNREVIEWED / NOT_ADMITTED"
}
result_path = ROOT / "X6_UNIT195_LAZY_A5_SIGNED_BRIDGE_RESULTS_20261120.json"
result_path.write_text(json.dumps(out,indent=2,sort_keys=True,ensure_ascii=False)+"\n")
print(json.dumps(out,sort_keys=True,ensure_ascii=False))
if violations:
    raise RuntimeError("mismatches")

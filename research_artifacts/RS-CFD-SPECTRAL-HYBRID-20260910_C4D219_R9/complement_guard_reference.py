from __future__ import annotations
import json, math, statistics, time
import numpy as np
try:
    from numba import njit
except Exception:
    njit = None

SEED = 20260921
N = 3*64*64*33  # matches 3-component r2c n=64 storage coefficient count used in prior guard microbench
REPS = 60
COUNTS = [384, int(round(N*0.01)), int(round(N*0.1)), int(round(N*0.25)), int(round(N*0.5)), int(round(N*0.75)), int(round(N*0.9))]
rng = np.random.default_rng(SEED)

def full_boolean_guard(a: np.ndarray, carrier: np.ndarray) -> bool:
    return not np.any((a != 0) & (~carrier))

def boolean_complement_guard(a: np.ndarray, outside: np.ndarray) -> bool:
    return not np.any(a[outside] != 0)

def index_complement_guard(a: np.ndarray, outside_idx: np.ndarray) -> bool:
    return not np.any(a[outside_idx] != 0)

if njit:
    @njit(cache=False)
    def jit_complement_guard(a, carrier):
        for i in range(a.size):
            if (not carrier[i]) and a[i] != 0:
                return False
        return True
else:
    jit_complement_guard = None

def pair_full(a, b, carrier):
    return full_boolean_guard(a, carrier) and full_boolean_guard(b, carrier)

def pair_bool_comp(a, b, outside):
    return boolean_complement_guard(a, outside) and boolean_complement_guard(b, outside)

def pair_idx_comp(a, b, outside_idx):
    return index_complement_guard(a, outside_idx) and index_complement_guard(b, outside_idx)

def pair_jit(a, b, carrier):
    return bool(jit_complement_guard(a, carrier)) and bool(jit_complement_guard(b, carrier))

def timed(fn, *args):
    # warmup external to samples
    fn(*args)
    vals=[]
    for _ in range(REPS):
        t0=time.perf_counter_ns(); out=fn(*args); t1=time.perf_counter_ns()
        if not out: raise AssertionError('unexpected escape in timing input')
        vals.append((t1-t0)/1e6)
    return {"median_ms": statistics.median(vals), "p10_ms": float(np.percentile(vals,10)), "p90_ms": float(np.percentile(vals,90))}

# exactness tests
correctness = []
for case in range(200):
    n=257
    k=int(rng.integers(1,n))
    idx=rng.choice(n,size=k,replace=False)
    carrier=np.zeros(n,dtype=np.bool_); carrier[idx]=True
    outside=~carrier; outside_idx=np.flatnonzero(outside)
    a=np.zeros(n,dtype=np.complex128)
    # legal inside mutation
    j=int(rng.choice(idx)); a[j]=complex(rng.normal(),rng.normal())
    expected=True
    got=[full_boolean_guard(a,carrier), boolean_complement_guard(a,outside), index_complement_guard(a,outside_idx)]
    if jit_complement_guard is not None: got.append(bool(jit_complement_guard(a,carrier)))
    assert all(x==expected for x in got)
    # illegal outside mutation
    j=int(rng.choice(outside_idx)); a[j]=complex(rng.normal() or 1.0,rng.normal())
    expected=False
    got=[full_boolean_guard(a,carrier), boolean_complement_guard(a,outside), index_complement_guard(a,outside_idx)]
    if jit_complement_guard is not None: got.append(bool(jit_complement_guard(a,carrier)))
    assert all(x==expected for x in got)
    correctness.append(True)

# adversarial lower-bound witness: if any outside coefficient is not queried, zero vector and one-spike escape agree on all queried coordinates.
for n in [7,31,257]:
    carrier=np.zeros(n,dtype=np.bool_); carrier[:max(1,n//4)]=True
    outside=np.flatnonzero(~carrier)
    missed=int(outside[-1])
    queried=set(int(i) for i in outside[:-1])
    x=np.zeros(n,dtype=np.complex128); y=x.copy(); y[missed]=1+2j
    assert all(x[i]==y[i] for i in queried)
    assert full_boolean_guard(x,carrier) is True and full_boolean_guard(y,carrier) is False

bench=[]
# compile JIT once before timing
if jit_complement_guard is not None:
    aa=np.zeros(32,np.complex128); cc=np.zeros(32,np.bool_); cc[:2]=True; jit_complement_guard(aa,cc)

for k in COUNTS:
    frac=k/N
    idx=np.sort(rng.choice(N,size=k,replace=False))
    carrier=np.zeros(N,dtype=np.bool_); carrier[idx]=True
    outside=~carrier; outside_idx=np.flatnonzero(outside)
    a=np.zeros(N,dtype=np.complex128)
    # populate carrier with nonzero complex values; no outside escape
    a[idx]=rng.normal(size=k)+1j*rng.normal(size=k)
    b=np.zeros(N,dtype=np.complex128)
    b[idx]=rng.normal(size=k)+1j*rng.normal(size=k)
    row={
        "carrier_fraction": frac,
        "carrier_count": int(k),
        "outside_count": int(N-k),
        "full_boolean": timed(full_boolean_guard,a,carrier),
        "boolean_complement": timed(boolean_complement_guard,a,outside),
        "index_complement": timed(index_complement_guard,a,outside_idx),
        "pair_full_boolean": timed(pair_full,a,b,carrier),
        "pair_boolean_complement": timed(pair_bool_comp,a,b,outside),
        "pair_index_complement": timed(pair_idx_comp,a,b,outside_idx),
    }
    if jit_complement_guard is not None:
        row["jit_complement"] = timed(jit_complement_guard,a,carrier)
        row["pair_jit_complement"] = timed(pair_jit,a,b,carrier)
    bench.append(row)

# pair guard = state + Source at step boundary, both mutable; exact query lower bound is 2*|outside| coefficient values in black-box coefficient-query model.
result={
    "seed":SEED,"N":N,"reps":REPS,"correctness_cases":len(correctness),
    "lower_bound": {
        "single_mutable_object_min_outside_value_queries": "|C^c|",
        "two_independently_mutable_objects_min_outside_value_queries": "2|C^c|",
        "scope": "deterministic exact black-box coefficient-query model; no trusted dirty bit/write barrier/mutation log",
        "reason": "an unqueried outside coefficient admits indistinguishable all-zero vs one-spike inputs"
    },
    "benchmarks":bench,
    "numba_available": jit_complement_guard is not None
}
print(json.dumps(result,indent=2))

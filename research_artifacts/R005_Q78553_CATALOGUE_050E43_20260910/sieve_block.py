"""Task-specific adapter around unchanged primesieve generation; half-open coverage."""
from __future__ import annotations
import argparse, hashlib, importlib.metadata, json, platform, sys, time
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
import primesieve
from primesieve.numpy import primes

def scan_block(lower: int, upper: int, threshold: int = 916) -> dict:
    if not (2 <= lower < upper <= 2**63):
        raise ValueError("Require 2 <= lower < upper <= 2^63.")
    if threshold < 1:
        raise ValueError("threshold must be positive")
    started = datetime.now(timezone.utc).isoformat()
    tick = time.perf_counter()
    values = primes(lower, upper - 1)
    if values.dtype != np.dtype("int64") or not values.flags.c_contiguous:
        raise ValueError("Unexpected primesieve NumPy carrier")
    count = int(values.size)
    first = int(values[0]) if count else None
    last = int(values[-1]) if count else None
    if count and not (lower <= first <= last < upper):
        raise ValueError("Prime endpoint leaves declared half-open block")
    differences = np.diff(values)
    if differences.size and int(differences.min()) <= 0:
        raise ValueError("Prime output is not strictly ordered")
    indices = np.flatnonzero(differences >= threshold)
    rows = [{"start":int(values[i]),"gap":int(differences[i]),"end":int(values[i+1])} for i in indices]
    max_i = int(differences.argmax()) if differences.size else None
    max_witness = None if max_i is None else {"start":int(values[max_i]),"gap":int(differences[max_i]),"end":int(values[max_i+1])}
    if sys.byteorder != "little":
        raise ValueError("This exact byte transcript requires little endian")
    digest = hashlib.sha256(memoryview(values.view("<u8")).cast("B")).hexdigest()
    elapsed = time.perf_counter() - tick
    return {
        "schema":"R005_PRIMESIEVE_HALF_OPEN_BLOCK_V1",
        "lower_inclusive":lower,"upper_exclusive":upper,
        "threshold":threshold,"prime_count":count,"first_prime":first,"last_prime":last,
        "max_internal_gap":0 if max_witness is None else max_witness["gap"],
        "max_internal_gap_witness":max_witness,
        "large_internal_gaps":rows,
        "prime_sequence_encoding":"uint64_le_in_strict_increasing_order",
        "prime_sequence_sha256":digest,
        "started_at":started,"completed_at":datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds":elapsed,
        "library_primesieve":primesieve.primesieve_version().decode("ascii"),
        "python_binding_primesieve":importlib.metadata.version("primesieve"),
        "numpy_version":np.__version__,"python_version":platform.python_version()
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--lower",type=int,required=True)
    p.add_argument("--upper",type=int,required=True)
    p.add_argument("--threshold",type=int,default=916)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    r=scan_block(a.lower,a.upper,a.threshold)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    if a.output.exists():
        raise FileExistsError("Preserve existing block output: "+str(a.output))
    a.output.write_text(json.dumps(r,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(r,sort_keys=True),flush=True)
if __name__=="__main__":
    main()


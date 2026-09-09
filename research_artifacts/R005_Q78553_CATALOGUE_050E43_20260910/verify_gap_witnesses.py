"""Independent trial-division certificates; does not call libprimesieve."""
import hashlib,importlib.util,json,sys
from math import isqrt
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
A=Path(__file__).resolve().parent
ROOT=A.parents[1]
def main():
    audit=json.loads((A/"construction_audit.json").read_text(encoding="utf-8"))
    assert audit["status"]=="PASS" and audit["all_four_independent_counts_match"]
    rows=audit["all_gaps_at_least_916"]+[x["max_within_cell_observed_gap"] for x in audit["independent_count_cells"]]+audit["cross_cell_pairs"]+[audit["global_max_observed_gap"]]
    unique={(r["start"],r["gap"]):r for r in rows}
    ordered=[unique[k] for k in sorted(unique)]
    limit=isqrt(max(r["end"] for r in ordered))
    path=ROOT/"src/enterprise_math/legendre.py"
    spec=importlib.util.spec_from_file_location("canonical_trial_division",path)
    reference=importlib.util.module_from_spec(spec);spec.loader.exec_module(reference)
    seed=reference.primes_up_to(isqrt(limit))
    flags=np.ones(limit+1,dtype=np.bool_);flags[:2]=False
    for p in seed:
        flags[p*p:limit+1:p]=False
    basis=np.flatnonzero(flags).astype(np.int64)
    del flags
    assert int(basis[0])==2 and int(basis[-1])<=limit
    basis_sha=hashlib.sha256(memoryview(basis.view("<u8")).cast("B")).hexdigest()
    def factor(n):
        stop=int(np.searchsorted(basis,isqrt(n),side="right"))
        begin=0
        for end in (min(stop,512),min(stop,4096),min(stop,65536),stop):
            if end>begin:
                block=basis[begin:end]
                hits=np.flatnonzero(n%block==0)
                if hits.size:
                    return int(block[int(hits[0])])
                begin=end
        return None
    out=A/"witness_certificates"
    out.mkdir(exist_ok=True)
    manifest=[]
    for r in ordered:
        start=r["start"];end=r["end"];gap=r["gap"]
        assert end-start==gap and gap%2==0 and start%2==1 and end%2==1
        endpoint_proofs=[]
        for n in (start,end):
            found=factor(n)
            assert found is None,("nonprime endpoint",n,found)
            count=int(np.searchsorted(basis,isqrt(n),side="right"))
            endpoint_proofs.append({"n":n,"prime":True,"method":"EXHAUSTIVE_DIVISION_BY_COMPLETE_REFERENCE_PRIME_BASIS",
                                  "trial_limit":isqrt(n),"tested_prime_count":count,
                                  "last_tested_prime":int(basis[count-1]),"basis_sha256":basis_sha})
        odd=[]
        for n in range(start+2,end,2):
            divisor=factor(n)
            assert divisor is not None,("interior prime",n)
            assert 1<divisor<n and n%divisor==0
            odd.append({"n":n,"factor":divisor,"cofactor":n//divisor})
        assert len(odd)==gap//2-1
        cert={"schema":"R005_INDEPENDENT_CONSECUTIVE_GAP_CERTIFICATE_V1",
              "start":start,"end":end,"gap":gap,"endpoint_primality_certificates":endpoint_proofs,
              "even_interior":{"first":start+1,"last":end-1,"step":2,"count":gap//2,"factor":2},
              "odd_interior_factor_witnesses":odd,"all_interior_count":gap-1,
              "all_verified":True}
        filename=f"gap_{start}_{gap}.json"
        target=out/filename
        if target.exists(): raise FileExistsError(str(target))
        raw=(json.dumps(cert,indent=2)+"\n").encode("utf-8")
        target.write_bytes(raw)
        manifest.append({"path":target.relative_to(A).as_posix(),"start":start,"gap":gap,
                         "bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()})
        print(json.dumps({"witness_verified":start,"gap":gap,"odd_factor_count":len(odd)}),flush=True)
    report={"schema":"R005_INDEPENDENT_WITNESS_VERIFICATION_V1","all_verified":True,
            "checked_at":datetime.now(timezone.utc).isoformat(),
            "reference_method":"Canonical integer trial division seeds plus independent Eratosthenes marking, then exhaustive endpoint trial division and explicit factors for every interior integer.",
            "canonical_seed_source_path":"src/enterprise_math/legendre.py",
            "canonical_seed_source_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
            "reference_basis_limit":limit,"reference_basis_count":int(basis.size),"reference_basis_sha256":basis_sha,
            "libprimesieve_called":False,"numpy_version":np.__version__,"python_version":sys.version,
            "catalogue_row_count":len(audit["task_gap_rows"]),
            "verified_catalogue_row_count":len(audit["task_gap_rows"]),
            "zero_catalogue_row_scope":"If this count is zero, relevant row checks are vacuous; full-band completeness comes from the separate completed construction audit.",
            "certificates":manifest}
    target=A/"independent_witness_verification.json"
    if target.exists(): raise FileExistsError(str(target))
    target.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"all_verified":True,"witness_count":len(manifest),"basis_primes":int(basis.size)}),flush=True)
if __name__=="__main__": main()


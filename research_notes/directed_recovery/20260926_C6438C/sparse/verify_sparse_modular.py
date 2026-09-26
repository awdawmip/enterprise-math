"""Actual BRC execution checks of the typed sparse compiler (no QFT reference)."""
from __future__ import annotations
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter_ns
import gzip, hashlib, json
from sparse_modular import (SparsePermutation, compile_modular_permutation,
    verify_modular_certificate, core_power, verify_vendor, CALLS, digest,
    sparse_modular_power_brc,sparse_modular_power_trace,sparse_modular_power_chain,
    sparse_classical_postprocess)
from stage78.shor_benchmark import modular_columns,modular_power_brc,classical_postprocess

ROOT=Path(__file__).resolve().parent

def equal_native_columns(N,b):
    start=perf_counter_ns();p,c=compile_modular_permutation(N,b);compile_ns=perf_counter_ns()-start
    verified=verify_modular_certificate(c)
    # Existing construction executes actual canonical BRC on every basis column.
    old=modular_columns(N,b)
    assert p.targets==old
    return p,c,{"N":N,"b":b,"compile_elapsed_ns":compile_ns,
      "all_original_native_columns_equal":True,**verified}

def serial_actual(p,q):
    n=len(p);graph=[[F(0)]*(3*n) for _ in range(3*n)]
    for y in range(n):graph[y][n+p[y]]=1;graph[n+y][2*n+q[y]]=1
    native=core_power(tuple(map(tuple,graph)),2);compiled=p.then(q)
    for y,row in enumerate(native[:n]):
        assert all(v==int(z==2*n+compiled[y]) for z,v in enumerate(row))
    assert compiled.provenance["left"]==p.provenance and compiled.provenance["right"]==q.provenance
    return {"carrier":n,"layered_native_states":3*n,"all_start_columns_equal":True}

def signed_naturality_actual(p,dim=61):
    n=len(p);graph=[[F(0)]*(2*n) for _ in range(2*n)]
    for y in range(n):
        for sign in (0,1):graph[2*y+sign][2*p[y]+sign]=1
    native=core_power(tuple(map(tuple,graph)),1)
    # Declared exact signed fibre input, with positive and negative companions.
    rows=tuple(tuple(F((y+1)*(j%7)-3*j,1+(j%3)) for j in range(dim)) for y in range(n))
    transported=p.transport_rows(rows)
    comparisons=0
    for z in range(n):
        for j in range(dim):
            pos=sum((max(rows[y][j],F(0))*native[2*y][2*z] + max(-rows[y][j],F(0))*native[2*y+1][2*z] for y in range(n)),F(0))
            neg=sum((max(rows[y][j],F(0))*native[2*y][2*z+1] + max(-rows[y][j],F(0))*native[2*y+1][2*z+1] for y in range(n)),F(0))
            assert pos-neg==transported[z][j];comparisons+=1
    assert sum(v*v for row in rows for v in row)==sum(v*v for row in transported for v in row)
    return {"carrier":n,"positive_sign_cover_states":2*n,"retained_modes":dim,
      "signed_coordinate_comparisons":comparisons,"character_commutes":True,"quadratic_norm_preserved":True}

def reject(thunk):
    try:thunk()
    except (ValueError,TypeError,AssertionError):return True
    raise AssertionError("invalid certificate/input was accepted")

def main():
    CALLS.clear();vendor=verify_vendor();cases=[];certificates={}
    for N,b in ((3,2),(5,2),(7,3),(15,2),(21,2),(21,20)):
        p,c,record=equal_native_columns(N,b);cases.append(record);certificates[f"{N}_{b}"]=c
    p,_=compile_modular_permutation(5,2);q,_=compile_modular_permutation(5,3)
    serial=serial_actual(p,q)
    controlled=p.controlled().native_dense_check()
    inverse=p.inverse().native_dense_check()
    assert p.then(p.inverse()).targets==tuple(range(len(p)))
    assert p.inverse().then(p).targets==tuple(range(len(p)))
    signs=signed_naturality_actual(p)
    exponent_traces=[]
    for exponent in range(32):
        assert sparse_modular_power_brc(21,2,exponent)==modular_power_brc(21,2,exponent)
        exponent_traces.append(sparse_modular_power_trace(21,2,exponent))
    powers,tables,origins=sparse_modular_power_chain(21,2,12)
    for i,b in enumerate(powers):
        assert b==modular_power_brc(21,2,1<<i)
        assert tables[i]==modular_columns(21,b)
        certificates[f"21_{b}"]=compile_modular_permutation(21,b)[1]
    postprocessing=[]
    for N,a,t in ((15,2,4),(21,2,6),(15,14,4)):
        rows=[]
        for k in range(1<<t):
            result=sparse_classical_postprocess(N,a,t,k)
            assert result==classical_postprocess(N,a,t,k)
            rows.append({"k":k,"result":result})
        postprocessing.append({"N":N,"a":a,"t":t,"complete_readouts":len(rows),"all_original_native_outputs_equal":True,"rows":rows})
    # Keep every modular-source certificate used by the native postprocessor.
    for N,a,t in ((15,2,4),(21,2,6),(15,14,4)):
        for b in sparse_modular_power_chain(N,a,t)[0]:
            certificates[f"{N}_{b}"]=compile_modular_permutation(N,b)[1]
    bad=[]
    original=certificates["21_2"]
    def mutated(kind):
        c=deepcopy(original)
        if kind=="digit":
            cells=list(c["steps"][1]["add_b"]["cells"]);cell=list(cells[0]);cell[2]^=1;cells[0]=tuple(cell);c["steps"][1]["add_b"]["cells"]=tuple(cells)
        elif kind=="target":c["targets"]=tuple(reversed(c["targets"]))
        elif kind=="missing_column":c["steps"]=c["steps"][:-1]
        elif kind=="edge_id":c["steps"][1]["edge_id"]=c["steps"][0]["edge_id"]
        elif kind=="tail":c["identity_tail"]["first"]+=1
        elif kind=="resource":c["resource_counts"]["adder_digit_applications"]-=1
        return c
    for kind in ("digit","target","missing_column","edge_id","tail","resource"):
        bad.append({"mutation":kind,"rejected":reject(lambda kind=kind:verify_modular_certificate(mutated(kind)))})
    bad.append({"mutation":"noncoprime_N21_b3","rejected":reject(lambda:compile_modular_permutation(21,3))})
    bad.append({"mutation":"duplicate_permutation_column","rejected":reject(lambda:SparsePermutation((0,0),{}))})
    large=[]
    for N,b in ((33,2),(257,3),(1009,37)):
        before=len(CALLS);started=perf_counter_ns();p,c=compile_modular_permutation(N,b)
        verified=verify_modular_certificate(c)
        large.append({"N":N,"b":b,"elapsed_ns":perf_counter_ns()-started,**verified,
          "new_dense_BRC_calls":len(CALLS)-before,"method":"actual certified full-adder columns reused; full provenance replay"})
        certificates[f"{N}_{b}"]=c
    out=ROOT/"output";out.mkdir(exist_ok=True)
    data=json.dumps(certificates,sort_keys=True,separators=(",",":")).encode()
    (out/"CERTIFICATES.json.gz").write_bytes(gzip.compress(data,mtime=0))
    result={"status":"PASS_AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED",
      "researcher":"EM-DIRECT-C6438C","activity":"RA-CAAAC604CB513AEA8BBC1DFC",
      "registration_source":"f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf",
      "frozen_source_head":"0852cad130c1d877174d235687cf60c19f318c58",
      "vendor":vendor,"small_native_equalities":cases,"serial":serial,
      "controlled_direct_sum":controlled,"inverse":inverse,"signed_fibres":signs,
      "modular_exponents":{"N":21,"a":2,"all_32_native_equalities":True,"traces":exponent_traces},
      "power_chain":{"N":21,"a":2,"powers":powers,"origins":origins,"all_12_native_equalities":True},
      "postprocessing":postprocessing,
      "rejected_negative_controls":bad,"larger_sparse_cases":large,"native_calls":CALLS,
      "certificate_file":{"path":"CERTIFICATES.json.gz","uncompressed_sha256":hashlib.sha256(data).hexdigest(),"uncompressed_bytes":len(data)},
      "general_claim_evidence":"SPARSE_MODULAR_PROOF.md, not finite case extrapolation",
      "not_claimed":["polynomial in logN", "new phase construction", "generic signed BRC core", "order oracle", "independent review"]}
    (out/"RESULTS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    manifest={}
    for path in (ROOT/"sparse_modular.py",ROOT/"verify_sparse_modular.py",ROOT/"SPARSE_MODULAR_PROOF.md",out/"RESULTS.json",out/"CERTIFICATES.json.gz"):
        raw=path.read_bytes();manifest[str(path.relative_to(ROOT))]={"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"git_blob":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
    (out/"MANIFEST.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"small_cases":len(cases),"native_basis_columns":sum(c["complete_columns"] for c in cases),
      "signed_comparisons":signs["signed_coordinate_comparisons"],"negative_controls":len(bad),
      "modular_exponents":len(exponent_traces),"power_chain_length":len(powers),
      "postprocess_exact_readouts":sum(c["complete_readouts"] for c in postprocessing),
      "large_columns":[c["complete_columns"] for c in large],"native_calls":len(CALLS),"output":str(out)},indent=2))

if __name__=="__main__":main()

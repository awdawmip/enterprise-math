"""Construct this task's labelled gap catalogue with unchanged libprimesieve.

The scan covers half-open integer blocks. Internal pairs plus the boundary pair
between consecutive nonempty blocks enumerate every consecutive pair from the
first emitted prime through the last. A catalogue is left UNATTESTED until the
separate independent count/coverage audit succeeds.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, sys, time
from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED
from datetime import datetime, timezone
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from sieve_block import scan_block

BAND_LOWER=1291005053866735
BAND_UPPER=1294364244470160
Q=78553
THRESHOLD=916

def write_json_new(path, value):
    path=Path(path)
    data=(json.dumps(value,indent=2)+"\n").encode("utf-8")
    if path.exists():
        if path.read_bytes()!=data:
            raise FileExistsError("Do not overwrite an existing different artifact: "+str(path))
        return
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("xb") as f:
        f.write(data)

def worker(job):
    index,lower,upper,output=job
    result=scan_block(lower,upper,THRESHOLD)
    result["block_index"]=index
    write_json_new(output,result)
    return result

def accepted_scanner():
    path=HERE.parents[1]/"experiments/r005a_p2_gap_shadow_inversion.py"
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    if digest!="6fe2dc9fe05ac16ef2bbd1919d3d03fc5b36037d010ca95afeafb62f4958d3f5":
        raise RuntimeError("Accepted scanner bytes drifted")
    spec=importlib.util.spec_from_file_location("r005_accepted_scanner",path)
    m=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=m
    spec.loader.exec_module(m)
    return m

def reduce_blocks(blocks, lower, upper, width):
    blocks=sorted(blocks,key=lambda b:b["block_index"])
    expected_count=(upper-lower+width-1)//width
    if len(blocks)!=expected_count:
        raise ValueError("Missing or duplicate coverage blocks")
    previous_last=None
    previous_index=None
    first=None
    rows=[]
    max_gap=0
    max_witness=None
    bridge_count=0
    count=0
    for i,b in enumerate(blocks):
        lo=lower+i*width
        hi=min(upper,lo+width)
        if b["block_index"]!=i or b["lower_inclusive"]!=lo or b["upper_exclusive"]!=hi:
            raise ValueError("Blocks do not form the declared exact half-open partition")
        if b["threshold"]!=THRESHOLD:
            raise ValueError("Incomplete gap threshold")
        n=b["prime_count"]
        f=b["first_prime"];l=b["last_prime"]
        if not isinstance(n,int) or n<0 or ((n==0)!=(f is None and l is None)):
            raise ValueError("Inconsistent block count/endpoints")
        count+=n
        if n:
            if not (lo<=f<=l<hi):
                raise ValueError("Prime endpoints leave block")
            if first is None:
                first=f
            if previous_last is not None:
                gap=f-previous_last
                if gap<=0:
                    raise ValueError("Non-increasing cross-block prime sequence")
                bridge_count+=1
                witness={"start":previous_last,"gap":gap,"end":f,
                         "origin":"cross_block","left_block":previous_index,"right_block":i}
                if gap>max_gap:
                    max_gap=gap;max_witness=witness
                if gap>=THRESHOLD:
                    rows.append(witness)
            previous_last=l;previous_index=i
        m=b["max_internal_gap"]
        witness=b["max_internal_gap_witness"]
        if m>max_gap:
            max_gap=m;max_witness={**witness,"origin":"internal","block_index":i}
        for row in b["large_internal_gaps"]:
            if not (lo<=row["start"]<row["end"]<hi) or row["end"]-row["start"]!=row["gap"] or row["gap"]<THRESHOLD:
                raise ValueError("Invalid reported internal gap")
            rows.append({**row,"origin":"internal","block_index":i})
    rows.sort(key=lambda r:(r["start"],r["gap"]))
    if len({(r["start"],r["gap"]) for r in rows})!=len(rows):
        raise ValueError("Duplicate reported consecutive gap")
    if first is None or not (first<=BAND_LOWER and previous_last>BAND_UPPER):
        raise ValueError("Observed endpoint primes do not bracket the entire task band")
    return {"schema":"R005_COMPLETE_PRIME_SEQUENCE_REDUCTION_V1",
            "scan_lower_inclusive":lower,"scan_upper_exclusive":upper,
            "block_width":width,"block_count":len(blocks),"prime_count":count,
            "first_prime":first,"last_prime":previous_last,
            "covered_gap_start_lower":first,"covered_gap_start_upper":previous_last-1,
            "internal_pair_count":sum(max(0,b["prime_count"]-1) for b in blocks),
            "cross_block_pair_count":bridge_count,
            "all_pair_count":count-1,
            "max_gap":max_gap,"max_gap_witness":max_witness,
            "all_gaps_at_least_threshold":rows,
            "task_band_gaps_at_least_threshold":[r for r in rows if BAND_LOWER<=r["start"]<=BAND_UPPER],
            "completeness_attestation":False,
            "status":"FULL_SCAN_COMPLETED_PENDING_INDEPENDENT_AUDIT"}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--lower",type=int,required=True)
    p.add_argument("--upper",type=int,required=True)
    p.add_argument("--block-width",type=int,default=10**9)
    p.add_argument("--workers",type=int,default=3)
    p.add_argument("--output-dir",type=Path,required=True)
    p.add_argument("--reuse-block-json",type=Path,action="append",default=[])
    a=p.parse_args()
    if not (a.lower<=BAND_LOWER<BAND_UPPER<a.upper and a.block_width>0 and 1<=a.workers<=os.cpu_count()):
        raise ValueError("Invalid frozen-band construction parameters")
    source_files=["sieve_block.py","construct_catalogue.py"]
    inputs={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in source_files}
    out=a.output_dir
    out.mkdir(parents=True,exist_ok=True)
    blocks_dir=out/"blocks"
    blocks_dir.mkdir(exist_ok=True)
    manifest={"schema":"R005_CATALOGUE_CONSTRUCTION_RUN_V1","lower_inclusive":a.lower,
              "upper_exclusive":a.upper,"block_width":a.block_width,"workers":a.workers,
              "threshold":THRESHOLD,"q":Q,"task_band":[BAND_LOWER,BAND_UPPER],
              "source_sha256":inputs,"interpreter":sys.executable,
              "initial_observations":[{"path":str(x),"sha256":hashlib.sha256(x.read_bytes()).hexdigest()} for x in a.reuse_block_json]}
    manifest_path=out/"run_manifest.json"
    write_json_new(manifest_path,manifest)
    total=(a.upper-a.lower+a.block_width-1)//a.block_width
    completed={}
    for path in a.reuse_block_json:
        b=json.loads(path.read_text(encoding="utf-8"))
        offset=b["lower_inclusive"]-a.lower
        index=offset//a.block_width
        if offset<0 or offset%a.block_width or b["upper_exclusive"]!=min(a.upper,b["lower_inclusive"]+a.block_width) or b["threshold"]!=THRESHOLD:
            raise ValueError("Reusable block does not match exact partition")
        b["block_index"]=index
        write_json_new(blocks_dir/f"{index:05d}.json",b)
    for path in blocks_dir.glob("*.json"):
        b=json.loads(path.read_text(encoding="utf-8"))
        i=b["block_index"]
        if i in completed or not 0<=i<total or b["lower_inclusive"]!=a.lower+i*a.block_width or b["upper_exclusive"]!=min(a.upper,a.lower+(i+1)*a.block_width):
            raise ValueError("Invalid saved coverage record")
        completed[i]=b
    scanner=accepted_scanner()
    seam=scanner.build_seam(Q)
    checked=set()
    def inspect_row(row):
        key=(row["start"],row["gap"])
        if key in checked or not BAND_LOWER<=row["start"]<=BAND_UPPER:
            return
        checked.add(key)
        if row["gap"]>THRESHOLD:
            write_json_new(out/"gap_bound_contradiction_alert.json",row)
            raise RuntimeError("Reported task-band gap contradicts frozen bound; inspect exact witness")
        candidates=scanner.scan_gap_shadows(seam,[scanner.GapRow(row["start"],row["gap"])])
        if candidates:
            scanner.verify_consecutive_gap(scanner.GapRow(row["start"],row["gap"]))
            write_json_new(out/"candidate_alert.json",{"gap":row,"candidates":candidates,
                           "status":"ACCEPTED_SCANNER_CANDIDATE_REQUIRES_INDEPENDENT_VERIFICATION"})
            raise RuntimeError("Exact scanner candidate found; stop construction for independent verification")
    def inspect_block(b):
        for row in b["large_internal_gaps"]:
            inspect_row(row)
        i=b["block_index"]
        for left,right in ((i-1,i),(i,i+1)):
            if left in completed and right in completed:
                u=completed[left];v=completed[right]
                if u["last_prime"] is not None and v["first_prime"] is not None:
                    gap=v["first_prime"]-u["last_prime"]
                    if gap>=THRESHOLD:
                        inspect_row({"start":u["last_prime"],"gap":gap,"end":v["first_prime"],"origin":"cross_block"})
    for b in list(completed.values()):
        inspect_block(b)
    missing=iter(i for i in range(total) if i not in completed)
    tick=time.perf_counter()
    def job(i):
        return (i,a.lower+i*a.block_width,min(a.upper,a.lower+(i+1)*a.block_width),str(blocks_dir/f"{i:05d}.json"))
    print(json.dumps({"event":"START","total_blocks":total,"reused_blocks":len(completed),"workers":a.workers}),flush=True)
    with ProcessPoolExecutor(max_workers=a.workers) as pool:
        pending={}
        for _ in range(a.workers):
            i=next(missing,None)
            if i is not None: pending[pool.submit(worker,job(i))]=i
        while pending:
            done,_=wait(pending,return_when=FIRST_COMPLETED)
            for future in done:
                index=pending.pop(future)
                b=future.result()
                completed[index]=b
                inspect_block(b)
                if len(completed)%25==0 or b["large_internal_gaps"]:
                    print(json.dumps({"event":"PROGRESS","completed_blocks":len(completed),"total_blocks":total,
                         "elapsed_seconds":round(time.perf_counter()-tick,3),"last_block":index,
                         "large_gaps_in_last_block":len(b["large_internal_gaps"])}),flush=True)
                i=next(missing,None)
                if i is not None: pending[pool.submit(worker,job(i))]=i
    reduction=reduce_blocks(list(completed.values()),a.lower,a.upper,a.block_width)
    reduction["completed_at"]=datetime.now(timezone.utc).isoformat()
    reduction["elapsed_run_seconds"]=time.perf_counter()-tick
    write_json_new(out/"construction_reduction.json",reduction)
    print(json.dumps({"event":"COMPLETE","block_count":total,"prime_count":reduction["prime_count"],
         "max_gap":reduction["max_gap"],"task_gap_rows":len(reduction["task_band_gaps_at_least_threshold"]),
         "elapsed_seconds":reduction["elapsed_run_seconds"]}),flush=True)

if __name__=="__main__":
    main()


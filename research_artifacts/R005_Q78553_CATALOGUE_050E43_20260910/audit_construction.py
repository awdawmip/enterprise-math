"""Independent integer audit of completed coverage records and published counts."""
import hashlib,json
from pathlib import Path
from datetime import datetime,timezone
A=Path(__file__).resolve().parent
R=A/"construction_full"
LOWER=1291000000000000
UPPER=1295000000000000
WIDTH=1000000000
BAND=(1291005053866735,1294364244470160)
def sha(b): return hashlib.sha256(b).hexdigest()
def write_new(name,obj):
    p=A/name
    if p.exists(): raise FileExistsError(str(p))
    p.write_text(json.dumps(obj,indent=2)+"\n",encoding="utf-8")
def main():
    run=json.loads((R/"run_manifest.json").read_text(encoding="utf-8"))
    assert (run["lower_inclusive"],run["upper_exclusive"],run["block_width"],run["threshold"])==(LOWER,UPPER,WIDTH,916)
    for name,digest in run["source_sha256"].items():
        assert sha((A/name).read_bytes())==digest,(name,"source changed during run")
    targets=json.loads((A/"independent-prime-count-targets.json").read_text(encoding="utf-8"))
    assert sha((A/"tos-primecount-1d12.txt").read_bytes())==targets["source_decoded_sha256"]
    paths=sorted((R/"blocks").glob("*.json"))
    assert len(paths)==4000
    blocks=[];input_manifest=[];internal_rows=[];maxima=[];versions=set()
    for i,path in enumerate(paths):
        raw=path.read_bytes();b=json.loads(raw)
        assert path.name==f"{i:05d}.json" and b["block_index"]==i
        assert (b["lower_inclusive"],b["upper_exclusive"])==(LOWER+i*WIDTH,LOWER+(i+1)*WIDTH)
        assert b["schema"]=="R005_PRIMESIEVE_HALF_OPEN_BLOCK_V1" and b["threshold"]==916
        assert isinstance(b["prime_count"],int) and b["prime_count"]>=2
        assert b["lower_inclusive"]<=b["first_prime"]<b["last_prime"]<b["upper_exclusive"]
        assert len(b["prime_sequence_sha256"])==64
        versions.add((b["library_primesieve"],b["python_binding_primesieve"],b["numpy_version"],b["python_version"]))
        witness=b["max_internal_gap_witness"]
        assert witness["end"]-witness["start"]==witness["gap"]==b["max_internal_gap"]
        assert b["first_prime"]<=witness["start"]<witness["end"]<=b["last_prime"]
        maxima.append({**witness,"origin":"internal","block_index":i})
        for row in b["large_internal_gaps"]:
            assert row["end"]-row["start"]==row["gap"] and 916<=row["gap"]<=b["max_internal_gap"]
            assert b["first_prime"]<=row["start"]<row["end"]<=b["last_prime"]
            internal_rows.append({**row,"origin":"internal","block_index":i})
        if b["max_internal_gap"]>=916:
            assert witness in b["large_internal_gaps"]
        input_manifest.append({"path":path.relative_to(A).as_posix(),"bytes":len(raw),"sha256":sha(raw)})
        blocks.append(b)
    assert versions=={("7.5","2.3.0","1.26.4","3.9.13")}
    bridges=[]
    for left,right in zip(blocks,blocks[1:]):
        row={"start":left["last_prime"],"end":right["first_prime"],
             "gap":right["first_prime"]-left["last_prime"],"origin":"cross_block",
             "left_block":left["block_index"],"right_block":right["block_index"]}
        assert row["gap"]>0
        bridges.append(row)
    total=sum(b["prime_count"] for b in blocks)
    internal_pairs=sum(b["prime_count"]-1 for b in blocks)
    assert internal_pairs+len(bridges)==total-1
    cells=[]
    for i,target in enumerate(targets["cells"]):
        segment=blocks[i*1000:(i+1)*1000]
        count=sum(b["prime_count"] for b in segment)
        assert count==target["expected_prime_count"],(i,count,target["expected_prime_count"])
        candidates=maxima[i*1000:(i+1)*1000]+bridges[i*1000:(i+1)*1000-1]
        maximum=max(candidates,key=lambda r:(r["gap"],-r["start"]))
        cells.append({**target,"observed_prime_count":count,"count_match":True,
                      "first_prime":segment[0]["first_prime"],"last_prime":segment[-1]["last_prime"],
                      "max_within_cell_observed_gap":maximum})
    assert total==targets["expected_total_count"]
    maximum=max(maxima+bridges,key=lambda r:(r["gap"],-r["start"]))
    assert maximum["gap"]<=916,("observed gap exceeds frozen G",maximum)
    rows=sorted(internal_rows+[r for r in bridges if r["gap"]>=916],key=lambda r:r["start"])
    assert len({r["start"] for r in rows})==len(rows)
    task_rows=[r for r in rows if BAND[0]<=r["start"]<=BAND[1]]
    first=blocks[0]["first_prime"];last=blocks[-1]["last_prime"]
    assert first<=BAND[0]<BAND[1]<last
    reduction=json.loads((R/"construction_reduction.json").read_text(encoding="utf-8"))
    assert reduction["prime_count"]==total and reduction["block_count"]==4000
    assert reduction["internal_pair_count"]==internal_pairs and reduction["cross_block_pair_count"]==len(bridges)
    assert reduction["all_pair_count"]==total-1 and reduction["max_gap"]==maximum["gap"]
    assert [(r["start"],r["gap"],r["end"]) for r in reduction["all_gaps_at_least_threshold"]]==[(r["start"],r["gap"],r["end"]) for r in rows]
    result={"schema":"R005_FULL_CONSTRUCTION_INDEPENDENT_AUDIT_V1","status":"PASS",
            "checked_at":datetime.now(timezone.utc).isoformat(),"block_count":4000,
            "scan_half_open":[LOWER,UPPER],"task_gap_start_band":list(BAND),
            "covered_gap_start_interval":[first,last-1],"prime_count":total,
            "internal_pair_count":internal_pairs,"cross_block_pair_count":len(bridges),"all_pair_count":total-1,
            "independent_count_cells":cells,"all_four_independent_counts_match":True,
            "global_max_observed_gap":maximum,"all_gaps_at_least_916":rows,"task_gap_rows":task_rows,
            "cross_cell_pairs":[bridges[i] for i in (999,1999,2999)],
            "all_cross_block_gaps_above_916":[r for r in bridges if r["gap"]>916],
            "source_code_sha256":run["source_sha256"],"implementation_versions":[list(x) for x in versions],
            "attestation_not_yet_granted":"Independent endpoint/interior witnesses and final scanner remain separate steps."}
    write_new("construction_input_byte_manifest.json",{"schema":"R005_RAW_BLOCK_BYTE_MANIFEST_V1","files":input_manifest})
    write_new("construction_audit.json",result)
    pure_rows=[{"start":r["start"],"gap":r["gap"]} for r in task_rows]
    rows_digest=sha("".join(f'{r["start"]},{r["gap"]}\n' for r in pure_rows).encode("ascii"))
    catalogue={"schema":"R005A_CONSECUTIVE_PRIME_GAP_CATALOG_V1",
               "source_id":"R005_Q78553_COMPLETE_SEGMENTED_SIEVE_050E43",
               "coverage_start":BAND[0],"coverage_end":BAND[1],"complete_for_gap_ge":916,
               "max_gap_bound":maximum["gap"],"max_gap_bound_start":first,"max_gap_bound_end":last-1,
               "completeness_attestation":False,"rows":pure_rows,"rows_sha256":rows_digest,
               "construction_audit_path":"research_artifacts/R005_Q78553_CATALOGUE_050E43_20260910/construction_audit.json"}
    write_new("catalogue.unattested.json",catalogue)
    print(json.dumps({"audit_status":"PASS","prime_count":total,"blocks":4000,"max_gap":maximum,
                      "all_rows_ge916":len(rows),"task_rows":len(task_rows),"independent_counts_match":True}),flush=True)
if __name__=="__main__": main()


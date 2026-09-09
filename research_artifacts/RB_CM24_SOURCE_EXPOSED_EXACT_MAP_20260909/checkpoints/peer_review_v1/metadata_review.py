"""Read-only byte/format checks and a --help-only archived-entry probe; no mathematics."""
import datetime as dt
import hashlib, json, os, subprocess, sys, time
from pathlib import Path
root=Path(sys.argv[1]).resolve(); out=Path(sys.argv[2]).resolve()
rel="research_artifacts/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909"
run=root.joinpath(rel,"runs","identity_v1")
h=lambda b:hashlib.sha256(b).hexdigest()
paths={"frozen_checker":run.joinpath("check_exact_map.py.frozen"),
       "source_freeze":root.joinpath(rel,"source_freeze.json"),
       "certificate":run.joinpath("certificate.json"),"receipt":run.joinpath("receipt.json"),
       "policy":root.joinpath(rel,"execution_policy.json"),
       "stdout":run.joinpath("stdout.txt"),"stderr":run.joinpath("stderr.txt")}
raw={k:p.read_bytes() for k,p in paths.items()}
expected={"frozen_checker":"dea05305c92545ddbf97e521310c0ba1f103213020945750b810e2c8ebc9dd63",
"source_freeze":"85946a8cb4e736021cef6cd311c8cfffbde1cce34fe728255db4b6703f5887f2",
"certificate":"c11db2a62c2c1926306117abcac0495ed7a518ae37e1fb6fbd27bfdd75ef6ab8",
"receipt":"d67a19adaf231cca83394206e865d2b5a869034ffef78530e5cc1ab6b8ba7a36"}
for k,v in expected.items(): assert h(raw[k])==v,(k,h(raw[k]))
cert=json.loads(raw["certificate"]); receipt=json.loads(raw["receipt"]); freeze=json.loads(raw["source_freeze"])
checks={}
for label,key in (("checker_sha256","frozen_checker"),("source_freeze_sha256","source_freeze"),
                  ("certificate_sha256","certificate"),("stdout_sha256","stdout"),("stderr_sha256","stderr")):
    checks[label]=receipt[label]==h(raw[key])
checks["certificate_source_pin"]=cert["source_freeze_sha256"]==h(raw["source_freeze"])
checks["certificate_policy_pin"]=cert["resource_policy_sha256"]==h(raw["policy"])
checks["exact_canonical_serialization"]=(json.dumps(cert,ensure_ascii=False,sort_keys=True,indent=2)+"\n").encode()==raw["certificate"]
checks["complete_remainder_empty"]=cert["complete_ring_remainder"]==[]
source_pins=[]
for pin in freeze["source_pins"]:
    src=root.joinpath(pin["path"]).read_bytes()
    source_pins.append({"path":pin["path"],"sha256":h(src),"expected_sha256":pin["sha256"],"matches":h(src)==pin["sha256"]})
checks["all_frozen_source_pins"]=all(p["matches"] for p in source_pins)
rows={}
for name in ("N","D0","k","lambda","C4","W"):
    terms=cert[name]
    exps=[tuple(x["exponents"]) for x in terms]
    valid=all(len(m)==10 and all(type(x)is int and x>=0 for x in m) and
              m[0]<4 and m[1]<2 and m[2]<2 and m[7]<2 and
              all(m[i]==0 for i in (3,4,5,8,9)) and
              type(row["coefficient"]) is int and row["coefficient"]!=0
              for row,m in zip(terms,exps))
    rows[name]={"terms":len(terms),"valid_reduced_shape":valid,"ordered_unique":exps==sorted(set(exps))}
checks["all_serialized_polynomial_shapes"]=all(x["valid_reduced_shape"] and x["ordered_unique"] for x in rows.values())
assert all(checks.values()),checks
env=os.environ.copy(); env.pop("PYTHONPATH",None)
argv=[sys.executable,"-B","-X","utf8",str(paths["frozen_checker"]),"--root",str(root),"--help"]
started=dt.datetime.now(dt.timezone.utc); tick=time.perf_counter()
proc=subprocess.run(argv,cwd=out,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=15)
(out/"archive-help.stdout").write_bytes(proc.stdout); (out/"archive-help.stderr").write_bytes(proc.stderr)
after={k:h(p.read_bytes()) for k,p in paths.items()}
assert after=={k:h(v) for k,v in raw.items()},after
report={"schema":"RB_CM24_IDENTITY_V1_PEER_SOURCE_REVIEW_V1","scope":"Source-exposed peer code/evidence review; no mathematical execution, no blind reproduction, no formal Driver disposition.",
"source_hashes":{k:{"path":str(paths[k]),"sha256":h(v),"bytes":len(v)} for k,v in raw.items()},
"metadata_checks":checks,"source_pins":source_pins,"serialized_rows":rows,
"author_actual_run":{"argv":receipt["argv"],"exit_code":receipt["exit_code"],"elapsed_nanoseconds":receipt["elapsed_nanoseconds"],"certificate_arithmetic":cert["arithmetic"],"remaining_gates":cert["remaining_gates"]},
"archive_entry_probe":{"argv":argv,"cwd":str(out),"PYTHONPATH":"absent for this child only","started_at":started.isoformat(),
"seconds":time.perf_counter()-tick,"exit_code":proc.returncode,"stdout_sha256":h(proc.stdout),"stderr_sha256":h(proc.stderr),"stderr":proc.stderr.decode("utf-8"),"math_executed":False},
"frozen_inputs_preserved":True,"completed_at":dt.datetime.now(dt.timezone.utc).isoformat()}
p=out/"review.json"; p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"metadata_checks":checks,"row_counts":{k:v["terms"] for k,v in rows.items()},"archive_help_exit":proc.returncode,
"archive_help_stderr":proc.stderr.decode("utf-8"),"receipt":str(p),"sha256":h(p.read_bytes())},ensure_ascii=False,indent=2))

from pathlib import Path
import json,hashlib
T=Path(r"D:/em/TEMP/r005-q78553-review-81273a-20260910")
WR=Path(r"D:/em/r005-q78553-research-050e43-20260910")
DEST=T/"frozen_science"
inputs=json.loads((T/"review_frozen_inputs.json").read_text(encoding="utf-8"))
def blob(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def sha(b):return hashlib.sha256(b).hexdigest()
rr_raw=inputs["result"]["content"].encode("utf-8")
assert sha(rr_raw)=="f8114a88ec3566fab477ea7c093ae35dec00fa53148d5f7a41c4de07cdcd5eec"
assert blob(rr_raw)=="dada488146abf7d728eedc2c6bf3e882e5ff888e"
rr=json.loads(rr_raw); rows=rr["output_manifest"]
assert len(rows)==105 and len({r["path"] for r in rows})==105
fm_raw=inputs["manifest"]["content"].encode("utf-8")
assert blob(fm_raw)=="ac01abba56abc91bda0b22d2288b675db5040d90"
fm=json.loads(fm_raw); source={f["path"]:f for f in fm["source_files"]}
assert len(source)==104
receipts=[]
def write_exact(p,data):
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists():
        assert p.read_bytes()==data,str(p)
    else:p.write_bytes(data)
for f in rows:
    path=f["path"];raw=(WR/path).read_bytes()
    assert sha(raw)==f["sha256"].split(":")[-1] and blob(raw)==f["git_blob_sha1"].split(":")[-1],path
    if path in source:
        q=source[path]
        assert len(raw)==q["bytes"] and sha(raw)==q["sha256"] and blob(raw)==q["git_blob_sha1"]
    else:assert path.endswith("/FINAL_SOURCE_MANIFEST.json") and raw==fm_raw
    write_exact(DEST/path,raw)
    receipts.append({"path":path,"bytes":len(raw),"sha256":sha(raw),"git_blob_sha1":blob(raw)})
for path in ["experiments/r005a_p2_gap_shadow_inversion.py","src/enterprise_math/legendre.py"]:
    raw=(WR/path).read_bytes()
    if path.startswith("experiments"):assert sha(raw)=="6fe2dc9fe05ac16ef2bbd1919d3d03fc5b36037d010ca95afeafb62f4958d3f5"
    write_exact(DEST/path,raw)
    receipts.append({"path":path,"bytes":len(raw),"sha256":sha(raw),"git_blob_sha1":blob(raw),"frozen_dependency":True})
out={"schema":"R005_DRIVER_FROZEN_SCIENCE_LOCAL_MATERIALIZATION_V1","science_source":rr["owner_head"],"result_source":inputs["result_source"],"result_id":rr["result_id"],"output_file_count":len(rows),"root":str(DEST),"all_local_files_match_immutable_result_manifest":True,"files":receipts}
(T/"frozen_science_materialization.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!="files"},ensure_ascii=True))


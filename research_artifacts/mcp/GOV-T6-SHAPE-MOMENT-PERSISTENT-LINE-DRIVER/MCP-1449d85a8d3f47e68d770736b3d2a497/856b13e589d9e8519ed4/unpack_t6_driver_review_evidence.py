"""Lossless extraction of the exact Source Driver review evidence bundle."""
import argparse,base64,gzip,hashlib,importlib.util,json
from pathlib import Path

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("pack",nargs="?",default="T6_Q2_1_DRIVER_REVIEW_AND_271_DIRECTION_EVIDENCE_PACKED.json")
parser.add_argument("destination",nargs="?",default="restored_driver_review_evidence")
parser.add_argument("--common-dir",type=Path,help="Exact Source portable_input.json and order2_problem.json directory")
parser.add_argument("--q2-source-dir",type=Path,help="All11 exact q2-1 Source files, by basename")
parser.add_argument("--review-work-dir",type=Path,default=Path("portable_independent_review"))
args=parser.parse_args();pack_path=Path(args.pack);destination=Path(args.destination)
p=json.loads(pack_path.read_bytes())
raw=gzip.decompress(base64.b64decode(p["payload"],validate=True))
assert len(raw)==p["original_bytes"]
assert hashlib.sha256(raw).hexdigest()==p["original_sha256"]
files=json.loads(raw)["files"]
pins={x["path"]:x for x in p["files"]}
assert len(files)==len(pins)==p["file_count"]
for f in files:
    relative=Path(f["path"])
    assert not relative.is_absolute() and ".." not in relative.parts
    b=f["content"].encode("utf-8");m=pins[f["path"]]
    assert len(b)==m["bytes"] and hashlib.sha256(b).hexdigest()==m["sha256"]
    assert hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()==m["git_blob_sha1"]
    target=destination/relative;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(b)
print("Verified and restored",len(files),"exact originals; no scientific checker executed")

if args.common_dir is not None or args.q2_source_dir is not None:
    assert args.common_dir is not None and args.q2_source_dir is not None
    # The original captured custody manifest remains unchanged. A derived
    # copy changes filesystem locations only; every Source digest/blob and
    # immutable commit is retained and rechecked by the unmodified checker.
    original=destination/"IMMUTABLE_Q2_1_COMPLETE_SOURCE_VERIFIED.json"
    manifest=json.loads(original.read_bytes());work=args.review_work_dir
    assert work.resolve()!=destination.resolve()
    for pin in manifest["rows"]:
        name=Path(pin["path"]).name;source_file=args.q2_source_dir/name
        b=source_file.read_bytes()
        assert len(b)==pin["bytes"] and hashlib.sha256(b).hexdigest()==pin["sha256"]
        assert hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()==pin["git_blob_sha1"]
        new_file=work/"source"/name;new_file.parent.mkdir(parents=True,exist_ok=True)
        new_file.write_bytes(b);pin["local_path"]=str(new_file.resolve())
    manifest["derived_path_binding_only_from_original_sha256"]=hashlib.sha256(original.read_bytes()).hexdigest()
    (work/"IMMUTABLE_Q2_1_COMPLETE_SOURCE_VERIFIED.json").write_text(json.dumps(manifest,indent=2)+"\n")
    spec=importlib.util.spec_from_file_location("independent_q2_review",destination/"reviewer_q2_1_exact_check.py")
    checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
    checker.HERE=work.resolve();checker.COMMON=args.common_dir.resolve()
    checker.q2_1_source_check()
    print("Reproduced q2-1 independent review from supplied exact Source files; no other pattern executed")

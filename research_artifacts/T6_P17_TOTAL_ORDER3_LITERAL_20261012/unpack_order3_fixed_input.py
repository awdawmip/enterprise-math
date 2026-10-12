"""Verify and restore prospective fixed inputs; execute no scientific search."""
import argparse,base64,gzip,hashlib,json
from pathlib import Path

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("package",type=Path)
parser.add_argument("destination",type=Path)
args=parser.parse_args()
p=json.loads(args.package.read_bytes())
assert p["schema"]=="T6_ORDER3_PROSPECTIVE_FIXED_INPUT_LOSSLESS_PACKAGE_V1"
compressed=base64.b64decode(p["payload"],validate=True)
assert hashlib.sha256(compressed).hexdigest()==p["gzip_sha256"]
raw=gzip.decompress(compressed)
assert len(raw)==p["original_container_bytes"] and hashlib.sha256(raw).hexdigest()==p["original_container_sha256"]
rows=json.loads(raw)["files"];pins={x["path"]:x for x in p["files"]}
assert len(rows)==len(pins)==p["file_count"]
for row in rows:
    relative=Path(row["path"]);assert not relative.is_absolute() and ".." not in relative.parts
    b=base64.b64decode(row["content_base64"],validate=True);pin=pins[row["path"]]
    assert len(b)==pin["bytes"] and hashlib.sha256(b).hexdigest()==pin["sha256"]
    assert hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()==pin["git_blob_sha1"]
    out=args.destination/relative;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(b)
print("Restored",len(rows),"byte/hash/blob verified fixed-input originals; no feasibility search executed")

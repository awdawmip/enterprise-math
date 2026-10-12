"""Losslessly restore bounded publication custody; execute no science."""
import argparse,base64,gzip,hashlib,json
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("package",type=Path)
parser.add_argument("destination",type=Path)
args=parser.parse_args();p=json.loads(args.package.read_bytes())
assert p["schema"]=="T6_ORDER3_CANONICAL_PUBLICATION_CUSTODY_EVIDENCE_LOSSLESS_V1"
z=base64.b64decode(p["payload"],validate=True)
assert hashlib.sha256(z).hexdigest()==p["gzip_sha256"]
raw=gzip.decompress(z)
assert len(raw)==p["original_container_bytes"] and hashlib.sha256(raw).hexdigest()==p["original_container_sha256"]
rows=json.loads(raw)["files"];pins={x["path"]:x for x in p["files"]}
assert len(rows)==len(pins)==p["file_count"]
for row in rows:
    path=Path(row["path"]);assert not path.is_absolute() and ".." not in path.parts
    b=row["content"].encode("utf-8");pin=pins[row["path"]]
    assert len(b)==pin["bytes"] and hashlib.sha256(b).hexdigest()==pin["sha256"]
    assert hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()==pin["git_blob_sha1"]
    out=args.destination/path;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(b)
print("Restored",len(rows),"complete byte/hash/blob-verified publication custody originals; no science executed")

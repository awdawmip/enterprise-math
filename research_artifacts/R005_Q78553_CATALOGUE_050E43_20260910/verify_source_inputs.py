"""Verify source input bytes and optionally restore the exact local data filenames."""
import argparse,base64,gzip,hashlib,json
from pathlib import Path
A=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument("--restore",action="store_true");args=p.parse_args()
manifest=json.loads((A/"source_input_manifest.json").read_text(encoding="utf-8"))
def sha(data):return hashlib.sha256(data).hexdigest()
for row in manifest["files"]:
    text=(A/row["path"]).read_bytes()
    assert len(text)==row["encoded_bytes"] and sha(text)==row["encoded_sha256"]
    zipped=base64.b64decode(b"".join(text.split()),validate=True)
    assert len(zipped)==row["compressed_bytes"] and sha(zipped)==row["compressed_sha256"]
    raw=gzip.decompress(zipped)
    assert len(raw)==row["decoded_bytes"] and sha(raw)==row["decoded_sha256"]
    if args.restore:
        for name,data in ((row["original_compressed_name"],zipped),(row["decoded_name"],raw)):
            target=(A/name).resolve()
            if not target.is_relative_to(A):raise ValueError("Input path leaves artifact directory")
            if target.exists():
                if target.read_bytes()!=data:raise FileExistsError(str(target))
            else:
                with target.open("xb") as f:f.write(data)
print(json.dumps({"source_inputs_verified":len(manifest["files"]),"restored":args.restore}),flush=True)


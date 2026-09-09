"""Verify the lossless raw block archive set; optionally reconstruct a new directory."""
import argparse,base64,gzip,hashlib,io,json,tarfile
from pathlib import Path
A=Path(__file__).resolve().parent
def sha(data): return hashlib.sha256(data).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument("--output-dir",type=Path);args=p.parse_args()
    manifest=json.loads((A/"block_archive_manifest.json").read_text(encoding="utf-8"))
    raw_manifest=(A/manifest["source_byte_manifest_path"]).read_bytes()
    assert sha(raw_manifest)==manifest["source_byte_manifest_sha256"]
    expected={x["path"]:x for x in json.loads(raw_manifest)["files"]}
    seen=set();byte_count=0
    destination=args.output_dir.resolve() if args.output_dir else None
    for group in manifest["groups"]:
        encoded=(A/group["path"]).read_bytes()
        assert len(encoded)==group["encoded_bytes"] and sha(encoded)==group["encoded_sha256"]
        zipped=base64.b64decode(b"".join(encoded.split()),validate=True)
        assert len(zipped)==group["gzip_bytes"] and sha(zipped)==group["gzip_sha256"]
        raw=gzip.decompress(zipped)
        assert len(raw)==group["tar_bytes"] and sha(raw)==group["tar_sha256"]
        names={f"blocks/{i:05d}.json" for i in range(group["first_block"],group["last_block"]+1)}
        with tarfile.open(fileobj=io.BytesIO(raw),mode="r:") as tar:
            assert set(tar.getnames())==names and len(tar.getmembers())==group["file_count"]
            for item in tar.getmembers():
                assert item.isfile()
                relative="construction_full/"+item.name
                assert relative not in seen
                seen.add(relative)
                value=tar.extractfile(item).read();record=expected[relative]
                assert len(value)==record["bytes"] and sha(value)==record["sha256"]
                byte_count+=len(value)
                if destination is not None:
                    output=(destination/relative).resolve()
                    if not output.is_relative_to(destination): raise ValueError("Invalid archive output path")
                    output.parent.mkdir(parents=True,exist_ok=True)
                    if output.exists():
                        if output.read_bytes()!=value: raise FileExistsError(str(output))
                    else:
                        with output.open("xb") as f:f.write(value)
    assert seen==set(expected) and len(seen)==4000
    result={"schema":"R005_RAW_BLOCK_ARCHIVE_VERIFICATION_V1","all_verified":True,"files":len(seen),
            "original_bytes":byte_count,"output_directory":str(destination) if destination else None}
    print(json.dumps(result),flush=True)
if __name__=="__main__":main()


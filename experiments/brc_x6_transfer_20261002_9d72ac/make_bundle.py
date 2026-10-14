#!/usr/bin/env python3
"""Inventory and deterministic backup of this experiment and exact runtime dependencies."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
EXCLUDE={"manifest.json","storage_receipt.json","publication.json","transfer_series.csv.gz"}


def source_files():
    sys.path.insert(0,str(ROOT/"src"))
    import enterprise_math.brc_transport  # noqa: F401
    deps={Path(m.__file__).resolve() for name,m in sys.modules.items()
          if name.startswith("enterprise_math") and getattr(m,"__file__",None)}
    for rel in ["AGENTS.md","p000_reality_foundation.json",
                "definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json",
                "definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json",
                "definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json",
                "definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md",
                "coordinate_address_contract.json",
                "research_notes/BRC_NATIVE_X6_SEMANTIC_ALIGNMENT_20261002_9D72AC.md"]:
        deps.add(ROOT/rel)
    science={p for p in HERE.iterdir() if p.is_file() and p.name not in EXCLUDE}
    return sorted(science|deps)


def inventory():
    files=[]
    for p in source_files():
        data=p.read_bytes()
        files.append({"path":str(p.relative_to(ROOT)),"bytes":len(data),
                      "sha256":hashlib.sha256(data).hexdigest(),
                      "git_blob_sha1":hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()})
    return {"schema":"BRC_X6_TRANSFER_ARCHIVE_V1","experiment":str(HERE.relative_to(ROOT)),
            "exclusions":sorted(EXCLUDE),"files":files,
            "reconstructed_data":{"path":str((HERE/'transfer_series.csv.gz').relative_to(ROOT)),
                                  "bytes":12661305,
                                  "sha256":"62a36e1d888e62acd90ceaac34d9563a234a45b9139559fe4f9533818790d9e4",
                                  "recipe":"restore_data.py concatenates the two byte fragments and verifies the original gzip SHA-256"},
            "meaning":"Exact local scientific/dependency snapshot. External storage receipts are excluded to avoid circular archive hashes. No mathematical promotion or remote-byte verification follows from this manifest."}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verify",action="store_true")
    parser.add_argument("--output",type=Path,default=Path('/workspace/BRC_X6_Transfer_20261002_9D72AC.zip'))
    args=parser.parse_args()
    current=inventory()
    if args.verify:
        assert json.loads((HERE/'manifest.json').read_text())==current,"Inventory differs"
        print(json.dumps({"status":"PASS","verified_files":len(current['files'])}))
        return
    (HERE/'manifest.json').write_text(json.dumps(current,ensure_ascii=False,indent=2)+'\n')
    files=source_files()+[HERE/'manifest.json']
    with zipfile.ZipFile(args.output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as out:
        for p in sorted(files):
            info=zipfile.ZipInfo(str(p.relative_to(ROOT)),date_time=(2026,10,2,0,0,0))
            info.compress_type=zipfile.ZIP_STORED if p.suffix=='.gz' else zipfile.ZIP_DEFLATED
            info.external_attr=0o644<<16
            out.writestr(info,p.read_bytes())
    with zipfile.ZipFile(args.output) as source:
        assert source.testzip() is None
        for item in current['files']:
            assert hashlib.sha256(source.read(item['path'])).hexdigest()==item['sha256']
    data=args.output.read_bytes()
    print(json.dumps({"archive":str(args.output),"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest(),
                      "source_files":len(current['files']),"archive_entry_checks":"PASS"}))


if __name__=='__main__':
    main()

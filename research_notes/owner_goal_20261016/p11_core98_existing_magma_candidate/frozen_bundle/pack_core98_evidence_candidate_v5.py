#!/usr/bin/env python3
"""Fixed custody codec candidate. Not imported/tested/executed by its author.
After the one authorized attempt only; never evaluates archived code.
"""
import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--attempt-dir", required=True)
    ap.add_argument("--return-file", required=True)
    ap.add_argument("--native-gate-summary", required=True)
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args()
    base = Path(__file__).resolve().parent
    attempt = Path(args.attempt_dir)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    names = ["core98_one_mixed_candidate.m",
             "CORE98_EXACT_FIXED_SCIENTIFIC_INPUT_V2.json",
             "submit_core98_once_frozen_candidate_v3.py",
             "core98_bounded_evidence_v3.py",
             "pack_core98_evidence_candidate_v5.py",
             "CORE98_PROSPECTIVE_SINGLE_CALL_SCOPE_COST_OUTPUT_AND_ROLE_ROUTE.md",
             "CORE98_COMPLETE_CODEC_COST_AND_CLOCK_ADDENDUM.md",
             "CORE98_V3_CURRENT_BUNDLE_COST_AND_EVIDENCE_BOUNDARIES.md",
             "CORE98_ACTUAL_NATIVE_BINDING_AND_CURRENT_BUNDLE_V5.md",
             "ACTUAL_NATIVE_NEW_SCIENCE_ROUTE_CONTROL_ONLY_FROZEN_COPY.md"]
    rows = []
    def add(label, path, cap):
        data = path.read_bytes()
        assert len(data) <= cap, label
        rows.append({"path": label, "bytes": len(data), "sha256": sha(data),
                     "git_blob_sha1": hashlib.sha1(
                         b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest(),
                     "encoding": "base64",
                     "content": base64.b64encode(data).decode("ascii")})
    for name in names:
        add("frozen_candidate/"+name, base/name, 50000)
    add("attempt/ORIGINAL_SINGLE_ATTEMPT_PREPARED.json",
        attempt/"ORIGINAL_SINGLE_ATTEMPT_PREPARED.json", 16384)
    add("attempt/ORIGINAL_ACTUAL_RESPONSE_AND_ASSESSMENT.json",
        attempt/"ORIGINAL_ACTUAL_RESPONSE_AND_ASSESSMENT.json", 2500000)
    assessment = json.loads((attempt/"ORIGINAL_ACTUAL_RESPONSE_AND_ASSESSMENT.json").read_bytes())
    raw = attempt/"ORIGINAL_RESPONSE_BYTES.xml"
    if raw.exists():
        add("attempt/ORIGINAL_RESPONSE_BYTES.xml", raw, 1048577)
    add("RETURN.md", Path(args.return_file), 32768)
    add("NATIVE_GATE_SUMMARY.json", Path(args.native_gate_summary), 16384)
    logical = json.dumps(
        {"schema": "P11_CORE98_COMPLETE_EVIDENCE_JSON_CARRIER_V5",
         "files": rows, "scientific_authority_granted": False},
        ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("ascii")
    assert sum(r["bytes"] for r in rows) <= 3800000
    carrier = base64.b64encode(gzip.compress(logical, compresslevel=9, mtime=0))
    index = {"schema": "P11_CORE98_COMPLETE_EVIDENCE_PARTS_INDEX_V5",
             "codec": "concat_ASCII_parts_then_base64_then_gzip_then_JSON",
             "logical_json_bytes": len(logical),
             "logical_json_sha256": sha(logical),
             "carrier_bytes": len(carrier), "carrier_sha256": sha(carrier),
             "decoded_regular_file_bytes": sum(r["bytes"] for r in rows),
             "file_pins": [{k: r[k] for k in ("path", "bytes", "sha256", "git_blob_sha1")}
                           for r in rows],
             "all_retained_attempt_file_bytes_archived_exactly": True,
             "raw_response_complete_claim": assessment.get("raw_response_complete"),
             "raw_prefix_only_claim": assessment.get("raw_response_retained_prefix_only"),
             "full_parsed_assessment_retained_claim": assessment.get("full_parsed_assessment_retained"),
             "assessment_state": assessment.get("state"),
             "missing_flags_are_UNKNOWN_not_complete": True,
             "raw_response_present": raw.exists(),
             "mathematical_acceptance": False,
             "parts": []}
    if len(carrier) > 2097152:
        index.update(state="CODEC_OVER_2MiB_NO_NATIVE_CARRIER_PUBLICATION",
                     original_local_evidence_preserved=True,
                     scientific_repeat_allowed=False)
        (out/"CODEC_RESOURCE_BOUNDARY.json").write_text(
            json.dumps(index, indent=2)+"\n")
        return
    for i, start in enumerate(range(0, len(carrier), 512000)):
        part = carrier[start:start+512000]
        name = "CORE98_EVIDENCE_PART_"+str(i).zfill(3)+".txt"
        target = out/name
        with target.open("xb") as stream:
            stream.write(part)
        index["parts"].append({"filename": name, "bytes": len(part), "sha256": sha(part)})
    assert len(index["parts"]) <= 5
    index["state"] = "COMPLETE_BOUNDED_CARRIER_READY_FOR_ACTUAL_SOURCE_PUBLICATION"
    encoded = (json.dumps(index, indent=2)+"\n").encode()
    assert len(encoded) <= 16384
    with (out/"CORE98_EVIDENCE_PARTS_INDEX.json").open("xb") as stream:
        stream.write(encoded)

if __name__ == "__main__":
    main()


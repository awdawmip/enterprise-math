"""Exact bounded transport check for this genuine p17 ledger container.
No producer import or mathematical enumeration occurs here.
"""
import argparse
import base64
import gzip
import hashlib
import io
import json
from pathlib import Path

COMPACT_HASH = "537d3fd3993903dd406695d7c32ef5cb2748c6917e77d9a7b06524a7e06981f2"
PRETTY_HASH = "185adc2dca61819c662e52523c9fea398f60a283864874d108d0cb03a7c593aa"
COMPACT_BYTES = 1054607
PRETTY_BYTES = 1574839


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def unpack_verify(container_path, reference_path, compact_path, pretty_path, receipt_path):
    container_bytes = Path(container_path).read_bytes()
    envelope = json.loads(container_bytes)
    require(envelope["schema"] == "T6_EXACT_JSON_GZIP_BASE64_CONTAINER_V1", "wrong container schema")
    require(envelope["compression"] == "gzip" and envelope["encoding"] == "base64", "wrong encoding")
    require(envelope["canonical_compact_json_bytes"] == COMPACT_BYTES
            and envelope["canonical_compact_json_sha256"] == COMPACT_HASH, "compact pin metadata")
    require(envelope["original_pretty_json_bytes"] == PRETTY_BYTES
            and envelope["original_pretty_json_sha256"] == PRETTY_HASH, "pretty pin metadata")
    require(envelope["unpacked_filename"] == "P17_ORDER1_COMPLETE_CLASSIFICATION.json", "wrong ledger name")
    compressed = base64.b64decode(envelope["payload"], validate=True)
    with gzip.GzipFile(fileobj=io.BytesIO(compressed), mode="rb") as stream:
        compact = stream.read(COMPACT_BYTES + 1)
        require(len(compact) == COMPACT_BYTES and stream.read(1) == b"", "decompressed size")
    require(digest(compact) == COMPACT_HASH, "decompressed compact SHA256")
    # JSON parsing/serialization below is transport only. Python integers retain
    # arbitrary precision. The sole ledger float is elapsed-time metadata; the
    # independent scientific verifier separately checks all arithmetic types.
    obj = json.loads(compact)
    pretty = (json.dumps(obj, indent=2) + "\n").encode()
    reference = Path(reference_path).read_bytes()
    require(len(reference) == PRETTY_BYTES and digest(reference) == PRETTY_HASH, "original raw pin")
    require(len(pretty) == PRETTY_BYTES and digest(pretty) == PRETTY_HASH, "rebuilt pretty raw pin")
    require(pretty == reference, "byte-for-byte original roundtrip")
    require(gzip.decompress(gzip.compress(compact, mtime=0)) == compact, "gzip/base transport roundtrip")
    for path in (compact_path, pretty_path, receipt_path):
        require(not Path(path).exists(), "refuse overwrite: " + str(path))
    for path, data in ((compact_path, compact), (pretty_path, pretty)):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with Path(path).open("xb") as stream:
            stream.write(data)
    receipt = {
        "schema": "T6_GENUINE_LEDGER_INDEPENDENT_PACKED_ROUNDTRIP_V1", "status": "PASS",
        "container_path": str(container_path), "container_bytes": len(container_bytes),
        "container_sha256": digest(container_bytes), "compressed_bytes": len(compressed),
        "compressed_sha256": digest(compressed), "compact_bytes": len(compact),
        "compact_sha256": digest(compact), "original_pretty_bytes": len(reference),
        "original_pretty_sha256": digest(reference), "rebuilt_pretty_sha256": digest(pretty),
        "compact_output": str(compact_path), "pretty_output": str(pretty_path),
        "reference_path": str(reference_path), "exact_original_byte_roundtrip": True,
        "unpacker_sha256": digest(Path(__file__).read_bytes()),
        "producer_imported_or_called": False, "mathematical_census_executed": False,
        "native_identity_or_result_created": False, "same_owner_nonblind": True
    }
    Path(receipt_path).parent.mkdir(parents=True, exist_ok=True)
    with Path(receipt_path).open("x") as stream:
        json.dump(receipt, stream, indent=2)
        stream.write("\n")
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--unpack-genuine-ledger", action="store_true")
    for name in ("container", "reference-pretty", "output-compact", "output-pretty", "receipt"):
        parser.add_argument("--" + name, type=Path)
    args = parser.parse_args()
    if not args.unpack_genuine_ledger:
        print(json.dumps({"status": "UNPACKER_READY_NO_LEDGER_READ"}))
        return
    require(all(getattr(args, x) is not None for x in
                ("container", "reference_pretty", "output_compact", "output_pretty", "receipt")),
            "all explicit paths required")
    result = unpack_verify(args.container, args.reference_pretty, args.output_compact,
                           args.output_pretty, args.receipt)
    print(json.dumps({"status": result["status"], "exact_original_byte_roundtrip": True,
                      "compact_bytes": result["compact_bytes"],
                      "original_pretty_bytes": result["original_pretty_bytes"]}))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(json.dumps({"status": "FAIL_HARD", "error": str(error)}))
        raise SystemExit(1)

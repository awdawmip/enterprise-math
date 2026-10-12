"""Strict byte-only q4 fixed-input capsule decoder; executes no restored code."""
import argparse
import base64
from hashlib import sha1, sha256
import json
from pathlib import Path
import re
import zlib


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key")
        result[key] = value
    return result


def load_canonical(path):
    raw = path.read_bytes()
    value = json.loads(raw, object_pairs_hook=no_duplicate_keys)
    expected = (json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n").encode()
    if raw != expected:
        raise ValueError("Noncanonical JSON bytes")
    return value, raw


def verify(raw, expected):
    actual = {"bytes": len(raw), "sha256": sha256(raw).hexdigest(),
              "git_blob_sha1": sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()}
    if any(actual[key] != expected[key] for key in actual):
        raise ValueError("Exact original/carrier bytepin mismatch")
    return actual


def safe_name(name):
    if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", name):
        raise ValueError("Unsafe/nonlocal capsule filename")
    return name


def unpack(package_path, output_dir):
    package, package_raw = load_canonical(package_path)
    if len(package_raw) > 1048576 or package["schema"] != "T6_P17_ORDER4_FIXED_INPUT_LOSSLESS_PACKAGE_V1":
        raise ValueError("Wrong package schema")
    parts = package["parts"]
    if len(parts) not in (2, 3) or package["part_count"] != len(parts):
        raise ValueError("Wrong carrier count")
    expected_keys = {"schema", "encoding", "input_sha256", "bundle_gzip_sha256", "part_index", "part_count", "payload_base64"}
    payloads = []
    offset = 0
    for position, expected in enumerate(parts):
        name = safe_name(expected["path"])
        part, raw = load_canonical(package_path.parent / name)
        verify(raw, expected)
        if len(raw) > 1048576 or set(part) != expected_keys:
            raise ValueError("Invalid outer carrier shape/size")
        if type(part["part_index"]) is not int or type(part["part_count"]) is not int:
            raise ValueError("Nonintegral carrier numbering")
        if part["schema"] != "T6_P17_ORDER4_FIXED_INPUT_LOSSLESS_PART_V1" or part["encoding"] != "gzip_then_base64_ascii_segments":
            raise ValueError("Wrong part schema/encoding")
        if part["part_index"] != position or part["part_count"] != len(parts):
            raise ValueError("Missing/reordered/duplicate part")
        if part["input_sha256"] != package["fixed_input_sha256"] or part["bundle_gzip_sha256"] != package["bundle_gzip_sha256"]:
            raise ValueError("Cross-package carrier")
        value = part["payload_base64"]
        if not isinstance(value, str) or len(value) != expected["base64_characters"] or expected["base64_offset"] != offset:
            raise ValueError("Wrong payload length/offset")
        value.encode("ascii")
        payloads.append(value)
        offset += len(value)
    encoded = "".join(payloads)
    if len(encoded) != package["bundle_base64_characters"]:
        raise ValueError("Wrong whole payload length")
    compressed = base64.b64decode(encoded, validate=True)
    if base64.b64encode(compressed).decode("ascii") != encoded:
        raise ValueError("Noncanonical base64")
    if len(compressed) != package["bundle_gzip_bytes"] or sha256(compressed).hexdigest() != package["bundle_gzip_sha256"]:
        raise ValueError("Wrong compressed-byte pin")
    total = package["bundle_raw_bytes"]
    if type(total) is not int or not 0 < total <= 64 * 1048576:
        raise ValueError("Invalid decompression resource bound")
    decoder = zlib.decompressobj(31)
    raw_bundle = decoder.decompress(compressed, total + 1)
    if not decoder.eof or decoder.unconsumed_tail or decoder.unused_data:
        raise ValueError("Truncated, oversized, trailing or concatenated gzip data")
    if len(raw_bundle) != total or sha256(raw_bundle).hexdigest() != package["bundle_raw_sha256"]:
        raise ValueError("Wrong raw-byte bundle pin")
    originals = package["originals"]
    cursor, names, verified = 0, set(), []
    for entry in originals:
        name = safe_name(entry["path"])
        if name in names or type(entry["offset"]) is not int or type(entry["bytes"]) is not int:
            raise ValueError("Duplicate/nonintegral original")
        if entry["offset"] != cursor or entry["bytes"] < 0:
            raise ValueError("Gap or overlap in original bundle")
        names.add(name)
        data = raw_bundle[cursor:cursor + entry["bytes"]]
        verify(data, entry)
        cursor += entry["bytes"]
        verified.append((name, data, entry))
    if cursor != len(raw_bundle) or package["original_count"] != len(verified):
        raise ValueError("Incomplete original coverage")
    fixed = next((entry for name, data, entry in verified if name == package["fixed_input_filename"]), None)
    if fixed is None or any(fixed[key] != package[target] for key, target in (
            ("bytes", "fixed_input_bytes"), ("sha256", "fixed_input_sha256"), ("git_blob_sha1", "fixed_input_git_blob_sha1"))):
        raise ValueError("Fixed input missing/mismatched")
    # Validate every byte before touching destinations; never overwrite differing files.
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, data, entry in verified:
        destination = output_dir / name
        if destination.is_symlink():
            raise ValueError("Refusing symlink destination")
        if destination.exists() and destination.read_bytes() != data:
            raise ValueError("Refusing to replace different destination bytes")
    for name, data, entry in verified:
        (output_dir / name).write_bytes(data)
    return {"schema": "T6_Q4_FIXED_INPUT_BYTE_ONLY_UNPACK_RECEIPT_V1", "status": "PASS_EXACT_ORIGINAL_BYTES",
            "package_sha256": sha256(package_raw).hexdigest(), "original_count": len(verified),
            "original_bytes": cursor, "fixed_input_sha256": package["fixed_input_sha256"],
            "restored_pins": [{"path": str((output_dir / name).resolve()), "bytes": entry["bytes"],
                               "sha256": entry["sha256"], "git_blob_sha1": entry["git_blob_sha1"]}
                              for name, data, entry in verified],
            "restored_code_executed": False, "scientific_feasibility_executed": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    receipt = unpack(args.package, args.output)
    if args.receipt:
        args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": receipt["status"], "original_count": receipt["original_count"],
                      "original_bytes": receipt["original_bytes"], "fixed_input_sha256": receipt["fixed_input_sha256"]}))

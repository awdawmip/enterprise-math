#!/usr/bin/env python3
"""Restore verified original bytes from a lossless Source files capsule.

Integrity and custody only: no producer, consumer, classifier or native tool
is imported or executed. No mathematical or native authority is granted.
"""
import argparse
import base64
import gzip
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re


SCHEMA = "T6_ORDER3_LOSSLESS_SOURCE_FILES_CAPSULE_V1"
ENCODING = "gzip+base64-of-UTF8-JSON-with-base64-original-files"
MAX_CAPSULE_BYTES = 1024 * 1024
MAX_CONTAINER_BYTES = 64 * 1024 * 1024


class CustodyError(ValueError):
    pass


def need(condition, message):
    if not condition:
        raise CustodyError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def git_blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def reject_number(_token):
    raise CustodyError("Floating and nonfinite JSON values are forbidden in capsule/container metadata")


def unique_object(items):
    result = {}
    for key, value in items:
        need(key not in result, "Duplicate JSON key")
        result[key] = value
    return result


def parse(raw):
    return json.loads(raw.decode("utf-8"), parse_float=reject_number,
                      parse_constant=reject_number, object_pairs_hook=unique_object)


def hex_digest(value, length):
    need(type(value) is str and re.fullmatch(r"[0-9a-f]{" + str(length) + r"}", value) is not None,
         "Malformed checksum")
    return value


def count(value, name):
    need(type(value) is int and value >= 0, "Nonnegative integer required: " + name)
    return value


def safe_path(value):
    need(type(value) is str and value and "\\" not in value and ":" not in value
         and "\0" not in value, "Unsafe original member path")
    path = PurePosixPath(value)
    need(not path.is_absolute() and path.parts and all(part not in (".", "..") for part in value.split("/"))
         and all(part for part in value.split("/")) and path.as_posix() == value,
         "Original member path must be a normalized relative POSIX path")
    return Path(*path.parts)


def bounded_gzip(compressed, size):
    need(size <= MAX_CONTAINER_BYTES, "Declared original container exceeds the portable decode bound")
    with gzip.GzipFile(fileobj=io.BytesIO(compressed), mode="rb") as stream:
        result = stream.read(size + 1)
        need(len(result) == size and stream.read(1) == b"", "Original container byte length mismatch")
    return result


def verify(capsule_path, expected_capsule_sha256):
    expected = hex_digest(expected_capsule_sha256, 64)
    capsule_raw = Path(capsule_path).read_bytes()
    need(len(capsule_raw) < MAX_CAPSULE_BYTES, "Capsule must be smaller than native one-MiB file cap")
    need(sha(capsule_raw) == expected, "Actual captured capsule SHA256 mismatch")
    capsule = parse(capsule_raw)
    need(type(capsule) is dict and capsule.get("schema") == SCHEMA
         and capsule.get("encoding") == ENCODING, "Wrong capsule schema/encoding")
    for key in ("file_count", "files", "gzip_sha256", "original_container_bytes",
                "original_container_sha256", "payload"):
        need(key in capsule, "Missing capsule field: " + key)
    compressed = base64.b64decode(capsule["payload"], validate=True)
    need(sha(compressed) == hex_digest(capsule["gzip_sha256"], 64), "Compressed payload SHA256 mismatch")
    container_size = count(capsule["original_container_bytes"], "original_container_bytes")
    container_raw = bounded_gzip(compressed, container_size)
    need(sha(container_raw) == hex_digest(capsule["original_container_sha256"], 64),
         "Original container SHA256 mismatch")
    container = parse(container_raw)
    need(type(container) is dict and set(container) == {"files"}, "Unexpected original container fields")
    rows, manifest = container["files"], capsule["files"]
    file_count = count(capsule["file_count"], "file_count")
    need(type(rows) is list and type(manifest) is list and file_count > 0
         and len(rows) == len(manifest) == file_count, "Original member inventory count mismatch")
    pins = {}
    for item in manifest:
        need(type(item) is dict and set(item) == {"path", "bytes", "sha256", "git_blob_sha1"},
             "Malformed original manifest row")
        safe_path(item["path"])
        need(item["path"] not in pins, "Duplicate original manifest path")
        count(item["bytes"], "member bytes")
        hex_digest(item["sha256"], 64)
        hex_digest(item["git_blob_sha1"], 40)
        pins[item["path"]] = item
    restored = []
    seen = set()
    for row in rows:
        need(type(row) is dict and set(row) == {"path", "content_base64"}, "Malformed original file row")
        relative = safe_path(row["path"])
        need(row["path"] in pins and row["path"] not in seen, "Duplicate or undeclared original member")
        need(type(row["content_base64"]) is str, "Original content must be base64 text")
        raw = base64.b64decode(row["content_base64"], validate=True)
        pin = pins[row["path"]]
        need(len(raw) == pin["bytes"] and sha(raw) == pin["sha256"] and git_blob(raw) == pin["git_blob_sha1"],
             "Original member byte/SHA/Git-blob mismatch")
        seen.add(row["path"])
        restored.append((relative, raw, pin))
    need(seen == set(pins), "Original member path set mismatch")
    need([row["path"] for row in rows] == [item["path"] for item in manifest],
         "Original container/manifest member order mismatch")
    return restored, {"capsule_bytes": len(capsule_raw), "capsule_sha256": expected,
                      "capsule_git_blob_sha1": git_blob(capsule_raw),
                      "gzip_sha256": sha(compressed), "original_container_bytes": len(container_raw),
                      "original_container_sha256": sha(container_raw), "file_count": file_count,
                      "member_pins": manifest, "mathematical_or_native_authority_granted": False,
                      "original_content_parsed_or_reserialized": False}


def restore(restored, destination):
    root = Path(destination)
    need(not root.is_symlink(), "Destination may not be a symlink")
    base = root.resolve()
    targets = []
    # Validate every member and output path before the first write. Originals
    # are never overwritten, and path components may not redirect via symlinks.
    for relative, raw, pin in restored:
        target = root / relative
        need(not target.exists() and not target.is_symlink(), "Destination original already exists")
        cursor = root
        for part in relative.parts[:-1]:
            cursor = cursor / part
            need(not cursor.is_symlink(), "Destination parent component may not be a symlink")
        need(target.resolve().is_relative_to(base), "Destination path leaves its root")
        targets.append((target, raw, pin))
    root.mkdir(parents=True, exist_ok=True)
    for target, raw, pin in targets:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(raw)
        actual = target.read_bytes()
        need(actual == raw and sha(actual) == pin["sha256"] and git_blob(actual) == pin["git_blob_sha1"],
             "Written original byte roundtrip mismatch")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capsule", type=Path)
    parser.add_argument("destination", type=Path, nargs="?")
    parser.add_argument("--expected-capsule-sha256", required=True)
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    need(args.verify_only or args.destination is not None, "Destination required for restoration")
    files, receipt = verify(args.capsule, args.expected_capsule_sha256)
    if not args.verify_only:
        restore(files, args.destination)
    receipt.update(status="BYTE_CUSTODY_PASS", originals_written=not args.verify_only,
                   scientific_functions_executed=False, native_or_Source_operations=False)
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (CustodyError, OSError, ValueError, TypeError, KeyError, EOFError) as error:
        print(json.dumps({"status": "BYTE_CUSTODY_FAIL_HARD", "error": str(error),
                          "scientific_or_native_authority_granted": False}))
        raise SystemExit(1)

#!/usr/bin/env python3
"""Strict byte-only recovery. Does not execute any restored scientific code."""
import argparse
import base64
import hashlib
import json
import re
import zlib
from pathlib import Path, PurePosixPath

SCHEMA = "T6_NEXT_DIRECTION_COMPLETE_BINARY_ORIGINALS_CAPSULE_V1"
MEMBER_SCHEMA = "T6_NEXT_DIRECTION_SELECTED_ORIGINAL_BYTES_V1"
MAX_OUTER = 1 << 20
MAX_INNER = 32 << 20
PIN_KEYS = {"path", "original_path", "bytes", "sha256", "git_blob_sha1"}


def strict_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def load_json(raw):
    return json.loads(raw.decode("utf-8"), object_pairs_hook=strict_object,
                      parse_constant=lambda value: (_ for _ in ()).throw(
                          ValueError("nonfinite JSON number")))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def checked_int(value, lower, upper):
    require(type(value) is int and lower <= value <= upper, "integer range")
    return value


def unbase64(value):
    require(type(value) is str and value.isascii(), "base64 text")
    data = base64.b64decode(value, validate=True)
    require(base64.b64encode(data).decode("ascii") == value, "noncanonical base64")
    return data


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def checked_pin(row):
    require(type(row) is dict and set(row) == PIN_KEYS, "pin field set")
    path = row["path"]
    require(type(path) is str and 0 < len(path) <= 1024, "member path")
    pure = PurePosixPath(path)
    require(not pure.is_absolute() and str(pure) == path, "noncanonical member path")
    require(all(re.fullmatch(r"[A-Za-z0-9_.-]+", part) and part not in {".", ".."}
                for part in pure.parts), "unsafe member path")
    require(type(row["original_path"]) is str and row["original_path"].startswith("/workspace/"),
            "original path provenance")
    checked_int(row["bytes"], 0, MAX_INNER)
    require(type(row["sha256"]) is str and re.fullmatch(r"[0-9a-f]{64}", row["sha256"]),
            "SHA256 syntax")
    require(type(row["git_blob_sha1"]) is str and re.fullmatch(r"[0-9a-f]{40}", row["git_blob_sha1"]),
            "Git blob syntax")
    return row


def recover(container_path, output=None):
    raw_outer = container_path.read_bytes()
    require(len(raw_outer) <= MAX_OUTER, "outer exceeds 1 MiB")
    outer = load_json(raw_outer)
    require(type(outer) is dict and set(outer) == {
        "schema", "codec", "single_gzip_member", "status", "file_count",
        "original_member_bytes", "inner_json_bytes", "inner_json_sha256",
        "gzip_bytes", "gzip_sha256", "files", "payload_base64"}, "outer field set")
    require(outer["schema"] == SCHEMA and outer["codec"] == "gzip+base64-binary-member-json", "codec")
    require(outer["single_gzip_member"] is True, "single member declaration")
    require(outer["status"] == "LOCAL_CANDIDATE_NOT_SOURCE_ADOPTED", "candidate status")
    count = checked_int(outer["file_count"], 1, 256)
    inner_size = checked_int(outer["inner_json_bytes"], 1, MAX_INNER)
    declared_members = checked_int(outer["original_member_bytes"], 0, MAX_INNER)
    checked_int(outer["gzip_bytes"], 1, MAX_OUTER)
    require(type(outer["files"]) is list and len(outer["files"]) == count, "pin count")
    pin_list = [checked_pin(row) for row in outer["files"]]
    require([row["path"] for row in pin_list] == sorted(row["path"] for row in pin_list),
            "pin order")
    pins = {row["path"]: row for row in pin_list}
    require(len(pins) == count, "duplicate member path")
    gzip_data = unbase64(outer["payload_base64"])
    require(len(gzip_data) == outer["gzip_bytes"] and sha256(gzip_data) == outer["gzip_sha256"],
            "gzip pin mismatch")
    decoder = zlib.decompressobj(31)
    inner_data = decoder.decompress(gzip_data, inner_size + 1)
    require(decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail,
            "truncated, oversized, or concatenated gzip")
    require(len(inner_data) == inner_size and sha256(inner_data) == outer["inner_json_sha256"],
            "inner JSON pin mismatch")
    inner = load_json(inner_data)
    require(type(inner) is dict and set(inner) == {"schema", "files"}, "inner field set")
    require(inner["schema"] == MEMBER_SCHEMA, "member schema")
    require(type(inner["files"]) is list and len(inner["files"]) == count, "member count")
    all_data = []
    seen = set()
    for row in inner["files"]:
        require(type(row) is dict and set(row) == PIN_KEYS | {"content_base64"}, "member field set")
        pin = checked_pin({key: row[key] for key in PIN_KEYS})
        path = row["path"]
        require(path not in seen and path in pins and pin == pins[path], "member pin bijection")
        seen.add(path)
        data = unbase64(row["content_base64"])
        require(len(data) == pin["bytes"] and sha256(data) == pin["sha256"]
                and blob(data) == pin["git_blob_sha1"], "member bytes/hash/blob mismatch")
        all_data.append((path, data))
    require([path for path, _ in all_data] == [pin["path"] for pin in pin_list], "member order")
    require(sum(len(data) for _, data in all_data) == declared_members, "member byte total")
    if output is not None:
        require(not output.exists(), "output must be a new directory")
        output.mkdir(parents=True)
        for path, data in all_data:
            target = output.joinpath(*PurePosixPath(path).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as stream:
                stream.write(data)
    return {"schema": "T6_NEXT_DIRECTION_BYTE_ONLY_UNPACK_RESULT_V1",
            "files_verified": count, "original_member_bytes": declared_members,
            "all_member_bytes_SHA256_and_Git_blobs_verified": True,
            "exact_single_gzip_member_CRC_and_EOF_verified": True,
            "mathematics_executed": False, "Source_adoption_performed": False,
            "output_written": output is not None}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capsule", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    print(json.dumps(recover(args.capsule, args.output), sort_keys=True))

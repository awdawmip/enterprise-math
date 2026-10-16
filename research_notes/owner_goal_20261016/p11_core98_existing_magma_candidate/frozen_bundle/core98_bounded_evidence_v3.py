"""CONTROL-only bounded evidence writer. Does not authorize or perform research.

All three filenames have pre-write caps; the attempt directory must be new.
This bounds this single writer's regular-file payload, not filesystem blocks,
host RSS or writes by another process with access to the directory.
"""
import hashlib
import json
import os
from pathlib import Path

RAW_CAP = 1048576
SIDECAR_CAP = 2500000
ATTEMPT_CAP = 4194304
MARKER_NAME = "ORIGINAL_SINGLE_ATTEMPT_PREPARED.json"
RAW_NAME = "ORIGINAL_RESPONSE_BYTES.xml"
ASSESSMENT_NAME = "ORIGINAL_ACTUAL_RESPONSE_AND_ASSESSMENT.json"
FILE_CAPS = {MARKER_NAME: 16384, RAW_NAME: RAW_CAP,
             ASSESSMENT_NAME: SIDECAR_CAP}


def encode_json(value):
    return (json.dumps(value, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


class EvidenceLimitError(RuntimeError):
    pass


class BoundedEvidence:
    def __init__(self, directory):
        self.directory = Path(directory)
        # Refuse any prior directory, including an interrupted prior attempt.
        # The caller supplies an existing task workspace parent. Persist the
        # newly created directory entry as well as the later marker entry.
        self.directory.mkdir(mode=0o700, parents=False, exist_ok=False)
        parent_fd = os.open(self.directory.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(parent_fd)
        finally:
            os.close(parent_fd)

    def total_bytes(self):
        total = 0
        for path in self.directory.iterdir():
            if path.is_symlink() or not path.is_file():
                raise EvidenceLimitError("unexpected non-regular evidence entry")
            total += path.stat().st_size
        return total

    def write(self, name, data):
        if name not in FILE_CAPS or not isinstance(data, bytes):
            raise EvidenceLimitError("unregistered evidence file or non-bytes")
        if len(data) > FILE_CAPS[name]:
            raise EvidenceLimitError("per-file evidence cap exceeded before write")
        if self.total_bytes() + len(data) > ATTEMPT_CAP:
            raise EvidenceLimitError("aggregate evidence cap exceeded before write")
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        flags |= getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(self.directory / name, flags, 0o600)
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        # Persist the directory entry too, before allowing the sole POST.
        parent_fd = os.open(self.directory, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(parent_fd)
        finally:
            os.close(parent_fd)

    def write_marker(self, record):
        encoded = encode_json(record)
        self.write(MARKER_NAME, encoded)
        return sha256(encoded)

    def write_raw(self, observed):
        retained = observed[:RAW_CAP]
        self.write(RAW_NAME, retained)
        return {
            "raw_response_bytes": len(retained),
            "raw_response_sha256": sha256(retained),
            "raw_response_observed_bytes": len(observed),
            "raw_response_complete": len(observed) <= RAW_CAP,
            "raw_response_retained_prefix_only": len(observed) > RAW_CAP,
        }

    def write_assessment(self, result):
        encoded = encode_json(result)
        if (len(encoded) > SIDECAR_CAP or
                self.total_bytes() + len(encoded) > ATTEMPT_CAP):
            # No provider-controlled field survives this fallback. In
            # particular, dropping only lines would leave unbounded headers.
            # The original retained raw file is never replaced or relabelled
            # as complete; inspect it and the marker for underlying details.
            result = {
                "schema": "P11_CORE98_BOUNDED_ASSESSMENT_FALLBACK_V3",
                "state": "PARSED_OR_TOTAL_EVIDENCE_CAP_UNKNOWN_NO_RESUBMISSION",
                "candidate_bit": None,
                "transport_attempts": 1,
                "retries": 0,
                "mathematical_acceptance": False,
                "portable_local_certificate_complete": False,
                "Native_Task_completion": False,
                "omitted_full_assessment_bytes": len(encoded),
                "omitted_full_assessment_sha256": sha256(encoded),
                "full_parsed_assessment_retained": False,
                "raw_evidence": "Inspect bounded ORIGINAL_RESPONSE_BYTES.xml; it may be a prefix.",
            }
            encoded = encode_json(result)
        # Enforce both limits again after fallback, before any file write.
        self.write(ASSESSMENT_NAME, encoded)
        return result

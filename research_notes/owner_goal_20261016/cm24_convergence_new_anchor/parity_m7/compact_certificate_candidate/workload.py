"""Non-self-authorizing worker definitions; no CLI and no work at import.

Only a genuinely admitted external Driver launcher may call run_from_bytes.
This module neither accepts an allow-run boolean nor creates a Task/claim.
The exact frozen manifest, launcher, code and input must be bound externally.
"""
from __future__ import annotations


def run_from_bytes(input_bytes, repository_root, meter):
    # These imports and all later preparation are inside the ONE supplied
    # whole-job clock/memory budget; the external launcher covers earlier work.
    import hashlib
    import json
    from pathlib import Path

    def no_duplicates(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result
    def bounded_json(value):
        chunks, size = [], 0
        encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"), ensure_ascii=True,
                                   allow_nan=False)
        for piece in encoder.iterencode(value):
            meter.check_time()
            part = piece.encode("ascii")
            size += len(part)
            meter.check_output_bound(size + 1)
            chunks.append(part)
        return b"".join(chunks) + b"\n"

    if not isinstance(input_bytes, bytes) or len(input_bytes) > 65_536:
        raise ValueError("fixed input byte bound")
    spec = json.loads(input_bytes, object_pairs_hook=no_duplicates)
    if not isinstance(spec, dict) or set(spec) != {
            "schema", "candidate_status", "math", "source_binding", "implementation_binding",
            "resources", "execution_contract"}:
        raise ValueError("fixed input fields")
    if spec["schema"] != "PARITY_M7_FIXED_INTERVAL_BERNSTEIN_INPUT_V1":
        raise ValueError("fixed input schema")
    if spec["candidate_status"] != "NOT_ADMITTED":
        raise ValueError("frozen input's historical disposition was modified")
    if spec["resources"] != {"primitive_exact_operations": 20_000_000, "whole_job_wall_seconds": 300,
                             "address_space_bytes": 536_870_912, "combined_output_bytes": 8_388_608,
                             "integer_bits": 16_384}:
        raise ValueError("resource plan changed")
    root = Path(repository_root).resolve(strict=True)
    total_source_bytes = 0
    for member in spec["source_binding"]["pinned_local_members"]:
        path = (root / member["workspace_repository_relative_path"]).resolve(strict=True)
        path.relative_to(root)
        size = path.stat().st_size
        total_source_bytes += size
        if size != member["bytes"] or total_source_bytes > 131_072:
            raise ValueError("original-source carrier byte bound")
        data = path.read_bytes()
        meter.check_time()
        if hashlib.sha256(data).hexdigest() != member["sha256"]:
            raise ValueError("original-source bytes changed")
        blob = hashlib.sha1(b"blob " + str(size).encode("ascii") + b"\0" + data).hexdigest()
        if blob != member["git_blob_sha1"]:
            raise ValueError("original-source Git blob changed")

    code_cache, total_code_bytes = {}, 0
    modules = spec["implementation_binding"]["modules"]
    if {m["filename"] for m in modules} != {"resource_budget.py", "workload.py", "producer.py", "checker.py"} or len(modules) != 4:
        raise ValueError("fixed implementation carrier changed")
    for member in modules:
        path = Path(__file__).resolve().with_name(member["filename"])
        size = path.stat().st_size
        total_code_bytes += size
        if size != member["bytes"] or size > 65_536 or total_code_bytes > 131_072:
            raise ValueError("fixed code carrier byte bound")
        data = path.read_bytes()
        meter.check_time()
        if hashlib.sha256(data).hexdigest() != member["sha256"]:
            raise ValueError("admitted implementation bytes changed")
        blob = hashlib.sha1(b"blob " + str(size).encode("ascii") + b"\0" + data).hexdigest()
        if blob != member["git_blob_sha1"]:
            raise ValueError("admitted implementation Git blob changed")
        code_cache[member["filename"]] = data

    def load_fixed(name):
        # Driver must hash-bind these exact files BEFORE this import. Absolute
        # file loading avoids accidental resolution to an unrelated module.
        path = Path(__file__).resolve().with_name(name + ".py")
        code = code_cache[name + ".py"]
        module = {"__name__": "parity_m7_fixed_" + name, "__file__": str(path)}
        # This occurs ONLY in a future admitted run. Reading/compiling/executing
        # definitions here has never been used as a preparation-time test.
        # Direct compilation creates no module __pycache__ side file.
        exec(compile(code, str(path), "exec"), module)
        meter.check_time()
        return module
    producer = load_fixed("producer")
    checker = load_fixed("checker")
    certificate = producer["produce"](spec, meter)
    # The checker consumes the full serialized certificate, not producer
    # polynomial objects or a shared intermediate polynomial representation.
    serialized_certificate = bounded_json(certificate)
    meter.check_output_bound(len(serialized_certificate))
    cold = json.loads(serialized_certificate, object_pairs_hook=no_duplicates)
    checked = checker["verify"](spec, cold, meter)
    result = {"schema": "PARITY_M7_FIXED_INTERVAL_WORKER_RESULT_V1",
              "input_sha256": hashlib.sha256(input_bytes).hexdigest(),
              "certificate_sha256": hashlib.sha256(serialized_certificate).hexdigest(),
              "certificate": cold, "algorithmically_independent_same_author_check": checked,
              "resource_snapshot_before_final_serialization": meter.snapshot(),
              "execution_authority": "EXTERNAL_GENUINE_ADMITTED_DRIVER_REQUIRED",
              "Native_acceptance_or_Task_completion": False}
    output = bounded_json(result)
    meter.output_bytes(output)
    meter.check_time()
    # No disk/network writes occur here. Launcher atomically emits this ONE
    # byte string while counting its own stdout/stderr against the same cap.
    return output

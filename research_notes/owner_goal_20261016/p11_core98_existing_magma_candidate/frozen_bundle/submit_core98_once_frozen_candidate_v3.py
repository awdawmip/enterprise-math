#!/usr/bin/env python3
"""V3 CONTROL evidence-cap repair by EM-DVR-18C67B. Launcher unexecuted.
Only its separate CONTROL writer is tested with synthetic data; no science.
A syntactic admission file is not Native authority: the actual Researcher must
first consume the original current Native/Source gate and independent audit.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import xml.etree.ElementTree as ET
from core98_bounded_evidence_v3 import BoundedEvidence, RAW_CAP

def digest(data):
    return hashlib.sha256(data).hexdigest()

def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--admission", required=True)
    ap.add_argument("--attempt-dir", required=True)
    args = ap.parse_args()
    base = Path(__file__).resolve().parent
    fixed_raw = (base / "CORE98_EXACT_FIXED_SCIENTIFIC_INPUT_V2.json").read_bytes()
    fixed = json.loads(fixed_raw)
    source = (base / fixed["script"]["bundle_filename"]).read_bytes()
    assert digest(source) == fixed["script"]["sha256"]
    assert len(source) == fixed["script"]["bytes"]
    admission_raw = Path(args.admission).read_bytes()
    admission = json.loads(admission_raw)
    # These checks bind files. They do not authenticate a role or grant a run.
    assert admission["scientific_start_allowed"] is True
    assert admission["fixed_input_sha256"] == digest(fixed_raw)
    assert admission["script_sha256"] == digest(source)
    for key in ("actual_researcher_id", "actual_own_session_id",
                "current_Task_id", "current_publication_id",
                "current_winning_claim_id", "current_claim_epoch",
                "current_own_RUN_id", "current_own_ER_id",
                "current_original_Native_and_Source_complete_gate",
                "independent_static_audit_immutable_Source",
                "actual_preparation_budget_ledger_and_stop_rule"):
        assert admission[key], key
    assert admission["same_stopped_fixed233_Task_or_run"] is False
    assert admission["original_current_Native_execution_authorization_consumed"] is True
    assert admission["exact_input_code_codec_cost_audit_pass"] is True
    assert admission["preparation_remaining_seconds_certified"] > 0
    assert admission["single_scientific_invocation_not_previously_consumed"] is True

    # Caller process limits. Provider allocator limit is separately asserted
    # in the frozen Magma source; it is not a host-RSS attestation.
    resource.setrlimit(resource.RLIMIT_AS, (536870912, 536870912))
    resource.setrlimit(resource.RLIMIT_CPU, (20, 21))
    def deadline(_signum, _frame):
        raise TimeoutError("absolute caller wall deadline reached")
    signal.signal(signal.SIGALRM, deadline)
    signal.alarm(90)

    attempt = Path(args.attempt_dir)
    store = BoundedEvidence(attempt)
    body = urlencode({"input": source.decode("utf-8")}).encode("ascii")
    assert len(source) <= 50000 and len(body) <= 50000
    record = {
        "schema": "P11_CORE98_FIXED_REMOTE_SINGLE_ATTEMPT_V1",
        "endpoint": fixed["runtime"]["official_endpoint"],
        "method": "POST",
        "content_type": "application/x-www-form-urlencoded",
        "script_sha256": digest(source),
        "fixed_input_sha256": digest(fixed_raw),
        "admission_sha256": digest(admission_raw),
        "body_ascii": body.decode("ascii"),
        "body_bytes": len(body),
        "body_sha256": digest(body),
        "actual_actor": admission["actual_researcher_id"],
        "actual_RUN": admission["current_own_RUN_id"],
        "request_utc": stamp(),
        "retry_policy": "ZERO_RETRIES_UNKNOWN_DO_NOT_RESUBMIT",
        "max_calls": 1,
        "caller_wall_seconds": 90,
        "caller_address_space_bytes": 536870912,
        "raw_response_cap_bytes": 1048576,
    }
    # The exclusive marker is durable BEFORE the sole POST. Any existing
    # attempt, even one interrupted before receiving a response, forbids replay.
    marker = attempt / "ORIGINAL_SINGLE_ATTEMPT_PREPARED.json"
    store.write_marker(record)
    result = {
        "schema": "P11_CORE98_FIXED_REMOTE_ORIGINAL_RESPONSE_V1",
        "request_sha256": digest(marker.read_bytes()),
        "transport_attempts": 1,
        "retries": 0,
        "mathematical_acceptance": False,
        "portable_local_certificate_complete": False,
        "Native_Task_completion": False,
        "candidate_bit": None,
    }
    started = time.monotonic()
    try:
        req = Request(record["endpoint"], data=body, method="POST", headers={
            "Content-Type": record["content_type"],
            "User-Agent": "Mozilla/5.0",
        })
        try:
            response = urlopen(req, timeout=80)
        except HTTPError as rejected:
            response = rejected  # Preserve the complete actual HTTP error body too.
        with response:
            result.update(http_status=response.status, final_url=response.url,
                          http_headers=dict(response.headers))
            raw = response.read(1048577)
        # At most RAW_CAP bytes are saved. The extra reader byte detects
        # overflow; an incomplete prefix is explicitly labelled, never a
        # complete original response or an implementation candidate.
        result.update(store.write_raw(raw))
        if len(raw) > 1048576:
            result["state"] = "RESPONSE_OVER_CAP_UNKNOWN_NO_RESUBMISSION"
        elif result["http_status"] != 200:
            result["state"] = "DEFINITE_HTTP_REJECTION_RETAINED_NO_RESUBMISSION"
        else:
            tree = ET.fromstring(raw)
            assert tree.tag == "calculator"
            lines = [node.text or "" for node in tree.findall(".//line")]
            header = tree.find(".//headers")
            headers = ({node.tag: node.text for node in header}
                       if header is not None else {})
            result.update(lines=lines, calculator_headers=headers,
                          offline=[node.text for node in tree.findall(".//offline")])
            complete = "EM_CORE98_MIXED_V1_END" in lines
            bitlines = [line for line in lines
                        if line.startswith("IMPLEMENTATION_CANDIDATE_MIXED_BIT ")]
            bit = None
            if complete and len(bitlines) == 1:
                token = bitlines[0].split()[-1]
                if token in ("0", "1"):
                    bit = int(token)
            # This is a vendor implementation observation, not certificate
            # acceptance. Any warning/alert is retained for real review.
            version_ok = headers.get("version") == "2.29-10"
            result.update(complete_end_marker=complete, candidate_bit=bit,
                          response_version_bound=version_ok)
            result["state"] = ("IMPLEMENTATION_CANDIDATE_PENDING_INDEPENDENT_REVIEW"
                               if bit is not None and version_ok
                               else "INCOMPLETE_OR_UNBOUND_UNKNOWN_NO_RESUBMISSION")
    except Exception as error:
        result.update(state="ORIGINAL_ATTEMPT_OUTCOME_UNKNOWN_NO_RESUBMISSION",
                      error=repr(error))
    finally:
        signal.alarm(0)
        result.update(elapsed_caller_monotonic_seconds=time.monotonic()-started,
                      response_observed_utc=stamp())
        # Enforce per-file and aggregate caps BEFORE each evidence write.
        # Oversized parsed fields all disappear into a bounded UNKNOWN
        # summary; raw retained bytes remain unchanged and explicitly typed.
        result = store.write_assessment(result)
        total = store.total_bytes()
        assert total <= 4194304
        print(json.dumps({"state": result["state"], "candidate_bit": result["candidate_bit"],
                          "mathematical_acceptance": False,
                          "attempt_evidence_bytes": total,
                          "attempt_evidence_within_4MiB": True}))
        # This does not call any Native mutation or authorize another attempt.

if __name__ == "__main__":
    main()


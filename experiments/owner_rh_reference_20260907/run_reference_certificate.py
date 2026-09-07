"""Bind one frozen RH reference enclosure to an exact interval-inertia witness.

This standard-library runner does not evaluate a Weil integral. Its verified
conclusion concerns the supplied interval family; identification with H_9/10
also requires the separately audited producer and analytic remainder bounds.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import time

import inertia_certificate as inertia

SCHEMA = "owner_rh_reference_inertia_packet_v1"
SOURCE_HASH = "4e337855d8605125ded80c029022fdc950d1b92cf78ce772480a7b99b9dad49b"
ENDPOINTS = {
    "O-": ("log(1/2)", "log(1)"),
    "O+": ("log(1)", "log(2)"),
    "S-": ("log(1/3)", "log(1/2)"),
    "S+": ("log(2)", "log(3)"),
}
LABELS = [dict(branch=b, k=k, a=ENDPOINTS[b][0], b=ENDPOINTS[b][1])
          for b in ("O-", "O+", "S-", "S+") for k in range(1, 9)]


def _digest(data):
    return hashlib.sha256(data).hexdigest()


def _canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((_canonical(value) + "\n").encode("utf-8"))


def _load_input(path):
    data = Path(path).read_bytes()
    payload = json.loads(data)
    if payload.get("schema") != "owner_rh_reference_bounds_v1":
        raise ValueError("unexpected producer payload schema")
    if payload.get("status") == "UNDETERMINED":
        return data, payload
    if payload.get("status") != "ENCLOSED":
        raise ValueError("producer status must be ENCLOSED or UNDETERMINED")
    if (type(payload.get("dimension")) is not int or payload["dimension"] != 32
            or payload.get("eta") != "9/10"
            or _canonical(payload.get("labels")) != _canonical(LABELS)):
        raise ValueError("payload does not describe the frozen labelled N8 reference")
    if payload.get("provenance", {}).get("source_sha256") != SOURCE_HASH:
        raise ValueError("inherited formula source binding differs from intake")
    budget = payload.get("error_budget", {})
    if budget.get("all_tails_in_bounds") is not True or budget.get("additional_beta") != "0/1":
        raise ValueError("all analytic errors must already be enclosed in entries")
    target = payload.get("target", {})
    if (target.get("matrix") != "[[81/100 A, B_ref], [B_ref^T, D]]"
            or target.get("cross") != "prime + Cauchy; no pole cross or regular arch cross"
            or target.get("diagonals") != "complete arch + prime + both pole channels"
            or target.get("frequency_cutoff") is not None):
        raise ValueError("declared target differs from the frozen reference contract")
    return data, payload


def _incomplete(reason, status="UNDETERMINED"):
    return dict(status=status, negative_count=None, negative_count_bounds=None,
                verification_complete=False, reason=reason,
                scope="INPUT_INTERVAL_FAMILY_ONLY")


def certify_file(input_path, output_path, report_path):
    started = time.perf_counter()
    data, payload = _load_input(input_path)
    packet = dict(schema=SCHEMA, input_file_sha256=_digest(data),
                  checker_source_sha256=_digest(Path(inertia.__file__).read_bytes()),
                  integration_source_sha256=_digest(Path(__file__).read_bytes()),
                  python=platform.python_version(), input_provenance=payload.get("provenance"),
                  certificate=None)
    if payload["status"] == "UNDETERMINED":
        report = _incomplete("producer did not enclose a complete matrix: " + str(payload.get("reason")))
    else:
        try:
            packet["certificate"] = inertia.certify_interval_inertia(payload["bounds"], payload["labels"])
            report = inertia.verify_interval_inertia(payload["bounds"], payload["labels"], packet["certificate"])
        except inertia.ComputationBudgetExceeded as error:
            report = _incomplete("certificate construction budget incomplete: " + str(error))
    report.update(input_file_sha256=packet["input_file_sha256"],
                  elapsed_seconds=time.perf_counter() - started,
                  target_identification="Requires the separate producer and analytic-bound audit.")
    if packet["certificate"] is not None:
        cert = packet["certificate"]
        report.update(delta=cert["delta"], minus_inertia=cert["minus"]["inertia"],
                      plus_inertia=cert["plus"]["inertia"])
    packet["initial_verification"] = report
    _write(output_path, packet)
    _write(report_path, report)
    return report


def verify_file(input_path, certificate_path, report_path):
    started = time.perf_counter()
    data, payload = _load_input(input_path)
    packet = json.loads(Path(certificate_path).read_bytes())
    if packet.get("schema") != SCHEMA or packet.get("input_file_sha256") != _digest(data):
        report = _incomplete("packet schema or full input file binding mismatch", "INVALID_CERTIFICATE")
    elif payload["status"] != "ENCLOSED" or packet.get("certificate") is None:
        report = _incomplete("no complete producer enclosure and inertia witness")
    else:
        report = inertia.verify_interval_inertia(payload["bounds"], payload["labels"], packet["certificate"])
    # The historical initial_verification field is deliberately never consulted.
    report.update(input_file_sha256=_digest(data),
                  current_checker_source_sha256=_digest(Path(inertia.__file__).read_bytes()),
                  elapsed_seconds=time.perf_counter() - started,
                  target_identification="Requires the separate producer and analytic-bound audit.")
    _write(report_path, report)
    return report


def rebind_file(previous_input, previous_certificate, input_path, output_path, report_path):
    """Reuse the exact witness only when the actual bounds and labels agree.

    A producer provenance repair changes the full-file hash, so it requires a
    new envelope. Verification still multiplies the exact original witness;
    no new elimination and no inherited reported status is used.
    """
    old_data, old_payload = _load_input(previous_input)
    new_data, new_payload = _load_input(input_path)
    old_packet_data = Path(previous_certificate).read_bytes()
    old_packet = json.loads(old_packet_data)
    if (old_packet.get("schema") != SCHEMA
            or old_packet.get("input_file_sha256") != _digest(old_data)
            or old_payload["status"] != "ENCLOSED" or new_payload["status"] != "ENCLOSED"):
        raise ValueError("previous packet binding or complete enclosure missing")
    for key in ("bounds", "labels"):
        if _canonical(old_payload[key]) != _canonical(new_payload[key]):
            raise ValueError("rebind requires identical bounds and labels; construct a new witness")
    certificate = old_packet.get("certificate")
    report = inertia.verify_interval_inertia(new_payload["bounds"], new_payload["labels"], certificate)
    report.update(input_file_sha256=_digest(new_data),
                  target_identification="Requires the separate producer and analytic-bound audit.")
    packet = dict(schema=SCHEMA, input_file_sha256=_digest(new_data),
                  checker_source_sha256=_digest(Path(inertia.__file__).read_bytes()),
                  integration_source_sha256=_digest(Path(__file__).read_bytes()),
                  python=platform.python_version(), input_provenance=new_payload.get("provenance"),
                  certificate=certificate, initial_verification=report,
                  witness_reuse=dict(previous_input_file_sha256=_digest(old_data),
                                     previous_packet_file_sha256=_digest(old_packet_data),
                                     bounds_and_labels_identical=True))
    if report["verification_complete"] and certificate is not None:
        report.update(delta=certificate["delta"], minus_inertia=certificate["minus"]["inertia"],
                      plus_inertia=certificate["plus"]["inertia"])
    _write(output_path, packet)
    _write(report_path, report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("certify", "verify", "rebind"))
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--previous-input", type=Path)
    parser.add_argument("--previous-certificate", type=Path)
    args = parser.parse_args()
    if args.mode == "certify":
        result = certify_file(args.input, args.certificate, args.report)
    elif args.mode == "verify":
        result = verify_file(args.input, args.certificate, args.report)
    else:
        if args.previous_input is None or args.previous_certificate is None:
            parser.error("rebind requires --previous-input and --previous-certificate")
        result = rebind_file(args.previous_input, args.previous_certificate,
                             args.input, args.certificate, args.report)
    print(_canonical(result), flush=True)
    return 0 if result["status"] == "CERTIFIED" and result["verification_complete"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

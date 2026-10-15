"""Exact RR133 prospective follow-up binding; never restores historical authority.

This is evidence inside an ordinary native DFU, not a Result replacement, receipt
kind or authority source. The transaction authenticates the live publisher;
replay checks the existing authority at the recorded time. No scientific code is
executed. The absent-field path has no effect on any existing target.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
from typing import Any

FIELD = "prospective_result_authority_binding"
SCHEMA = "ENTERPRISE_MATH_RR133_PROSPECTIVE_RESULT_AUTHORITY_BINDING_V2"
SOURCE_TASK = "RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY"
SOURCE_PUBLICATION = "TP2-5D9C21A7B40E683F1C52"
OLD_RESULT = "RR-1337737608BDE3D7E620"
OLD_REVIEW = "DR-1337737608BDE3D7E621"
OLD_PACKET = "DFU-1337737608BDE3D7E622"
OLD_EXECUTION = "ER-907FEC0874745310610E"
COVERAGE_TASK = "RS-N-COUPLED-PUBLIC-EFFECTIVE-RESOURCE-COVERAGE-OR-ESCAPE-CLASSIFICATION"
OLD_PUBLICATION = "TP2-3F7A91C4E82D105B6A38"
REQUEST = {
    "schema": "ENTERPRISE_MATH_RR133_PROSPECTIVE_BINDING_REQUEST_V2",
    "historical_result_id": OLD_RESULT,
    "historical_packet_id": OLD_PACKET,
    "historical_source_publication_id": SOURCE_PUBLICATION,
    "supersedes_publication_id": OLD_PUBLICATION,
}
# Frozen literals below are generated from the thirteen actual historical files.
# No new Result, execution, review or packet ID is preselected.
OLD_PINS = [{'path': 'driver_reviews/N_COUPLED_PUBLIC_EFFECTIVE_DISTRIBUTIONAL_EXTERNALIZATION_DRIVER_REVIEW_20260905.md',
  'sha256': '7be20f6300788dc27d1ff36e96c27a8e85a866776a0aa2daf5994989dba05828',
  'git_blob_sha1': '9282fbc4d05eb9cbbe4188505142cd96a3c7df17'},
 {'path': 'research_artifacts/N_COUPLED_PUBLIC_N_DISTRIBUTIONAL_NONEXTERNALIZABILITY/effect_dist_public_emulator_certificate.json',
  'sha256': '80459f904e3970ce94b9c4a805cc016becac3e30a249e45cf0157f40c2a9e42f',
  'git_blob_sha1': '1a069261cc02d3ee6b87d05ae696f2ea030c6b57'},
 {'path': 'research_artifacts/N_COUPLED_PUBLIC_N_DISTRIBUTIONAL_NONEXTERNALIZABILITY/effect_dist_public_emulator_contract.json',
  'sha256': '1b2eb316133319b608f9255e567a9baa258e1222c60484be94bc388fbb547d5b',
  'git_blob_sha1': '978b26d2d51274495100295a3119e8620b86f560'},
 {'path': 'research_checks/N_COUPLED_PUBLIC_N_DISTRIBUTIONAL_NONEXTERNALIZABILITY_CHECK_20260904.py',
  'sha256': '4b7b4de15a291526c1615b276248aa5a093c08459c835b07003d82a8eb131265',
  'git_blob_sha1': 'd984550a0fc5c61de48cc9db52cec46f0b2f5123'},
 {'path': 'research_execution_records/RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY/ER-907FEC0874745310610E.json',
  'sha256': '1b4087cea3ce3eb293470ead430b4689e08e06cf19de56bfa6a672706dd62dec',
  'git_blob_sha1': 'af15aadec9a883aedf75ac0b68fde87da6dc4a56'},
 {'path': 'research_result_records/RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY/RR-1337737608BDE3D7E620.json',
  'sha256': '6aa50538385eece0fc236824262c8fe149070c0070043ba275c1f88f10340fb6',
  'git_blob_sha1': 'c618fd689127b6b532ba47416c20fb61d28000ff'},
 {'path': 'research_result_reviews/RR-1337737608BDE3D7E620/DR-1337737608BDE3D7E621.json',
  'sha256': 'd2c963ded45adaddec265e59ea93534e87a0f4bb1a5372d595b0225e5e289156',
  'git_blob_sha1': '6210a153d048b2065e6156e2d953dc4ee6b937c3'},
 {'path': 'research_returns/N_COUPLED_PUBLIC_N_DISTRIBUTIONAL_NONEXTERNALIZABILITY_RETURN_20260904.md',
  'sha256': 'd2b8119ea453568bac2f4e33c8c4c4f2d15b906f8956a2d2ec846ff4f22aa7b3',
  'git_blob_sha1': 'bc7e4a6e4bf8cd7054f44509c9734053bcc37714'},
 {'path': 'research_task_records/RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY/TP2-5D9C21A7B40E683F1C52.json',
  'sha256': '792116597e69f62ba7f95aa2a8b48ca3c2b03e59452dc52ef430c9abf4a70425',
  'git_blob_sha1': '1eb4fe4825ff1ff4eeac929ba72fb5a277614c2e'},
 {'path': 'research_tasks/N_COUPLED_PUBLIC_N_DISTRIBUTIONAL_NONEXTERNALIZABILITY_20260903.md',
  'sha256': 'c45d888ce01dd1a9a9c25f7b065e8b89f23e9690bfc6c5baab63daa6d8047a87',
  'git_blob_sha1': '7be6bca90aeb7b1e8222090ea6e22797f9e96f8c'},
 {'path': 'research_driver_followups/DR-1337737608BDE3D7E621/DFU-1337737608BDE3D7E622.json',
  'sha256': '74ccb3b5936d03ce4bfb7c030f609affb7df05948567d29d64be40fa2f8b1fc8',
  'git_blob_sha1': 'c7eccddd4544c8f04409f0f5958a874d74da28d4'},
 {'path': 'research_task_records/RS-N-COUPLED-PUBLIC-EFFECTIVE-RESOURCE-COVERAGE-OR-ESCAPE-CLASSIFICATION/TP2-3F7A91C4E82D105B6A38.json',
  'sha256': '4c42812831985ecc39973a7785cd66f222b4e6e8045f3b7baaa7a226af097b1f',
  'git_blob_sha1': '6db8b61cdd4fde1c6f77752f669e256ca1c03261'},
 {'path': 'research_tasks/N_COUPLED_PUBLIC_EFFECTIVE_RESOURCE_COVERAGE_OR_ESCAPE_CLASSIFICATION_20260905.md',
  'sha256': '001cb13f0f4bd944873ecacda1642c811ed7ac1970df1cb976b47d9a9a78a875',
  'git_blob_sha1': 'c3d4230acf4aab5d11d895a614cc498135df88d4'}]
OLD_QUARANTINE_ROW_SHA256 = ['116a9c957d5dd1f8f9ee65ba365b7836dcd213f209073400eb05cdcf001cb9f6', '9f83e9dcd8a38605105d639a0e14e0cca65d1cc8b068a3e45944d35de586fb3c']

# Exact already-published Source launch. This classification is not a DFU and
# does not restore its quarantined source Result/review/packet or RR133 authority.
SOURCE_LAUNCH_PUBLICATION = "TP2-7B35867C594D13793C9F"
SOURCE_LAUNCH_PACKET = "DFU-83B1D6E4C9027A5F3148"
SOURCE_LAUNCH_DRIVER = "EM-DVR-FBF223"
SOURCE_LAUNCH_DA = "DA-A1DB35C00ED2F8C2A9FA"
SOURCE_LAUNCH_SESSION = "MCP-cd5eefdde49843898b2a70c1af94d8dd"
SOURCE_LAUNCH_OBJECTIVE = "OBJ-N-COUPLED-ASYMMETRIC-SINGULARIZATION"
SOURCE_LAUNCH_OBJECTIVE_GENERATION = "OG-7F2B4C1D9A6E83F05211"
SOURCE_LAUNCH_QUARANTINE_SHA256 = "da429d3ff2c89059503e0fbe4644a29c50b7cd425173b5584c7b3fcffb9b35a4"
SOURCE_LAUNCH_PINS = [{'path': 'research_driver_followups/DR-4B7576B2FDCA2CCBAB38/DFU-83B1D6E4C9027A5F3148.json',
  'sha256': '1f28d520a8c04c8ed89a17ae673eea9582a50b5580bb2063c88a5aadef80204d',
  'git_blob_sha1': 'f25952c92cd19e2935dac5ae6351923467e37e52'},
 {'path': 'research_task_records/RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY/TP2-7B35867C594D13793C9F.json',
  'sha256': '999b1078d53bf3e1c652169041c02f6f8f439752cb8cfd86b68f16cb8e7bd51d',
  'git_blob_sha1': '66892a4aa56c58c0686b546af9ff46523fb01ccc'},
 {'path': 'research_tasks/N_COUPLED_PUBLIC_N_DISTRIBUTIONAL_NONEXTERNALIZABILITY_GEN2_PROSPECTIVE_20261015.md',
  'sha256': 'a3869fbedf4ed0c07edfd41932474af20bbc43acbeafa385e20feb90369550ee',
  'git_blob_sha1': '4a0ecb0753267a86ae2704b0d2f189a7d58ff784'},
 {'path': 'research_objective_records/OBJ-N-COUPLED-ASYMMETRIC-SINGULARIZATION/OG-7F2B4C1D9A6E83F05211.json',
  'sha256': '4c26c11a1ca55f26cbd0fa425e4a30963013e1c6e50d1dc40228f4d97a05c709',
  'git_blob_sha1': '3818a464ea3a3f9cc7401f3a7be4ea5e5e75eb3c'},
 {'path': 'research_objective_head_events/OBJ-N-COUPLED-ASYMMETRIC-SINGULARIZATION/OG-7F2B4C1D9A6E83F05211.json',
  'sha256': '1ff79c1d05bd05a60d232606b34408f1beadfe65590d322c10c0ba07b5bfdb18',
  'git_blob_sha1': '24668f73410c1ff365e15e330e2f9783005febec'},
 {'path': 'research_driver_authority_records/EM-DVR-FBF223/DA-A1DB35C00ED2F8C2A9FA.json',
  'sha256': '6ada7e5128bf10187cc48d19af08c6ee7e6107e7b0fc01fbfcc54d63117e5436',
  'git_blob_sha1': 'ee0efd29554fdcb8cca69266e60d80ee4f731cbd'},
 {'path': 'research_session_records/MCP-cd5eefdde49843898b2a70c1af94d8dd.json',
  'sha256': '55f1af52cbd06d3f05edd23afdbda758ad0456031ef76a853b74f73d1fe8e560',
  'git_blob_sha1': '03e2379359e23c86786dcdd884fb3f4a340bfd4e'}]


def _require(condition: bool, reason: str) -> None:
    if not condition:
        from research_driver_followup import DriverFollowupError
        raise DriverFollowupError("RR133 prospective binding: " + reason)


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def validate_request(value: Any) -> None:
    _require(_canonical(value) == _canonical(REQUEST), "request is not the exact closed RR133 request")


def _path(root: Path, value: Any) -> Path:
    _require(isinstance(value, str) and bool(value) and "\\" not in value and ":" not in value,
             "invalid repository-local path")
    relative = PurePosixPath(value)
    _require(not relative.is_absolute() and relative.as_posix() == value
             and all(part not in {".", ".."} for part in relative.parts), "noncanonical path")
    path = root / value
    _require(path.resolve().is_relative_to(root.resolve()) and path.is_file(), "missing or escaped source path")
    return path


def _pin(root: Path, relative: str) -> dict[str, str]:
    data = _path(root, relative).read_bytes()
    return {"path": relative, "sha256": hashlib.sha256(data).hexdigest(),
            "git_blob_sha1": hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()}


def _object(root: Path, relative: str) -> dict[str, Any]:
    value = json.loads(_path(root, relative).read_text(encoding="utf-8"))
    _require(isinstance(value, dict), "source JSON must be an object")
    return value


def _ordinary_receipt(record: dict[str, Any], kind: str, root: Path) -> None:
    from control_plane import research_continuation_write_authority as writer
    cutover = writer._pins(root)
    receipt = record.get("write_authorization")
    _require(cutover is not None and writer.record_path(record, kind) not in cutover,
             "prospective authority cannot use a missing cutover or legacy exemption")
    _require(isinstance(receipt, dict) and receipt.get("schema") == writer.SCHEMA
             and receipt.get("kind") == kind and receipt.get("payload_sha256") == writer.payload_digest(record),
             f"{kind} requires a prospective payload-bound native receipt")
    error = writer.receipt_error(record, kind, root)
    _require(error is None, f"{kind} existing write authority failed: {error}")


def _manifest(result: dict[str, Any], root: Path) -> list[dict[str, str]]:
    rows = result.get("output_manifest")
    _require(isinstance(rows, list) and bool(rows), "missing new output manifest")
    pins = []
    for row in rows:
        _require(isinstance(row, dict) and set(row) == {"path", "sha256", "git_blob_sha1"},
                 "invalid output manifest row")
        pin = _pin(root, row["path"])
        _require(row["sha256"] == "sha256:" + pin["sha256"]
                 and str(row["git_blob_sha1"]).removeprefix("sha1:") == pin["git_blob_sha1"],
                 "new output manifest byte drift")
        pins.append(pin)
    _require(len({pin["path"] for pin in pins}) == len(pins), "duplicate output manifest path")
    return sorted(pins, key=lambda pin: pin["path"])


def source_generation_body(old_body: str, research_value: str) -> str:
    """Exact single-target legacy-section render, preserving every science clause.

    No generic heading alias and no custody-only substitute for mathematical
    success. The full old target/negative alternative is repeated in criteria.
    Old bytes are independently pinned before this function is used in binding.
    """
    headings = ["Mother question", "Frozen boundary", "Hard target", "Mechanism firewall", "Required evidence"]
    parts = old_body.split("\n## ")
    _require(len(parts) == 6, "source Gen1 exact legacy section structure drift")
    sections = {}
    for expected, part in zip(headings, parts[1:]):
        title, separator, content = part.partition("\n")
        _require(separator == "\n" and title == expected and bool(content.strip()), "source Gen1 legacy section drift")
        sections[title] = content.strip()
    supplemental = (
        "Evidence reuse and current execution provenance (additional custody requirements, not a replacement mathematical target):\n\n"
        "Consume the exact preserved RR133 scientific evidence and independently check its applicability to the full mathematical target above. "
        "Do not rerun already completed scientific checks merely to obtain a new ID. "
        "Return the actual mathematical verdict, including the original permitted negative boundary and unresolved parent scope; custody success alone is not mathematical success. "
        "Publish this session's genuine return and RR133_PROSPECTIVE_EVIDENCE_MANIFEST.json, preserving all original contributor attribution and disclosing source exposure. "
        "The evidence manifest must bind the exact historical pins; it confers no authority on old records."
    )
    values = [
        ("Mother question", sections["Mother question"]),
        ("Frozen inputs and scope", "Frozen boundary (verbatim):\n\n" + sections["Frozen boundary"]
         + "\n\nMechanism firewall (verbatim):\n\n" + sections["Mechanism firewall"]),
        ("Hard target and required outputs", "Hard target (verbatim):\n\n" + sections["Hard target"]
         + "\n\nRequired evidence (verbatim):\n\n" + sections["Required evidence"]),
        ("Research value to preserve", research_value),
        ("Success, kill, and return criteria", "The original mathematical success/negative-boundary criteria remain mandatory (verbatim):\n\n"
         + sections["Hard target"] + "\n\nThe original evidence and scope limits remain mandatory (verbatim):\n\n"
         + sections["Required evidence"] + "\n\n" + supplemental),
    ]
    return parts[0].strip() + "\n\n" + "\n\n".join("## " + name + "\n\n" + content for name, content in values) + "\n"


def _generation(root: Path, task_id: str, old_id: str, pid: str,
                publisher: dict[str, Any] | None = None) -> tuple[dict[str, Any], list[dict[str, str]]]:
    from tools import research_task_records as tasks, research_taskbook as books
    _require(isinstance(pid, str) and pid != old_id and "/" not in pid,
             "a distinct native publication is required")
    relative = f"research_task_records/{task_id}/{pid}.json"
    new = _object(root, relative)
    old = _object(root, f"research_task_records/{task_id}/{old_id}.json")
    _require(new.get("publication_id") == pid and new.get("task_id") == task_id
             and type(new.get("publication_generation")) is int and new["publication_generation"] == 2
             and new.get("supersedes_publication_id") == old_id
             and new.get("record_schema") == tasks.RECORD_SCHEMA and new.get("record_state") == "ACTIVE",
             "only direct Gen2 supersession of the pinned Gen1 is permitted")
    old_meta, old_body = books.split_taskbook(_path(root, old["taskbook_path"]).read_text(encoding="utf-8"))
    new_path = _path(root, new.get("taskbook_path"))
    _require(new_path.resolve().is_relative_to((root / "research_tasks").resolve()), "successor is outside native taskbook store")
    meta, body = tasks._prepared(new_path, root=root)
    fields = ("task_id", "registry_key", "kind", "owner", "parent_objective_id", "origin_kind", "origin_candidate_id",
              "origin_candidate_state", "task_lineage", "parent_task_id", "identity_lane", "successor_gate",
              "source_refs", "dependencies", "frontier", "next_action")
    def scope(text: str) -> tuple[str, dict[str, str]]:
        lines = text.splitlines()
        start = next((i for i, line in enumerate(lines) if line.lstrip().startswith("##")
                      and "mother question" in line.lower()), len(lines))
        _require(len([line for line in lines if line.lstrip().startswith("##")]) == len(tasks.MANDATORY_BODY_SECTIONS),
                 "successor has extra or missing semantic sections")
        return "\n".join(lines[:start]).strip(), tasks._section_payloads(text)
    expected_body = source_generation_body(old_body, old["research_value"]) if task_id == SOURCE_TASK else old_body
    old_prefix, old_sections = scope(expected_body)
    prefix, sections = scope(body)
    native_prefix = f"# {old_meta['title']}\n\nStatus: `READY / DRIVER REVIEW FOLLOW-UP / PENDING IMMUTABLE PUBLICATION`"
    expected_meta = dict(old_meta)
    if task_id == SOURCE_TASK:
        # The old origin literal is not a current legal publication origin.
        # This is a new Driver roadmap generation, not a rewrite of Gen1.
        _require(old_meta.get("origin_kind") == "DRIVER_REVIEW_FOLLOWUP", "old source origin drift")
        expected_meta["origin_kind"] = "DRIVER_ROADMAP"
    _require(prefix in {old_prefix, native_prefix} and sections == old_sections
             and meta.get("title") == old_meta.get("title")
             and all(meta.get(k) == expected_meta.get(k) == new.get(k) for k in fields),
             "successor changed the exact frozen scope")
    blob = tasks.taskbook_blob(new_path)
    _require(new.get("taskbook_blob_sha1") == blob
             and pid == tasks.publication_id(task_id, blob, new.get("publisher_id", ""), old_meta["parent_objective_id"])
             and (publisher is None or new.get("publisher_id") == publisher["driver_id"])
             and new.get("publisher_role") == "RESEARCH_DRIVER"
             and new.get("research_value") == old.get("research_value")
             and new.get("terminal_scope") == "TASK"
             and new.get("working_truth_granted") is False and new.get("canonical_promotion_granted") is False,
             "successor publication identity/publisher/no-grant mismatch")
    import research_driver_authority as authority
    active = authority.require_active_driver(new["publisher_id"], new["published_at"], root)
    _require(active is not None, "Gen2 publication requires actual Driver authority at publication")
    from research_driver_followup import _parse_time
    _require(_parse_time(old["published_at"], "Gen1 publication") <= _parse_time(new["published_at"], "Gen2 publication"),
             "Gen2 publication predates its historical predecessor")
    return new, [_pin(root, relative), _pin(root, new["taskbook_path"]), _pin(root, active["_record_path"])]


def validate_exact_source_launch_successor(
    task: dict[str, Any], row: dict[str, Any], source_packet: dict[str, Any],
    active_heads: set[str], root: Path,
) -> bool:
    """Classify only the pinned prospective Source launch, never a follow-up.

    Its future Result/DR/DFU cannot be a prerequisite to launching the research.
    Coverage publication still requires the ordinary complete native chain.
    All other tasks/publications retain the existing independent-successor path.
    """
    if task.get("task_id") != SOURCE_TASK or task.get("publication_id") != SOURCE_PUBLICATION:
        return False
    _require(active_heads == {SOURCE_LAUNCH_PUBLICATION}, "source launch must have its one exact existing Gen2 head")
    _require(hashlib.sha256(_canonical(row).encode()).hexdigest() == SOURCE_LAUNCH_QUARANTINE_SHA256
             and row.get("packet_id") == SOURCE_LAUNCH_PACKET
             and row.get("derived_task_publications") == [task], "source launch historical isolation row drift")
    for pin in [*OLD_PINS, *SOURCE_LAUNCH_PINS]:
        _require(_pin(root, pin["path"]) == pin, "source launch exact original or publication pin drift")
    _require(source_packet == _object(root, row["packet_path"]), "source launch source packet differs from pinned original")
    new, _ = _generation(root, SOURCE_TASK, SOURCE_PUBLICATION, SOURCE_LAUNCH_PUBLICATION)
    _require(new.get("publisher_id") == SOURCE_LAUNCH_DRIVER
             and new.get("origin_kind") == "DRIVER_ROADMAP"
             and new.get("parent_objective_id") == SOURCE_LAUNCH_OBJECTIVE
             and new.get("parent_objective_generation_id") == SOURCE_LAUNCH_OBJECTIVE_GENERATION,
             "source launch publisher, origin or parent drift")
    import research_driver_authority as authority
    import research_objective_authority as parent
    import research_objective_driver_authority as objective_driver
    def root_action(at: str) -> None:
        active = authority.require_active_driver(SOURCE_LAUNCH_DRIVER, at, root)
        _require(active is not None and active.get("authority_record_id") == SOURCE_LAUNCH_DA
                 and json.loads(active["source_body"]).get("session_id") == SOURCE_LAUNCH_SESSION,
                 "source launch requires the exact Root Driver authority and session at action time")
        _require(not objective_driver._errors_for_action(
            actor=SOURCE_LAUNCH_DRIVER, at=at, authority_record_id=SOURCE_LAUNCH_DA,
            authority_source_comment_id=active["source_comment_id"], prefix="exact RR133 source launch", root=root),
            "source launch Driver action authority failed")
    root_action(new["published_at"])
    session = _object(root, f"research_session_records/{SOURCE_LAUNCH_SESSION}.json")
    _require(session.get("session_id") == SOURCE_LAUNCH_SESSION
             and session.get("role") == "RESEARCH_DRIVER"
             and session.get("execution_id") == SOURCE_LAUNCH_DRIVER, "source launch public session binding drift")
    resolved = parent.resolve_authoritative_task_parent_binding(new, root)
    _require(resolved.get("binding_source") == "TASK_PUBLICATION_DIRECT"
             and resolved.get("objective_id") == SOURCE_LAUNCH_OBJECTIVE
             and resolved.get("objective_generation_id") == SOURCE_LAUNCH_OBJECTIVE_GENERATION
             and resolved.get("objective_authority_verified") is True, "source launch lacks direct authoritative parent tenure")
    receipt = resolved["operational_selection"]["receipt"]
    _require(receipt.get("selected_by") == SOURCE_LAUNCH_DRIVER
             and receipt.get("objective_status") == "OPEN", "source launch selection actor or status drift")
    root_action(receipt["selected_at"])
    objective = _object(root, f"research_objective_records/{SOURCE_LAUNCH_OBJECTIVE}/{SOURCE_LAUNCH_OBJECTIVE_GENERATION}.json")
    _require(not objective_driver._errors_for_action(
        actor=objective["publisher_id"], at=objective["created_at"],
        authority_record_id=objective["driver_authority_record_id"],
        authority_source_comment_id=objective["driver_authority_source_comment_id"],
        prefix="retained RR133 source Objective", root=root), "source launch retained Objective authority failed")
    return True


def expected_binding(packet: dict[str, Any], root: Path) -> dict[str, Any]:
    """Construct from actual bytes; never trusts the supplied nested binding."""
    import research_driver_followup as followup
    import research_driver_authority as authority
    import research_driver_followup_guard as guard
    from tools import research_execution_records as executions
    from control_plane import research_result_records_impl as results
    from control_plane import research_result_review_audit_fault_isolation as review_audit
    from control_plane import research_result_authority_fault_isolation as result_isolation
    from control_plane import research_driver_followup_fault_isolation as followup_isolation

    _require(packet.get("decision") == "TASK_SET_PUBLISHED"
             and packet.get("task_id") == SOURCE_TASK,
             "wrong decision or source Task/publication")
    for pin in OLD_PINS:
        _require(_pin(root, pin["path"]) == pin, "historical evidence byte drift: " + pin["path"])
    old_rows = (result_isolation.quarantine_rows(root).get(OLD_RESULT),
                followup_isolation.quarantine_rows(root).get(OLD_PACKET))
    _require([hashlib.sha256(_canonical(row).encode()).hexdigest() for row in old_rows] == OLD_QUARANTINE_ROW_SHA256,
             "historical quarantine row changed or disappeared")

    source_id = packet.get("source_publication_id")
    source, source_publication_pins = _generation(root, SOURCE_TASK, SOURCE_PUBLICATION, source_id)
    rid, drid = packet.get("result_id"), packet.get("review_id")
    _require(isinstance(rid, str) and rid.startswith("RR-") and rid != OLD_RESULT and "/" not in rid,
             "a distinct ordinary Result is required")
    _require(isinstance(drid, str) and drid.startswith("DR-") and drid != OLD_REVIEW and "/" not in drid,
             "a distinct ordinary native DR is required")
    result_path = f"research_result_records/{SOURCE_TASK}/{rid}.json"
    review_path = f"research_result_reviews/{rid}/{drid}.json"
    result, review = _object(root, result_path), _object(root, review_path)
    _require(result.get("result_id") == rid and result.get("task_id") == SOURCE_TASK
             and result.get("publication_id") == source_id, "new Result identity/source mismatch")
    _require(review.get("review_id") == drid and review.get("result_id") == rid
             and review.get("disposition") == "ACCEPTED" and review.get("result_record_path") == result_path,
             "new DR must accept the exact new Result")
    operational_result = followup.result_map(root).get(rid)
    operational_review = guard.authority_map(root).get(drid)
    _require(operational_result is not None and operational_review is not None
             and operational_review.get("review_authority_kind") == "IMMUTABLE_REVIEW"
             and operational_review.get("source_review_ids") == [drid],
             "new Result/unique native DR is not current operational authority")
    _ordinary_receipt(result, "RESULT", root)
    _ordinary_receipt(review, "REVIEW", root)
    eid = result.get("execution_record_id")
    _require(isinstance(eid, str) and eid != OLD_EXECUTION and "/" not in eid, "a different canonical execution is required")
    execution_path = f"research_execution_records/{SOURCE_TASK}/{eid}.json"
    execution = _object(root, execution_path)
    _require(execution.get("record_schema") == executions.SCHEMA and execution.get("execution_record_id") == eid
             and results.execution_map(root).get(eid) is not None, "new execution is not in the canonical native map")
    # This narrowly scoped route is the original single-owner, noncohort Task.
    _require(all(execution.get(k) is None and result.get(k) is None for k in ("execution_cohort_id", "execution_lane_id", "lane_output_prefix")),
             "this binding cannot add an execution cohort/lane")
    _require(eid == executions.execution_record_id(SOURCE_TASK, source_id, result.get("claim_id", ""),
                result.get("researcher_id", ""), result.get("execution_branch", "")), "new execution ID is not canonical")
    _require(all(execution.get(k) == source.get(k) for k in ("task_id", "publication_id", "taskbook_path", "taskbook_blob_sha1"))
             and execution.get("execution_branch_base") == result.get("execution_branch_base")
             and result.get("taskbook_path") == execution.get("taskbook_path"), "new execution source/base mismatch")
    _require(not results.audit_result_record(result, execution, root), "new Result failed its existing strict native audit")
    _require(not review_audit._review_errors(review, result, root)
             and not authority.review_authority_errors(review, root), "new DR failed its existing native integrity/authority audit")
    old_result = _object(root, f"research_result_records/{SOURCE_TASK}/{OLD_RESULT}.json")
    pins = _manifest(result, root)
    by_path = {pin["path"]: pin for pin in pins}
    evidence = [pin for pin in pins if PurePosixPath(pin["path"]).name == "RR133_PROSPECTIVE_EVIDENCE_MANIFEST.json"]
    _require(len(evidence) == 1, "new Result requires its unique native evidence manifest output")
    custody = _object(root, evidence[0]["path"])
    historical_authors = sorted(set(old_result.get("contributor_ids", [])) | {old_result["researcher_id"]})
    expected_custody = {"schema": "ENTERPRISE_MATH_RR133_PROSPECTIVE_EVIDENCE_CUSTODY_V2",
                        "historical_request": REQUEST, "historical_pins": OLD_PINS,
                        "historical_contributor_ids": historical_authors}
    _require(_canonical(custody) == _canonical(expected_custody), "closed historical evidence manifest mismatch")
    _require(result.get("return_path") != old_result.get("return_path")
             and result.get("return_path") in by_path and result.get("return_path") != evidence[0]["path"],
             "new Result requires its distinct new return and custody manifest")
    _require(result.get("source_exposure_status") == "NONBLIND_DISCLOSED", "historical evidence reuse requires nonblind disclosure")
    _require(not set(historical_authors) & (set(review.get("reviewer_contribution_ids", [])) | {review.get("driver_id")}),
             "current reviewer overlaps the preserved historical scientific authors")
    # Check native allowed-output scope as well as content hashes; no ER alias.
    rebuilt = results.build_output_manifest([_path(root, pin["path"]) for pin in pins], execution, root)
    _require(len(rebuilt) == len(pins), "new execution output scope drift")
    publisher = packet.get("materialization_publisher")
    _require(isinstance(publisher, dict), "native authenticated publisher binding is required")
    expected_publisher = followup._materialization_binding(drid, publisher.get("driver_id"), publisher.get("session_id"),
                                                         packet.get("created_at"), root)
    _require(expected_publisher is not None and publisher == expected_publisher, "native publisher binding drift")
    rows = packet.get("task_publications")
    _require(isinstance(rows, list) and len(rows) == 1 and isinstance(rows[0], dict)
             and rows[0].get("task_id") == COVERAGE_TASK, "only the exact single coverage Task is permitted")
    new, publication_pins = _generation(root, COVERAGE_TASK, OLD_PUBLICATION, rows[0].get("publication_id"), publisher)
    parse = followup._parse_time
    _require(parse(source.get("published_at"), "new source publication") <= parse(result.get("frozen_at"), "new freeze")
             and parse(old_result.get("frozen_at"), "old freeze") <= parse(result.get("frozen_at"), "new freeze")
             <= parse(review.get("reviewed_at"), "new review") <= parse(new.get("published_at"), "new publication")
             <= parse(packet.get("created_at"), "new packet"), "prospective time order is invalid")
    new_pins = [_pin(root, relative) for relative in (execution_path, result_path, review_path, review["review_path"])]
    return {"schema": SCHEMA, "historical_request": dict(REQUEST), "historical_pins": OLD_PINS,
            "historical_quarantine_row_sha256": OLD_QUARANTINE_ROW_SHA256,
            "new_result_id": rid, "new_execution_record_id": eid, "new_review_id": drid,
            "new_source_publication_id": source_id, "new_source_publication_pins": source_publication_pins,
            "new_packet_id": packet.get("packet_id"), "new_source_pins": new_pins,
            "new_output_manifest_pins": pins, "successor_publication_pins": publication_pins,
            "historical_contributor_ids": historical_authors,
            "historical_authority_restored": False, "working_truth_granted": False,
            "foundation_authority_granted": False, "canonical_promotion_granted": False}


def validate_binding(packet: dict[str, Any], root: Path) -> None:
    _require(FIELD in packet and _canonical(packet[FIELD]) == _canonical(expected_binding(packet, root)),
             "closed binding differs from recomputed exact evidence")


def successor_target(packet: dict[str, Any], task: dict[str, Any], row: dict[str, Any],
                        source_packet: dict[str, Any], root: Path) -> tuple[str, str]:
    """The sole optional departure from historical same-Result equality."""
    if FIELD not in packet:
        return row["result_id"], source_packet["source_publication_id"]
    _require(row.get("result_id") == OLD_RESULT and source_packet.get("packet_id") == OLD_PACKET
             and source_packet.get("review_id") == OLD_REVIEW and source_packet.get("result_id") == OLD_RESULT
             and task.get("task_id") == COVERAGE_TASK and task.get("publication_id") == OLD_PUBLICATION,
             "binding cannot be reused for another quarantine/ancestor")
    validate_binding(packet, root)
    return packet["result_id"], packet["source_publication_id"]

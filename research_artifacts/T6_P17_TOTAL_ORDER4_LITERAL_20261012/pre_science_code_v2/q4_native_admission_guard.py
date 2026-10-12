"""NEW Q4 actual-admission guard; extension of Source-covered q3 control joins.
No native API, remote write, identity registration or import-time execution.
Absent real published Task/current own Source claim/open inputs => fail closed.
"""
from pathlib import Path
from datetime import datetime, timezone
import base64,json,re,zlib
from order4_exact_math_and_input import require,read,digest,blob,nofloat,unique_object,INPUT_SHA,InvariantError
ACTOR="EM-T6-B4F89F"
SID="MCP-2b2adc7725e84b0c90908ba5db66a17f"
RA="RA-B6662BE3C64EEFC2AA156A87"
GLOBAL_GOAL="EM-T6-SHAPE-MOMENT-EXACT-THRESHOLD"
PORTABLE_SHA="7060ee638986a5c71a9775093e6b7f03ff3d5ff205ed438e3f5fa5aa93ca62ce"
SCOPE="ALL_30992_LITERAL_RELAXED_TOTAL_ORDER4_PATTERNS"
FORBIDDEN_RUNS={"RUN-7660266e1c79ee012f9dc469","RUN-487a00106ee481b05e05902d","RUN-03ce4e87c7c7defc4bc767ec","RUN-56050ddbae8ccb1f54296dd8"}
FORBIDDEN_CLAIMS={"MCP-280ddc7735532406ab95a2ba","MCP-c6ee554bb4e23442bc892094","MCP-18b6941bcefb78bff971609b"}
FORBIDDEN_TASKS={"RS-T6-P17-VERTICAL-ORDER1-EXACT-AFFINE-BUDGET","RS-T6-P17-ORDER2-PORTABLE-CERTIFICATE-20260923","RS-T6-P17-TOTAL-ORDER3-LITERAL-PORTABLE-20261012"}
FORBIDDEN_PUBLICATIONS={"TP2-26869C0B4D63A6BB761D","TP2-33BFE7DD84657DAB803C","TP2-74DDE98D322E020794E5","TP2-7B92A919379F827FE997"}
SOURCE_AUTHORS={"EM-DIRECT-49ADE6","EM-DIRECT-E1F2B6","EM-DIRECT-FA0C27","EM-DVR-4C90FB","EM-DVR-C1A1D9","EM-DVR-FBF223","EM-T6-B4F89F","EM-DVR-4CF7AF"}

def source_input_bytes(source_bytes, descriptor):
    """Verify/decode exact Source package+parts; never execute the builder."""
    package_raw=source_bytes[descriptor['source_path']]
    require(len(package_raw)==4514 and digest(package_raw)==
            '870a56a5a6da305023e16fc6f3e0bd3f08ab95a17a813208da8e1091661511a5',
            'Frozen exact independently reviewed package index bytes')
    package=parsed_raw(package_raw)
    require(package['schema']=='T6_P17_ORDER4_FIXED_INPUT_LOSSLESS_PACKAGE_V1'
            and package['fixed_input_sha256']==INPUT_SHA
            and package['fixed_input_bytes']==13084243, 'Exact adopted q4 input package')
    source_paths=descriptor['carrier_source_paths']
    require(len(source_paths)==package['part_count']==len(package['parts']), 'All input carriers required')
    encoded=[];offset=0
    for i,(path,pin) in enumerate(zip(source_paths,package['parts'])):
        raw=source_bytes[path]
        require(path.endswith('/'+pin['path']) and len(raw)==pin['bytes']
                and digest(raw)==pin['sha256'] and blob(raw)==pin['git_blob_sha1'], 'Source carrier byte pins')
        row=parsed_raw(raw)
        require(row['schema']=='T6_P17_ORDER4_FIXED_INPUT_LOSSLESS_PART_V1'
                and row['part_index']==i and row['part_count']==len(source_paths)
                and row['input_sha256']==INPUT_SHA
                and row['bundle_gzip_sha256']==package['bundle_gzip_sha256'], 'Carrier order/bundle bindings')
        payload=row['payload_base64']
        require(type(payload) is str and len(payload)==pin['base64_characters']
                and pin['base64_offset']==offset, 'Carrier Base64 offsets')
        encoded.append(payload);offset+=len(payload)
    text=''.join(encoded);require(len(text)==package['bundle_base64_characters'], 'Complete Base64 length')
    compressed=base64.b64decode(text,validate=True)
    require(base64.b64encode(compressed).decode('ascii')==text
            and len(compressed)==package['bundle_gzip_bytes']
            and digest(compressed)==package['bundle_gzip_sha256'], 'Whole compressed input pins')
    total=package['bundle_raw_bytes'];require(type(total) is int and 0<total<=64*1048576,'Decode bound')
    decoder=zlib.decompressobj(31);data=decoder.decompress(compressed,total+1)
    require(decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail
            and len(data)==total and digest(data)==package['bundle_raw_sha256'], 'Bounded single gzip/CRC/EOF')
    cursor=0;members={}
    for pin in package['originals']:
        name=pin['path'];require(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*',name)
            and name not in members and pin['offset']==cursor
            and type(pin['bytes']) is int and pin['bytes']>=0, 'Member path/offset/duplicate')
        raw=data[cursor:cursor+pin['bytes']]
        require(len(raw)==pin['bytes'] and digest(raw)==pin['sha256']
                and blob(raw)==pin['git_blob_sha1'], 'All adopted input original bytes')
        members[name]=raw;cursor+=len(raw)
    require(cursor==len(data) and len(members)==package['original_count'], 'Member closure')
    raw=members[package['fixed_input_filename']]
    require(len(raw)==13084243 and digest(raw)==INPUT_SHA, 'Full ordered input pin')
    return raw
def native_descriptor(context, name):
    refs = context.get("actual_receipts", {})
    if name in refs:
        descriptor = refs[name]
    else:
        descriptor = {"path": context.get("native_" + name + "_receipt_path"),
                      "sha256": context.get("native_" + name + "_receipt_sha256")}
    require(type(descriptor) is dict and type(descriptor.get("path")) is str
            and type(descriptor.get("sha256")) is str, "Missing dynamic " + name + " receipt descriptor")
    return descriptor

def success_receipt(descriptor):
    value = read(descriptor["path"], descriptor["sha256"])
    bridge = value["bridge_receipt"]
    require(bridge["status"] == "SUCCEEDED" and bridge.get("error") is None,
            "Actual native receipt is not successful")
    return bridge["receipt"]

def check_lease(context):
    value = context["owner_lease_until"]
    require(type(value) is str and bool(value), "Actual owner lease required")
    lease = datetime.fromisoformat(value.replace("Z", "+00:00"))
    require(lease.tzinfo is not None and lease > datetime.now(timezone.utc), "Actual owner lease expired")

def check_binding(binding, context):
    require(binding["executor_role"] == "RESEARCHER", "Wrong native executor role")
    for name in ("researcher_id", "session_id", "publication_id", "claim_id", "execution_record_id"):
        require(binding[name] == context[name], "Native binding mismatch: " + name)
    require(binding["researcher_id"] == ACTOR and binding["session_id"] == SID,
            "Existing actual actor/SID required")
    require(binding["allowed_outputs"] == context["allowed_outputs"], "Native allowed outputs mismatch")
    if "owner_lease_until" in binding:
        require(binding["owner_lease_until"] == context["owner_lease_until"], "Native lease mismatch")

def record_field(record, *names):
    values = [record[name] for name in names if name in record]
    require(values and all(value == values[0] for value in values),
            "Missing or inconsistent Source field aliases: " + "/".join(names))
    return values[0]

def verify_source_entry(entry):
    require(type(entry) is dict and type(entry.get("path")) is str
            and type(entry.get("local_path")) is str and type(entry.get("source_commit")) is str,
            "Full actual Source file descriptor required")
    raw = Path(entry["local_path"]).read_bytes()
    require(len(raw) == entry["bytes"] and digest(raw) == entry["sha256"]
            and blob(raw) == entry["git_blob_sha1"].split(":")[-1], "Actual Source byte/pin mismatch")
    return raw

def parsed_raw(raw):
    return json.loads(raw, parse_float=nofloat, parse_constant=nofloat, object_pairs_hook=unique_object)

def taskbook_metadata(book, task_id):
    comments = list(re.finditer(r"<!--\s*ENTERPRISE_MATH_TASK_V1\s*(\{.*?\})\s*-->", book, re.DOTALL))
    if comments:
        require(len(comments) == 1, "Duplicate canonical Taskbook metadata comments")
        header = parsed_raw(comments[0].group(1).encode())
        require(type(header) is dict and header["task_id"] == task_id,
                "Canonical Taskbook metadata Task mismatch")
        if "schema" in header:
            require(header["schema"] == "ENTERPRISE_MATH_TASK_V1", "Canonical Taskbook schema mismatch")
        return header
    # Explicit alternate metadata requires a recognized schema. An arbitrary
    # first illustrative JSON fence never becomes a control record.
    headers = []
    for match in re.finditer(r"```json\s*\n(.*?)\n```", book, re.DOTALL):
        try:
            candidate = parsed_raw(match.group(1).encode())
        except (json.JSONDecodeError, InvariantError):
            continue
        if (type(candidate) is dict and candidate.get("schema") == "ENTERPRISE_MATH_TASK_V1"
                and candidate.get("task_id") == task_id):
            headers.append(candidate)
    require(len(headers) == 1, "Actual Taskbook has no unique recognized metadata block")
    return headers[0]

def authorize(context_path):
    """Validate actual native/Source control bytes before any common/case mathematics."""
    context_raw = Path(context_path).read_bytes()
    context = parsed_raw(context_raw)
    require(context.get("native_authorized") is True, "Q4 LOCAL PREPARATION IS NOT EXECUTION AUTHORITY")
    task_id, publication_id = context["task_id"], context["publication_id"]
    require(type(task_id) is str and task_id.startswith("RS-") and task_id not in FORBIDDEN_TASKS,
            "Genuine new order4 Task required; old q1/q2 authority is not applicable")
    require(type(publication_id) is str and publication_id.startswith("TP2-")
            and publication_id not in FORBIDDEN_PUBLICATIONS, "Genuine new order4 publication required")
    require(context["researcher_id"] == ACTOR and context["session_id"] == SID
            and context["activity_id"] == RA, "Existing actual actor/SID/RA required")
    require(context["native_authorized"] is True, "Prospective/local preparation is not authorization")
    require(context["run_id"] not in FORBIDDEN_RUNS and context["claim_id"] not in FORBIDDEN_CLAIMS,
            "Old q1/q2 run/claim cannot authorize order4 execution")
    require(type(context["run_generation"]) is int and context["run_generation"] > 0
            and context.get("fenced_by_claim_id") is None, "Current unfenced generation required")
    require(context["scope"] == SCOPE and context["include_outside_domain_patterns"] is True
            and context["excluded_replay_pattern_ids"] == [] and context["total_vertical_order"] == 4,
            "Native context must authorize the whole literal order4 packet")
    require(context["global_goal_id"] == GLOBAL_GOAL and context["global_goal_status"] == "OPEN"
            and type(context["global_goal_generation_id"]) is str, "Actual open global Goal required")
    require(context["platform_session_attested"] is False, "Existing nonattested provenance cannot reset")
    prepared_receipt = success_receipt(native_descriptor(context, "prepare"))
    prepared = prepared_receipt["result"]
    claimed = success_receipt(native_descriptor(context, "claim"))["result"]
    opened = success_receipt(native_descriptor(context, "open"))
    for result in (claimed, opened["result"]):
        require(result["authorized"] is True
                and result["authorization_authority"] == "CURRENT_AUTHORIZED_WINNING_ISSUE_240_CLAIM"
                and result["task_id"] == task_id, "Actual current winning claim/open required")
        check_binding(result["execution_binding"], context)
        require(result["task_registration"]["publication_id"] == publication_id,
                "Native registration/publication join mismatch")
    if prepared.get("schema") == "ENTERPRISE_MATH_CONTINUATION_PREPARE_V1":
        require(prepared["execution_authorized"] is False, "Prepare is not execution authorization")
        binding = prepared_receipt["executor_binding"]
        require(binding["researcher_id"] == ACTOR and binding["session_id"] == SID
                and binding["activity_id"] == RA, "Typed prepare actual executor mismatch")
    else:
        intent = prepared["intent"]
        require(intent["claim_id"] == context["claim_id"]
                and intent["execution_record_id"] == context["execution_record_id"], "Prepare claim/ER mismatch")
    run = opened["run"]
    for name in ("run_id", "task_id", "publication_id", "researcher_id", "session_id", "claim_id"):
        require(run[name] == context[name], "Actual run join mismatch: " + name)
    require(run["generation"] == context["run_generation"] and run["fenced_by_claim_id"] is None,
            "Actual run generation/fence mismatch")
    proof_ref = context["source_scope_proof"]
    proof = read(proof_ref["path"], proof_ref["sha256"])
    require(proof["Source_session_RA_ER_publication_book_full_bytes_verified"] is True
            and proof["own_actor"] == ACTOR and proof["own_SID"] == SID and proof["own_RA"] == RA
            and proof["native_claim_authorized"] is True and proof["native_open_authorized"] is True,
            "Actual full Source control proof required")
    check_binding(proof["execution_binding"], context)
    require(proof["source_commit"] == opened["source_sha"], "Source proof must pin the actual open Source")
    require(type(proof["files"]) is list and len(proof["files"]) >= 9, "Complete control/Goal/input packet required")
    entries, source_bytes = {}, {}
    for entry in proof["files"]:
        require(entry["path"] not in entries, "Duplicate actual Source path")
        entries[entry["path"]] = entry
        source_bytes[entry["path"]] = verify_source_entry(entry)
    session_path = "research_session_records/" + SID + ".json"
    activity_path = "research_activity_records/" + RA + ".json"
    er_path = "research_execution_records/" + task_id + "/" + context["execution_record_id"] + ".json"
    pub_path = "research_task_records/" + task_id + "/" + publication_id + ".json"
    for path in (session_path, activity_path, er_path, pub_path):
        require(entries[path]["source_commit"] == proof["source_commit"], "Control file must use current Source")
    session, activity = parsed_raw(source_bytes[session_path]), parsed_raw(source_bytes[activity_path])
    session_identities = []
    if "researcher_id" in session:
        session_identities.append(session["researcher_id"])
    if "execution_id" in session:
        # In the established session-registration schema this is the actor
        # identifier, not an ER-record identifier or a session identifier.
        session_identities.append(session["execution_id"])
    if type(session.get("identity")) is dict and "researcher_id" in session["identity"]:
        session_identities.append(session["identity"]["researcher_id"])
    require(session["session_id"] == SID and session_identities
            and all(value == ACTOR for value in session_identities), "Source session identity mismatch")
    require(activity["activity_id"] == RA and activity["researcher_id"] == ACTOR
            and activity["session_id"] == SID, "Source RA identity mismatch")
    execution, publication = parsed_raw(source_bytes[er_path]), parsed_raw(source_bytes[pub_path])
    require(execution["execution_record_id"] == context["execution_record_id"],
            "Source ER identity mismatch")
    for name in ("task_id", "publication_id", "researcher_id", "claim_id"):
        require(execution[name] == context[name], "Source ER control join mismatch: " + name)
    if "session_id" in execution:
        require(execution["session_id"] == SID, "Source ER SID, when present, must match actual native bindings")
    require(publication["task_id"] == task_id and publication["publication_id"] == publication_id,
            "Source publication identity mismatch")
    goal_generation = context["global_goal_generation_id"]
    generation_bindings = [record["parent_objective_generation_id"]
                           for record in (publication, execution, claimed["execution_binding"],
                                          opened["result"]["execution_binding"])
                           if "parent_objective_generation_id" in record]
    require(generation_bindings and all(value == goal_generation for value in generation_bindings),
            "Actual fresh publication/ER/native bindings must join the current Goal generation")
    book_path = publication["taskbook_path"]
    require(book_path.startswith("research_tasks/") and entries[book_path]["source_commit"] == proof["source_commit"],
            "Actual current Source taskbook required")
    book_blob = entries[book_path]["git_blob_sha1"].split(":")[-1]
    require(book_blob == publication["taskbook_blob_sha1"].split(":")[-1]
            and book_blob == opened["result"]["execution_binding"]["taskbook_blob_sha1"].split(":")[-1],
            "Actual taskbook blob binding mismatch")
    goal_ref, head_ref = context["goal_record_source_path"], context["goal_head_source_path"]
    require(goal_ref.startswith("research_objective_records/") and head_ref.startswith("research_objective_heads/"),
            "Actual Goal record/head Source paths required")
    require(entries[goal_ref]["source_commit"] == proof["source_commit"]
            and entries[head_ref]["source_commit"] == proof["source_commit"], "Goal state must use current Source")
    goal, head = parsed_raw(source_bytes[goal_ref]), parsed_raw(source_bytes[head_ref])
    require(record_field(goal, "objective_id", "goal_id") == GLOBAL_GOAL
            and record_field(goal, "objective_generation_id", "generation_id") == goal_generation
            and record_field(goal, "status", "objective_status") == "OPEN", "Actual Goal record mismatch")
    require(record_field(head, "objective_id", "goal_id") == GLOBAL_GOAL
            and record_field(head, "objective_generation_id", "current_generation_id", "current_objective_generation_id") == goal_generation,
            "Actual current Goal head mismatch")
    require(record_field(head, "objective_status", "status") == "OPEN"
            and head["objective_record_sha256"].split(":")[-1] == entries[goal_ref]["sha256"],
            "Actual open Goal head must bind the exact current Goal record SHA256")
    require(head["generation"] == goal["generation"], "Actual Goal head/record numeric generation mismatch")
    input_ref = context["order4_input_descriptor"]
    require(input_ref["sha256"] == INPUT_SHA and input_ref["bytes"] == 13084243,
            "Future packet must preserve the prepared literal input bytes")
    source_path = input_ref["source_path"]
    require(entries[source_path]["source_commit"] == proof["source_commit"], "Order3 input must belong to admitted Source")
    literal_raw = source_input_bytes(source_bytes, input_ref)
    literal_local = Path(input_ref["path"]).read_bytes()
    require(literal_raw == literal_local and len(literal_raw) == input_ref["bytes"]
            and digest(literal_raw) == INPUT_SHA
            and blob(literal_raw) == input_ref["git_blob_sha1"].split(":")[-1], "Actual logical input byte join mismatch")
    problem_header = parsed_raw(literal_raw)
    common_ref = problem_header["common_input"]
    common_path = common_ref["path"]
    require(common_ref["sha256"] == PORTABLE_SHA and digest(source_bytes[common_path]) == PORTABLE_SHA
            and len(source_bytes[common_path]) == common_ref["bytes"]
            and blob(source_bytes[common_path]) == common_ref["git_blob_sha1"], "Actual pinned common input mismatch")
    require(entries[common_path]["source_commit"] == common_ref["source_commit"], "Pinned common Source commit mismatch")
    book = source_bytes[book_path].decode("utf-8")
    require(source_path in book and INPUT_SHA in book and common_path in book and PORTABLE_SHA in book,
            "Actual taskbook must declare the exact order4 and common Source inputs")
    header = taskbook_metadata(book, task_id)
    require(header["parent_objective_id"] == GLOBAL_GOAL,
            "Actual taskbook metadata must name the original parent objective")
    if "parent_objective_generation_id" in header:
        require(header["parent_objective_generation_id"] == goal_generation,
                "Taskbook generation binding, when present, must match the actual fresh Goal")
    if "member_path" in input_ref:
        require(input_ref["member_path"] in book, "Actual taskbook must identify the logical packaged input member")
    normalized_book = re.sub(r"[^a-z0-9]", "", book.lower())
    require("30992" in normalized_book and "order4" in normalized_book,
            "Actual Taskbook must declare the new full30992 q4 scope")
    review = context["new_code_static_review"]
    review_path = review["source_path"]
    require(review_path in entries and entries[review_path]["sha256"] == review["sha256"],
            "Actual Source-covered nonauthor new code static review required")
    # The immutable review JSON supplies the verdict/actor/math input and code
    # scope. The local descriptor only locates that reviewed evidence and code.
    actual_review = parsed_raw(source_bytes[review_path])
    require(actual_review["schema"] == "T6_Q4_PRE_SCIENCE_STATIC_IMPLEMENTATION_REVIEW_V1"
            and actual_review["review_scope"] == "NEW_Q4_IMPLEMENTATION_STATIC_ONLY"
            and actual_review["scientific_execution"] is False,
            "Exact Source review machine schema and static-only scope required")
    for key in ("reviewer_actor", "verdict", "producer_sha256", "verifier_sha256", "input_sha256"):
        require(actual_review[key] == review[key],
                "Source review and descriptor disagree: " + key)
    require(review["reviewer_actor"] not in SOURCE_AUTHORS and review["verdict"] == "PASS"
            and review["producer_sha256"] == digest(Path(context["producer_path"]).read_bytes())
            and review["verifier_sha256"] == digest(Path(context["verifier_path"]).read_bytes())
            and review["input_sha256"] == INPUT_SHA,
            "Nonauthor static review must cover these exact code/input bytes")
    implementation = review["implementation_pins"]
    require(type(implementation) is list and len(implementation) >= 5
            and len({row["path"] for row in implementation}) == len(implementation),
            "Review must cover every imported producer dependency plus separate verifier")
    def content_pin_map(rows):
        require(type(rows) is list and len(rows) >= 6, "All six actual review implementation pins")
        result = {}
        for row in rows:
            name = row.get("filename", Path(row.get("path", "")).name)
            require(type(name) is str and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", name)
                    and name not in result and type(row["bytes"]) is int and row["bytes"] > 0,
                    "Unique exact implementation filename/length")
            result[name] = (row["bytes"], row["sha256"], row["git_blob_sha1"])
        return result
    # Physical runtime locations may be rebound, but every basename and full
    # byte fingerprint must match the immutable reviewed code scope exactly.
    require(content_pin_map(actual_review["implementation_pins"]) == content_pin_map(implementation),
            "Actual Source review and runtime implementation byte scope must agree")
    required_names = {"order4_exact_batch_executor.py", "order4_exact_math_and_input.py",
                      "q4_native_admission_guard.py", "q4_dfs_wire.py"}
    require(required_names <= {Path(row["path"]).name for row in implementation},
            "All four producer implementation files must be frozen and reviewed")
    for row in implementation:
        raw = Path(row["path"]).read_bytes()
        require(digest(raw) == row["sha256"] and len(raw) == row["bytes"]
                and blob(raw) == row["git_blob_sha1"],
                "Frozen static-reviewed implementation byte pin changed")
    require(any(Path(row["path"]).resolve() == Path(context["verifier_path"]).resolve()
                for row in implementation), "Separate verifier must join implementation pin closure")
    require(context["q3_native_Task_closed"] is True and context["q3_acceptance_source_reference"],
            "Actual q3 closure antecedent required")
    check_lease(context)
    evidence = {"context_sha256": digest(context_raw), "Source_scope_proof": proof_ref,
                "actual_receipts": {name: native_descriptor(context, name) for name in ("prepare", "claim", "open")},
                "Source_order4_input_path": source_path, "order4_input_encoding": input_ref["encoding"],
                "logical_order4_input_sha256": INPUT_SHA, "native_authority_granted_by_local_code": False}
    inputs = {"order4_input_path": input_ref["path"], "portable_path": entries[common_path]["local_path"]}
    return context, evidence, inputs

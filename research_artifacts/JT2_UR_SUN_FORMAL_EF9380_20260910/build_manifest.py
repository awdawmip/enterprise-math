"""Package this UR return and verify exact input/output byte bindings."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
TASK = "RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT"
RETURN = "research_returns/EMW59A_JT2_UR_SUN_PARITY_DEFECT_RETURN_EF9380_20260910.md"
ER = f"research_execution_records/{TASK}/ER-D9A31C2F856C87718DC2.json"


def digest(raw):
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
            "blob": hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}


def source(path, ref, role):
    return {"path": path, "ref": ref, "repository": "awdawmip/enterprise-math",
            "role": role, **digest((ROOT/path).read_bytes())}


def write(name, value):
    (BASE/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")


observed = json.loads((BASE/"inputs/full-readbacks.json").read_text(encoding="utf-8"))
sources = []
expected = {
    "UR-CM-TWO-PORT-CANDIDATE": "7ce059dbe841e5cd78b78c07773be143f1926487bbf91ae3807b20ddf4986415",
    "UR-CM-TWO-PORT-PRIOR-CHECK": "ca74aea22690b599dd232a7608fa76381d23287e691aadacbff2af11c3bd9f2d",
    "UR-ORIGINAL-DIVIDED-NORMALIZATION": "54ab94a1899f649ae1488bececaa7c57aafbc89aef44bdd1e40cc0b45590e827",
}
for row in observed["observations"]:
    data = row["response"]["structuredContent"]
    evidence = digest(data["content"].encode("utf-8"))
    assert evidence["blob"] == data["sha"], row["id"]
    if row["id"] in expected:
        assert evidence["sha256"] == expected[row["id"]], row["id"]
    sources.append({"id":row["id"],"repository":row["repo"],"ref":row["ref"],
                    "path":row["path"],"url":data["display_url"], **evidence,
                    "read_scope":"Actual immutable full-file readback; consume prior input/proof/review with source exposure disclosed."})

local = [
    ("research_tasks/EMW59A_JT2_UR_SUN_PARITY_DEFECT_GEN2_20260909.md","TASKBOOK"),
    (f"research_task_records/{TASK}/TP2-22F5729C777040ECA121.json","PUBLICATION"),
    ("research_notes/EM_FREE_W59A_JT2_UR_QTF3_STATE_MACHINE_HANDOFF_20260909.md","FROZEN_MATHEMATICAL_HANDOFF"),
    ("tool_invocation_policy.json","TOOL_POLICY"),
    ("definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json","TYPED_BRC_BOUNDARY"),
    ("src/enterprise_math/precision.py","EXISTING_EXECUTED_FINITE_PRECISION_API"),
]
sources += [source(path,"52775e4f53b4a34210341f7ac07f7c6c2d3834df",role) for path,role in local]
assert sources[4]["blob"] == "7d77a7c1ff08f75b74b38c586e37a9deb8c7518f"
assert sources[5]["blob"] == "59098283328cb863aa1f0ee3112bf19f33d52ab3"
assert sources[6]["blob"] == "48cfda2d4f49c88ff2efd0ca013d9806c2e8d216"
return_bytes = (ROOT/RETURN).read_bytes()
assert return_bytes.decode("utf-8").rstrip().endswith(f"Researcher-ID: EM-JT2-EF9380 / {TASK}")
assert b"UNIFORM UR VANISHING OPEN" in return_bytes
check = json.loads((BASE/"mathematics/elimination_check.json").read_text(encoding="utf-8"))
assert [row["p"] for row in check["rows"]] == [13,19]
assert check["uniform_proof"] is False and check["old_77_prime_replay"] is False
assert all(row["norm_jet_target_equivalence_mod_p2_at_CM"] for row in check["rows"])
execution = json.loads((ROOT/ER).read_text(encoding="utf-8"))
assert execution["task_id"] == TASK and execution["claim_id"] == "ur-sun-ef9380-20260910-201847"
manifest = {
 "schema":"JT2_UR_FORMAL_SOURCE_MANIFEST_V1","task_id":TASK,
 "publication_id":"TP2-22F5729C777040ECA121","execution_record_id":"ER-D9A31C2F856C87718DC2",
 "claim_id":"ur-sun-ef9380-20260910-201847","researcher_id":"EM-JT2-EF9380",
 "session_id":"local:codex-agent:jt2-bounded-reference-review:20260909:EF9380",
 "branch":"research/ur-sun-ef9380-20260910-201847",
 "actual_branch_base":"52775e4f53b4a34210341f7ac07f7c6c2d3834df",
 "startup_source":"5ea38607c755a47a914037d8eb93f475a91de7db",
 "execution_record":{"path":ER,**digest((ROOT/ER).read_bytes())},
 "return":{"path":RETURN,**digest(return_bytes)},"sources":sources,
 "primary_source":{"url":"https://arxiv.org/html/1101.5386v5","version":"v5 (2012-02-01)",
                    "read":"Definition1.1, Lemma2.1, Theorem2.1, Corollary2.1, Theorem2.2"},
 "new_result":"Exact Sun parity/derivative elimination and uniform equivalence to one degree<=2n+1 ordinary-Legendre norm/jet congruence.",
 "unresolved":"All-prime vanishing of 9P_n(t)P_n'(t)-p(2 integral_0^t P_n(v)^2 dv+3t) modulo p².",
 "uniform_UR_proof":False,"formal_logical_independence_proof":False,
 "source_exposure_status":"NONBLIND_DISCLOSED","independence_status":"NOT_INDEPENDENT",
 "new_math_author":"EM-JT2-EF9380 in this authorized UR execution",
 "prior_input_authors_preserved":True,"new_method_family":False,"method_harvest_proposal":"RESULT_ONLY",
 "frozen_complete_system_retained":["fixed Legendre coefficients","degree bounds","endpoint normalization","barycentric lift","CM0/SIMPLE","both Frobenius ports","p² parity defects","x^p derivative-kernel term"],
 "finite_checks":"Two exact new transcription checks p=13,19; not all-prime proof; no old 77-prime replay.",
 "current_source_scope":"delivery/pre-freeze-source-scope.json; complete5277 local source, scoped unchanged authority/code against later data-only main; no complete current main overlay claim."
}
write("source_manifest.json",manifest)
paths = [RETURN,ER] + [p.relative_to(ROOT).as_posix() for p in BASE.rglob("*") if p.is_file()
    and p.suffix in {".md",".json",".py",".txt"}
    and "__pycache__" not in p.parts
    and p.name not in {"postclaim-full-raw-comments.json","metadata_validation.json"}]
paths=sorted(set(paths))
validation={"schema":"JT2_UR_PACKET_BYTE_VALIDATION_V1","input_blob_and_sha_checks":"PASS",
            "task_execution_binding":"PASS","source_exposure_disclosed":True,
            "uniform_vanishing_claimed":False,"prior_activity_events_untouched":True,
            "manifest":digest((BASE/"source_manifest.json").read_bytes()),
            "return":manifest["return"],"packet_paths":paths}
write("metadata_validation.json",validation)
new_paths=[RETURN]+[p.relative_to(ROOT).as_posix() for p in BASE.rglob("*") if p.is_file()
    and "authorization" not in p.parts and "__pycache__" not in p.parts
    and p.suffix in {".md",".json",".py",".txt"}]
(ROOT/".."/"TEMP"/"jt2-ur-execution-ef9380-20260910"/"return-publish-paths.json").write_text(json.dumps(sorted(set(new_paths)),indent=2)+"\n",encoding="utf-8")
print(json.dumps({"return":manifest["return"],"source_count":len(sources),"new_publish_file_count":len(set(new_paths)),"validation":"PASS"},indent=2))

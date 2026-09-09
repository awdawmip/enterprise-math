"""Grant a finite catalogue attestation only after actual audit and witness success."""
import hashlib,json
from pathlib import Path
A=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
audit=json.loads((A/"construction_audit.json").read_text(encoding="utf-8"))
witness=json.loads((A/"independent_witness_verification.json").read_text(encoding="utf-8"))
assert audit["status"]=="PASS" and audit["block_count"]==4000 and audit["all_four_independent_counts_match"]
assert audit["prime_count"]==114956492689 and audit["global_max_observed_gap"]["gap"]<=916
assert witness["all_verified"] and witness["catalogue_row_count"]==len(audit["task_gap_rows"])==witness["verified_catalogue_row_count"]
available={(c["start"],c["gap"]) for c in witness["certificates"]}
assert all((r["start"],r["gap"]) in available for r in audit["task_gap_rows"])
for c in witness["certificates"]:
    path=A/c["path"]
    assert sha(path)==c["sha256"]
    proof=json.loads(path.read_text(encoding="utf-8"))
    assert proof["all_verified"] and all(x["prime"] for x in proof["endpoint_primality_certificates"])
    assert all(x["factor"]*x["cofactor"]==x["n"] and 1<x["factor"]<x["n"] for x in proof["odd_interior_factor_witnesses"])
catalogue=json.loads((A/"catalogue.unattested.json").read_text(encoding="utf-8"))
assert catalogue["completeness_attestation"] is False
assert (catalogue["coverage_start"],catalogue["coverage_end"],catalogue["complete_for_gap_ge"])==(1291005053866735,1294364244470160,916)
catalogue["completeness_attestation"]=True
catalogue["attestation_basis"]={
    "kind":"COMPLETE_FINITE_SEGMENTED_ERATOSTHENES_CONSTRUCTION_WITH_ALL_PAIR_STITCHING",
    "covered_integer_interval_half_open":audit["scan_half_open"],
    "recorded_prime_count":audit["prime_count"],
    "audited_consecutive_pair_count":audit["all_pair_count"],
    "independent_count_checks":4,
    "construction_audit_sha256":sha(A/"construction_audit.json"),
    "independent_witness_verification_sha256":sha(A/"independent_witness_verification.json"),
    "run_manifest_sha256":sha(A/"construction_full/run_manifest.json"),
    "source_code_sha256":audit["source_code_sha256"],
    "scope":"Exact frozen task gap-start band; no result for another q and no Driver acceptance implied.",
    "execution_assumptions":"Recorded execution of pinned numerical libraries and task adapter; this is a finite computational certificate, not a formal compiler/hardware verification."
}
target=A/"catalogue.json"
if target.exists():raise FileExistsError(str(target))
target.write_text(json.dumps(catalogue,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"attestation":True,"row_count":len(catalogue["rows"]),"rows_sha256":catalogue["rows_sha256"],"max_gap_bound":catalogue["max_gap_bound"],"catalogue":str(target)}),flush=True)


#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
def load(n): return json.loads((ROOT/n).read_text(encoding="utf-8"))
def sha(n): return hashlib.sha256((ROOT/n).read_bytes()).hexdigest()
checks=[]
def ck(name,cond,detail=None):
    checks.append({"name":name,"pass":bool(cond),**({"detail":detail} if detail is not None else {})})

inp=load("R057X_STAGE_FR2_EXACT_INPUT_REGISTRY.json")
ver=load("R057X_STAGE_FR2_FINAL_VERDICT.json")
ck("INPUT_GATE_FAIL",inp["gate_result"]=="FAIL")
ck("HARD_STOP_EXACT_INPUT",inp["hard_stop"]=="FR2_HARD_STOP_EXACT_INPUT_UNAVAILABLE")
ck("ZERO_TARGET_FILES_MOUNTED",inp["runtime_probe"]["target_file_count_found"]==0)
ck("FOUR_EXPECTED_INPUTS",len(inp["inputs"])==4)
ck("ALL_INPUTS_RUNTIME_UNAVAILABLE",all("UNAVAILABLE" in v["runtime_byte_gate"] for v in inp["inputs"].values()))
ck("NO_SUBSTITUTION",all(v.get("metadata_or_transport_not_substituted",v.get("metadata_or_parsed_json_not_substituted")) is True for v in inp["inputs"].values()))
ck("SCIENCE_NOT_EXECUTED",inp["science_replay_executed"] is False and ver["science_replay_executed"] is False)
ck("FINAL_VERDICT_HARD_STOP",ver["reconciliation_verdict"]=="FR2_HARD_STOP_EXACT_INPUT_UNAVAILABLE")
ck("V1_IMMUTABLE",ver["V1_byte_identity"]["immutable"] is True)
ck("V1_HASH",ver["V1_byte_identity"]["checkpoint_sha256"]=="4cf6a1fd4d748e1175e77503247f41706aacb4946802a3da7bd03a52a4fdad54")
ck("V1_DISPOSITION",ver["V1_byte_identity"]["disposition"]=="INSUFFICIENT")
ck("V2_NOT_CREATED",ver["V2"]["created"] is False)
ck("NO_RULE_CHANGE_ASSERTION",ver["rule_change_detected"] is False)
ck("D4_BLOCKED",ver["D4_authorized"] is False)
ck("FR_ANCHOR",inp["frozen_anchors"]["R057X_STAGE_FR_FREEZE_IDENTITY_CHECKPOINT_SHA256"]=="dde3a3edd0a2af71885c6e686747e81cd96d15f692b51494f7416fd6625192c6")
ck("STAGE_E_ANCHOR",inp["frozen_anchors"]["R057X_STAGE_E_COMMON_COMPONENT_CHECKPOINT_SHA256"]=="3937572b2f8099f9ce125a86ccf90ec9aad6f9470b0af9ec4b8026df67796385")
ck("A_SAMPLE_IDENTITY",inp["inputs"]["A_sample"]["expected_bytes"]==2089833 and inp["inputs"]["A_sample"]["expected_sha256"]=="4baad1a7c3528d9b147a3ee38fb5436a3e607a2141178a284f540bfc1ce5eaf3")
ck("A_NUISANCE_IDENTITY",inp["inputs"]["A_nuisance"]["expected_bytes"]==50118 and inp["inputs"]["A_nuisance"]["expected_sha256"]=="ac58760ca6f460961e41287452127060e3e3d2dfd9cf069a65fc6029f1b06e6f")
ck("G_SAMPLE_IDENTITY",inp["inputs"]["G_sample"]["expected_bytes"]==1467133 and inp["inputs"]["G_sample"]["expected_sha256"]=="f50c9cdab6143e6d1e5339bfb3079e30b56e70991bca40ce9225cfdcc2415c22")
ck("G_NUISANCE_IDENTITY",inp["inputs"]["G_nuisance"]["expected_bytes"]==44983 and inp["inputs"]["G_nuisance"]["expected_sha256"]=="14b198f6d1b87cc40454453e99046a946b7f841a6b76469fbbf2f84009b1e723")
res={"schema":"R057X_STAGE_FR2_EXACT_CHECK_RESULTS_V1","researcher_id":"EM-R057X-5E8C41","status":"PASS" if all(c["pass"] for c in checks) else "FAIL","total":len(checks),"passed":sum(c["pass"] for c in checks),"failed":[c for c in checks if not c["pass"]],"checks":checks,"science_code_executed":False,"ci":"CI_NOT_REQUIRED_FOR_RESEARCH"}
b=(json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2,separators=(",",": "))+"\n").encode("utf-8")
(ROOT/"R057X_STAGE_FR2_EXACT_CHECK_RESULTS.json").write_bytes(b)
print(json.dumps({"status":res["status"],"checks":res["total"],"sha256":hashlib.sha256(b).hexdigest()},sort_keys=True))

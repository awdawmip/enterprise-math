#!/usr/bin/env python3
import json,hashlib
from pathlib import Path
OUT=Path(__file__).resolve().parent
EXPECTED={
"R057X_STAGE_F_V1_FREEZE_REGISTRY.json":"33540d769964f7e20871d98ea190a041f2e5f4297c66741713ad6d44256e9278",
"R057X_STAGE_FR_WORKSPACE_IDENTITY_AUDIT.json":"015c16234ef23034fd5776140c4ecd34e1fab783c043fef5fa8e3f4bdec8d5a6",
"R057X_STAGE_FR_V1_V2_DIFF_LEDGER.json":"08326cc3fef24983c420bcded2af02868cad38fba139e6c10effbb1bb11ce72f",
"R057X_STAGE_FR_RULE_REPRODUCTION_AUDIT.json":"7578818365ad9427494a9cfad0ec6604161bade486aa764059e71fee8deec92d",
"R057X_STAGE_FR_DECISION_DIVERGENCE_LEDGER.json":"e97eb97c1a7867227026cd6dee1fa30ef1383004426790b042b1ee68b670bffa",
"R057X_STAGE_FR_FREEZE_IDENTITY_VERDICT.json":"ff36221d71283ef5af32a9d2f7fd892bdd4b76619ee207235ef759af06da729c",
"R057X_STAGE_FR_FREEZE_IDENTITY_CHECKPOINT.json":"dde3a3edd0a2af71885c6e686747e81cd96d15f692b51494f7416fd6625192c6",
"R057X_STAGE_FR_REPORT.md":"6f1477178b69f91248a47933710eded2d25b591e2cb9abcd1cffb6a9fa90d572",
}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(n): return json.loads((OUT/n).read_text(encoding="utf-8"))
checks=[]
def ck(name,cond,detail=None): checks.append({"name":name,"pass":bool(cond),"detail":detail})
for n,h in EXPECTED.items(): ck("HASH_"+n,sha(OUT/n)==h,sha(OUT/n))
r=load("R057X_STAGE_F_V1_FREEZE_REGISTRY.json")
i=load("R057X_STAGE_FR_WORKSPACE_IDENTITY_AUDIT.json")
d=load("R057X_STAGE_FR_V1_V2_DIFF_LEDGER.json")
a=load("R057X_STAGE_FR_RULE_REPRODUCTION_AUDIT.json")
g=load("R057X_STAGE_FR_DECISION_DIVERGENCE_LEDGER.json")
v=load("R057X_STAGE_FR_FREEZE_IDENTITY_VERDICT.json")
c=load("R057X_STAGE_FR_FREEZE_IDENTITY_CHECKPOINT.json")
ck("RESEARCHER",r["researcher_id"]=="EM-R057X-5E8C41")
ck("BASE",c["required_branch_base"]=="872e23d76fe9c29b8a5fd922a3c05b98ef39062c")
ck("TASKBOOK",c["taskbook_source"]=="918867b6dae5099d33d2ea6aed07994b00b0051f")
ck("V1_CHECKPOINT",r["V1"]["checkpoint_sha256"]=="4cf6a1fd4d748e1175e77503247f41706aacb4946802a3da7bd03a52a4fdad54")
ck("V1_DISPOSITION",r["V1"]["disposition"]=="INSUFFICIENT")
ck("V1_VERDICT",r["V1"]["verdict_sha256"]=="14285c351e076996d040e41d31b044bb5b66af195398adc4caeb34af8bf30e8f")
ck("V1_EXACT",r["V1"]["exact_check_sha256"]=="8889a44f2801fab2015bbadf8a376514e986b500a4b51f8ee37c3193b75a5edf")
ck("V1_MANIFEST",r["V1"]["manifest_sha256"]=="9cb0fb2c75533ad5b0afe4641122d67215573cf1315582a389f76a213ec370bc")
ck("ONE_IDENTITY",i["classification"]=="ONE_STAGE_F_BYTE_IDENTITY_FOUND")
ck("THREE_SURFACES_EQUAL",i["exact_comparison"]["all_three_surfaces_single_identity"] is True)
ck("NO_V2",d["V2_byte_identity_status"]=="NOT_FOUND")
ck("NO_RULE_CHANGE",d["post_freeze_rule_change_detected"] is False)
ck("REPLAY_NOT_EXECUTED",a["clean_replay"]["executed"] is False)
ck("A_SAMPLE_NOT_RECOVERED",a["frozen_input_byte_availability"]["A_sample_surface"]["current_exact_bytes_recovered"] is False)
ck("A_NUIS_NOT_RECOVERED",a["frozen_input_byte_availability"]["A_nuisance_surface"]["current_exact_bytes_recovered"] is False)
ck("CONFLICT_NO_MOTIFS",len(g["conflicting_later_narrative"]["concrete_motif_ids_frozen"])==0)
ck("PRIMARY_VERDICT",v["primary_verdict"]=="FREEZE_IDENTITY_UNRESOLVED"==c["primary_verdict"])
ck("NO_V2_CHECKPOINT",c["R057X_STAGE_F_V2_MATCHED_RESIDUAL_HOTSPOT_CHECKPOINT_SHA256"].startswith("NOT_CREATED"))
ck("D4_BLOCKED",v["D4_status"]=="BLOCKED")
p=a["prohibitions_preserved"]
ck("NO_PROHIBITED_ACTION",not any(p.values()),p)
ck("NO_NEW_SCIENCE",g["no_new_science"] is True)
ck("STOP",c["stop_rule"].startswith("STOP_AFTER_STAGE_FR"))
res={"schema":"R057X_STAGE_FR_EXACT_CHECK_RESULTS_V1","researcher_id":"EM-R057X-5E8C41","stage":"FR","status":"PASS" if all(x["pass"] for x in checks) else "FAIL","total":len(checks),"passed":sum(x["pass"] for x in checks),"failed":[x for x in checks if not x["pass"]],"checks":checks,"ci":"CI_NOT_REQUIRED_FOR_RESEARCH"}
b=(json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2,separators=(",",": "))+"\n").encode()
(OUT/"R057X_STAGE_FR_EXACT_CHECK_RESULTS.json").write_bytes(b)
print(json.dumps({"status":res["status"],"checks":len(checks),"sha256":hashlib.sha256(b).hexdigest()},sort_keys=True))
raise SystemExit(0 if res["status"]=="PASS" else 1)

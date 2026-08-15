#!/usr/bin/env python3
import hashlib, json, sys
from pathlib import Path

EXPECTED={
"R056_LOCALITY_MODEL.json":"1f610591b3f32b1540da1fa55733faeb1ec1a1fff054902affb087626cda729a",
"R056_SHELL_ESCAPE_PROTOCOL.json":"746d154f39f108c75c779cbeceb5ae6b35c4bb692c62486a2209766b316bb45a",
"R056_COMPUTATION_REGISTRY.json":"d87e107b814090d4ec528a7a593d0119b26666fa82070a6e5c967f6dd6be09ea",
"R056_MULTI_REPLACEMENT_IDENTITY.json":"a07325d019f9ebced6108d69f831aa72570fa3d2a3e43cd2726c1cb11f6cf8f6",
"R056_THEOREM_COUNTEREXAMPLE_LEDGER.json":"3f4506c6b177cf021929075c2835621eeda742051e80f471adda2482a8fcc27c",
}
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main(root):
    root=Path(root); checks=[]
    for f,h in EXPECTED.items():
        assert sha(root/f)==h,(f,sha(root/f),h)
    checks.append("FROZEN_ANCHORS_IMMUTABLE")
    atlas=json.loads((root/"R056_SHELL_ESCAPE_ATLAS.json").read_text())
    rows={x["r"]:x for x in atlas["construction_results"]}
    assert [rows[r]["m1"]["rho_1"] for r in [2,3,4,5,6]]==["infinity","infinity","infinity","infinity",13]
    checks.append("SMALL_M1_EXACT_RESULTS")
    for r in [8,10,12,16]:
        row=rows[r]
        if "m1" in row:
            assert row["m1"]["rho_1"]==row["m2"]["rho_2"]==row["m3"]["rho_3"]==3
        else:
            assert row["rho_1"]==row["rho_2"]==row["rho_3"]==3
            assert row["witness_check"]["support_diameter"]==3
            assert row["witness_check"]["connected"] and row["witness_check"]["hole_free"]
            assert row["witness_check"]["DeltaG_full_recompute"]<0
    checks.append("CONSTRUCTION_THEOREM_ROWS")
    h=json.loads((root/"R056_HOLDOUT_RESULTS.json").read_text())
    assert h["holdout_radii"]==[7,9,11,13,17,24]
    for x in h["results"]:
        assert x["support_diameter"]==3 and x["connected"] and x["hole_free"]
        assert x["DeltaG_full_recompute"]==x["DeltaG_incremental"]<0
        assert x["rho_1"]==x["rho_2"]==x["rho_3"]==3
        assert x["rho_le_2_single_pair_exact_min_DeltaQsum"]==3
    checks.append("STRICT_HOLDOUT_ALL_PASS")
    a=json.loads((root/"R056_ADVERSARIAL_TEST_RESULTS.json").read_text())
    assert a["failed_tests"]==0 and all(x["status"]=="PASS" for x in a["tests"])
    checks.append("ADVERSARIAL_ALL_PASS")
    l=json.loads((root/"R056_THEOREM_COUNTEREXAMPLE_LEDGER.json").read_text())
    assert l["primary_classification"]=="FINITE_LOCAL_COOPERATIVE_ESCAPE_FOUND"
    checks.append("FROZEN_LEDGER_CLASSIFICATION")
    pre=json.loads((root/"R056_SHELL_ESCAPE_ATLAS.preholdout.json").read_text())
    assert pre["status"]=="FROZEN_BEFORE_STRICT_HOLDOUT" and pre["holdout_opened"] is False
    assert pre["m1_preholdout_program"]["locked_holdout_radii"]==[7,9,11,13,17,24]
    checks.append("PREHOLDOUT_DISCIPLINE")
    print(json.dumps({"status":"PASS","count":len(checks),"checks":checks},sort_keys=True))
if __name__=="__main__": main(sys.argv[1])

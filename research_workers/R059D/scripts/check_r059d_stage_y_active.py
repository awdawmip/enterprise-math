#!/usr/bin/env python3
import json
from pathlib import Path
R059D=Path(__file__).resolve().parents[1]
REPO=R059D.parents[1]
def load(name): return json.loads((R059D/"objects"/name).read_text())
def floor_root(n,m):
    k=0
    while (k+1)**m<=n: k+=1
    return k
def ceil_root(n,m):
    k=floor_root(n,m)
    return k if k**m==n else k+1
def staircase(a): return a[0]==0 and a[1]==1 and all(a[i]-a[i-1] in (0,1) for i in range(1,len(a)))
r=load("R059D_STAGE_Y_COUNT_CARRIER_REGISTRY.json")
p=load("R059D_STAGE_Y_TRANSVERSE_PAIR_BLOCK_COUNT.json")
c=load("R059D_STAGE_Y_CONSTRUCTIVE_COUPLING_LEDGER.json")
t=load("R059D_STAGE_Y_PERFECT_POWER_THRESHOLD_AUDIT.json")
g=load("R059D_STAGE_Y_GAP_BRANCH_ALLOCATION_LEDGER.json")
f=load("R059D_STAGE_Y_FIVE_TO_FOUR_OR_NINE_CONTROL.json")
y=load("R059D_STAGE_Y_CYCLIC_COUNT_RECIPROCITY.json")
ri=load("R059D_STAGE_Y_ROOT_DEGREE_INTERPRETATION.json")
tl=load("R059D_STAGE_Y_TRIVIALITY_LEAKAGE_LEDGER.json")
m=load("R059D_STAGE_Y_ACTIVE_MANIFEST_20260816.json")
assert r["phase"]=="PRE_SCORE_REGISTRY_FREEZE" and r["registry_closed"]
assert [x["id"] for x in r["carriers"]]==["TRANSVERSE_ORDERED_PAIR_BLOCK","TRANSVERSE_TRIANGULAR_PAIR_CARRIER","A2_SHELL_CONTROL","A2_BALL_CONTROL","A2_SECTOR_CONTROL","M_FOLD_CARTESIAN_LEVEL_CARRIER"]
for row in p["finite_controls"]:
    k=row["k"]
    assert row["B2"]==k*k and row["dB2"]==2*k+1
    assert row["T2"]==k*(k+1)//2 and row["dT2"]==k+1
    assert row["A2_shell"]==(1 if k==0 else 6*k)
    assert row["A2_ball"]==1+3*k*(k+1)
    assert row["A2_sector"]==(k+1)*(k+2)//2 and row["dA2_sector"]==k+2
    assert all(row["Bm"][str(q)]==k**q for q in range(1,5))
for row in c["stage_x_fiber_theorem"]["fixed_n_controls"]: assert row["possible_a_n"]==list(range(1,row["n"]+1))
assert all(staircase(a) for a in c["decisive_witnesses"].values()) and c["accepted_couplings"]==[]
for block in t["admissibility_controls"]:
    q=block["m"]
    assert block["completed_floor_root"]==[floor_root(n,q) for n in range(1,17)]
    assert block["activated_ceil_root"]==[ceil_root(n,q) for n in range(1,17)]
    assert all(b-a in (0,1) for a,b in zip([0]+block["completed_floor_root"][:-1],block["completed_floor_root"]))
    assert all(b-a in (0,1) for a,b in zip([0]+block["activated_ceil_root"][:-1],block["activated_ceil_root"]))
assert t["selected_m"] is None and not t["square_count_coupling_established"]
for row in g["finite_controls"]:
    L=row["k"]**row["m"]; U=(row["k"]+1)**row["m"]
    assert row["L"]==L and row["U"]==U and row["gap"]==U-L and (U-L)%2==1
    assert row["lower_max"]==(L+U-1)//2 and row["upper_min"]==(L+U+1)//2
assert g["independently_selected_semantics"] is None
assert not f["entry_gate"]["satisfied"] and f["active_stage_y5_result"]=="NOT_ENTERED"
assert staircase(f["stage_x_direct_witnesses"]["a_5_equals_2_prefix"]) and staircase(f["stage_x_direct_witnesses"]["a_5_equals_3_prefix"])
assert not y["axis_name_privilege"] and not y["accepted_positive_count_coupling_to_test"]
assert ri["selected_m"] is None and ri["candidate_interpretation"]["not_euclidean_dimension"]
assert not tl["accepted_as_independent_count_meaning"] and all(e["status"]=="REJECTED" for e in tl["entries"])
for rel in m["required_core_artifacts"]: assert (REPO/rel).exists(), rel
assert all(m["hard_firewalls"].values()) and m["gate"]=="STOP_FOR_DRIVER_REVIEW"
for premise in m["native_premises"]:
    s=premise.replace(" ","").lower()
    assert "n=a_n^2" not in s and "n=a_n^p" not in s and "area" not in s and "volume" not in s
report=(R059D/"notes/R059D_STAGE_Y_ACTIVE_RESEARCH_REPORT_20260816.md").read_text()
for sentinel in ("NATIVE_PREMISE: n=a_n^2","NATIVE_PREMISE: n=a_n^p","NATIVE_AREA_PROOF:","NATIVE_VOLUME_PROOF:","AXIS_PRIVILEGE: true"): assert sentinel not in report
print("OK: R059D active Stage Y exact count audit is self-consistent; staircase-fiber underdetermination, carrier counts, coupling failure, conditional gap reflection, cyclic reciprocity, triviality and hard firewalls all pass.")

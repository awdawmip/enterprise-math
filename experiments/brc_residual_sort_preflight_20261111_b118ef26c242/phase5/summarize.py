"""Summarize 5 within-bank repeats before weighting the 8 banks equally."""
import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import geometric_mean, mean, median
import json

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("result_dir", type=Path)
args = p.parse_args()
root = args.result_dir
new = ["gate", "gate_range", "child_range"]
base = "certified_combined_1024"
inputs = {}
times = defaultdict(list)

def put(name, records):
    with (root / name).open("w", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=list(records[0]))
        w.writeheader()
        w.writerows(records)

with (root / "timings.csv").open() as f:
    for row in csv.DictReader(f):
        k = (row["family"], int(row["bank"]), row["algorithm"])
        tag = (row["stage"], int(row["n"]))
        if row["family"] in inputs:
            assert inputs[row["family"]] == tag
        inputs[row["family"]] = tag
        times[k].append((int(row["round"]), int(row["ns"])))
bank_medians = {}
for key,values in times.items():
    values.sort()
    assert [i for i,_ in values] == list(range(5)), (key,values)
    bank_medians[key] = median(t for _,t in values)/1000
stats = []
pairs = []
table = []
for family,(stage,n) in inputs.items():
    banks=sorted({b for fm,b,_ in times if fm==family})
    methods=sorted({a for fm,_,a in times if fm==family})
    assert len(banks)==8 and len(methods)==30 and base in methods
    per_method={}
    for m in methods:
        vals = [bank_medians[family,b,m] for b in banks]
        per_method[m]=median(vals)
        stats.append(dict(stage=stage,family=family,n=n,method=m,bank_median_us=median(vals),
                          min_bank_us=min(vals),max_bank_us=max(vals)))
    best=min((m for m in methods if m not in new), key=per_method.get)
    for m in new:
        paired_old = [bank_medians[family,b,base]/bank_medians[family,b,m] for b in banks]
        paired_best = [bank_medians[family,b,best]/bank_medians[family,b,m] for b in banks]
        for b,p_old,p_best in zip(banks,paired_old,paired_best):
            pairs.append(dict(stage=stage,family=family,n=n,bank=b,method=m,us=bank_medians[family,b,m],
                previous_us=bank_medians[family,b,base],fastest_control=best,control_us=bank_medians[family,b,best],
                previous_ratio=p_old,control_ratio=p_best))
        table.append(dict(stage=stage,family=family,n=n,method=m,median_us=per_method[m],
            previous_us=per_method[base],previous_ratio=per_method[base]/per_method[m],
            fastest_control=best,control_us=per_method[best],control_ratio=per_method[best]/per_method[m],
            paired_previous_median=median(paired_old),paired_previous_wins=sum(t>1 for t in paired_old),
            paired_control_median=median(paired_best),paired_control_wins=sum(t>1 for t in paired_best)))
put("all_methods.csv", stats)
put("bank_pairs.csv", pairs)
put("comparisons.csv",table)
totals = []
for stage in ("known","fresh","mechanism"):
    for method in new:
        rs=[r for r in table if (r["stage"],r["method"])==(stage,method)]
        for key in ("previous_ratio","control_ratio"):
            ratios=[r[key] for r in rs]
            totals.append(dict(stage=stage,method=method,reference=key,conditions=len(rs),
                geometric_ratio=geometric_mean(ratios),wins=sum(x>1 for x in ratios),
                gain_ge_10pct=sum(x>=1.10 for x in ratios),runtime_over_ge_10pct=sum(x<=1/1.1 for x in ratios)))
put("stage_summary.csv",totals)

with (root/"nodes.csv").open() as f:
    nodes=list(csv.DictReader(f))
pool=defaultdict(list)
for r in nodes:
    for key in ("depth","n","probes","misses","early","actual_misses","scan_visits","range_slots",
                "counter_slots","model_selected","range_sorted","threshold","range_visits","bank"):
        r[key]=int(r[key])
    pool[r["stage"],r["family"],r["algorithm"],r["depth"]].append(r)
node_stats=[]
confusion=[]
for (stage,family,method,depth),group in pool.items():
    # Conditional per represented node; their count is reported explicitly.
    elig=[r for r in group if r["probes"]==64]
    pos=[r for r in elig if r["actual_misses"]>r["n"]//2]
    neg=[r for r in elig if r["actual_misses"]<=r["n"]//2]
    node_stats.append(dict(stage=stage,family=family,method=method,depth=depth,nodes=len(group),
        model_count=sum(r["model_selected"] for r in group),probe_count=len(elig),rejected=sum(r["early"] for r in group),
        range_hits=sum(r["range_sorted"] for r in group),
        mean_n=mean(r["n"] for r in group),mean_scan_visits=mean(r["scan_visits"] for r in group),
        mean_counter_slots=mean(r["counter_slots"] for r in group),mean_range_slots=mean(r["range_slots"] for r in group),
        mean_range_visits=mean(r["range_visits"] for r in group)))
    if method=="observe" and elig:
        confusion.append(dict(stage=stage,family=family,depth=depth,probed=len(elig),
            actual_fail=len(pos),actual_pass=len(neg),TP=sum(r["early"] for r in pos),FN=sum(not r["early"] for r in pos),
            FP=sum(r["early"] for r in neg),TN=sum(not r["early"] for r in neg)))
put("node_summary.csv",node_stats)
put("observe_confusion.csv",confusion)
meta=dict(cases=len(inputs),old_methods=27,new_methods=len(new),banks=8,rounds=5,
          checked_timed_outputs=sum(map(len,times.values())),checked_diagnostic_outputs=len(inputs)*8*4,
          diagnostic_node_records=len(nodes))
(root/"summary.json").write_text(json.dumps(meta,indent=2)+"\n")
print(meta)

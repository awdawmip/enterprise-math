"""Paired bank medians and equal-family descriptive speed comparisons for phase 6."""
import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import geometric_mean, mean, median
import json

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("result_dir", type=Path)
root=parser.parse_args().result_dir
new=("deep_gate","radix","range_radix")
fourth="certified_combined_1024"
fifth="child_range"
times=defaultdict(dict)
bank_order=defaultdict(set)
sizes={}
def write(name, data):
    with (root/name).open("w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(data[0]))
        writer.writeheader()
        writer.writerows(data)
with (root/"timings.csv").open() as f:
    for r in csv.DictReader(f):
        fam,b,rnd,method=r["family"],int(r["bank"]),int(r["round"]),r["algorithm"]
        seq=int(r["order"])
        assert seq not in bank_order[fam,b,rnd]
        bank_order[fam,b,rnd].add(seq)
        assert rnd not in times[fam,b,method] and int(r["ns"])>0
        times[fam,b,method][rnd]=int(r["ns"])
        sizes[fam]=int(r["n"])
assert len(bank_order)==240 and all(s==set(range(32)) for s in bank_order.values())
assert all(set(v)==set(range(5)) for v in times.values())
assert len(sizes)==6 and {b for fam,b,m in times}==set(range(32,40))
bankus={k:median(v.values())/1000 for k,v in times.items()}
allrows=[]; paired=[]; comparisons=[]; overview=[]
for fam,n in sizes.items():
    methods={k[2] for k in times if k[0]==fam}
    assert len(methods)==32
    us={m:median(bankus[fam,b,m] for b in range(32,40)) for m in methods}
    for m in sorted(us):allrows.append(dict(family=fam,n=n,method=m,median_us=us[m]))
    best=min(methods-set(new),key=us.get)
    for m in new:
        for label,ref in [("previous_child_range",fifth),("phase4_certified",fourth),("fastest_29",best)]:
            ratios=[]
            for b in range(32,40):
                t=bankus[fam,b,m];u=bankus[fam,b,ref]
                ratios.append(u/t)
                paired.append(dict(family=fam,n=n,bank=b,method=m,comparison=label,reference=ref,
                    method_us=t,reference_us=u,speedup=u/t))
            comparisons.append(dict(family=fam,n=n,method=m,comparison=label,reference=ref,
                method_us=us[m],reference_us=us[ref],speedup=us[ref]/us[m],
                paired_median=median(ratios),paired_wins=sum(x>1 for x in ratios)))
for method in new:
    for comp in ("previous_child_range","phase4_certified","fastest_29"):
        vals=[r["speedup"] for r in comparisons if r["method"]==method and r["comparison"]==comp]
        overview.append(dict(method=method,comparison=comp,families=len(vals),
            geomean=geometric_mean(vals),wins=sum(x>1 for x in vals),
            gain_ge_10pct=sum(x>=1.1 for x in vals),runtime_over_ge_10pct=sum(x<=1/1.1 for x in vals)))
write("all_methods.csv",allrows);write("bank_pairs.csv",paired)
write("comparisons.csv",comparisons);write("stage_summary.csv",overview)

traces=defaultdict(list)
with (root/"nodes.csv").open() as f:
    for r in csv.DictReader(f):
        traces[r["family"],r["algorithm"],int(r["depth"])].append(r)
noderows=[]
for (fam,m,d),group in traces.items():
    def total(k): return sum(int(r[k]) for r in group)
    noderows.append(dict(family=fam,method=m,depth=d,nodes=len(group),gate_runs=sum(int(r["probes"])==(1024 if m=="deep_gate" else 64) for r in group),
        gate_rejects=total("early"),range_hits=total("range_sorted"),mean_input=total("n")/len(group),
        mean_scan_visits=total("scan_visits")/len(group),mean_range_visits=total("range_visits")/len(group),
        mean_counter_slots=total("counter_slots")/len(group),mean_range_slots=total("range_slots")/len(group)))
write("node_summary.csv",noderows)
# gate and deep_gate instrument actual_misses over the complete node before acting.
# Child-only deep probing is compared on the intersection with the 64-probe gate;
# the root-only short gate is recorded separately by the depth column.
predictions=[]
for (fam,m,d),group in traces.items():
    if m not in ("gate","deep_gate"): continue
    target=1024 if m=="deep_gate" else 64
    obs=[r for r in group if int(r["probes"])==target]
    if not obs: continue
    fail=[r for r in obs if int(r["actual_misses"])>int(r["n"])//2]
    passed=[r for r in obs if int(r["actual_misses"])<=int(r["n"])//2]
    predictions.append(dict(family=fam,method=m,depth=d,probed=len(obs),actual_fail=len(fail),
        actual_pass=len(passed),TP=sum(int(r["early"]) for r in fail),FN=sum(not int(r["early"]) for r in fail),
        FP=sum(int(r["early"]) for r in passed),TN=sum(not int(r["early"]) for r in passed)))
write("prediction_matrix.csv",predictions)
summary=dict(families=len(sizes),bank_ids=list(range(32,40)),rounds=5,old_methods=29,new_methods=3,
             checked_timed_outputs=sum(map(len,times.values())),checked_diagnostic_outputs=240,
             diagnostic_node_records=sum(map(len,traces.values())))
(root/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
print(summary)

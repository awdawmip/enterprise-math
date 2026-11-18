#!/usr/bin/env python3
"""R5 nine-state NEW20: independent exact response check; optional full Bellman rerun.
Run in this folder with frozen EXACT_R5_ALL_101_BUDGETS.json copied from pinned
R5 original source. --solve recompiles/executes all 20 recorded exact cases.
--partition-tsv PATH also verifies the full prior endpoint partition class sizes.
"""
import argparse,hashlib,json,re,subprocess
from pathlib import Path
L=25845652773852463277015040000
U=58182461585441404127941754880
PIN="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
P=Path(__file__).resolve().parent
def maximal(masks):
    s=set(masks)
    return tuple(sorted(m for m in s if not any(m!=t and (m&t)==m for t in s)))
def windows(c,t):
    return maximal(sum(1<<i for i,v in enumerate(c) if a<=v<=a+t) for a in c)
def sweep(c,t):
    ends=sorted(set(z for x in c for z in (2*x-t,2*x+t)))
    masks=[sum(1<<i for i,x in enumerate(c) if abs(z-2*x)<=t) for z in ends]
    masks += [sum(1<<i for i,x in enumerate(c) if abs(a+b-4*x)<=2*t)
              for a,b in zip(ends,ends[1:])]
    return maximal(masks)
def input_for(D,x,y):
    H=(18,24,82,34,17,x,144,208,y)
    sig={}
    for k in range(214,315):
        c=[int(D[str(k)]['counts'][h]) for h in H]
        fam=windows(c,U-1)
        if fam not in sig or k<sig[fam]:sig[fam]=k
    actions=sorted((k,fam) for fam,k in sig.items())
    lines=["9 8",str(len(actions))]
    for k,fam in actions:lines.append(" ".join(map(str,(k,len(fam),*fam))))
    return ("\\n".join(lines)+"\\n").encode(),len(actions)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--solve",action="store_true")
    ap.add_argument("--partition-tsv")
    a=ap.parse_args()
    raw=(P/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest()==PIN
    D=json.loads(raw)['counts_and_cohorts']
    data=json.loads((P/"RESULTS_R5_NINE_NEW20.json").read_text())
    rows=data["runs"]
    assert len(rows)==20 and sum(r["class_size"] for r in rows)==3560
    assert len({(r["x"],r["y"]) for r in rows})==20
    if a.partition_tsv:
        import csv
        table=list(csv.DictReader(open(a.partition_tsv),delimiter="\\t"))
        assert len(table)==2026 and sum(int(r["count"]) for r in table)==30876
        look={(int(r["representative_x"]),int(r["representative_y"])):r for r in table}
        for r in rows:
            t=look[(r["x"],r["y"])]
            assert int(t["group"])==r["group_id"] and int(t["count"])==r["class_size"]
    checks=0
    if a.solve:
        subprocess.run(["g++","-std=c++17","-O3","EXACT_NINE_NEW20.cpp","-o","EXACT_NINE_NEW20"],cwd=P,check=True)
    for r in rows:
        x,y=r["x"],r["y"]
        H=(18,24,82,34,17,x,144,208,y)
        assert len(set(H))==9
        for k in range(214,315):
            c=[int(D[str(k)]['counts'][h]) for h in H]
            assert windows(c,U-1)==sweep(c,U-1),(x,y,k)
            checks+=1
        inp,nacts=input_for(D,x,y)
        assert hashlib.sha256(inp).hexdigest()==r["input_sha256"]
        assert nacts==r["action_families"]
        assert r["exact_cost"]==8335 and r["exit_code"]==0
        if a.solve:
            result=subprocess.run(["./EXACT_NINE_NEW20"],cwd=P,input=inp,capture_output=True,check=True)
            m=re.fullmatch(r"EXACT cost=(\\d+) states=(\\d+) actions=(\\d+) time=([\\d.]+)",result.stdout.decode().strip())
            assert m and list(map(int,m.group(1,2,3)))==[8335,r["memo_states"],nacts]
    assert checks==2020
    print("PASS_R5_NINE_NEW20",checks,"support_checks",len(rows),"exact_solver_logs",sum(r["class_size"] for r in rows),"covered_pairs")
if __name__=="__main__":main()

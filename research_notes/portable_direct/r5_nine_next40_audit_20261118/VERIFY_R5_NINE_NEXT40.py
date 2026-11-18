#!/usr/bin/env python3
"""Independent exact support checks; --solve re-executes all 40 Bellman cases.
Place the original SHA-256-pinned EXACT_R5_ALL_101_BUDGETS.json beside this file.
"""
import argparse, csv, hashlib, json, subprocess, re
from pathlib import Path
P=Path(__file__).resolve().parent
U=58182461585441404127941754880
PIN="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
PRIOR={0,76,1713,331,469,1717,1722,1727,1801,1879,333,336,339,342,344,347,350,619,627,853,861,1159,1161,1170,1382,1384,1164,1167,1172,1175,1178,1390,1578,1586,1694,1698,1703,1708,1791,1796,1805,1810,1874,1883,1888,1935}
def maximal(masks):
 s=set(masks)
 return tuple(sorted(m for m in s if not any(m!=t and (m&t)==m for t in s)))
def windows(c,t):
 return maximal(sum(1<<j for j,z in enumerate(c) if a<=z<=a+t) for a in c)
def endpoint_sweep(c,t):
 edges=sorted(set(e for a in c for e in (2*a-t,2*a+t)))
 masks=[sum(1<<j for j,a in enumerate(c) if abs(e-2*a)<=t) for e in edges]
 masks += [sum(1<<j for j,a in enumerate(c) if abs(e+f-4*a)<=2*t) for e,f in zip(edges,edges[1:])]
 return maximal(masks)
def make_input(D,x,y):
 H=(18,24,82,34,17,x,144,208,y)
 assert len(set(H))==9
 acts={}
 for k in range(214,315):
  c=[int(D[str(k)]["counts"][h]) for h in H]
  fam=windows(c,U-1)
  assert fam==endpoint_sweep(c,U-1),(x,y,k)
  if fam not in acts or k<acts[fam]:acts[fam]=k
 actions=sorted((k,fam) for fam,k in acts.items())
 lines=["9 8",str(len(actions))]+[" ".join(map(str,(k,len(fam),*fam))) for k,fam in actions]
 return ("\n".join(lines)+"\n").encode(),len(actions)
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--solve",action="store_true");args=ap.parse_args()
 raw=(P/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
 assert hashlib.sha256(raw).hexdigest()==PIN
 D=json.loads(raw)["counts_and_cohorts"]; assert len(D)==101
 rows=list(csv.DictReader((P/"RESULTS_R5_NINE_NEXT40.tsv").open(),delimiter="\t"))
 ids=[int(r["group_id"]) for r in rows]
 assert len(rows)==len(set(ids))==40 and set(ids).isdisjoint(PRIOR)
 assert len({(int(r["x"]),int(r["y"])) for r in rows})==40
 assert sum(int(r["class_size"]) for r in rows)==4543
 if args.solve:subprocess.run(["g++","-O3","-std=c++17","EXACT_NINE_NEXT40.cpp","-o","EXACT_NINE_NEXT40"],cwd=P,check=True)
 for row in rows:
  data,num=make_input(D,int(row["x"]),int(row["y"]))
  assert hashlib.sha256(data).hexdigest()==row["input_sha256"]
  assert num==int(row["action_families"])
  assert int(row["exact_cost"])==8335
  if args.solve:
   o=subprocess.run(["./EXACT_NINE_NEXT40"],cwd=P,input=data,capture_output=True,check=True)
   m=re.fullmatch(r"EXACT cost=(\d+) states=(\d+) actions=(\d+) time=([\d.]+)",o.stdout.decode().strip())
   assert m and (int(m.group(1)),int(m.group(2)),int(m.group(3)))==(8335,int(row["memo_states"]),num)
 print("PASS_R5_NINE_NEXT40: 40 exact source inputs; 4040 independent support checks; 4543 new pairs; Bellman replay="+str(args.solve))
if __name__=="__main__":main()

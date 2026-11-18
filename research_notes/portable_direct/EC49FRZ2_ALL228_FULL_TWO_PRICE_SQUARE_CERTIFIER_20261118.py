#!/usr/bin/env python3
"""EC49FRZ2 full [0,1]^2 original native BRC 20-tree certificate.
Run in the downloadable 38-file SHA256-manifested evidence archive root.
--quick: replay all 20 full native trees; --full: also rerun exact Bellman points.
"""
import sys,json,hashlib,subprocess
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"code"))
from EC49FRW_TWO_PRICE_SOLVER import V,PIN
assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert len(V)==228 and all(len(v)==141 for v in V)
for file,sha in [
 ("frozen_original_master.txt","cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"),
 ("EC49FPG_PROFILE.csv","a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f")
]:
 assert hashlib.sha256((ROOT/"source"/file).read_bytes()).hexdigest()==sha
cert=json.loads((ROOT/"evidence"/"EC49FRZ2_FULL_SQUARE_MACHINE_CERT.json").read_text())
rows=cert["regions"]; knots=list(map(F,cert["breakpoints"]))
assert len(rows)==10 and len(knots)==11 and knots[0]==0 and knots[-1]==1
lines=[]
for i,row in enumerate(rows):
 U,K=row["U"],row["K"]
 assert list(map(F,row["m_interval"]))==knots[i:i+2]
 for key,qroot in (("q32_root_tree",32),("q34_root_tree",34)):
  tree=json.loads((ROOT/row[key]).read_text())["tree"]
  assert tree["named_observer"]==qroot
  calls=Counter();maxdepth=0
  for state in range(141):
   n=tree;seen=set();depth=0
   while "named_observer" in n:
    q=n["named_observer"]
    assert 0<=q<228 and q not in seen
    seen.add(q);calls[q]+=1;depth+=1
    n=n["children"][str(V[q][state])]
   assert n["leaf"]==state,(i,key,state)
   maxdepth=max(maxdepth,depth)
  assert (sum(calls.values()),calls[32]+calls[34])==(U,K)
  assert calls[qroot]==141 and maxdepth<=4
  print("TREE_OK",i,key,U,K,flush=True)
 lines.append((U,K))
def diag(s): return min(F(U)-s*K for U,K in lines)
def formula(a,b):
 m,M=min(a,b),max(a,b)
 return diag(m)-141*(M-m)
def bellman(a,b):
 p=subprocess.run([sys.executable,str(ROOT/"code"/"EC49FRW_TWO_PRICE_SOLVER.py"),str(a),str(b)],
                  text=True,capture_output=True,check=True,timeout=120)
 info=json.loads(p.stdout.strip().splitlines()[-1])
 return F(info["Bellman_integer_value"],info["denominator"])
if "--full" in sys.argv:
 for s in knots:
  v=bellman(s,s);assert v==diag(s),(s,v)
  print("DIAGONAL_BELLMAN_OK",s,v,flush=True)
 for a,b in [(F(1),F(0)),(F(3,4),F(2,3)),(F(2,3),F(3,4))]:
  v=bellman(a,b);assert v==formula(a,b),(a,b,v)
  print("OFFDIAGONAL_BELLMAN_OK",a,b,v,flush=True)
else:
 print("Exact DP not rerun; retained successful eleven-diagonal-vertex log is in the archive.")
print("PASS: 20 original native complete tree witnesses × 141 named state paths each.")

#!/usr/bin/env python3
import json,hashlib
from fractions import Fraction
from collections import Counter,defaultdict
from pathlib import Path
try: import numpy as np
except Exception: np=None
ROOT=Path(__file__).resolve().parent; checks=[]
def ck(n,c,d=""):
    checks.append((n,bool(c),str(d)))
    if not c: raise AssertionError(f"{n}: {d}")
def load(n):
 o=json.loads((ROOT/n).read_text())
 if isinstance(o,dict) and o.get("codec")=="zlib+base64":
  import zlib,base64
  raw=zlib.decompress(base64.b64decode(o["compressed_payload_b64"]))
  ck(f"compressed_sha_{n}",hashlib.sha256(raw).hexdigest()==o["uncompressed_sha256"])
  return json.loads(raw)
 return o
def cid(c):return f"{c[0]}:{c[1]}:{c[2]}"
def verts(c):
 o,a,b=c
 return ((a,b),(a+1,b),(a,b+1)) if o=="U" else ((a+1,b),(a,b+1),(a+1,b+1))
def cent(c):
 v=verts(c);return sum(x for x,y in v),sum(y for x,y in v)
def q(a,b):return a*a+a*b+b*b
def rotp(p,k=1):
 a,b=p
 for _ in range(k%6): a,b=-b,a+b
 return a,b
def sector0(c):
 A,B=cent(c)
 return A>0 and B>0
def cand(r):
 B=2*r+3;L=9*(r+1)**2
 return [(o,a,b) for a in range(-B,B+1) for b in range(-B,B+1) for o in ("U","D") if q(*cent((o,a,b)))<=L]
M={}
def micro(s):
 if s in M:return M[s]
 z=[(3*i+1,3*j+1) for i in range(s) for j in range(s-i)]
 z += [(3*i+2,3*j+2) for i in range(max(0,s-1)) for j in range(s-1-i)]
 ck(f"micro_{s}",len(z)==s*s,len(z));M[s]=z;return z
def cov(c,r,s):
 P0,P1,P2=verts(c);D=3*s;rr=(r*D)**2
 uv=np.asarray(micro(s),dtype=np.int64) if np is not None else micro(s)
 if np is not None:
  U=uv[:,0];V=uv[:,1]
  x=D*P0[0]+U*(P1[0]-P0[0])+V*(P2[0]-P0[0]);y=D*P0[1]+U*(P1[1]-P0[1])+V*(P2[1]-P0[1])
  w=x*x+x*y+y*y;return int(np.count_nonzero(w<=rr)),s*s
 n=0
 for U,V in uv:
  x=D*P0[0]+U*(P1[0]-P0[0])+V*(P2[0]-P0[0]);y=D*P0[1]+U*(P1[1]-P0[1])+V*(P2[1]-P0[1])
  n += q(x,y)<=rr
 return int(n),s*s
def field(r,s):return {c:cov(c,r,s) for c in cand(r)}
covreg=load("R059D_STAGE_AD_COVERAGE_FIELD_REGISTRY.json");front=load("R059D_STAGE_AD_FRONTIER_REGISTRY.json")
gate=load("R059D_STAGE_AD_RESOLVER_GATE_MATRIX.json");src=load("R059D_STAGE_AD_SOURCE_CIRCLE_TEACHER_PROTOCOL.json");cp=load("R059D_STAGE_AD_COVERAGE_PROTOCOL.json")
near=load("R059D_STAGE_AD_NEAREST_CELL_RESOLVER.json");thr=load("R059D_STAGE_AD_COVERAGE_THRESHOLD_RESOLVER.json");resid=load("R059D_STAGE_AD_ACCUMULATED_RESIDUAL_RESOLVER.json")
prec=load("R059D_STAGE_AD_COVERAGE_PRECISION_AUDIT.json");ref=load("R059D_STAGE_AD_NATIVE_REFINEMENT_AUDIT.json");hist=load("R059D_STAGE_AD_HISTORICAL_STAIRCASE_BRIDGE_LEDGER.json")
ck("case96",len(covreg["primary_cases"])==96)
ck("front96",len(front["cases"])==96)
ck("gate_disp",gate["primary_disposition"]=="COVERAGE_BRIDGE_ESTABLISHED__RESOLVE_RULE_UNDERDETERMINED")
ck("N96",near["summary"]["primary_circle_gate_pass_cases"]==96)
ck("C96",thr["summary"]["primary_circle_gate_pass_cases"]==96)
ck("R12",resid["summary"]["primary_circle_gate_pass_cases"]==12)
ck("NC25",gate["arms"]["C"]["differs_from_N_cases"]==25)
ck("Rorder82",gate["arms"]["R"]["forward_reverse_different_cases"]==82)
ck("Rref14",resid["summary"]["reflection_pass_cases"]==14)
ck("Rerr",resid["symbolic_invariant"]["proved"] is True and gate["arms"]["R"]["exact_prefix_error_bound"]=="1/2")
ck("teacher_metric_typed",src["source_semantics"]["Q_typing"]=="SOURCE_COMPATIBILITY_CLASSIFIER_ONLY__NOT_ENTERPRISE_NATIVE_METRIC")
ck("theta_half",cp["resolvers_predeclared"]["C"]["theta"]==[1,2])
ck("no_tuning",cp["anti_tuning"]=={"radius_specific_threshold":False,"radius_specific_scan_order":False})
ck("Nsampling",prec["statuses"]["N"]=="EXACT_SAMPLING_PRECISION_STABILITY")
ck("Rrefine",ref["statuses"]["R"]=="CROSS_PRECISION_INCONSISTENT")
ck("hist_open",hist["status"].endswith("EXACT_HISTORICAL_BRC_SELECTION_BRIDGE_OPEN"))
# every stored frontier rational is valid and total=s^2
for case in front["cases"]:
 r,s,gn,gc,sn,sc,rows=case
 ck(f"front_n_{r}_{s}",gn==6*len(rows),(gn,len(rows)))
 ck(f"sector_n_{r}_{s}",sn==len(rows),(sn,len(rows)))
 for o,a,b,k,t in rows:
  ck(f"frac_{r}_{s}_{o}_{a}_{b}",0<k<t and t==s*s)
# exact full replay on frozen discriminator matrix
disc={1,2,3,5,8,13,21}
cmap={(x["r"],x["s"]):x for x in covreg["primary_cases"]}
fmap={(x[0],x[1]):x for x in front["cases"]}
for r in sorted(disc):
 for s in (4,8,16,32):
  F=field(r,s); row=cmap[(r,s)]
  payload="\n".join(f"{cid(c)}:{F[c][0]}/{F[c][1]}" for c in sorted(F,key=cid)).encode()
  ck(f"digest_{r}_{s}",hashlib.sha256(payload).hexdigest()==row["field_sha256"])
  fr=sorted((c for c,(k,t) in F.items() if 0<k<t),key=cid)
  sf=sorted((c for c in fr if sector0(c)),key=cid)
  stored=fmap[(r,s)][6]
  exp=[[0 if c[0]=="U" else 1,c[1],c[2],F[c][0],F[c][1]] for c in sf]
  ck(f"front_sector_replay_{r}_{s}",exp==stored)
  ck(f"front_D6_count_{r}_{s}",len(fr)==6*len(sf),(len(fr),len(sf)))
# exact residual recurrence invariant, independent of data
vals=[Fraction(-1,2),Fraction(-1,3),Fraction(0),Fraction(1,3),Fraction(499,1000)]
cs=[Fraction(0),Fraction(1,7),Fraction(1,2),Fraction(6,7),Fraction(1)]
for e in vals:
 for c in cs:
  if not (Fraction(-1,2)<=e<Fraction(1,2)):continue
  z=e+c;b=1 if z>=Fraction(1,2) else 0;en=z-b
  ck(f"res_inv_{e}_{c}",Fraction(-1,2)<=en<Fraction(1,2),en)
payload="\n".join(f"{n}:{int(ok)}:{d}" for n,ok,d in checks).encode()
out={"schema":"R059D_STAGE_AD_DETERMINISTIC_CHECKER_OUTPUT_V1","status":"PASS","checks_total":len(checks),"checks_passed":sum(o for _,o,_ in checks),"checks_failed":sum(not o for _,o,_ in checks),"checks_digest_sha256":hashlib.sha256(payload).hexdigest(),"history_gate":"PENDING_EXTERNAL_GITHUB_COMPARE","summary":"Artifact invariants, all frontier rational rows, 28 exact full coverage-field replays, resolver gate summaries, residual invariant and hard semantic firewalls pass."}
print(json.dumps(out,sort_keys=True))

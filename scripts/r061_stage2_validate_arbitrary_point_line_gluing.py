#!/usr/bin/env python3
"""Deterministic R061 Stage 2 checker: arbitrary-point native-line translation/gluing."""
from __future__ import annotations
import argparse, hashlib, itertools, json
from collections import Counter, defaultdict
from math import comb, isqrt
from pathlib import Path

TASKBOOK_SOURCE="8b197776249e0b18850cee8375488de9aa57cbb4"
OWNER_BRANCH="research/r061-stage2-arbitrary-point-line-gluing"
RESEARCHER_ID="EM-R061S2-3CE600"
STAGE1R_HEAD="653071b8e230d1e707e0544cab22ad2a408b92bd"
TARGET={
"coordinate_fiber_sha256":"0f4bccc2ff3fd7e7ae22ccd9e4abf248cf215bffea7bdd02aabca9b8c2bb8338",
"explicit_shuffle_sha256":"572562117dbc2ba388543fbbeaa73bd26359ef47c26ef7ff31314ee92b318f93",
"explicit_shuffle_word_count":8388607,
"compressed_pascal_sha256":"780c833ed685c707b2e57d70a2ecf015e56bc5196ee8e62a646720eb0707d002",
"native_replay_sha256":"359474ba6b53ffbb3c326cf331d55dd3ed098837451a46b0754926b7c642d702",
"native_pair_count":190,"native_formal_linearization_count":524287,
"native_three_sector_path_count":1572861,
"compressed_trace_sha256":"aa0e3761f7446cf89e782c74b8020157b41713a37022daf44a2f8e95179e4ead"}
SECTORS=("S12","S23","S31")
BASIS={"S12":((3,0),(0,3)),"S23":((0,3),(-3,-3)),"S31":((-3,-3),(3,0))}
ANCHOR={"S12":(1,2),"S23":(-2,-1),"S31":(1,-1)}
INCIDENT=((-2,-1),(1,-1),(1,2))
AXCH={"E1":(("S12",0),("S31",1)),"E2":(("S12",1),("S23",0)),"E3":(("S23",1),("S31",0))}
STARTS=((0,0),(1,0),(0,1),(-1,-1),(2,-1),(-2,1),(3,2))

def dump(p,o): Path(p).write_text(json.dumps(o,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
def add(p,q): return p[0]+q[0],p[1]+q[1]
def sub(p,q): return p[0]-q[0],p[1]-q[1]
def mul(k,p): return k*p[0],k*p[1]
def p3(p): return 3*p[0],3*p[1]
def q3(p): x,y=p; return x*x+y*y-x*y

def opensector(s,v):
 x,y=v
 return (x>0 and y>0) if s=="S12" else (x<0 and y-x>0) if s=="S23" else (y<0 and x-y>0)
def v3(s,a,b): return add(mul(a,BASIS[s][0]),mul(b,BASIS[s][1]))
def c3(P,s,a,b): return add(p3(P),add(ANCHOR[s],v3(s,a,b)))
def vv3(P,s,a,b): return add(p3(P),v3(s,a,b))

def can(p,q): m=min(p,q,0); return p-m,q-m,-m
def carrier(D): A,B,C=D; assert min(D)==0; return A-C,B-C
def vid(P): return {"kind":"NATIVE_COORDINATE_VERTEX","addr":list(can(*P))}
def dtype(D):
 A,B,C=D
 if D==(0,0,0): return {"class":"ZERO"}
 pos=[i for i,x in enumerate(D) if x>0]; z=[i for i,x in enumerate(D) if x==0]
 if len(pos)==1 and len(z)==2: return {"class":"AXIS","axis":f"E{pos[0]+1}","n":D[pos[0]]}
 if C==0 and A>0 and B>0:return {"class":"OPEN_SECTOR","sector":"S12","a":A,"b":B}
 if A==0 and B>0 and C>0:return {"class":"OPEN_SECTOR","sector":"S23","a":B,"b":C}
 if B==0 and C>0 and A>0:return {"class":"OPEN_SECTOR","sector":"S31","a":C,"b":A}
 raise AssertionError(D)
def presentations(dp):
 x,y=dp; out=[]
 if x>=0 and y>=0: out.append(("S12",x,y))
 a,b=y-x,-x
 if a>=0 and b>=0: out.append(("S23",a,b))
 a,b=-y,x-y
 if a>=0 and b>=0: out.append(("S31",a,b))
 return out
def decdiff(dp):
 D=can(*dp); t=dtype(D); o={"native_components":list(D),**t}
 o["chart_presentations"]=[list(x) for x in presentations(dp)] if t["class"]!="ZERO" else [[s,0,0] for s in SECTORS]
 return o
def decomp(P,Q): return {"start":vid(P),"end":vid(Q),"implementation_carrier_diff":list(sub(Q,P)),**decdiff(sub(Q,P))}
def lid(P,Q):
 d=decomp(P,Q)
 if d["class"]=="ZERO": return {"kind":"TRANSLATED_ZERO_TRACE","start":d["start"]}
 if d["class"]=="AXIS": return {"kind":"TRANSLATED_AXIS_TRACE","start":d["start"],"axis":d["axis"],"n":d["n"]}
 return {"kind":"TRANSLATED_COMPONENT_TRACE","start":d["start"],"sector":d["sector"],"a":d["a"],"b":d["b"]}
def lsq(P,Q): A,B,C=can(*sub(Q,P)); return A*A+B*B+C*C

# Exact frozen Stage 1R regressions; no Stage 1/1R result artifact is read.
def coord_hash(limit=100000):
 f=defaultdict(list); m=isqrt(limit)
 for a in range(m+1):
  for b in range(m+1):
   n=a*a+b*b
   if n<=limit:f[n].append((a,b))
 h=hashlib.sha256()
 for n in range(limit+1):h.update((f"{n}:"+",".join(f"{a}.{b}" for a,b in sorted(f.get(n,())))+"\n").encode())
 return h.hexdigest()
def word(n,pos): p=set(pos); return "".join("X" if i in p else "Y" for i in range(n))
def shuffle_hash(mx=22):
 h=hashlib.sha256(); c=0
 for n in range(mx+1):
  for a in range(n+1):
   b=n-a
   for p in itertools.combinations(range(n),a):h.update(f"{a},{b}:{word(n,p)}\n".encode());c+=1
 return h.hexdigest(),c
def pascal_hash(mx=512):
 h=hashlib.sha256(); prev=None
 for n in range(mx+1):
  row=[1] if n==0 else [1]+[prev[k-1]+prev[k] for k in range(1,n)]+[1]
  for a,c in enumerate(row):h.update(f"{n},{a},{c}\n".encode())
  prev=row
 return h.hexdigest()
def native_replay(mx=18):
 h=hashlib.sha256(); pairs=formal=paths=bad=dup=0
 def prefix(s,x,y):
  if s=="S12":gx,gy=1+3*x,2+3*y;return gx>0 and gy>0
  if s=="S23":gx,gy=-2-3*y,-1+3*x-3*y;return gx<0 and gy-gx>0
  gx,gy=1-3*x+3*y,-1-3*x;return gy<0 and gx-gy>0
 for n in range(mx+1):
  for a in range(n+1):
   b=n-a;pairs+=1;seen=set()
   for pos in itertools.combinations(range(n),a):
    mask=sum(1<<i for i in pos);dup+=mask in seen;seen.add(mask);w=word(n,pos);x=y=0;states=["0.0"];ok={s:prefix(s,0,0) for s in SECTORS}
    for ch in w:
     x+=ch=="X";y+=ch=="Y";states.append(f"{x}.{y}")
     for s in SECTORS:ok[s]=ok[s] and prefix(s,x,y)
    bad+=0 if (x,y)==(a,b) and all(ok.values()) else 1;formal+=1;ss=";".join(states)
    for s in SECTORS:h.update(f"{s}:{a},{b}:{w}:{ss}\n".encode());paths+=1
 return h.hexdigest(),pairs,formal,paths,bad,dup
def ctrace(mx=256):
 h=hashlib.sha256()
 for n in range(mx+1):
  for a in range(n+1):h.update(f"{n},{a},{n-a},{comb(n,a)}\n".encode())
 return h.hexdigest()
def s1reg():
 ch=coord_hash();sh,sw=shuffle_hash();ph=pascal_hash();nh,np,nf,npaths,bad,dup=native_replay();ct=ctrace()
 g={"coordinate_fiber_sha256":ch,"explicit_shuffle_sha256":sh,"explicit_shuffle_word_count":sw,"compressed_pascal_sha256":ph,
 "native_replay_sha256":nh,"native_pair_count":np,"native_formal_linearization_count":nf,"native_three_sector_path_count":npaths,"compressed_trace_sha256":ct,
 "native_structural_mismatch_count":bad+dup}
 checks={k:g[k]==v for k,v in TARGET.items()};checks["native_structural_zero"]=g["native_structural_mismatch_count"]==0
 return {"generated":g,"target_comparisons":checks,"pass":all(checks.values())}

def incidence(r=4):
 mm=[];tested=0
 for x in range(-r,r+1):
  for y in range(-r,r+1):
   P=(x,y)
   for s in SECTORS:
    tested+=1; hits=[z for z in INCIDENT if opensector(s,z)]
    if hits!=[ANCHOR[s]] or q3(ANCHOR[s])!=3:mm.append((P,s,hits))
   for axis,chs in AXCH.items():
    s,i=chs[0];step=BASIS[s][i]
    for n in range(5):
     V=add(p3(P),mul(n,step))
     if V[0]%3 or V[1]%3 or ((V[0]-1)%3==0 and (V[1]-2)%3==0):mm.append((P,axis,n))
 return {"patch_radius":r,"vertex_count":(2*r+1)**2,"translated_sector_anchor_checks":tested,"sector_hit_totals":{s:(2*r+1)**2 for s in SECTORS},"mismatch_count":len(mm),"smallest_mismatch":mm[0] if mm else None,"pass":not mm}
def decensus(r=4):
 pts=[(x,y) for x in range(-r,r+1) for y in range(-r,r+1)];cc=Counter();pc=Counter();mm=[]
 for P in pts:
  for Q in pts:
   d=decomp(P,Q);cc[d["class"]]+=1;pc[len(d["chart_presentations"])]+=1
   D=tuple(d["native_components"]); exp=3 if d["class"]=="ZERO" else 2 if d["class"]=="AXIS" else 1
   if carrier(D)!=sub(Q,P) or len(d["chart_presentations"])!=exp:mm.append((P,Q,d))
 six={k:decdiff(v) for k,v in {"+E1":(1,0),"+E2":(0,1),"+E3":(-1,-1),"opposite_E1":(-1,0),"opposite_E2":(0,-1),"opposite_E3":(1,1)}.items()}
 return {"patch_radius":r,"vertex_count":len(pts),"directed_pair_count":len(pts)**2,"class_counts":dict(cc),"chart_presentation_count_histogram":{str(k):v for k,v in sorted(pc.items())},"six_carrier_direction_audit":six,"mismatch_count":len(mm),"smallest_mismatch":mm[0] if mm else None,"pass":not mm}
def pathaudit(mx=12):
 mm=[];traces=paths=trans=0;per=Counter()
 for P in STARTS:
  for s in SECTORS:
   u,v=BASIS[s];anchor=add(p3(P),ANCHOR[s])
   for n in range(mx+1):
    for a in range(n+1):
     b=n-a;traces+=1;seen=set()
     for pos in itertools.combinations(range(n),a):
      x=y=0;cur=anchor;sig=[cur];paths+=1;per[s]+=1
      for ch in word(n,pos):
       step=u if ch=="X" else v;x+=ch=="X";y+=ch=="Y";trans+=1
       if q3(step)!=9:mm.append((P,s,a,b,"neighbor"))
       cur=add(cur,step);sig.append(cur)
       if not opensector(s,sub(cur,p3(P))):mm.append((P,s,a,b,"prefix"))
      if (x,y)!=(a,b) or cur!=c3(P,s,a,b) or q3(sub(cur,vv3(P,s,a,b)))!=3:mm.append((P,s,a,b,"terminal"))
      if tuple(sig) in seen:mm.append((P,s,a,b,"collision"))
      seen.add(tuple(sig))
     if len(seen)!=comb(n,a):mm.append((P,s,a,b,"binomial"))
 return {"max_a_plus_b":mx,"start_count":len(STARTS),"start_vertices":[vid(p) for p in STARTS],"translated_trace_count":traces,"explicit_path_count":paths,"center_transition_count":trans,"per_sector_path_count":dict(per),"mismatch_count":len(mm),"smallest_mismatch":mm[0] if mm else None,"pass":not mm}
def axisaudit(mx=12):
 mm=[];ids=pres=distinct=0
 for P in STARTS:
  for axis,chs in AXCH.items():
   for n in range(mx+1):
    ids+=1;ends=[];tr=[]
    for s,i in chs:
     pres+=1;a,b=(n,0) if i==0 else (0,n);step=BASIS[s][i];st=c3(P,s,0,0);ends.append(vv3(P,s,a,b));tr.append(tuple(add(st,mul(k,step)) for k in range(n+1)))
    if ends[0]!=ends[1]:mm.append((P,axis,n,"endpoint"))
    if tr[0]==tr[1]:mm.append((P,axis,n,"dedup"))
    else:distinct+=1
 z=all(len({c3(P,s,0,0) for s in SECTORS})==3 for P in STARTS)
 if not z:mm.append(("zero",))
 return {"start_count":len(STARTS),"axis_n_range":[0,mx],"global_axis_identity_count":ids,"chart_presentation_count":pres,"distinct_adjacent_chart_trajectory_pairs":distinct,"zero_trace_has_three_distinct_incidence_support_branches":z,"mismatch_count":len(mm),"smallest_mismatch":mm[0] if mm else None,"pass":not mm}
def transcov(r=3):
 pts=[(x,y) for x in range(-r,r+1) for y in range(-r,r+1)];Rs=((1,0),(0,1),(-1,-1),(2,-1),(-2,1));mm=[];t=0
 for P in pts:
  for Q in pts:
   d=decdiff(sub(Q,P));L=lsq(P,Q)
   for R in Rs:
    t+=1;P2=add(P,R);Q2=add(Q,R);d2=decdiff(sub(Q2,P2))
    if d!=d2 or L!=lsq(P2,Q2):mm.append((P,Q,R))
 return {"pair_patch_radius":r,"translations":[list(x) for x in Rs],"tested_translation_cases":t,"mismatch_count":len(mm),"smallest_mismatch":mm[0] if mm else None,"pass":not mm}
def thirdaudit(mx=12):
 mm=[];t=0;small=None
 for P in STARTS:
  for s in SECTORS:
   u,v=BASIS[s];diag=add(u,v)
   for n in range(2,mx+1):
    for a in range(1,n):
     b=n-a;t+=1;m=min(a,b);cur=c3(P,s,0,0);cur=add(cur,mul(m,diag));cur=add(cur,mul(a-m,u));cur=add(cur,mul(b-m,v))
     if cur!=c3(P,s,a,b):mm.append((P,s,a,b))
     if small is None and a==b==1:small={"start_vertex":vid(P),"sector":s,"branch":[1,1],"trace_linearizations":["XiXj","XjXi"],"carrier_endpoint_shortcut":["-Xk"],"classification":"CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE","jump_count_used_for_classification":False,"same_carrier_endpoint":True}
 return {"max_a_plus_b":mx,"start_count":len(STARTS),"tested_nondegenerate_translated_branches":t,"smallest_witness":small,"classification":"SAME_CARRIER_ENDPOINT / DIFFERENT_NATIVE_COMPONENT_TRACE","mismatch_count":len(mm),"smallest_mismatch":mm[0] if mm else None,"pass":not mm}
def reversal(r=4):
 pts=[(x,y) for x in range(-r,r+1) for y in range(-r,r+1)];struct=[];sym=0;tested=0
 for P in pts:
  for Q in pts:
   if P==Q:continue
   tested+=1;D=can(*sub(Q,P));R=can(*sub(P,Q));M=max(D)
   if R!=tuple(M-x for x in D):struct.append((P,Q,D,R))
   if sum(x*x for x in D)!=sum(x*x for x in R):sym+=1
 P=(0,0);Q=(1,0);D=can(*sub(Q,P));R=can(*sub(P,Q))
 ce={"minimality":"smallest nonzero forward native squared length (=1), canonicalized up to translation and cyclic axis relabeling","P":[0,0],"Q":[1,0],"start":vid(P),"end":vid(Q),"forward_components":list(D),"reverse_components":list(R),"forward_length_squared":1,"reverse_length_squared":2,"forward_line_identity":lid(P,Q),"reverse_line_identity":lid(Q,P),"groupoid_inverse_is_positive_trace_representative":False}
 return {"patch_radius":r,"tested_nonzero_directed_pairs":tested,"reversal_component_complement_formula":"D_rev = M*(1,1,1)-D, M=max(D)","structural_reversal_map_without_native_negative_axes":not struct,"length_symmetry":sym==0,"length_symmetry_failure_count":sym,"smallest_length_symmetry_counterexample":ce,"symmetry_condition_nonzero":"2*sum(D)=3*max(D); with one zero, larger active component = 2*smaller active component","mismatch_count":len(struct),"smallest_mismatch":struct[0] if struct else None,"pass_structural":not struct}
def tri(r=4):
 pts=[(x,y) for x in range(-r,r+1) for y in range(-r,r+1)];L={(P,Q):lsq(P,Q) for P in pts for Q in pts};bad=[];n=0
 def le(A,B,C): return A<=B+C or (A-B-C)*(A-B-C)<=4*B*C
 for P in pts:
  for Q in pts:
   for R in pts:
    n+=1
    if not le(L[P,R],L[P,Q],L[Q,R]):bad.append((P,Q,R,L[P,R],L[P,Q],L[Q,R]))
 return {"patch_radius":r,"vertex_count":len(pts),"tested_ordered_triples":n,"failure_count":len(bad),"smallest_counterexample":bad[0] if bad else None,"exact_comparator":"sqrt(A)<=sqrt(B)+sqrt(C): A<=B+C OR (A-B-C)^2<=4BC","global_proof_key":"canonicalize D1+D2 by subtracting m=min_i(D1_i+D2_i)>=0 componentwise, then ||can||_2<=||D1+D2||_2<=||D1||_2+||D2||_2","pass":not bad}

def run(out):
 out.mkdir(parents=True,exist_ok=True);s1=s1reg();inc=incidence();dc=decensus();pa=pathaudit();ax=axisaudit();tc=transcov();th=thirdaudit();rv=reversal();ti=tri()
 unexpected=[("stage1r",0 if s1["pass"] else 1),("incidence",inc["mismatch_count"]),("decomposition",dc["mismatch_count"]),("path",pa["mismatch_count"]),("axis",ax["mismatch_count"]),("translation",tc["mismatch_count"]),("third",th["mismatch_count"]),("reversal_structure",rv["mismatch_count"]),("triangle",ti["failure_count"])]
 mc=sum(n for _,n in unexpected);metric=rv["length_symmetry"] and ti["pass"]
 summary={"schema":"R061_STAGE2_REPLAY_SUMMARY_V1","taskbook_source":TASKBOOK_SOURCE,"owner_branch":OWNER_BRANCH,"researcher_id":RESEARCHER_ID,"stage1r_head":STAGE1R_HEAD,"hard_target":"ARBITRARY_POINT_TO_POINT_NATIVE_LINE_TRACE_AND_CROSS_SECTOR_GLUING_DERIVED","hard_target_derived_in_weaker_directed_line_length_sense":mc==0,"NATIVE_INTEGER_VERTEX_DISTANCE_IS_METRIC":metric,"POINT_TO_POINT_NATIVE_LINE_LENGTH_OBJECT":"DIRECTED_NATIVE_LINE_GAUGE","triangle_inequality_pass":ti["pass"],"reversal_length_symmetry_pass":rv["length_symmetry"],"full_stage2_metric_acceptance":False,"stage1r_regression":s1,"translated_sector_atlas":inc,"point_pair_decomposition":dc,"path_fiber":pa,"axis_gluing":ax,"translation_covariance":tc,"third_direction":th,"reversal":rv,"triangle_inequality":ti,"mismatch_count":mc,"unexpected_mismatch_sources":unexpected,"CI_NOT_REQUIRED_FOR_RESEARCH":True,"stop_after_stage2_for_driver_review":True}
 mism={"schema":"R061_STAGE2_MISMATCHES_V1","mismatch_count":mc,"smallest_mismatch":next(({"source":s,"count":n} for s,n in unexpected if n),None),"classified_negative_results_not_counted_as_checker_mismatches":{"reversal_length_symmetry":rv["length_symmetry"],"reversal_length_symmetry_failure_count":rv["length_symmetry_failure_count"],"smallest_reversal_counterexample":rv["smallest_length_symmetry_counterexample"],"native_integer_vertex_distance_is_metric":metric}}
 dump(out/"R061_STAGE2_REPLAY_SUMMARY.json",summary);dump(out/"R061_STAGE2_TRANSLATED_ORIGIN_INCIDENCE.json",inc);dump(out/"R061_STAGE2_POINT_PAIR_DECOMPOSITION_CENSUS.json",dc);dump(out/"R061_STAGE2_TRANSLATED_PATH_FIBER_CERTIFICATE.json",pa);dump(out/"R061_STAGE2_REVERSAL_SYMMETRY_OBSTRUCTION.json",{"schema":"R061_STAGE2_REVERSAL_SYMMETRY_OBSTRUCTION_V1","metric_symmetry":rv["length_symmetry"],"smallest_counterexample":rv["smallest_length_symmetry_counterexample"],"component_formula":rv["reversal_component_complement_formula"],"symmetry_condition_nonzero":rv["symmetry_condition_nonzero"],"classification":"EXACT_METRIC_OBSTRUCTION / DIRECTED_LINE_LENGTH_SURVIVES"});dump(out/"R061_STAGE2_TRIANGLE_INEQUALITY_CERTIFICATE.json",ti);dump(out/"R061_STAGE2_MISMATCHES.json",mism)
 return summary
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("--out",default="research_results/R061_STAGE2");a=ap.parse_args();s=run(Path(a.out));print(json.dumps({"hard_target_directed_line_length":s["hard_target_derived_in_weaker_directed_line_length_sense"],"metric":s["NATIVE_INTEGER_VERTEX_DISTANCE_IS_METRIC"],"mismatch_count":s["mismatch_count"],"reversal_symmetry":s["reversal_length_symmetry_pass"],"triangle":s["triangle_inequality_pass"]},sort_keys=True));raise SystemExit(0 if s["mismatch_count"]==0 else 1)

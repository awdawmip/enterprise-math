#!/usr/bin/env python3
"""PREFIX-306: exact Gaussian-integer BRC reference-error certificate.
Source matrices: awdawmip/enterprise-math research_notes/research6_prefix299_rank2_left_orbits_20261027/RESULTS_PREFIX299.json
Git blob b6acffe158f014469235f5428d2889ff43b62810, read at main@6cd1699501c7a63844809607730f2e32677f39fb.
This embedded subset is verified against 16H-S, not an independent rediscovery of its exhaustive classification.
Run: python3 verify_prefix306.py > RESULTS_PREFIX306.json
"""
import itertools, json
from fractions import Fraction

MATRIX_REPS = {
"S4": [
[[[-5,2],[0,0],[2,0]],[[-4,1],[4,0],[-2,1]],[[-1,0],[0,-4],[-1,-6]]],
[[[-5,-2],[0,0],[2,0]],[[-4,-1],[4,0],[-2,-1]],[[-1,0],[0,4],[-1,6]]],
[[[-5,-2],[0,0],[2,0]],[[-3,2],[4,0],[1,4]],[[-2,1],[0,-4],[-4,-3]]],
[[[-5,2],[0,0],[2,0]],[[-3,-2],[4,0],[1,-4]],[[-2,-1],[0,4],[-4,3]]],
[[[-5,-2],[0,0],[2,0]],[[-3,1],[0,0],[-5,3]],[[-2,-2],[4,4],[2,2]]],
[[[-5,2],[0,0],[2,0]],[[-3,-1],[0,0],[-5,-3]],[[-2,-2],[4,4],[2,2]]]
],
"S7": [
[[[-6,1],[4,0],[0,1]],[[-2,0],[0,0],[5,-2]],[[-2,1],[-4,0],[-4,1]]],
[[[-6,-1],[4,0],[0,-1]],[[-2,-1],[-4,0],[-4,-1]],[[-2,0],[0,0],[5,2]]],
[[[-5,3],[0,0],[-3,1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,2]]],
[[[-5,-3],[0,0],[-3,-1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,-2]]],
[[[-4,-3],[0,4],[-2,1]],[[-4,1],[0,-4],[-2,-3]],[[-2,0],[0,0],[5,2]]],
[[[-4,-1],[0,4],[-2,3]],[[-4,3],[0,-4],[-2,-1]],[[-2,0],[0,0],[5,-2]]]
]}

def z(x=0,y=0): return (int(x),int(y))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cj(a): return (a[0],-a[1])
def scl(a,n): return (a[0]*n,a[1]*n)
def ns(a): return a[0]*a[0]+a[1]*a[1]
Q = [z(1),z(0,1),z(-1),z(0,-1)]
ONE = z(1)
W = list(dict.fromkeys(z(e1-e0,ei-e0) for e0,e1,ei in itertools.product((-1,1),repeat=3)))
assert len(W)==7 and set(W)==set(map(tuple,[(0,0),(2,0),(-2,0),(0,2),(0,-2),(2,2),(-2,-2)]))

def gram(M,kind):
 H=((3,-1,0),(-1,2,1),(0,1,3))
 S=(1,0,2) if kind=="S4" else (2,0,1)
 for k in range(3):
  for l in range(3):
   v=z()
   for row in M:v=add(v,mul(cj(row[k]),row[l]))
   assert v==z(16*H[k][l]-(S[k] if k==l else 0),0), (kind,k,l)

def brc_mass(paths):
 """All ordered, labeled path pairs; their Gaussian numerator is the source-aware BRC carrier."""
 result=z()
 for p in paths:
  for r in paths: result=add(result,mul(p[1],cj(r[1])))
 assert result[1]==0 and result[0]>=0
 return result[0]

def row_error_max(M,j,q,u):
 """Maximum squared ||delta a||/epsilon over signed measurement-error corners.
 w_P=(e_P1-e_P0)+i(e_Pi-e_P0).
 N=4 w_R - (u m0)w_E - (u m2)q w_C, T=u(-m0+m1+m2).
 delta b0=(T wE-N)/T, delta b1=N/T, delta b2=(T q wC+N)/T.
 ||delta a||=||delta b|| since q is C4.
 """
 row=[mul(u,x) for x in M[j]]
 T=add(sub(row[1],row[0]),row[2]); d=ns(T)
 assert d>0
 best_n=-1; best_w=None
 for we,wc,wr in itertools.product(W,repeat=3):
  N=sub(sub(scl(wr,4),mul(row[0],we)),mul(row[2],mul(q,wc)))
  val=ns(sub(mul(T,we),N))+ns(N)+ns(add(mul(T,mul(q,wc)),N))
  if val>best_n:best_n,best_w=val,(we,wc,wr)
 return Fraction(best_n,d),[list(x) for x in best_w],d

def run():
 rows=[]; winner_dist={};maxC=Fraction(-1);maxC_record=None
 counts={"gram_exact_entries":0,"labeled_BRC_bin_readouts":0,"ordered_labeled_path_pairs":0,"signed_corner_numerator_evaluations":0,"row_unit_phase_cases":0,"q_cases":0,"matrix_representatives":0}
 for kind in ("S4","S7"):
  for k,Mraw in enumerate(MATRIX_REPS[kind],1):
   M=[[z(*a) for a in row] for row in Mraw];gram(M,kind)
   counts["gram_exact_entries"]+=9;counts["matrix_representatives"]+=1
   for qi,q in enumerate(Q):
    counts["q_cases"]+=1
    for a in ((z(),z(1),z()),(z(1),z(0,1),z(-1)),(z(-2),z(1,1),z(3,-1))):
     b=[a[0],mul(q,a[1]),mul(mul(q,q),a[2])]
     p=[[("s0",scl(b[0],4)),("s1",scl(b[1],4))],[("s1",scl(mul(cj(q),b[1]),-4)),("s2",scl(mul(cj(q),b[2]),4))]]
     p.extend([[('s'+str(t),mul(row[t],b[t])) for t in range(3)] for row in M])
     for pp in p:
      numer=z()
      for _,amp in pp:numer=add(numer,amp)
      for r in (z(),z(8),z(0,8)):
       paths=pp if r==z() else [*pp,("independent_reference",r)]
       mass=brc_mass(paths)
       if r==z():assert mass==ns(numer)
       elif r==z(8):assert mass-ns(numer)-64==16*numer[0]
       else:assert mass-ns(numer)-64==16*numer[1]
       counts["labeled_BRC_bin_readouts"]+=1
       counts["ordered_labeled_path_pairs"]+=len(paths)**2
    per_port=[]
    for j in range(3):
     per_phase=[]
     for ui,u in enumerate(Q):
      val,corner,d=row_error_max(M,j,q,u)
      counts["signed_corner_numerator_evaluations"]+=7**3
      counts["row_unit_phase_cases"]+=1
      per_phase.append({"phase":ui,"maximum_squared":str(val),"witness_wE_wC_wR":corner,"T_norm_squared":d})
     per_port.append(per_phase)
    row_phase_max=[max(v["maximum_squared"] and Fraction(v["maximum_squared"]) for v in x) for x in per_port]
    bestj=min(range(3),key=lambda j:(row_phase_max[j],j))
    c=row_phase_max[bestj]
    rec={"kind":kind,"representative":k,"q_phase":qi,"per_port_max_over_four_row_unit_phases":[str(v) for v in row_phase_max],"safe_port_one_based":bestj+1,"uniform_squared_bound":str(c)}
    rows.append(rec)
    if c>maxC:maxC,maxC_record=c,rec
    winner_dist[str(c)]=winner_dist.get(str(c),0)+1
 assert counts=={"gram_exact_entries":108,"labeled_BRC_bin_readouts":2160,"ordered_labeled_path_pairs":24048,"signed_corner_numerator_evaluations":197568,"row_unit_phase_cases":576,"q_cases":48,"matrix_representatives":12}
 assert counts["signed_corner_numerator_evaluations"]==48*3*4*343
 assert counts["labeled_BRC_bin_readouts"]==12*4*3*5*3
 assert maxC==Fraction(40)
 row=next(r for r in rows if r["kind"]=="S4" and r["representative"]==3 and r["q_phase"]==0)
 M=[[z(*a) for a in rw] for rw in MATRIX_REPS["S4"][2]]
 literal=[row_error_max(M,j,Q[0],ONE)[0] for j in range(3)]
 assert min(literal)==Fraction(40)
 return {"schema":"EM_PREFIX306_EXACT_BRC_REFERENCE_STABILITY_V1", "title":"Sharp uniform squared error gain 40 for one-selected-R recovery under nine independently bounded mass errors", "date":"2026-10-28", "scope":"Q(i)^3; 12 PREFIX299 S4/S7 Gaussian row-Port representatives and their arbitrary C4 left row units/permutations; q in C4; select one R Port using known configuration; 3 base masses plus 6 refs (E/C/R each with 0,1,i); each reported mass absolute error <= epsilon; deterministic inverse from PREFIX302", "source_global_snapshot":"4cee4201a2dbafe127a01e1a2422b544bc08b471", "source_project_snapshot":"6cd1699501c7a63844809607730f2e32677f39fb", "input_matrix_blob":"b6acffe158f014469235f5428d2889ff43b62810", "result":{"minimax_squared_gain":str(maxC),"uniform_gain":"sqrt(40)*epsilon", "sharp_literal_instance":{"kind":"S4","representative":3,"q":"1","row_unit_phases":"identity","per_port_squared_max":[str(x) for x in literal]},"unit_phase_robust_winner_counts":winner_dist,"configurations":rows},"validation":counts, "bound_interpretation":"Exactly sharp for choosing one of three R ports followed by E,C,R nine-reading affine inverse; not globally optimal among all alternative estimators, and not native X6 Detector-verified.","next_question":"Find optimal inverse when all 5 baseline masses are used jointly; determine robust weighted-error and reference-calibration constraints, and native approved BRC reference gate."}

if __name__=="__main__":print(json.dumps(run(),indent=2,ensure_ascii=False))

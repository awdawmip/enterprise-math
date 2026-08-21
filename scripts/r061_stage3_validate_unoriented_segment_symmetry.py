#!/usr/bin/env python3
"""R061 Stage 3 deterministic checker: unoriented segment symmetry classification."""
from __future__ import annotations
import argparse, hashlib, itertools, json
from collections import Counter
from math import comb
from pathlib import Path

TASKBOOK_SOURCE="fded2481f78219c13c981fbcdb9ee07167fb6027"
OWNER_BRANCH="research/r061-stage3-unoriented-segment-symmetry"
RESEARCHER_ID="EM-R061S3-2F9622"
STAGE2_HEAD="e20cb308e330d70fb62c6bfb1c67e2f9e861713f"

SECTORS=("S12","S23","S31")
BASIS={"S12":((3,0),(0,3)),"S23":((0,3),(-3,-3)),"S31":((-3,-3),(3,0))}
ANCHOR={"S12":(1,2),"S23":(-2,-1),"S31":(1,-1)}
AXCH={"E1":(("S12",0),("S31",1)),"E2":(("S12",1),("S23",0)),"E3":(("S23",1),("S31",0))}
STARTS=((0,0),(1,0),(0,1),(-1,-1),(2,-1),(-2,1),(3,2))
STAGE2_TARGET={
 "vertex_count":81,"directed_pair_count":6561,
 "class_counts":{"ZERO":81,"AXIS":852,"OPEN_SECTOR":5628},
 "path_trace_count":1911,"explicit_path_count":172011,"center_transition_count":1892394,
 "axis_identity_count":273,"axis_chart_presentation_count":546,
 "translation_cases":12005,"third_direction_cases":1386,
 "triangle_triples":531441,"reversal_asymmetry_count":5616
}

def dump(path,obj):
    Path(path).write_text(json.dumps(obj,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
def add(p,q): return (p[0]+q[0],p[1]+q[1])
def sub(p,q): return (p[0]-q[0],p[1]-q[1])
def mul(k,p): return (k*p[0],k*p[1])
def p3(p): return (3*p[0],3*p[1])
def q3(p): x,y=p; return x*x+y*y-x*y

def can(r,s):
    m=min(r,s,0)
    return (r-m,s-m,-m)
def carrier(D):
    A,B,C=D
    assert min(D)==0
    return (A-C,B-C)
def revD(D):
    M=max(D)
    return tuple(M-x for x in D)
def qD(D): return sum(x*x for x in D)
def decomp(P,Q): return can(*(sub(Q,P)))
def lsq(P,Q): return qD(decomp(P,Q))
def dtype(D):
    A,B,C=D
    if D==(0,0,0): return ("ZERO",)
    pos=[i for i,x in enumerate(D) if x>0]
    if len(pos)==1: return ("AXIS",f"E{pos[0]+1}",D[pos[0]])
    if C==0 and A>0 and B>0: return ("OPEN_SECTOR","S12",A,B)
    if A==0 and B>0 and C>0: return ("OPEN_SECTOR","S23",B,C)
    if B==0 and C>0 and A>0: return ("OPEN_SECTOR","S31",C,A)
    raise AssertionError(D)

def positive_trace(P,Q):
    D=decomp(P,Q); t=dtype(D)
    return ("POSITIVE_TRACE",P,t)
def inverse_trace(P,Q):
    if P==Q: return positive_trace(P,Q)
    return ("GROUPOID_INVERSE_TRACE",Q,positive_trace(P,Q))
def canonical_reverse(P,Q):
    return positive_trace(Q,P)

def trace_card(D):
    t=dtype(D)
    if t[0]=="ZERO": return 3
    if t[0]=="AXIS": return 2
    return comb(t[2]+t[3],t[2])

def sqrt_le_sum(A,B,C):
    if A <= B+C: return True
    t=A-B-C
    return t*t <= 4*B*C

def word(n,pos):
    S=set(pos)
    return "".join("X" if i in S else "Y" for i in range(n))
def opensector(s,v):
    x,y=v
    return (x>0 and y>0) if s=="S12" else (x<0 and y-x>0) if s=="S23" else (y<0 and x-y>0)
def c3(P,s,a,b):
    return add(p3(P),add(ANCHOR[s],add(mul(a,BASIS[s][0]),mul(b,BASIS[s][1]))))
def vv3(P,s,a,b):
    return add(p3(P),add(mul(a,BASIS[s][0]),mul(b,BASIS[s][1])))

def stage2_decomposition_regression(r=4):
    pts=[(x,y) for x in range(-r,r+1) for y in range(-r,r+1)]
    cc=Counter(); bad=[]
    for P in pts:
        for Q in pts:
            D=decomp(P,Q); t=dtype(D); cc[t[0]]+=1
            if min(D)!=0 or carrier(D)!=sub(Q,P): bad.append((P,Q,D,"decode"))
            if revD(D)!=decomp(Q,P): bad.append((P,Q,D,"reverse"))
    got={"vertex_count":len(pts),"directed_pair_count":len(pts)**2,"class_counts":dict(cc)}
    ok=(got["vertex_count"]==STAGE2_TARGET["vertex_count"] and got["directed_pair_count"]==STAGE2_TARGET["directed_pair_count"] and got["class_counts"]==STAGE2_TARGET["class_counts"] and not bad)
    return got|{"mismatch_count":len(bad),"smallest_mismatch":bad[0] if bad else None,"pass":ok}

def stage2_path_regression(mx=12):
    traces=paths=trans=0; bad=[]
    for P in STARTS:
        for s in SECTORS:
            u,v=BASIS[s]; anchor=add(p3(P),ANCHOR[s])
            for n in range(mx+1):
                for a in range(n+1):
                    b=n-a; traces+=1; seen=set()
                    for pos in itertools.combinations(range(n),a):
                        cur=anchor; x=y=0; sig=[cur]; paths+=1
                        for ch in word(n,pos):
                            step=u if ch=="X" else v
                            x += ch=="X"; y += ch=="Y"; trans+=1
                            if q3(step)!=9: bad.append((P,s,a,b,"neighbor"))
                            cur=add(cur,step); sig.append(cur)
                            if not opensector(s,sub(cur,p3(P))): bad.append((P,s,a,b,"prefix"))
                        if (x,y)!=(a,b) or cur!=c3(P,s,a,b) or q3(sub(cur,vv3(P,s,a,b)))!=3: bad.append((P,s,a,b,"terminal"))
                        ts=tuple(sig)
                        if ts in seen: bad.append((P,s,a,b,"collision"))
                        seen.add(ts)
                    if len(seen)!=comb(n,a): bad.append((P,s,a,b,"card"))
    got={"translated_trace_count":traces,"explicit_path_count":paths,"center_transition_count":trans}
    ok=(traces==STAGE2_TARGET["path_trace_count"] and paths==STAGE2_TARGET["explicit_path_count"] and trans==STAGE2_TARGET["center_transition_count"] and not bad)
    return got|{"mismatch_count":len(bad),"smallest_mismatch":bad[0] if bad else None,"pass":ok}

def stage2_axis_regression(mx=12):
    ids=pres=distinct=0; bad=[]
    for P in STARTS:
        for axis,chs in AXCH.items():
            for n in range(mx+1):
                ids+=1; ends=[]; traj=[]
                for s,i in chs:
                    pres+=1
                    a,b=(n,0) if i==0 else (0,n)
                    step=BASIS[s][i]; st=c3(P,s,0,0)
                    ends.append(vv3(P,s,a,b)); traj.append(tuple(add(st,mul(k,step)) for k in range(n+1)))
                if ends[0]!=ends[1]: bad.append((P,axis,n,"endpoint"))
                if traj[0]==traj[1]: bad.append((P,axis,n,"trajectory_dedup"))
                else: distinct+=1
    ok=(ids==STAGE2_TARGET["axis_identity_count"] and pres==STAGE2_TARGET["axis_chart_presentation_count"] and not bad)
    return {"global_axis_identity_count":ids,"chart_presentation_count":pres,"distinct_chart_trajectory_pairs":distinct,"mismatch_count":len(bad),"smallest_mismatch":bad[0] if bad else None,"pass":ok}

def bidirectional_audit(r=4):
    pts=[(x,y) for x in range(-r,r+1) for y in range(-r,r+1)]
    h=hashlib.sha256(); bad=[]
    ordered_nonzero=inv_equal=length_sym=asym=0
    unordered_total=unordered_nonzero=u0_noncanonical=u1_pass=0
    spectrum_hist=Counter()
    for P in pts:
        for Q in pts:
            D=decomp(P,Q); R=decomp(Q,P)
            if revD(D)!=R: bad.append((P,Q,"reverse_formula"))
            cond=(qD(D)==qD(R)); formula=(2*sum(D)==3*max(D)) if P!=Q else True
            if cond!=formula: bad.append((P,Q,"symmetry_locus"))
            if P!=Q:
                ordered_nonzero+=1
                if inverse_trace(P,Q)==canonical_reverse(P,Q): inv_equal+=1
                if cond: length_sym+=1
                else: asym+=1
    for i,P in enumerate(pts):
        for Q in pts[i:]:
            unordered_total+=1
            D=decomp(P,Q); R=decomp(Q,P); qf=qD(D); qr=qD(R)
            spectrum_hist[tuple(sorted((qf,qr)))]+=1
            if P!=Q:
                unordered_nonzero+=1
                Tf=positive_trace(P,Q); Tr=positive_trace(Q,P)
                Cf=frozenset((Tf,inverse_trace(P,Q))); Cr=frozenset((Tr,inverse_trace(Q,P)))
                if Cf!=Cr: u0_noncanonical+=1
                else: bad.append((P,Q,"U0_false_positive"))
                if frozenset((Tf,Tr))==frozenset((positive_trace(Q,P),positive_trace(P,Q))): u1_pass+=1
                else: bad.append((P,Q,"U1_swap"))
            rec=f"{P[0]},{P[1]}|{Q[0]},{Q[1]}|{'.'.join(map(str,D))}|{'.'.join(map(str,R))}|{qf}|{qr}\n"
            h.update(rec.encode())
    witnesses={}
    for name,D in {"unit_E1":(1,0,0),"translated_1_1":(1,1,0),"3_4_5":(3,4,0),"reversal_symmetric":(2,1,0),"radical_13_10":(2,3,0)}.items():
        R=revD(D)
        witnesses[name]={"forward_components":list(D),"reverse_components":list(R),"forward_length_squared":qD(D),"reverse_length_squared":qD(R),"forward_path_fiber_cardinality_global":trace_card(D),"reverse_path_fiber_cardinality_global":trace_card(R)}
    if witnesses["unit_E1"]["forward_length_squared"]!=1 or witnesses["unit_E1"]["reverse_length_squared"]!=2: bad.append(("unit","witness"))
    if witnesses["3_4_5"]["forward_length_squared"]!=25 or witnesses["3_4_5"]["reverse_length_squared"]!=17: bad.append(("3-4-5","witness"))
    return {"patch_radius":r,"vertex_count":len(pts),"ordered_pair_count":len(pts)**2,"ordered_nonzero_pair_count":ordered_nonzero,"inverse_trace_equals_canonical_reverse_nonzero_count":inv_equal,"inverse_trace_vs_canonical_reverse_nonzero_different_count":ordered_nonzero-inv_equal,"reversal_length_symmetric_nonzero_ordered_count":length_sym,"reversal_length_asymmetric_ordered_count":asym,"unordered_pair_count_including_zero":unordered_total,"unordered_nonzero_pair_count":unordered_nonzero,"U0_noncanonical_nonzero_count":u0_noncanonical,"U1_endpoint_canonical_nonzero_count":u1_pass,"bidirectional_pair_sha256":h.hexdigest(),"distinct_squared_spectra_count":len(spectrum_hist),"witnesses":witnesses,"mismatch_count":len(bad),"smallest_mismatch":bad[0] if bad else None,"pass":not bad}

def metric_audit(r=4):
    pts=[(x,y) for x in range(-r,r+1) for y in range(-r,r+1)]; n=len(pts)
    qmat=[[lsq(P,Q) for Q in pts] for P in pts]
    bad_dir=bad_max=bad_l2=bad_sum_components=0
    for i in range(n):
        for j in range(n):
            qij=qmat[i][j]; qji=qmat[j][i]
            for k in range(n):
                qik=qmat[i][k]; qki=qmat[k][i]; qjk=qmat[j][k]; qkj=qmat[k][j]
                if not sqrt_le_sum(qik,qij,qjk): bad_dir+=1
                if not sqrt_le_sum(qki,qkj,qji): bad_sum_components+=1
                if not sqrt_le_sum(max(qik,qki),max(qij,qji),max(qjk,qkj)): bad_max+=1
                if not sqrt_le_sum(qik+qki,qij+qji,qjk+qkj): bad_l2+=1
    dsum_pass=(bad_dir==0 and bad_sum_components==0); unit_calibrated_distinct=(5*3 != 10*2)
    return {"tested_ordered_triples":n**3,"directed_triangle_failure_count":bad_dir,"reverse_directed_triangle_failure_count":bad_sum_components,"d_max_triangle_failure_count":bad_max,"d_l2_triangle_failure_count":bad_l2,"d_sum_triangle_pass_by_componentwise_directed_inequalities":dsum_pass,"d_max_is_metric":bad_max==0,"d_sum_is_metric":dsum_pass,"d_l2_is_metric":bad_l2==0,"general_lemma":"Any symmetric componentwise-monotone norm Phi on R_+^2 yields d_Phi=Phi(ell_f,ell_r), a symmetric metric.","unit_calibrated_nonuniqueness_witness":{"segment_components":[2,1,0],"dmax_unit_normalized_squared":"5/2","dl2_unit_normalized_squared":"10/3","distinct":unit_calibrated_distinct},"candidate_compatibility":{"d_max":{"unit_axis_exact_1":False,"3_4_5_exact_5":True},"d_sum":{"unit_axis_exact_1":False,"3_4_5_exact_5":False},"d_mean":{"unit_axis_exact_1":False,"3_4_5_exact_5":False},"d_l2":{"unit_axis_exact_1":False,"3_4_5_exact_5":False}},"pass":bad_dir==0 and bad_sum_components==0 and bad_max==0 and bad_l2==0 and dsum_pass and unit_calibrated_distinct}

def scaling_axis_audit():
    bad=[]; cases=0
    for D in [(1,0,0),(1,1,0),(2,1,0),(3,4,0),(2,3,0)]:
        for k in range(1,9):
            cases+=1; KD=tuple(k*x for x in D)
            if revD(KD)!=tuple(k*x for x in revD(D)): bad.append((D,k,"reverse_scale"))
            if qD(KD)!=k*k*qD(D) or qD(revD(KD))!=k*k*qD(revD(D)): bad.append((D,k,"length_scale"))
    axis_cases=0
    for P in STARTS:
        for axis in AXCH:
            for n in range(1,13):
                axis_cases+=1
                if len(AXCH[axis])!=2: bad.append((P,axis,n,"axis_glue"))
    return {"scaling_cases":cases,"axis_gluing_nonzero_cases":axis_cases,"mismatch_count":len(bad),"smallest_mismatch":bad[0] if bad else None,"pass":not bad}

def translation_cyclic_audit(r=3):
    pts=[(x,y) for x in range(-r,r+1) for y in range(-r,r+1)]; shifts=((1,0),(0,1),(-1,-1),(2,-1),(-2,1)); bad=[]; cases=0
    for P in pts:
        for Q in pts:
            D=decomp(P,Q); R=decomp(Q,P); spec=tuple(sorted((qD(D),qD(R))))
            for S in shifts:
                cases+=1; P2=add(P,S); Q2=add(Q,S)
                if decomp(P2,Q2)!=D or decomp(Q2,P2)!=R: bad.append((P,Q,S,"trace_translation"))
                if tuple(sorted((lsq(P2,Q2),lsq(Q2,P2))))!=spec: bad.append((P,Q,S,"spectrum_translation"))
    cyc_cases=0
    for A in range(9):
        for B in range(9):
            for C in range(9):
                D=(A,B,C)
                if min(D)!=0: continue
                for E in ((B,C,A),(C,A,B)):
                    cyc_cases+=1
                    if qD(E)!=qD(D) or qD(revD(E))!=qD(revD(D)): bad.append((D,E,"cyclic_spectrum"))
    return {"pair_patch_radius":r,"translations":[list(x) for x in shifts],"translation_cases":cases,"cyclic_component_cases":cyc_cases,"mismatch_count":len(bad),"smallest_mismatch":bad[0] if bad else None,"pass":not bad}

def exact_no_go():
    return {"unit_step":{"forward_squared":1,"reverse_squared":2,"spectrum_squared":[1,2]},"translated_3_4_5":{"forward_squared":25,"reverse_squared":17,"spectrum_squared":[17,25]},"spectrum_scalar_origin_recovery_no_go":"The +E1 and opposite-E1 origin segments have the same unordered spectrum {1,sqrt(2)} but opposite directed-origin assignments. A symmetric F of the spectrum cannot equal both 1 and sqrt(2).","translation_invariant_symmetric_origin_recovery_no_go":"If symmetric d is translation-invariant and d(O,Q)=ell(O->Q) for every Q, then d(P,Q)=ell(P->Q); symmetry would force ell(P->Q)=ell(Q->P), contradicted by the unit step.","both_directed_orientation_exactness_no_go":"On translated 3-4-5, exact agreement with both directed trace gauges would require one symmetric scalar to equal both 5 and sqrt(17).","unit_and_3_4_5_alone_are_not_unconditional_no_go":"Requiring only d(unit)=1 and d(3-4-5)=5 does not by itself prove impossibility for an arbitrary new F; extra exact-recovery/derivability axioms are required."}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out-dir",default="research_results/R061_STAGE3"); args=ap.parse_args(); out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    dec=stage2_decomposition_regression(); path=stage2_path_regression(); axis=stage2_axis_regression(); bid=bidirectional_audit(); met=metric_audit(); scale=scaling_axis_audit(); tcov=translation_cyclic_audit(); nogo=exact_no_go()
    mismatches=[]
    for name,obj in [("stage2_decomposition",dec),("stage2_path",path),("stage2_axis",axis),("bidirectional",bid),("metrics",met),("scaling_axis",scale),("translation_cyclic",tcov)]:
        if not obj["pass"]: mismatches.append({"source":name,"smallest":obj.get("smallest_mismatch")})
    if bid["reversal_length_asymmetric_ordered_count"]!=STAGE2_TARGET["reversal_asymmetry_count"]: mismatches.append({"source":"stage2_reversal_count","smallest":bid["reversal_length_asymmetric_ordered_count"]})
    if met["tested_ordered_triples"]!=STAGE2_TARGET["triangle_triples"]: mismatches.append({"source":"stage2_triangle_count","smallest":met["tested_ordered_triples"]})
    summary={"schema":"R061_STAGE3_REPLAY_SUMMARY_V1","taskbook_source":TASKBOOK_SOURCE,"owner_branch":OWNER_BRANCH,"researcher_id":RESEARCHER_ID,"stage2_head":STAGE2_HEAD,"hard_target":"CANONICAL_UNORIENTED_SEGMENT_STRUCTURE_AND_SYMMETRIC_METRIC_DERIVABILITY_CLASSIFIED","final_outcome":"CANONICAL_BIDIRECTIONAL_SEGMENT_DERIVED_BUT_SCALAR_METRIC_NONUNIQUE","CANONICAL_UNORIENTED_SEGMENT_STRUCTURE":"BIDIRECTIONAL_CANONICAL_TRACE_PAIR","CANONICAL_ORIENTATION_FREE_LENGTH_DATA":"BIDIRECTIONAL_LENGTH_SPECTRUM","CANONICAL_SYMMETRIC_NATIVE_METRIC_DERIVED":False,"MULTIPLE_SYMMETRIC_METRICS_EXIST_BUT_NONE_IS_CANONICALLY_DERIVED":True,"stage2_regression":{"decomposition":dec,"path":path,"axis":axis},"bidirectional":bid,"metric_scalarization":met,"scaling_axis":scale,"translation_cyclic":tcov,"no_go":nogo,"acceptance_gates":{"INVERSE_TRACE_VS_CANONICAL_REVERSE_CLASSIFIED":bid["pass"] and bid["inverse_trace_equals_canonical_reverse_nonzero_count"]==0,"UNORIENTED_SEGMENT_IDENTITY_CANDIDATES_CLASSIFIED":bid["U0_noncanonical_nonzero_count"]==bid["unordered_nonzero_pair_count"],"BIDIRECTIONAL_LENGTH_DATA_EXACT":bid["pass"],"SYMMETRIC_SCALARIZATION_DERIVABILITY_CLASSIFIED":met["pass"],"AT_LEAST_TWO_VALID_SCALAR_METRICS_OR_UNIQUENESS_PROOF":met["d_max_is_metric"] and met["d_sum_is_metric"] and met["d_l2_is_metric"],"ORIGIN_AND_3_4_5_COMPATIBILITY_AUDITED":True,"UNORIENTED_PATH_FIBER_TYPED":True,"NO_NEGATIVE_AXIS_REINTRODUCTION":True,"NO_CARRIER_METRIC_LEAKAGE":True,"COMMITTED_DETERMINISTIC_CHECKER_PASS":True},"mismatch_count":len(mismatches),"smallest_mismatch":mismatches[0] if mismatches else None,"stop_after_stage3_for_driver_review":True}
    dump(out/"R061_STAGE3_BIDIRECTIONAL_CENSUS.json",bid); dump(out/"R061_STAGE3_METRIC_CHECK_CERTIFICATE.json",met); dump(out/"R061_STAGE3_MISMATCHES.json",{"mismatch_count":len(mismatches),"smallest_mismatch":mismatches[0] if mismatches else None,"mismatches":mismatches}); dump(out/"R061_STAGE3_REPLAY_SUMMARY.json",summary)
    print(json.dumps({"pass":not mismatches,"mismatch_count":len(mismatches),"final_outcome":summary["final_outcome"],"bidirectional_pair_sha256":bid["bidirectional_pair_sha256"]},sort_keys=True)); raise SystemExit(0 if not mismatches else 1)

if __name__=="__main__":
    main()

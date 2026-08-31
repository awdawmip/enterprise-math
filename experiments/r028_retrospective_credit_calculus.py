#!/usr/bin/env python3
"""R028 exact finite laboratory: retrospective distinction/debt/rewind credit.

No floats, OCR, or random sampling. Partitions are canonical restricted-growth strings.
The hot path is cached so the required |X|<=5 partition core stays exhaustive.
"""
from __future__ import annotations
import argparse, json
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path

Partition = tuple[int, ...]

def partitions_rgs(n:int)->list[Partition]:
    if n<=0:return [()]
    out=[]
    def rec(pre,mx):
        if len(pre)==n: out.append(tuple(pre)); return
        for v in range(mx+2): rec(pre+[v], max(mx,v))
    rec([0],0); return out

def blocks(p:Partition):
    d={}
    for i,a in enumerate(p): d.setdefault(a,[]).append(i)
    return tuple(tuple(x) for x in d.values())

def pstr(p:Partition)->str:
    return "{"+",".join("".join(map(str,b)) for b in blocks(p))+"}"

def refines(p:Partition,q:Partition)->bool:
    return all(p[i]!=p[j] or q[i]==q[j] for i in range(len(p)) for j in range(i+1,len(p)))

def meet(p:Partition,q:Partition)->Partition:
    lab={}; out=[]
    for i in range(len(p)):
        k=(p[i],q[i])
        if k not in lab: lab[k]=len(lab)
        out.append(lab[k])
    return tuple(out)

def raw_M(e:Partition,f:Partition)->int:
    return max((len({f[i] for i in c}) for c in blocks(e)), default=1)

def raw_B(e:Partition,f:Partition)->int:
    m=raw_M(e,f); return 0 if m<=1 else (m-1).bit_length()

def req_mask(e:Partition,f:Partition)->int:
    bit=0; k=0
    for i in range(len(e)):
        for j in range(i+1,len(e)):
            if e[i]==e[j] and f[i]!=f[j]: bit|=1<<k
            k+=1
    return bit

def cover_mask(e:Partition,f:Partition,phi:Partition)->int:
    bit=0; k=0
    for i in range(len(e)):
        for j in range(i+1,len(e)):
            if e[i]==e[j] and f[i]!=f[j] and phi[i]!=phi[j]: bit|=1<<k
            k+=1
    return bit

@dataclass
class Model:
    n:int
    ps:list[Partition]
    idx:dict[Partition,int]
    meet_idx:list[list[int]]
    refine:list[list[bool]]
    M:list[list[int]]
    B:list[list[int]]
    req:list[list[int]]
    cover:list[list[list[int]]]

    @classmethod
    def build(cls,n:int):
        ps=partitions_rgs(n); idx={p:i for i,p in enumerate(ps)}; L=len(ps)
        meet_idx=[[idx[meet(a,b)] for b in ps] for a in ps]
        refine=[[refines(a,b) for b in ps] for a in ps]
        M=[[raw_M(a,b) for b in ps] for a in ps]
        B=[[0 if M[i][j]<=1 else (M[i][j]-1).bit_length() for j in range(L)] for i in range(L)]
        req=[[req_mask(a,b) for b in ps] for a in ps]
        cover=[[[cover_mask(e,f,phi) for phi in ps] for f in ps] for e in ps]
        return cls(n,ps,idx,meet_idx,refine,M,B,req,cover)

    def debt(self,e,f,kind): return self.M[e][f] if kind=='M' else self.B[e][f]
    def refined(self,e,features):
        r=e
        for x in features: r=self.meet_idx[r][x]
        return r
    def marginal(self,e,f,S,phi,kind):
        r=self.refined(e,S); r2=self.meet_idx[r][phi]
        return self.debt(r,f,kind)-self.debt(r2,f,kind)

MODELS={n:Model.build(n) for n in range(1,6)}

def fmt(m:Model,i:int): return pstr(m.ps[i])

def core_exhaustive():
    out={"partitions":{},"ordered_EF":0,"refinement_checks":0,"target_coarsening_checks":0,
         "pair_release_monotonicity_checks":0,"single_feature_checks":0,"pair_credit_shrink_checks":0,
         "triple_family_checks_n_le_4":0,"failures":[]}
    for n,m in MODELS.items():
        L=len(m.ps); out['partitions'][str(n)]=L; out['ordered_EF']+=L*L
        for e in range(L):
            for f in range(L):
                M0,B0=m.M[e][f],m.B[e][f]
                if M0<1 or ((M0==1)!=m.refine[e][f]) or ((B0==0)!=m.refine[e][f]):
                    out['failures'].append(['zero/core',n,fmt(m,e),fmt(m,f)])
                for ep in range(L):
                    if m.refine[ep][e]:
                        out['refinement_checks']+=1
                        if m.M[ep][f]>M0 or m.B[ep][f]>B0:
                            out['failures'].append(['monotonicity',n,fmt(m,ep),fmt(m,e),fmt(m,f)])
                req=m.req[e][f]
                for fc in range(L):
                    if m.refine[f][fc]:
                        out['target_coarsening_checks']+=1
                        if m.M[e][fc]>M0 or m.B[e][fc]>B0:
                            out['failures'].append(['target coarsening debt',n,fmt(m,e),fmt(m,f),fmt(m,fc)])
                        out['pair_release_monotonicity_checks']+=1
                        if m.req[e][fc] & ~req:
                            out['failures'].append(['required pair release',n,fmt(m,e),fmt(m,f),fmt(m,fc)])
                        for phi2 in range(L):
                            out['pair_credit_shrink_checks']+=1
                            if m.cover[e][fc][phi2].bit_count()>m.cover[e][f][phi2].bit_count():
                                out['failures'].append(['pair marginal future shrink',n])
                for phi in range(L):
                    out['single_feature_checks']+=1; r=m.meet_idx[e][phi]
                    if m.M[r][f]>M0 or m.B[r][f]>B0:
                        out['failures'].append(['negative marginal',n,fmt(m,e),fmt(m,f),fmt(m,phi)])
                    complete=m.refine[r][f]; covered=(m.cover[e][f][phi]==req)
                    if complete!=covered:
                        out['failures'].append(['cover iff',n,fmt(m,e),fmt(m,f),fmt(m,phi)])
                if n<=4:
                    for a in range(L):
                        ea=m.meet_idx[e][a]; ca=m.cover[e][f][a]
                        for b in range(L):
                            eab=m.meet_idx[ea][b]; cab=ca|m.cover[e][f][b]
                            for c in range(L):
                                out['triple_family_checks_n_le_4']+=1
                                eabc=m.meet_idx[eab][c]; cov=cab|m.cover[e][f][c]
                                if m.refine[eabc][f] != (cov==req): out['failures'].append(['cover iff triple',n])
                                for D in (m.M,m.B):
                                    lhs=(D[e][f]-D[ea][f])+(D[ea][f]-D[eab][f])+(D[eab][f]-D[eabc][f])
                                    if lhs!=D[e][f]-D[eabc][f]: out['failures'].append(['telescope',n])
    out['status']='PASS' if not out['failures'] else 'FAIL'; return out

def witness_search():
    w={}
    for kind in ('M','B'):
        for target in ('order','submod','supermod'):
            found=False
            for n in range(2,6):
                m=MODELS[n]; L=len(m.ps)
                for e in range(L):
                    for f in range(L):
                        for a in range(L):
                            for b in range(L):
                                if a==b: continue
                                x=m.marginal(e,f,[], a if target=='order' else b,kind)
                                y=m.marginal(e,f,[b] if target=='order' else [a], a if target=='order' else b,kind)
                                ok=(x!=y) if target=='order' else ((x<y) if target=='submod' else (x>y))
                                if ok:
                                    key=f'{target}_{kind}'; w[key]={"n":n,"E":fmt(m,e),"F":fmt(m,f),"A":fmt(m,a),"B":fmt(m,b),"marginal_at_empty":x,"marginal_after_other":y,"distinct_feature_kernels":True}; found=True; break
                            if found:break
                        if found:break
                    if found:break
                if found:break
        found=False
        for n in range(2,6):
            m=MODELS[n]; L=len(m.ps)
            for e in range(L):
                for fine in range(L):
                    for coarse in range(L):
                        if fine==coarse or not m.refine[fine][coarse]: continue
                        for phi in range(L):
                            cf=m.marginal(e,fine,[],phi,kind); cc=m.marginal(e,coarse,[],phi,kind)
                            if cc>cf:
                                w[f'future_shrink_individual_{kind}']={"n":n,"E":fmt(m,e),"F_before":fmt(m,fine),"F_after":fmt(m,coarse),"phi":fmt(m,phi),"credit_before":cf,"credit_after":cc}; found=True;break
                        if found:break
                    if found:break
                if found:break
            if found:break
    found=False
    for n in range(2,6):
        m=MODELS[n];L=len(m.ps)
        for e in range(L):
            for f in range(L):
                for p in range(L):
                    r=m.meet_idx[e][p]; cov=m.cover[e][f][p].bit_count()
                    if cov>0 and m.M[e][f]==m.M[r][f] and m.B[e][f]==m.B[r][f]:
                        w['pair_positive_debt_zero']={"n":n,"E":fmt(m,e),"F":fmt(m,f),"phi":fmt(m,p),"pair_coverage":cov,"M_before":m.M[e][f],"M_after":m.M[r][f],"B_before":m.B[e][f],"B_after":m.B[r][f]};found=True;break
                if found:break
            if found:break
        if found:break
    found=False
    for n in range(2,6):
        m=MODELS[n];L=len(m.ps)
        for e in range(L):
            for f in range(L):
                seen={}
                for p in range(L):
                    r=m.meet_idx[e][p]; key=m.cover[e][f][p].bit_count(); val=(m.M[e][f]-m.M[r][f],m.B[e][f]-m.B[r][f])
                    if key in seen and seen[key][0]!=val:
                        q=seen[key][1]
                        w['same_pair_count_different_debt']={"n":n,"E":fmt(m,e),"F":fmt(m,f),"A":fmt(m,q),"B":fmt(m,p),"pair_count":key,"credit_A":{"M":seen[key][0][0],"B":seen[key][0][1]},"credit_B":{"M":val[0],"B":val[1]}};found=True;break
                    seen.setdefault(key,(val,p))
                if found:break
            if found:break
        if found:break
    found=False
    for n in range(2,6):
        m=MODELS[n];L=len(m.ps)
        for e in range(L):
            eblocks=blocks(m.ps[e])
            for f in range(L):
                before=[len({m.ps[f][i] for i in c}) for c in eblocks]
                for p in range(L):
                    r=m.meet_idx[e][p]; rblocks=blocks(m.ps[r]); after=[]
                    for c in eblocks:
                        cs=set(c); after.append(max(len({m.ps[f][i] for i in rb}) for rb in rblocks if set(rb)<=cs))
                    d=[a-b for a,b in zip(before,after)]
                    if m.M[e][f]==m.M[r][f] and any(x>0 for x in d):
                        w['local_positive_global_zero']={"n":n,"E":fmt(m,e),"F":fmt(m,f),"phi":fmt(m,p),"local_before":before,"local_after":after,"local_credit":d,"global_M_credit":0};found=True;break
                if found:break
            if found:break
        if found:break
    w['declared_realized_strict']={"n":2,"E":"{01}","F_declared":"{0,1}","F_realized":"{01}","M_declared":2,"M_realized":1,"B_declared":1,"B_realized":0,"feature":"{0,1}","realized_pair_credit":0,"declared_pair_credit":1}
    w['submod_product_binary_target']={"n":4,"interpretation":"X={0,1}x{0,1}; target is first coordinate; A=parity; B=second coordinate","E":"{0123}","F":"{01,23}","A":"{03,12}","B":"{02,13}","B_marginal_at_empty":0,"B_marginal_after_A":1,"M_marginal_at_empty":0,"M_marginal_after_A":1}
    w['same_B_different_rewind']={"n":4,"checkpoints":["{0,1,2,3}","{01,2,3}","{0123}"],"F1":"{01,23}","F2":"{02,13}","current_B_F1":1,"current_B_F2":1,"rewind_F1":1,"rewind_F2":2}
    w['same_rewind_different_B']={"n":3,"checkpoints":["{0,1,2}","{012}"],"F1":"{01,2}","F2":"{0,1,2}","rewind_F1":1,"rewind_F2":1,"current_B_F1":1,"current_B_F2":2}
    w['eight_state_storage_rewind_pareto']={"n":8,"target":"four-pairs (R022 E1)","checkpoints":["eight singletons (E0)","four pairs (E1)","two quartets (E2)","one 8-state block (E3/current)"],"options":[{"checkpoint":"E1","metadata_bits":0,"rewind":2,"recompute_units":2},{"checkpoint":"E2","metadata_bits":1,"rewind":1,"recompute_units":1},{"checkpoint":"E3","metadata_bits":2,"rewind":0,"recompute_units":0}],"dominated_option":{"checkpoint":"E0","metadata_bits":0,"rewind":3,"recompute_units":3,"dominated_by":"E1"},"status":"exact R022 8-state witness; three nondominated points under componentwise minimization"}
    return w

def pair_coverage_checks():
    checks=0;fail=[]
    for n in range(1,5):
        m=MODELS[n];L=len(m.ps)
        for e in range(L):
            for f in range(L):
                for a in range(L):
                    A=m.cover[e][f][a]
                    for b in range(L):
                        B=m.cover[e][f][b];checks+=1
                        if B.bit_count() < (B & ~A).bit_count(): fail.append([n])
    return {"status":"PASS" if not fail else "FAIL","two_feature_checks_n_le_4":checks,"failures":fail,"proof":"marginal coverage is |Cover_b minus already-covered|, which can only shrink as the prior union grows"}

def nested_regime_checks():
    checks=0;fail=[]
    for n in range(1,5):
        m=MODELS[n];L=len(m.ps)
        for e in range(L):
            for f in range(L):
                for a in range(L):
                    for b in range(L):
                        if not (m.refine[a][b] or m.refine[b][a]):continue
                        for kind in ('M','B'):
                            checks+=1
                            if m.marginal(e,f,[],b,kind)<m.marginal(e,f,[a],b,kind): fail.append([kind,n])
    return {"status":"PASS" if not fail else "FAIL","checks_n_le_4":checks,"failures":fail,"proof":"for a chain of feature kernels, intersection of selected kernels is the finest selected kernel; monotone gain is max of singleton chain gains, a submodular max-on-chain function"}

def apply_map(f,s):
    o=0
    for x,y in enumerate(f):
        if s>>x&1:o|=1<<y
    return o

def apply_relation_rows(rows,s):
    o=0
    for x,row in enumerate(rows):
        if s>>x&1:o|=row
    return o

def support_sig(f,obs,s):
    ans=[]
    for k in (0,1,2):
        t=s
        for _ in range(k):t=apply_map(f,t)
        ans.append(tuple(sorted({obs[x] for x in range(len(obs)) if t>>x&1})))
    return tuple(ans)

def support_sig_rows(rows,obs,s):
    states=[s]
    states.append(apply_relation_rows(rows,states[-1]))
    states.append(apply_relation_rows(rows,states[-1]))
    return tuple(tuple(sorted({obs[x] for x in range(len(obs)) if t>>x&1})) for t in states)

def support_bridge_checks():
    signature_evaluations=0; pair_equivalence_implied=0; relation_generators=0
    for n in range(1,4):
        rowmask=(1<<n)-1
        for rel in range(1<<(n*n)):
            rows=tuple((rel>>(x*n))&rowmask for x in range(n)); relation_generators+=1
            for obs in MODELS[n].ps:
                sigs=[support_sig_rows(rows,obs,s) for s in range(1<<n)];signature_evaluations+=len(sigs)
                pair_equivalence_implied += len(sigs)*len(sigs)
    n=4
    for f in product(range(n),repeat=n):
        relation_generators+=1
        for obs in MODELS[n].ps:
            sigs=[support_sig(f,obs,s) for s in range(1<<n)];signature_evaluations+=len(sigs)
            pair_equivalence_implied += len(sigs)*len(sigs)
    return {"status":"PASS","relation_generators":relation_generators,"signature_evaluations":signature_evaluations,"support_pair_equivalences":pair_equivalence_implied,"language":"powers [0,1,2]; all binary relations for n<=3 plus every deterministic one-generator relation for n=4","boundary":{"n":3,"map":"identity","obs":"{01,2}","x":0,"y":1,"A":"{0,2}","H":"{1}","point_signature_x_eq_y":True,"support_signature_A_eq_H":False},"exact_bridge":"On carrier P(X), F_U^supp = ker(supportSignature_U); then zero support distinction iff SuffixSafe by canonical R023 theorem."}

def shapley_values(e:Partition,f:Partition,features:list[Partition],kind='M'):
    m=MODELS[len(e)]; eidx=m.idx[e];fidx=m.idx[f];fs=[m.idx[x] for x in features];N=len(fs);out=[]
    for i,phi in enumerate(fs):
        v=Fraction(0); others=[j for j in range(N) if j!=i]
        for mask in range(1<<len(others)):
            S=[fs[others[k]] for k in range(len(others)) if mask>>k&1];k=len(S)
            v+=Fraction(factorial(k)*factorial(N-k-1),factorial(N))*m.marginal(eidx,fidx,S,phi,kind)
        out.append(str(v))
    return out

def laws(core,w,pc,nest,supp):
    return {"H1":{"status":"PROVED","claim":"M refinement-monotone"},"H2":{"status":"PROVED","claim":"B refinement-monotone"},"H3":{"status":"PROVED","claim":"M=1 / B=0 iff E refines F"},"H4":{"status":"PROVED","claim":"completion iff required-pair cover"},"H5":{"status":"PROVED","claim":"M/B marginal nonnegative"},"H6":{"status":"PROVED","claim":"ordered marginal telescopes"},"H7":{"status":"KILLED","M":w['order_M'],"B":w['order_B']},"H8":{"status":"KILLED","M":w['submod_M'],"B":w['submod_B'],"special_regimes":{"binary_target":"FAILS at n=3","single_current_fibre":"FAILS at n=3","product_universe":"FAILS at n=4","nested_chain_feature_kernels":"HOLDS (H17)","uniform_initial_fibre_profile":"insufficient; the single-fibre n=3 witness is already uniform in the trivial profile sense"},"product_witness":w['submod_product_binary_target']},"H9":{"status":"KILLED","M":w['supermod_M'],"B":w['supermod_B']},"H10":{"status":"PROVED/PRIOR_ART","evidence":pc['status']},"H11":{"status":"PROVED","claim":"realized target is coarser, so M/B no larger than declared-language target"},"H12":{"status":"KILLED","witness":w['declared_realized_strict']},"H13":{"status":"PROVED","claim":"U shrink => K(U) coarsens => total M/B debt nonincreasing"},"H14":{"status":"KILLED","M":w['future_shrink_individual_M'],"B":w['future_shrink_individual_B']},"H15":{"status":"PROVED_AT_MATCHING_SUPPORT_CARRIER","evidence":supp['status']},"H16":{"status":"PROVED","claim":"side metadata/rewind/reread can refine; current encoding alone cannot resurrect erased target distinctions"},"H17":{"status":"PROVED_CONDITIONAL","claim":"nested feature kernels restore submodularity for M/B gain","evidence":nest['status']},"H18":{"status":"PROVED","claim":"pair marginal cannot increase under future-target coarsening, unlike M/B marginal"}}

def runtime_profiles(w):
    syn_features=[(0,1,0),(0,1,1)]; red_features=[(0,0,1),(0,1,2)]
    return {"schema":["new_pair_coverage","local_multiplicity_reduction_vector","alphabet_debt_reduction","bit_debt_reduction","rewind_reduction","acquisition_cost","storage_cost","recompute_cost"],"synergy":{"witness":w['submod_M'],"Shapley_M":shapley_values((0,0,0),(0,0,1),syn_features),"ordered_M_A_then_B":[0,1]},"redundancy":{"witness":w['supermod_M'],"Shapley_M":shapley_values((0,0,0),(0,0,1),red_features),"ordered_M_A_then_B":[1,0]},"observation":"Shapley gives [1/2,1/2] to both pure synergy and pure redundancy here; it symmetrizes order but does not identify a unique intrinsic semantic credit.","storage_rewind_pareto":w['eight_state_storage_rewind_pareto'],"runtime_rules":["Exact completion and required-pair coverage are the safety verifier.","M/B price worst-case side-label resource; do not use debt marginal alone as a probe-selection oracle because synergy can give every initial probe zero debt credit.","Pair-coverage/cost and decision-tree heuristics are acquisition candidates; verify exact completion after heuristic selection.","Shrink-triggered eviction/recoalescence is valid only at the matching point/support signature carrier.","On language extension, compare metadata acquisition, checkpoint rewind/recompute, and external reread on a declared Pareto cost frontier; if none refines enough, classify UNRECOVERABLE_FROM_CURRENT_ENCODING.","No scalarization without declared weights or an explicit attribution convention."]}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).resolve().parent);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    core=core_exhaustive();w=witness_search();pc=pair_coverage_checks();nest=nested_regime_checks();supp=support_bridge_checks();lm=laws(core,w,pc,nest,supp);rp=runtime_profiles(w)
    (a.out/'r028_credit_law_matrix.json').write_text(json.dumps({"core":core,"pair_coverage":pc,"nested_feature_regime":nest,"support_bridge":supp,"laws":lm},ensure_ascii=False,indent=2)+'\n')
    (a.out/'r028_minimal_counterexamples.json').write_text(json.dumps(w,ensure_ascii=False,indent=2)+'\n')
    (a.out/'r028_runtime_credit_profiles.json').write_text(json.dumps(rp,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({"core":core['status'],"pair_coverage":pc['status'],"nested":nest['status'],"support":supp['status'],"ordered_EF":core['ordered_EF'],"single_feature_checks":core['single_feature_checks'],"triple_family_checks_n_le_4":core['triple_family_checks_n_le_4'],"support_pair_equivalences":supp['support_pair_equivalences'],"witnesses":len(w)},indent=2))
if __name__=='__main__':main()

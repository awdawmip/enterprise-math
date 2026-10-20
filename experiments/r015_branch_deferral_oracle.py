#!/usr/bin/env python3
"""R015 exact result-support oracle. Integer/Boolean only; no floating point."""
from __future__ import annotations
import argparse, ast, json, random
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from pathlib import Path

@dataclass(frozen=True)
class Relation:
    src_size:int; dst_size:int; edges:frozenset[tuple[int,int]]
    def __post_init__(self):
        if any(not(0<=x<self.src_size and 0<=y<self.dst_size) for x,y in self.edges):
            raise ValueError("edge out of range")

def direct_image(A,R):
    A=set(A); return frozenset(y for x,y in R.edges if x in A)

def compose_relations(R,S): # S o R
    if R.dst_size!=S.src_size: raise ValueError("dimension mismatch")
    return Relation(R.src_size,S.dst_size,frozenset((x,z) for x,y in R.edges for y2,z in S.edges if y==y2))

def eager_support_engine(A,word):
    A=frozenset(A)
    for R in word: A=direct_image(A,R)
    return A

def lazy_support_engine(A,word):
    A=frozenset(A)
    if not word:return A
    R=word[0]
    for S in word[1:]:R=compose_relations(R,S)
    return direct_image(A,R)

def mask(A):
    m=0
    for x in A:m|=1<<x
    return m

def support(m,n):return frozenset(i for i in range(n) if m&(1<<i))

def rows(R):
    out=[0]*R.src_size
    for x,y in R.edges:out[x]|=1<<y
    return tuple(out)

def vecmat(v,M):
    out=0
    for x,row in enumerate(M):
        if v&(1<<x):out|=row
    return out

def matmul(A,middle,B):
    out=[]
    for row in A:
        r=0
        for y in range(middle):
            if row&(1<<y):r|=B[y]
        out.append(r)
    return tuple(out)

def boolean_matrix_engine(A,word):
    v=mask(A)
    n=word[0].src_size if word else v.bit_length()
    for R in word:
        if R.src_size!=n:raise ValueError("dimension mismatch")
        v=vecmat(v,rows(R)); n=R.dst_size
    return support(v,n)

def all_relations(nx,ny):
    slots=[(x,y) for x in range(nx) for y in range(ny)]
    return tuple(Relation(nx,ny,frozenset(e for i,e in enumerate(slots) if m&(1<<i))) for m in range(1<<len(slots)))

def all_supports(n):return tuple(support(m,n) for m in range(1<<n))

def rel_table(R):return tuple(mask(direct_image(support(a,R.src_size),R)) for a in range(1<<R.src_size))

@lru_cache(None)
def family_unions(nx):
    k=1<<nx; out=[0]*(1<<k)
    for fm in range(1,1<<k):
        b=fm&-fm; a=b.bit_length()-1; out[fm]=out[fm^b]|a
    return tuple(out)

def preserves_arbitrary_unions(T,nx):
    U=family_unions(nx); rhs=[0]*len(U)
    for fm in range(len(U)):
        if fm:
            b=fm&-fm; a=b.bit_length()-1; rhs[fm]=rhs[fm^b]|T[a]
        if T[U[fm]]!=rhs[fm]:return False
    return True

def preserves_binary_unions_and_empty(T,nx):
    if T[0]!=0:return False
    return all(T[a|b]==(T[a]|T[b]) for a in range(1<<nx) for b in range(1<<nx))

def singleton_generated(T,nx):
    if T[0]!=0:return False
    for A in range(1<<nx):
        r=0
        for x in range(nx):
            if A&(1<<x):r|=T[1<<x]
        if r!=T[A]:return False
    return True

def singleton_relation_table(T,nx,ny):
    return tuple(vecmat(A,tuple(T[1<<x]&((1<<ny)-1) for x in range(nx))) for A in range(1<<nx))

def all_transformers(nx,ny):return product(range(1<<ny),repeat=1<<nx)

def family_witness(T,nx,two=False):
    U=family_unions(nx); fms=sorted(range(len(U)),key=lambda z:(z.bit_count(),z))
    for fm in fms:
        mem=[a for a in range(1<<nx) if fm&(1<<a)]
        if two and len([a for a in mem if a])<2:continue
        rhs=0
        for a in mem:rhs|=T[a]
        lhs=T[U[fm]]
        if lhs!=rhs:return {"family_mask":fm,"members":mem,"union":U[fm],"lazy":lhs,"eager":rhs}
    return None

def bounded_reps(n,cap=2):
    parts=list(range(1,1<<n)); out={m:[] for m in range(1<<n)}
    for counts in product(range(cap+1),repeat=len(parts)):
        c=[]; u=0
        for p,k in zip(parts,counts):
            c.extend([p]*k)
            if k:u|=p
        out[u].append(tuple(c))
    return {k:tuple(v) for k,v in out.items()}

def eager_T(T,components):
    r=0
    for a in components:r|=T[a]
    return r

def lazy_T(T,components):
    u=0
    for a in components:u|=a
    return T[u]

def exhaustive_two_state_relations(max_horizon=4):
    n=2; Rs=all_relations(n,n); Ss=all_supports(n); Ts=[rel_table(R) for R in Rs]; Ms=[rows(R) for R in Rs]; reps=bounded_reps(n,2)
    one=0
    for T in Ts:
        for u,rr in reps.items():
            for c in rr:
                one+=1
                if eager_T(T,c)!=T[u] or lazy_T(T,c)!=T[u]:raise AssertionError("schedule divergence")
    cases=matcases=statechecks=paths=0; per={}
    for h in range(max_horizon+1):
        hc=hs=hp=0
        for w in product(range(16),repeat=h):
            word=tuple(Rs[i] for i in w)
            for A in Ss:
                cases+=1; hc+=1
                e=eager_support_engine(A,word); l=lazy_support_engine(A,word); b=boolean_matrix_engine(A,word)
                if not(e==l==b):raise AssertionError((h,w,A,e,l,b))
                u=mask(A); p=len(reps[u]); statechecks+=len(reps[u]); hs+=len(reps[u])
                for i in w:
                    T=Ts[i]; nxt=T[u]
                    for c in reps[u]:
                        if eager_T(T,c)!=nxt:raise AssertionError("representation divergence")
                    u=nxt; p*=len(reps[u]); statechecks+=len(reps[u]); hs+=len(reps[u])
                paths+=p; hp+=p
                if h:
                    R=word[0]; M=Ms[w[0]]
                    for i in w[1:]:R=compose_relations(R,Rs[i]); M=matmul(M,n,Ms[i])
                    if rows(R)!=M:raise AssertionError("matrix composition divergence")
                    matcases+=1
        per[str(h)]={"relation_words":16**h,"initial_supports":4,"engine_cases":hc,"schedule_representation_state_checks":hs,"implicit_bounded_schedule_paths":hp}
    return {"state_size":2,"relations":16,"initial_supports":4,"max_horizon":max_horizon,"engine_cases":cases,"matrix_composition_cases":matcases,"bounded_duplicate_multiplicity":2,"bounded_representations_by_union":{str(k):len(v) for k,v in reps.items()},"one_step_schedule_transition_checks":one,"schedule_representation_state_checks":statechecks,"implicit_bounded_schedule_paths":paths,"per_horizon":per}

def exhaustive_transformer_characterization(max_x=3,max_y=2):
    totals=[0,0,0,0]; per={}
    for nx in range(max_x+1):
        for ny in range(max_y+1):
            c=[0,0,0,0]; reltabs={rel_table(R) for R in all_relations(nx,ny)}; good=set()
            for T in all_transformers(nx,ny):
                c[0]+=1; u=preserves_arbitrary_unions(T,nx); s=singleton_generated(T,nx); b=preserves_binary_unions_and_empty(T,nx); r=singleton_relation_table(T,nx,ny)==T
                if not(u==s==b==r):raise AssertionError((nx,ny,T,u,s,b,r))
                if u:c[1]+=1;good.add(T)
                if s:c[2]+=1
                if b:c[3]+=1
            if good!=reltabs or c[1]!=(1<<(nx*ny)):raise AssertionError("representation count mismatch")
            per[f"X{nx}_Y{ny}"]={"transformers":c[0],"union_preserving":c[1],"singleton_generated":c[2],"binary_union_plus_empty":c[3],"relational_tables":len(reltabs),"expected_relations":1<<(nx*ny)}
            totals=[a+b for a,b in zip(totals,c)]
    return {"max_x":max_x,"max_y":max_y,"total_transformers":totals[0],"total_union_preserving":totals[1],"total_singleton_generated":totals[2],"total_binary_union_plus_empty":totals[3],"per_size":per}

def mutation_suite():
    muts={"pair_required":(0,0,0,1),"exactly_one":(0,1,1,0),"bottom_injection":(1,0,0,0)}; out={}; d=0
    for name,T in muts.items():
        w=family_witness(T,2,name!="bottom_injection"); ok=preserves_arbitrary_unions(T,2)
        if (not ok) and w and w["eager"]!=w["lazy"]:d+=1
        out[name]={"table":list(T),"union_preserving":ok,"witness":w}
    anymin=twomin=None
    for nx in range(3):
        for T in all_transformers(nx,1):
            if preserves_arbitrary_unions(T,nx):continue
            if anymin is None:anymin={"x_size":nx,"y_size":1,"table":list(T),"witness":family_witness(T,nx)}
            w=family_witness(T,nx,True)
            if w and twomin is None:twomin={"x_size":nx,"y_size":1,"table":list(T),"witness":w}
            if anymin and twomin:break
        if anymin and twomin:break
    distinct=None
    for T in all_transformers(2,1):
        if eager_T(T,(1,2))!=lazy_T(T,(1,2)):
            distinct={"x_size":2,"y_size":1,"table":list(T),"components":[1,2],"eager":eager_T(T,(1,2)),"lazy":lazy_T(T,(1,2))};break
    if d!=3:raise AssertionError("mutations did not diverge")
    return {"mutations":out,"detected_non_union_preserving":3,"detected_eager_lazy_divergence":3,"minimal_any_union_failure":anymin,"minimal_nonempty_two_branch_failure":twomin,"minimal_distinct_singleton_branch_failure":distinct}

def negative_boundaries():
    return {
      "hidden_history":{"visible_states":["s"],"hidden_states":["h0","h1"],"visible_projection":{"h0":"s","h1":"s"},"future":{"h0":"y0","h1":"y1"},"witness":"same visible {s} would need different futures","classification":["SEMANTIC_CONTRACT_VIOLATION","WRONG_STATE_TYPE","CURRENT_STATE_NOT_SUFFICIENT"],"repair":"include future-readable history discriminator in current state"},
      "multiplicity":{"branch_multiset_a":["x"],"branch_multiset_b":["x","x"],"boolean_support_a":["x"],"boolean_support_b":["x"],"readout":{"count=1":"y1","count=2":"y2"},"classification":["OUT_OF_CONTRACT_OBSERVABLE","WRONG_STATE_TYPE"],"repair":"multiset/N-semimodule or explicit count"},
      "support_global_nonlinear":{"X":["a","b"],"Y":["y"],"rule":"T(A)={y} iff both a,b are present","eager_on_singletons":[],"lazy_on_union":["y"],"classification":["THEOREM_HYPOTHESIS_FAILURE","NON_UNION_PRESERVING_TRANSFORMER"],"repair":"encode simultaneous-presence state or leave relational direct-image semantics"},
      "discarded_probability_weights":{"support":["x0","x1"],"distribution_a":["3/4","1/4"],"distribution_b":["1/4","3/4"],"same_boolean_support":True,"different_exact_weighted_result":True,"classification":["OUT_OF_CONTRACT_OBSERVABLE","WRONG_CARRIER"],"repair":"probability distributions/stochastic kernels"},
      "signed_amplitude_cancellation":{"current_support":["x0","x1"],"relation_edges":[["x0","y"],["x1","y"]],"amplitudes":{"x0->y":"+1","x1->y":"-1"},"boolean_reachable_support":["y"],"combined_amplitude_at_y":"0","nonzero_amplitude_support":[],"classification":["OUT_OF_CONTRACT_OBSERVABLE","BOOLEAN_SUPPORT_NOT_FAITHFUL","RICHER_MODULE_REQUIRED"],"repair":"signed/complex module with additive cancellation"}}

def randomized_property_suite(seed=15015,trials=500):
    rng=random.Random(seed); ms=mh=0
    for _ in range(trials):
        n=rng.randint(2,8); h=rng.randint(1,12); ms=max(ms,n);mh=max(mh,h); word=[]
        for _ in range(h):
            E={(x,y) for x in range(n) for y in range(n) if rng.randrange(4)==0};word.append(Relation(n,n,frozenset(E)))
        A=frozenset(i for i in range(n) if rng.randrange(2)); e=eager_support_engine(A,word);l=lazy_support_engine(A,word);b=boolean_matrix_engine(A,word)
        if not(e==l==b):raise AssertionError("random engine divergence")
        R=word[rng.randrange(h)]; fam=[frozenset(i for i in range(n) if rng.randrange(2)) for _ in range(rng.randint(0,8))]; U=frozenset().union(*fam) if fam else frozenset(); rhs=frozenset().union(*(direct_image(B,R) for B in fam)) if fam else frozenset()
        if direct_image(U,R)!=rhs:raise AssertionError("random union divergence")
    return {"seed":seed,"trials":trials,"max_states_seen":ms,"max_horizon_seen":mh}

def audit(path):
    tree=ast.parse(path.read_text()); f=[n for n in ast.walk(tree) if isinstance(n,ast.Constant) and isinstance(n.value,float)]; d=[n for n in ast.walk(tree) if isinstance(n,ast.BinOp) and isinstance(n.op,ast.Div)]
    if f or d:raise AssertionError("non-integer arithmetic")
    return {"float_constants":0,"true_division_nodes":0}

relation_direct_image_table=rel_table
relation_to_boolean_rows=rows
boolean_matrix_product=matmul
no_float_or_true_division_audit=audit

def theorem_matrix():
    return {"task":"RS-R015-RESULT-SUPPORT-BRANCH-DEFERRAL-INVARIANCE","researcher_id":"EM-R015-R7A3","final_verdict":"RESULT_SUPPORT_BRANCH_DEFERRAL_PROVED / EXECUTABLE_EXHAUSTIVE_PASS / FOUNDATION_REWRITE_CANDIDATE / NOT_CANONICAL","positive_contract":{"observable":"final Boolean reachable-result support only","state_requirement":"all future-readable facts are in current state","future_step":"relational direct image","discarded_by_contract":["path identity","multiplicity","weights/probability","cost","amplitude"]},"theorems":{"R015-T01":{"status":"PROVED","class":"ROOTING_SUCCESS / PRIOR_ART"},"R015-T02":{"status":"PROVED","class":"ROOTING_SUCCESS / PRIOR_ART"},"R015-T03":{"status":"PROVED","class":"ENTERPRISE_SEMANTIC_SPECIALIZATION"},"R015-T04a":{"status":"PROVED","class":"ROOTING_SUCCESS / PRIOR_ART"},"R015-T04b":{"status":"PROVED","class":"ROOTING_SUCCESS / PRIOR_ART"},"R015-T04c":{"status":"PROVED","class":"ROOTING_SUCCESS / PRIOR_ART"},"R015-T05":{"status":"PROVED","class":"ROOTING_SUCCESS / PRIOR_ART"},"R015-T06":{"status":"PROVED","class":"ENTERPRISE_SEMANTIC_SPECIALIZATION"}},"characterization_assumptions":{"all_families_including_empty":"complete union preservation and T(empty)=empty","nonempty_families_only":"bottom preservation not forced","arbitrary_X":"complete union preservation iff singleton-generated iff unique relational direct image","finite_X":"binary union + bottom suffices","infinite_X_counterexample":"T(A)=A when finite, N when infinite"},"boolean_matrix_contract":{"orientation":"row vectors; M_(S o R)=M_R*M_S over Boolean semiring","observable":"Boolean reachability","explicitly_not":"path counts"},"negative_boundaries":negative_boundaries(),"impact_matrix":{"P023":{"split":["FUNCTIONAL_SAFE","SUPPORT_SAFE","SUPPORT_UNSAFE"],"unchanged":"deterministic theorems remain valid in functional scope"},"R009":{"routing":"IMPACT_ONLY_DO_NOT_MODIFY","forbidden_assumption":"{a^p,(a+1)^p} not assumed"},"P018":{"routing":"functional vs support-valued projection"},"P021":{"routing":"witness/multiplicity semantics remain richer"},"R013":{"routing":"result-support is one declared semantic fibre"},"R014":{"routing":"eager/lazy/matrix are resource alternatives only after semantic equality"}},"prior_art":{"relations":"ROOTING_SUCCESS / PRIOR_ART","powerset_direct_image":"ROOTING_SUCCESS / PRIOR_ART","join_preservation":"ROOTING_SUCCESS / PRIOR_ART","Boolean_reachability":"ROOTING_SUCCESS / PRIOR_ART","enterprise_residue":"collapse execution consequence and P023 safety split"},"canonical_mutations":[],"canonical_status":"NOT_CANONICAL"}

def run_all(h=4,mx=3,my=2,trials=500):
    return {"task":"RS-R015-RESULT-SUPPORT-BRANCH-DEFERRAL-INVARIANCE","researcher_id":"EM-R015-R7A3","positive_contract":"result-only current-state-sufficient relational direct-image support semantics","relation_exhaustive":exhaustive_two_state_relations(h),"transformer_characterization_exhaustive":exhaustive_transformer_characterization(mx,my),"mutation_tests":mutation_suite(),"randomized_properties":randomized_property_suite(trials=trials),"integer_boolean_audit":audit(Path(__file__)),"negative_boundaries":negative_boundaries(),"pass":True}

def main():
    p=argparse.ArgumentParser();p.add_argument("--max-horizon",type=int,default=4);p.add_argument("--max-x",type=int,default=3);p.add_argument("--max-y",type=int,default=2);p.add_argument("--random-trials",type=int,default=500);p.add_argument("--summary-out",type=Path);p.add_argument("--matrix-out",type=Path);a=p.parse_args();s=run_all(a.max_horizon,a.max_x,a.max_y,a.random_trials);text=json.dumps(s,indent=2,sort_keys=True);print(text)
    if a.summary_out:a.summary_out.write_text(text+"\n")
    if a.matrix_out:a.matrix_out.write_text(json.dumps(theorem_matrix(),indent=2,sort_keys=True)+"\n")
if __name__=="__main__":main()
